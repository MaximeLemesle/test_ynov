# Projet Bibliothèque

## Installation

1. Cloner le dépôt ou télécharger le projet.
2. Se placer dans le dossier `bibliotheque_projet`.
3. Créer un environnement virtuel :
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Tests

Pour lancer tous les tests :

```bash
pytest
```

Ou avec le Makefile :

```bash
make test
```

## Couverture

Pour générer un rapport de couverture :

```bash
pytest --cov=src/bibliotheque --cov-report=html
```

Le rapport HTML sera disponible dans le dossier `htmlcov/index.html`.

Avec le Makefile :

```bash
make coverage
```

## Structure

- `src/bibliotheque/` : contient le code métier (Book, User, Library)
- `tests/` : contient les tests unitaires organisés par fonctionnalité
- `requirements.txt` : liste des dépendances
- `pytest.ini` : configuration de pytest
- `Makefile` : commandes d'automatisation (tests, couverture, nettoyage)
- `.github/workflows/` : configuration de l'intégration continue (GitHub Actions)

Cette organisation sépare clairement le code source, les tests et les outils d'automatisation pour faciliter la maintenance et la collaboration.
