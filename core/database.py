from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from core.config import DATABASE_URL

# Строка подключения с asyncpg
async_engine = create_async_engine(DATABASE_URL, echo=True)
# Фабрика асинхронных сессий
async_session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass