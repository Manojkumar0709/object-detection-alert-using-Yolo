# 🚚 Real-Time Object Detection & Tracking for Logistics

A real-time computer vision system for object detection and tracking in logistics processes, built with **YOLOv8**, **Flask**, and **OpenCV**. The system provides live alerting, KPI monitoring, and REST API integration for external applications.

---

## 📌 Project Overview

This project addresses the need for automated monitoring in logistics and warehouse environments. It detects and tracks objects in real time, triggers alerts on defined events, and exposes a REST API for seamless integration with external systems or dashboards.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Object Detection | YOLO (YOLOv8) |
| Backend API | Flask, REST APIs |
| Image Processing | OpenCV |
| Language | Python |
| Monitoring | KPI Dashboard (Object throughput, detection events) |

---

## ✨ Features

- 🎯 **Real-time object detection** using YOLO for accurate, low-latency tracking in logistics pipelines
- 🔔 **Event-based alerting** — triggers notifications on specific detection events or process deviations
- 🌐 **Flask REST API** for event processing and integration with external applications
- 📊 **KPI Monitoring** — tracks object throughput, detection event counts, and process anomalies
- 🔄 **Modular architecture** enabling easy swap of detection models or alert destinations

---

## 🗂️ Project Structure

```
object-detection-alert-using-Yolo/
│
├── detection/           # YOLO model loading & inference logic
├── api/                 # Flask REST API endpoints
├── alerts/              # Alert logic and notification handlers
├── monitoring/          # KPI tracking and metrics
├── utils/               # Preprocessing and helper functions
├── config.py            # Configuration (thresholds, model paths, API keys)
├── main.py              # Application entry point
└── requirements.txt     # Python dependencies
```

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python main.py
```

The Flask API will start at `http://localhost:5000`. Connect a video feed or webcam stream to begin detection.

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/status` | System health check |
| `POST` | `/detect` | Submit frame for detection |
| `GET` | `/kpi` | Retrieve current KPI metrics |
| `GET` | `/alerts` | Fetch recent alert log |

---

## 📈 KPIs Tracked

- **Object Throughput** — number of objects detected per time window
- **Detection Events** — logged instances of specific object classes
- **Process Deviations** — anomalies flagged against baseline thresholds

---

## 🔮 Future Improvements

- [ ] Add multi-camera support
- [ ] Integrate with a Streamlit dashboard for live visualization
- [ ] Add database logging (PostgreSQL) for historical event analysis
- [ ] Deploy via Docker for containerized production use

---

## 👤 Author

**Manoj Kumar Mohankumar**  
M.Sc. Artificial Intelligence for Smart Sensors and Actuators  
Technische Hochschule Deggendorf, Germany  
📧 manojmelarcode@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/manojkumar-m-93996714b) | [GitHub](https://github.com/Manojkumar0709)
