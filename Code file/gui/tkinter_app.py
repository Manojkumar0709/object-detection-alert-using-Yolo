import os
import subprocess
import tkinter as tk
from tkinter import ttk

import cv2
import numpy as np
from gtts import gTTS


class ObjectRecognition:
    def __init__(
        self,
        weights_path="models/yolov3.weights",
        config_path="models/yolov3.cfg",
        class_names_path="Dataset/coco.names",
        conf_threshold=0.5,
        nms_threshold=0.4,
        audio_dir="audio",
    ):
        self.weights_path = weights_path
        self.config_path = config_path
        self.class_names_path = class_names_path
        self.conf_threshold = conf_threshold
        self.nms_threshold = nms_threshold
        self.audio_dir = audio_dir

        self.audio_enabled = False
        os.makedirs(self.audio_dir, exist_ok=True)

        self.classes = self.load_classes()
        self.net = self.load_model()
        self.output_layers = self.net.getUnconnectedOutLayersNames()
        self.video_capture = self.init_camera()

        self.root = tk.Tk()
        self.root.title("Object Recognition with Audio")
        ttk.Button(self.root, text="Toggle Audio", command=self.toggle_audio).pack(pady=10)
        self.root.after(10, self.detect_objects)

    def load_classes(self):
        with open(self.class_names_path, "r") as f:
            return [line.strip() for line in f.readlines()]

    def load_model(self):
        return cv2.dnn.readNet(self.weights_path, self.config_path)

    def init_camera(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise RuntimeError("Could not open webcam.")
        return cap

    def toggle_audio(self):
        self.audio_enabled = not self.audio_enabled
        print(f"Audio {'Enabled' if self.audio_enabled else 'Disabled'}")

    def play_audio(self, audio_path):
        try:
            subprocess.run(["afplay", audio_path], check=False)
        except FileNotFoundError:
            print("afplay not found. Audio playback works on macOS with afplay.")

    def speak_label(self, label):
        audio_path = os.path.join(self.audio_dir, "label.mp3")
        tts = gTTS(text=label, lang="en")
        tts.save(audio_path)
        self.play_audio(audio_path)

    def extract_detections(self, outs, width, height):
        boxes = []
        confidences = []
        class_ids = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = int(np.argmax(scores))
                confidence = float(scores[class_id])

                if confidence > self.conf_threshold:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(confidence)
                    class_ids.append(class_id)

        return boxes, confidences, class_ids

    def draw_detections(self, frame, boxes, confidences, class_ids, indices):
        if len(indices) > 0:
            for i in indices.flatten():
                x, y, w, h = boxes[i]
                label_name = self.classes[class_ids[i]]
                confidence = confidences[i]
                label = f"{label_name}: {confidence:.2f}"

                if self.audio_enabled:
                    self.speak_label(label_name)

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    label,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2,
                )

    def detect_objects(self):
        ret, frame = self.video_capture.read()
        if not ret:
            self.root.after(10, self.detect_objects)
            return

        height, width, _ = frame.shape
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.output_layers)

        boxes, confidences, class_ids = self.extract_detections(outs, width, height)
        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.conf_threshold, self.nms_threshold)

        self.draw_detections(frame, boxes, confidences, class_ids, indices)

        cv2.imshow("Object Recognition", frame)
        key = cv2.waitKey(1)
        if key == 27:
            self.shutdown()
            return

        self.root.after(10, self.detect_objects)

    def shutdown(self):
        self.video_capture.release()
        cv2.destroyAllWindows()
        self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ObjectRecognition()
    app.run()
