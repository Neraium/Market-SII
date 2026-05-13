from abc import ABC, abstractmethod


class StreamingProvider(ABC):
    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    async def subscribe(self, symbols):
        pass

    @abstractmethod
    async def stream(self):
        yield None
