class RedisStateCache:
    def __init__(self):
        self.connected = False

    async def connect(self):
        self.connected = True
        return self.connected

    async def publish_state(self, key, payload):
        return {
            'status': 'queued',
            'key': key,
            'payload': payload,
        }

    async def get_latest_state(self, key):
        return {
            'status': 'placeholder',
            'key': key,
        }
