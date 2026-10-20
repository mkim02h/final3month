import aiosqlite
from database import queries
from config import path_db


async def init_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.books_table)
        await conn.execute(queries.books_detail_table)
        await conn.commit()
    print('База данных успешно подключена!')

async def add_book_db(book_id, name, author, genre):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.insert_book, (book_id, name, author))
        await conn.execute(queries.insert_book_detail, (book_id, genre))
        await conn.commit()

async def get_books_db():
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.get_books)
        return await cursor.fetchall()
