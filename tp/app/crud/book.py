from sqlalchemy.orm import Session
from ..models import Book
from ..schemas.book import BookCreate

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()

def create_book(db: Session, book: BookCreate):
    db_book = Book(
        title=book.title,
        isbn=book.isbn,
        year=book.year,
        total_copies=book.total_copies,
        available_copies=book.total_copies,
        author_id=book.author_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book