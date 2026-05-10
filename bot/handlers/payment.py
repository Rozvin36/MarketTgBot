from aiogram import Router, F
from aiogram.types import PreCheckoutQuery, Message


from core.redis import redis_client
from core.database import async_session
from core.enums import Status
from core.models import ProductORM, PurchaseORM

payment_router = Router()

@payment_router.pre_checkout_query()
async def on_pre_checkout(pre_checkout_query: PreCheckoutQuery):

    payload = pre_checkout_query.invoice_payload
    async with async_session() as session:
        product = await session.get(ProductORM, payload)
    if not product:
        await pre_checkout_query.answer(
            ok=False,
            error_message="Товар не найден"
        )
        return

    if product.status != Status.IN_STOCK.value:
        await pre_checkout_query.answer(
            ok=False,
            error_message="Товара нет в наличии"
        )
        return

    if product.price != pre_checkout_query.total_amount:
        await pre_checkout_query.answer(
            ok=False,
            error_message="Неверная сумма"
        )
        return

    await redis_client.set(f"{pre_checkout_query.from_user.id}:product_buying", product.name, ex=120)
    await pre_checkout_query.answer(ok=True)
    return


@payment_router.message(F.successful_payment)
async def on_successful_payment(message: Message):
    payload = message.successful_payment.invoice_payload
    user_id = message.from_user.id

    product_name = await redis_client.get(f"{user_id}:product_buying")

    async with async_session() as session:
        purchase = PurchaseORM(
            user_id=user_id,
            product_id=payload,
            amount=message.successful_payment.total_amount
        )
        session.add(purchase)
        if product_name is None:
            need_product = await session.get(ProductORM, payload)
            product_name = need_product.name
        await session.commit()

    await message.answer(
        f"Спасибо за покупку!\n"
        f"Товар: {product_name}\n"
        f"Ваш ключ: KEY-{payload[:8].upper()}"
    )