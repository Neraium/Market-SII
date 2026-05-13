class AlertRouter:
    def __init__(self):
        self.channels = {}

    def register_channel(self, name, handler):
        self.channels[name] = handler

    async def route(self, severity, payload):
        results = {}

        for name, handler in self.channels.items():
            results[name] = await handler(severity, payload)

        return results


async def console_alert_handler(severity, payload):
    return {
        "status": "sent",
        "severity": severity,
        "payload": payload,
    }
