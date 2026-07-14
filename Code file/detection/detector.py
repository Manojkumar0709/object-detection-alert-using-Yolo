"""
YOLOv3 Object Detector
Handles model loading, inference, and Non-Maximum Suppression.
Used by both the Tkinter GUI app and the Flask REST API.
"""

import cv2
import numpy as np


class ObjectDetector:
    def __init__(
        self,
        weights_path="models/yolov3.weights",
        config_path="models/yolov3.cfg",
        class_names_path="Dataset/coco.names",
        conf_threshold=0.5,
        nms_threshold=0.4,
    ):
        self.weights_path = weights_path
        self.config_path = config_path
        self.class_names_path = class_names_path
        self.conf_threshold = conf_threshold
        self.nms_threshold = nms_threshold

        self.classes = self._load_classes()
        self.net = self._load_model()
        self.output_layers = self.net.getUnconnectedOutLayersNames()

    def _load_classes(self):
        with open(self.class_names_path, "r") as f:
            return [line.strip() for line in f.readlines()]

    def _load_model(self):
        return cv2.dnn.readNet(self.weights_path, self.config_path)

    def _extract_detections(self, outputs, width, height):
        boxes, confidences, class_ids = [], [], []

        for output in outputs:
            for detection in output:
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

    def detect(self, frame):
        """
        Runs YOLOv3 detection on a single frame.
        Returns a list of detections: [{label, confidence, box}, ...]
        """
        height, width, _ = frame.shape
        blob = cv2.dnn.blobFromImage(
            frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False
        )
        self.net.setInput(blob)
        outputs = self.net.forward(self.output_layers)

        boxes, confidences, class_ids = self._extract_detections(outputs, width, height)
        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.conf_threshold, self.nms_threshold)

        results = []
        if len(indices) > 0:
            for i in indices.flatten():
                results.append({
                    "label": self.classes[class_ids[i]],
                    "confidence": round(confidences[i], 2),
                    "box": boxes[i],  # [x, y, w, h]
                })

        return results

    def draw_boxes(self, frame, detections):
        """
        Draws bounding boxes and labels on a frame (used for GUI display).
        """
        for det in detections:
            x, y, w, h = det["box"]
            label = f"{det['label']}: {det['confidence']:.2f}"
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                frame, label, (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2
            )
        return frame
