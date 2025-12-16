from sqlalchemy.orm import Session
from .. import models, schemas

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
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

def update_book(db: Session, book_id: int, book_update: schemas.BookUpdate):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        return None
    for key, value in book_update.dict(exclude_unset=True).items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        return False
    active_loans = db.query(models.Loan).filter(models.Loan.book_id == book_id, models.Loan.return_date == None).count()
    if active_loans > 0:
        return False
    db.delete(book)
    db.commit()
    return True