import os
from dotenv import load_dotenv

load_dotenv()

# Сборка строки подключения
DATABASE_URL = (
    f"postgresql+asyncpg://"
    f"{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

TOKEN = os.getenv("BOT_TOKEN")

REDIS_URL = os.getenv("REDIS_URL")