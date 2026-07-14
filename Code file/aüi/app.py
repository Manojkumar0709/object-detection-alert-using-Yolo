from flask import Flask, jsonify, request
from code.detection.detector import ObjectDetector
from code.monitoring.kpi_tracker import KPITracker

app = Flask(__name__)
detector = ObjectDetector()
kpi = KPITracker()

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "running"})

@app.route("/detect", methods=["POST"])
def detect():
    frame = request.files["frame"]
    results = detector.detect(frame)
    kpi.log_detections(results)
    return jsonify(results)

@app.route("/kpi", methods=["GET"])
def get_kpi():
    return jsonify(kpi.get_metrics())

@app.route("/alerts", methods=["GET"])
def get_alerts():
    return jsonify(kpi.get_alerts())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
