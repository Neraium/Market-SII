class PersistentAlertEngine:
    def __init__(self, confirmation_threshold=3):
        self.confirmation_threshold = confirmation_threshold
        self.hit_counter = {}

    def evaluate(self, key, triggered):
        current = self.hit_counter.get(key, 0)

        if triggered:
            current += 1
        else:
            current = max(current - 1, 0)

        self.hit_counter[key] = current

        return {
            "key": key,
            "hits": current,
            "confirmed": current >= self.confirmation_threshold,
        }
