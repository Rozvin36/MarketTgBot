from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, LabeledPrice
from sqlalchemy import select

from bot.keyboards.inline import generate_start_inline_keyboard
from core.database import async_session
from core.models import ProductORM

user_router = Router()

@user_router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привет! Это магазин цифровых товаров."
    )

@user_router.message(Command("buy"))
async def buy(message: Message):
    async with async_session() as session:
        result = await session.execute(select(ProductORM))
        all_product = result.scalars().all()
    keyboard = generate_start_inline_keyboard(all_product)
    if not all_product:
        await message.answer("Товаров пока нет.")
        return
    await message.answer(
        "Выбери, что хочешь купить:",
        reply_markup=keyboard
    )

@user_router.callback_query(F.data.startswith("buy_"))
async def buy_one(callback: CallbackQuery):
    product_id = callback.data.split("_", 1)[1]
    user_id = callback.from_user.id
    async with async_session as session:
        result = await session.get(ProductORM, product_id)
        need_product = result.first()
    await callback.answer(f"Вы выбрали товар: {need_product.name}."
                          f"Описание: {need_product.description}."
                          f"Цена: {need_product.price} ⭐."
                          "Сейчас я создам счёт для оплаты..."
    )
    await callback.bot.send_invoice(
        chat_id=user_id,
        title=need_product.name,
        description=need_product.description,
        payload=need_product.id,
        provider_token="",
        currency="XTR",
        prices=[LabeledPrice(label=need_product.name, amount=need_product.price)]
    )
