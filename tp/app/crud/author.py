from sqlalchemy.orm import Session
from ..models import Author
from ..schemas.author import AuthorCreate

def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Author).offset(skip).limit(limit).all()

def create_author(db: Session, author: AuthorCreate):
    db_author = Author(
        first_name=author.first_name,
        last_name=author.last_name,
        birth_date=author.birth_date,
        nationality=author.nationality
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author