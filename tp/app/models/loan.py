from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from ..database import Base


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    borrower_name = Column(String, nullable=False)
    borrower_email = Column(String, nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    loan_date = Column(DateTime, default=datetime.utcnow)
    return_date = Column(DateTime, nullable=True)
    
    book = relationship("Book")