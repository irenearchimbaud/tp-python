from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import book as crud_book
from ..schemas.book import BookCreate, BookRead
from ..dependencies import get_db

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=BookRead)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return crud_book.create_book(db, book)

@router.get("/", response_model=list[BookRead])
def list_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_book.get_books(db, skip=skip, limit=limit)