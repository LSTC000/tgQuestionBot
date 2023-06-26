from loader import dp, bot

from data.messages import SUCCESSFULLY_PAYMENT_MESSAGE

from aiogram import types
from aiogram.types import ContentType


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=SUCCESSFULLY_PAYMENT_MESSAGE)
