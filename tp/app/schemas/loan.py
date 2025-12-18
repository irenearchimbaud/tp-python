from datetime import datetime
from pydantic import BaseModel, EmailStr


class LoanBase(BaseModel):
    borrower_name: str
    borrower_email: EmailStr
    book_id: int


class LoanCreate(LoanBase):
    pass


class LoanRead(LoanBase):
    id: int
    loan_date: datetime
    return_date: datetime | None

    class Config:
        from_attributes = True