from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database import db

router_add_book = Router()

class Add_Book(StatesGroup):
    book_id = State()
    name = State()
    author = State()
    genre = State()

@router_add_book.message(Command('add_book'))
async def add_start_fsm(message: Message, state: FSMContext):
    await message.answer('Введите номер книги: ')
    await state.set_state(Add_Book.book_id)

@router_add_book.message(Add_Book.book_id)
async def add_book_id(message: Message, state: FSMContext):
    await state.update_data(book_id=message.text)
    if not message.text.isdigit():
        await message.answer('Номер должен быть числом! Пожалуйста, введите корректный номер.')
        return
    book_id = int(message.text)
    await message.answer('Введите название книги: ')
    await state.set_state(Add_Book.name)

@router_add_book.message(Add_Book.name)
async def add_book_id(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Укажите автора: ')
    await state.set_state(Add_Book.author)

@router_add_book.message(Add_Book.author)
async def add_book_id(message: Message, state: FSMContext):
    await state.update_data(author=message.text)
    await message.answer('Укажите жанр: ')
    await state.set_state(Add_Book.genre)

@router_add_book.message(Add_Book.genre)
async def add_book_id(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    data = await state.get_data()
    await message.answer(f'Информация о книге: \nНомер книги: {data['book_id']} \nНазвание книги: {data['name']}' 
                         f'\nАвтор: {data['author']} \nЖанр: {data['genre']}')
    await db.add_book_db(book_id=data['book_id'], name=data['name'], author=data['author'], genre=data['genre'])
    await state.clear()