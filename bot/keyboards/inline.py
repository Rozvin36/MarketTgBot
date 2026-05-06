from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from core.enums import Status
from core.models import ProductORM


def generate_start_inline_keyboard(mass: list[ProductORM]) -> InlineKeyboardMarkup:
    """Делает клавиатуру с товарами"""
    button_mass = []
    # ORM -> InlineKeyboardButton
    for one in mass:
        if one.status == Status.IN_STOCK.value:
            button_mass.append(
                InlineKeyboardButton(
                    text=f"Купить {one.name}\nза {one.price}⭐",
                    callback_data=f"buy_{one.id}"
                )
            )


    inline_keyboard_mass = []
    to_2 = False
    mini_mass = []
    # Одномерный массив в двумерный
    for i in range(0, len(button_mass)):
        if to_2:
            mini_mass.append(button_mass[i])
            inline_keyboard_mass.append(mini_mass)
            mini_mass = []
            to_2 = False
        else:
            mini_mass.append(button_mass[i])
            to_2 = True

    if mini_mass:
        inline_keyboard_mass.append(mini_mass)

    buy_inline_keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_keyboard_mass
    )

    return buy_inline_keyboard

