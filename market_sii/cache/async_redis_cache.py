class AsyncRedisCache:
    def __init__(self):
        self.connected = False
        self.memory = {}

    async def connect(self):
        self.connected = True

    async def set(self, key, value):
        self.memory[key] = value

    async def get(self, key):
        return self.memory.get(key)

    async def publish(self, channel, payload):
        return {
            "channel": channel,
            "payload": payload,
        }
