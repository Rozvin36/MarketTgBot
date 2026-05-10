import redis.asyncio as aioredis
from core.config import REDIS_URL

redis_client = aioredis.from_url(REDIS_URL, decode_responses=True)