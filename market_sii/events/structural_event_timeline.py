class StructuralEventTimeline:
    def __init__(self):
        self.events = []

    def add_event(self, timestamp, category, severity, description, metadata=None):
        self.events.append(
            {
                "timestamp": str(timestamp),
                "category": category,
                "severity": severity,
                "description": description,
                "metadata": metadata or {},
            }
        )

    def recent(self, n=50):
        return self.events[-n:]

    def filter_category(self, category):
        return [event for event in self.events if event["category"] == category]
