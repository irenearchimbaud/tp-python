from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class AuthorCreate(BaseModel):
    first_name: str
    last_name: str
    nationality: str


class AuthorOut(AuthorCreate):
    id: int

    class Config:
        from_attributes = True


class BookCreate(BaseModel):
    title: str
    isbn: str = Field(..., min_length=13, max_length=13)
    year: int = Field(..., ge=1450)
    total_copies: int = Field(..., gt=0)
    author_id: int


class BookOut(BookCreate):
    id: int
    available_copies: int

    class Config:
        from_attributes = True


class LoanCreate(BaseModel):
    borrower_name: str
    borrower_email: EmailStr
    book_id: int


class LoanOut(LoanCreate):
    id: int
    return_date: Optional[str]

    class Config:
        from_attributes = True