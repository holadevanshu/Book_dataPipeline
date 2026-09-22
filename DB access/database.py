import sqlite3
from typing import List, Dict, Any, Optional

class BookDatabaseManager:
    """
    OOP SQLite Database Manager providing full CRUD operations for Book records.
    """
    def __init__(self, db_name: str = "books.db"):
        self.db_name = db_name
        self.init_db()

    def get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self) -> None:
        """Creates books table if it does not already exist."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    price REAL NOT NULL,
                    in_stock INTEGER NOT NULL,
                    rating INTEGER NOT NULL
                )
            """)
            conn.commit()

    def create_book(self, title: str, price: float, in_stock: bool, rating: int) -> Dict[str, Any]:
        """CREATE: Insert a single book record."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO books (title, price, in_stock, rating) VALUES (?, ?, ?, ?)",
                (title, price, 1 if in_stock else 0, rating)
            )
            conn.commit()
            book_id = cursor.lastrowid
            return self.get_book_by_id(book_id)

    def get_all_books(self) -> List[Dict[str, Any]]:
        """READ: Retrieve all book records."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, price, in_stock, rating FROM books")
            rows = cursor.fetchall()
            return [
                {
                    "id": row["id"],
                    "title": row["title"],
                    "price": row["price"],
                    "in_stock": bool(row["in_stock"]),
                    "rating": row["rating"]
                }
                for row in rows
            ]

    def get_book_by_id(self, book_id: int) -> Optional[Dict[str, Any]]:
        """READ: Retrieve a single book record by ID."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, price, in_stock, rating FROM books WHERE id = ?", (book_id,))
            row = cursor.fetchone()
            if row:
                return {
                    "id": row["id"],
                    "title": row["title"],
                    "price": row["price"],
                    "in_stock": bool(row["in_stock"]),
                    "rating": row["rating"]
                }
            return None

    def update_book(self, book_id: int, title: str, price: float, in_stock: bool, rating: int) -> Optional[Dict[str, Any]]:
        """UPDATE: Update an existing book entry."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE books SET title = ?, price = ?, in_stock = ?, rating = ? WHERE id = ?",
                (title, price, 1 if in_stock else 0, rating, book_id)
            )
            conn.commit()
            if cursor.rowcount > 0:
                return self.get_book_by_id(book_id)
            return None

    def delete_book(self, book_id: int) -> bool:
        """DELETE: Delete a book record by ID."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
            conn.commit()
            return cursor.rowcount > 0