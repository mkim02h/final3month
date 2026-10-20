books_table = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL UNIQUE,
        name TEXT NOT NULL, 
        author TEXT
    )
"""
insert_book = "INSERT INTO books (book_id, name, author) VALUES (?, ?, ?)" 


books_detail_table = """
    CREATE TABLE IF NOT EXISTS books_detail (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL UNIQUE,
        genre TEXT,
        FOREIGN KEY (book_id) REFERENCES books(book_id)
    )
"""

insert_book_detail = "INSERT INTO books_detail (book_id, genre) VALUES (?, ?)" 

get_books = """
    SELECT books.book_id, books.name, books.author, books_detail.genre
    FROM books
    INNER JOIN books_detail ON books.book_id = books_detail.book_id
"""
