from datetime import datetime
from pydantic import BaseModel, EmailStr


class LoanBase(BaseModel):
    borrower_name: str
    borrower_email: EmailStr
    book_id: int


class LoanCreate(LoanBase):
    """
    Schéma pour créer un emprunt
    """
    pass


class LoanRead(LoanBase):
    """
    Schéma retourné par l'API
    """
    id: int
    loan_date: datetime
    return_date: datetime | None

    class Config:
        from_attributes = True