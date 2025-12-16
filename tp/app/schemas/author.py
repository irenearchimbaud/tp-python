from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    """
    Schéma pour créer un auteur
    """
    pass


class AuthorRead(AuthorBase):
    """
    Schéma retourné par l'API
    """
    id: int

    class Config:
        from_attributes = True