# SysWatch

Outil de monitoring système en Python.

## Fonctionnalités
- Collecte CPU / RAM / Disques
- Historique SQLite
- Statistiques 24h
- Export JSON
- CLI avec argparse

## Installation
```bash
pip install psutil
```

## Différentes commandes:

```bash
python syswatch_final.py
python syswatch_final.py --collect --interval 30
python syswatch_final.py --stats
python syswatch_final.py --export data.json
python syswatch_final.py --cleanup 7
```