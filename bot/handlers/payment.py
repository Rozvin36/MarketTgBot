from aiogram import Router, F
from aiogram.types import PreCheckoutQuery, Message

payment_router = Router()

@payment_router.pre_checkout_query()
async def on_pre_checkout(pre_checkout_query: PreCheckoutQuery):
    ...


@payment_router.message(F.successful_payment)
async def on_successful_payment(message: Message):
    ...