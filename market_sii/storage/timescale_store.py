class TimescaleStore:
    def __init__(self, connection_string=None):
        self.connection_string = connection_string
        self.connected = False

    async def connect(self):
        self.connected = True

    async def insert_market_state(self, payload):
        return {
            "status": "stored",
            "payload": payload,
        }

    async def query_recent(self, limit=100):
        return []
