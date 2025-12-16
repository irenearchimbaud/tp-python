from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    isbn: str
    year: int
    total_copies: int
    author_id: int


class BookCreate(BookBase):
    """
    Schéma pour créer un livre
    """
    pass


class BookRead(BookBase):
    """
    Schéma retourné par l'API
    """
    id: int

    class Config:
        from_attributes = True