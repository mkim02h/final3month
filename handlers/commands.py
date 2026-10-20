from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from database import db

router_commands = Router()

@router_commands.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f'Привет, {message.from_user.full_name}!',
        # reply_markup=reply_keyboard 
    )

@router_commands.message(Command('books'))
async def cmd_books(message: Message):
    books = await db.get_books_db()
    if not books:
        await message.answer('В базе книг нет!')
        return
    else: 
        for book_id, name, author, genre in books:
            await message.answer(f'Данные товара: \Номер книги: {book_id} '
                            f'\nНазвание - {name} \nАвтор - {author} \nЖанр - {genre}') 
