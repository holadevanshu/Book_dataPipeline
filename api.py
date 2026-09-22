from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List
import importlib

# Dynamically import database manager class handling spaced directory name
db_module = importlib.import_module("DB access.database")
BookDatabaseManager = db_module.BookDatabaseManager

app = FastAPI(title="Book Data Pipeline API")
db = BookDatabaseManager()

class BookBase(BaseModel):
    title: str
    price: float = Field(..., gt=0)
    in_stock: bool
    rating: int = Field(..., ge=1, le=5)

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int

@app.get("/books", response_model=List[BookResponse])
def get_books():
    """Retrieve all stored books."""
    return db.get_all_books()

@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
    """Retrieve a single book by ID."""
    book = db.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book

@app.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    """Create a new book entry."""
    created = db.create_book(book.title, book.price, book.in_stock, book.rating)
    return created

@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookCreate):
    """Update an existing book entry."""
    updated = db.update_book(book_id, book.title, book.price, book.in_stock, book.rating)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return updated

@app.delete("/books/{book_id}", status_code=status.HTTP_200_OK)
def delete_book(book_id: int):
    """Delete a book entry by ID."""
    success = db.delete_book(book_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return {"message": f"Book {book_id} successfully deleted"}