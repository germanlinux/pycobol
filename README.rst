Projet pycobol
==============

Objectifs
---------

Le langage COBOL est partout et il sera difficile de s'en débarrasser.
Des solutions de transformation plus ou moins automatiques existent.

Pycobol est avant tout une expérience visant à :
- Passer du COBOL  au Python
- Convertir des structures COBOL en objets Python
- Offrir des facilités de manipulations.

Principes.
----------

La première étape vise à convertir la DATA-DIVISION  en objet Python
Puis à utiliser des méthodes pour retranscrire les manipulations COBOL en Python.

Point d'etape
-------------

Le projet utilise POETRY pour sa mise en oeuvre.
Le traitement des zones élémentaires  de niveau 77 est en cours de developpement
Pycobol utilise deux types de test:
- Doctest pour les tests de non regression
- unittest pour les tests plus complets.

Depuis le répertoire du projet:
-------------------------------

Pour lancer les tests intégrés.

 python .\pycobol\zonage.py
ou poetry run python .\pycobol\zonage.py

Pour lancer les tests complets:

python -m unittest discover
ou poetry run python -m unittest discover

Comment contribuer ? .
======================

- En installant le projet

et en ajoutant des cas de test dans le fichier pic77ok.txt

- En developpant des nouveaux traitements de format.
- En faisant des refactorisations de code.
- Ajouter de la documentation
- En apportant des idées.

Feuille de route.
=================

- Developper la prise en charge des formats non pris en charge (exemple COMP ) FAIT
- concevoir la classe des zones groupes: A FAIRE
- Developper la prise en charge des clauses de formatage (exemple BLANK WHEN ZERO):  A FAIRE


Merci

Eric German

Journal
=======
Le 08/10/2022: 
--------------
Ajout d'un repertoire COBOL qui contiendra des sources COBOL pour étudier le comportement 
de GnuCOBOL 

Developpement du premier exemple de programme utilisant pycobol qui mnanipule des zones de niveau 77
