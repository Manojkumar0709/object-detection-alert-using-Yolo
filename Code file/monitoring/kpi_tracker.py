class KPITracker:
    def __init__(self):
        self.throughput = 0
        self.events = []

    def log_detections(self, results):
        self.throughput += len(results)
        self.events.extend(results)

    def get_metrics(self):
        return {"throughput": self.throughput, "event_count": len(self.events)}

    def get_alerts(self):
        return self.events[-10:]
