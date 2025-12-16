from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import author as crud_author
from ..schemas.author import AuthorCreate, AuthorRead
from ..dependencies import get_db

router = APIRouter(prefix="/authors", tags=["Authors"])

@router.post("/", response_model=AuthorRead)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return crud_author.create_author(db, author)

@router.get("/", response_model=list[AuthorRead])
def list_authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_author.get_authors(db, skip=skip, limit=limit)