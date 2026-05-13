import os
from dataclasses import dataclass


@dataclass
class Settings:
    polygon_api_key: str | None = os.getenv('POLYGON_API_KEY')
    redis_url: str = os.getenv('REDIS_URL', 'redis://localhost:6379')
    postgres_url: str = os.getenv('POSTGRES_URL', 'postgresql://localhost/market_sii')
    environment: str = os.getenv('ENVIRONMENT', 'development')
    frontend_origin: str = os.getenv('FRONTEND_ORIGIN', 'http://localhost:3000')


settings = Settings()
