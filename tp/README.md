# Library API

API REST de gestion de bibliothèque développée avec FastAPI.

## Installation
Se mettre a la racine du projet. Première commande pour installer les dépendances, deuxieme comamnde pour lancer l'api
```bash
python -m pip install -r tp/requirements.txt
python -m uvicorn tp.app.main:app --reload
python -m pip install "pydantic[email]"
```

## Ouvrir projet
http://127.0.0.1:8000/docs dans le navigateur