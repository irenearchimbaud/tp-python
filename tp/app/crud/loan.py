from sqlalchemy.orm import Session
from ..models import Loan, Book
from ..schemas.loan import LoanCreate
from datetime import datetime, timedelta

def create_loan(db: Session, loan: LoanCreate):
    book = db.query(Book).filter(Book.id == loan.book_id).first()
    if not book or book.available_copies < 1:
        return None
    book.available_copies -= 1
    db_loan = Loan(
        borrower_name=loan.borrower_name,
        borrower_email=loan.borrower_email,
        book_id=loan.book_id,
        loan_date=datetime.utcnow(),
        return_date=datetime.utcnow() + timedelta(days=14)
    )
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan

def get_loans(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Loan).offset(skip).limit(limit).all()