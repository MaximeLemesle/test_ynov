# TP3 - Organisation et Automatisation des Tests

## Partie 1 : Créer la structure du projet

### Étape 1 : Analyser une structure mal organisée

1. **Quels problèmes voyez-vous dans cette organisation ?**

   - Les fichiers de tests et de code sont mélangés.
   - Les noms de fichiers ne suivent pas de convention.
   - Difficile de repérer les fichiers de tests et le code source.

2. **Comment un nouveau développeur s'y retrouverait-il ?**

   - Il aurait du mal à comprendre l'architecture du projet.
   - Il risque de ne pas respecter les conventions.

3. **Comment lancer tous les tests d'un coup ?**
   - Il n'existe pas de commande pour exécuter tous les tests automatiquement.
   - Il faudrait lancer chaque fichier de test à la main.

### Étape 2 : Créer la structure recommandée

- La nouvelle architecture est meilleure car elle sépare le code, les tests et les fichiers de configuration. De plus, cette organisation permet d'automatiser l'exécution des tests.

## Partie 5 : Lancement et couverture

### Étape 10 : Lancer les tests de différentes façons

1. **pytest**

- Lance tous les tests du dossier défini dans pytest.ini.

2. **pytest -v**

- Affiche le nom de chaque test et son résultat.
- Permet de mieux repérer les tests exécutés et leur statut.

3. **pytest tests/test_book.py**

- Lance uniquement les tests du fichier `test_book.py`.
- Pratique pour cibler une fonctionnalité précise.

4. **pytest tests/test_book.py::TestBookCreation::test_create_valid_book**

- Lance un test précis.
- Utile pour déboguer un cas particulier.

**Différences d'affichage :**

- Plus on cible, plus l'affichage est court et précis.
- L'option `-v` donne plus de détails sur chaque test.

### Étape 11 : Générer le rapport de couverture

1. **Quel pourcentage de couverture avez-vous ?**

   - Le pourcentage de couverture est de 86%.

2. **Quelles lignes ne sont pas testées ? Pourquoi ?**

   - Il s'agit souvent de cas d'erreur ou d'exceptions qui n'ont pas été gérées dans les tests.

3. **Comment améliorer la couverture ?**
   - Ajouter des tests pour couvrir tous les cas, notamment les cas d'erreur et les exceptions.
   - Vérifier que chaque branche conditionnelle (if/else) est testée.
   - Utiliser le rapport HTML pour cibler précisément les lignes manquantes.

## Partie 7 : Analyse et bonnes pratiques

### 1. Structure des tests

- Les tests suivent la même organisation que le code source : un dossier `src/bibliotheque` pour le code métier, un dossier `tests` pour les tests.
- Les noms de fichiers sont cohérents et explicites (`test_book.py`, `test_library.py`, etc.).

### 2. Nommage des tests

- Chaque fonction de test a un nom explicite qui décrit ce qu'elle vérifie.
- Les classes de test regroupent logiquement les tests par fonctionnalité (création, emprunt, etc.).

### 3. Couverture

- Les parties du code non testées sont généralement des cas d'erreur ou des exceptions peu courantes.
- Il n'y a pas de tests redondants, chaque test cible un comportement précis.

### 4. Automatisation

- Une seule commande (`make test` ou `pytest`) permet de lancer tous les tests.
- Un nouveau développeur peut facilement contribuer grâce à la structure claire et à l'automatisation (Makefile, GitHub Actions).

### 5. Maintenance

- Cette organisation facilite l'ajout de nouvelles fonctionnalités : il suffit d'ajouter le code dans `src/bibliotheque` et les tests associés dans `tests`.
- La séparation claire et les conventions de nommage réduisent les risques d'erreur et accélèrent la prise en main du projet.

## Partie 8 : Rapport final

### Rapport final : 97% 🎉

## Reflexion finale

1. **Organisation :**

- Cette structure rend le projet lisible, et facilite la maintenance. N'importe qui peux le comprendre.

2. **Automatisation :**

- Les outils comme Makefile, pytest et GitHub Actions permettent à toute l’équipe de lancer les tests automatiquement et simplement.

3. **Couverture :**

- Un taux de couverture élevé ne garantit pas l’absence de bugs, mais il réduit les risques d’oublier des cas importants.

4. **Intégration continue :**

- GitHub Actions exécute automatiquement les tests à chaque commit, ce qui permet de détecter immédiatement les problèmes.

5. **Maintenance :**

- L’organisation claire permet d’ajouter ou modifier des fonctionnalités sans tout casser, et de facilement ajouter les nouveaux tests.
