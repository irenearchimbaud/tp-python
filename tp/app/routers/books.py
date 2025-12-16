from fastapi import APIRouter
from typing import List
from .. import schemas, crud
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from ..dependencies import get_db

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=List[schemas.BookRead])
async def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@router.get("/{book_id}", response_model=schemas.BookRead)
async def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.post("/", response_model=schemas.BookRead)
async def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@router.put("/{book_id}", response_model=schemas.BookRead)
async def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    return crud.update_book(db, book_id, book)

@router.delete("/{book_id}", response_model=schemas.BookRead)
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    return crud.delete_book(db, book_id)