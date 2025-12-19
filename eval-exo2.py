from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()  # base pour tous les modèles SQLAlchemy

class Book(Base): 
    __tablename__ = "books"  # nom de la table en bdd et ci dessous modele pour la bdd
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    titre = Column(String, nullable=False)
    auteur = Column(String, nullable=False)
    isbn = Column(String, unique=True)
    annee_publication = Column(Integer)
    disponible = Column(Boolean, default=True)
    date_ajout = Column(DateTime, default=datetime.now)

class BookCreate(Book):  # utilisé pour créer un livre (pas besoin d'id ni date ajout)
    pass

class BookUpdate(Book):  # champs optionnels pour mise à jour
    titre: str | None = None
    isbn: str | None = None
    auteur: str | None = None
    annee_publication: int | None = None
    disponible: bool | None = None

class BookRead(Book):  # utilisé pour la lecture simple, ça retourbne tous les champs
    id: int

    class Config:
        orm_mode = True  # pour que Pydantic lises les objets SQLAlchemy direct