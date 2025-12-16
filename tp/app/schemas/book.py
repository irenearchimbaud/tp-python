from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    isbn: str
    year: int
    total_copies: int
    author_id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    title: str | None = None
    isbn: str | None = None
    year: int | None = None
    total_copies: int | None = None
    author_id: int | None = None

class BookRead(BookBase):
    id: int

    class Config:
        from_attributes = True