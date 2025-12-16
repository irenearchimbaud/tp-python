from sqlalchemy import Column, Integer, String, ForeignKey
from ..database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    isbn = Column(String, unique=True, index=True)
    year = Column(Integer)
    total_copies = Column(Integer)
    available_copies = Column(Integer)
    author_id = Column(Integer, ForeignKey("authors.id"))