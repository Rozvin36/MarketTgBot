import os
from dotenv import load_dotenv

load_dotenv()

# PostgreSQL по частям
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")  # значение по умолчанию
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

# Сборка строки подключения
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

TOKEN = os.getenv("TOKEN")

REDIS_URL = os.getenv("REDIS_URL")