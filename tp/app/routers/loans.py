from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import loan as crud_loan
from ..schemas.loan import LoanCreate, LoanRead
from ..dependencies import get_db

router = APIRouter(prefix="/loans", tags=["Loans"])

@router.post("/", response_model=LoanRead)
def create_loan(loan: LoanCreate, db: Session = Depends(get_db)):
    db_loan = crud_loan.create_loan(db, loan)
    if not db_loan:
        raise HTTPException(status_code=400, detail="Book not available")
    return db_loan

@router.get("/", response_model=list[LoanRead])
def list_loans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_loan.get_loans(db, skip=skip, limit=limit)