# Dataset Info

This project uses the **MS COCO (Microsoft Common Objects in Context)** dataset class labels together with a pretrained **YOLOv3** model for real-time object detection.

## Files in this folder

- `coco.names` : COCO object class labels used by YOLOv3 for detection and labeling

## Dataset Details

- **Dataset Name:** MS COCO
- **Total Images:** 330,000+
- **Object Categories:** 91 total, 82 labeled categories
- **Classes Used by YOLOv3:** 80 (subset used for object detection)

## Why COCO

MS COCO is a widely used benchmark for object detection because it contains common real-world objects captured in complex, cluttered scenes. Its emphasis on multiple object instances per image makes it effective for training and evaluating detection accuracy.

## Use in This Project

The dataset labels are used to:
- Identify and classify objects detected in real-time via webcam
- Generate bounding boxes with class names and confidence scores
- Convert detected labels into spoken audio feedback using gTTS
- Support the Tkinter-based GUI for toggling audio alerts

## Model Files Required

To run detection, the following files must be present alongside the dataset labels:

- `yolov3.weights` (pretrained YOLOv3 weights)
- `yolov3.cfg` (YOLOv3 network configuration)
- `coco.names` (this dataset's class labels)

## Notes

Only the class label file (`coco.names`) is included in this repository. The full MS COCO image dataset is not included due to its large size (330,000+ images) and should be downloaded separately if training or fine-tuning is required.
