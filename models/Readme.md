# Model Files Required

This project requires the following YOLOv3 files, which are not included in this repository due to file size limits.

## Files Needed
- `yolov3.weights` — pretrained YOLOv3 weights (~236 MB)
- `yolov3.cfg` — YOLOv3 network configuration

## Where to Get Them
- YOLOv3 weights: https://pjreddie.com/media/files/yolov3.weights
- YOLOv3 config: https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg

## Setup
1. Download both files.
2. Place them inside this `models/` folder.
3. Ensure `code/main.py` paths match:
   - `models/yolov3.weights`
   - `models/yolov3.cfg`
