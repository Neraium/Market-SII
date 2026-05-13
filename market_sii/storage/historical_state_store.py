class HistoricalStateStore:
    def __init__(self):
        self.records = []

    def append(self, payload):
        self.records.append(payload)

    def latest(self, n=100):
        return self.records[-n:]

    def filter_regime(self, regime):
        return [record for record in self.records if record.get('regime') == regime]
