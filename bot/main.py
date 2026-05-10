import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.handlers.user import user_router
from bot.handlers.payment import payment_router
from core import config

bot = Bot(
    token=config.TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

dp.include_router(user_router)
dp.include_router(payment_router)

async def main():
    from core.database import async_engine, Base
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())