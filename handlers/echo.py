from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router

router_echo = Router()

@router_echo.message()
async def echo(message: Message):
    await message.answer(f'Вы написали: {message.text}')