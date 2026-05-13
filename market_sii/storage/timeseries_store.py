class TimeSeriesStore:
    def __init__(self):
        self.rows = []

    def insert(self, payload):
        self.rows.append(payload)

    def latest(self, limit=100):
        return self.rows[-limit:]

    def range_query(self, start=None, end=None):
        return self.rows
