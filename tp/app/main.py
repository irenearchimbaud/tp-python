from fastapi import FastAPI
from .database import Base, engine
from .routers import authors, books, loans

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library API", version="1.0")

app.include_router(authors.router)
app.include_router(books.router)
app.include_router(loans.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Library API"}