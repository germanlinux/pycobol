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

Il est possible d'instancier des structures Python se comportant comme des zones COBOL.
Un eventail de classe est proposé pour manipuler des zones simples, zones groupes etc.



Point d'etape
-------------

Le projet utilise POETRY pour sa mise en oeuvre.
Le traitement des zones élémentaires  de niveau 77 est en cours de developpement
Pycobol utilise deux types de test:
- Doctest pour les tests de non regression
- unittest pour les tests plus complets.
Utilisation de SPHINX pour la documentation


Depuis le répertoire du projet:
-------------------------------

Pour lancer les tests intégrés.

 python .\pycobol\zonage.py
ou poetry run python .\pycobol\zonage.py

Pour lancer les tests complets:

python -m unittest discover
ou poetry run python -m unittest discover

Utilisation
===========

Le module fonctionne en 2modes:

* Soit en fournissant les lignes COBOL
* Soit en instanciant soi-même les objets à manipuler

Exemple à partir du COBOL::

    zg2 ='''
                10            MADATE.                                   
                    11            AAAA   PICTURE  9(4).                 
                    11            MOIS   PICTURE  99.                      
                    11            JJ   PICTURE  99.                 
                10   DATEBRUT REDEFINE MADATE PIC 9(8).'''     

Utiliser la méthode : ZoneGroupe.fake_read_file_redefine(zg2) (mise en token)
Puis la methode: ZoneGroupe.read_groupe_from_code(tlignes)  (mise en objet)

5 instances seront disponibles prefixées par '_' suivi du nom cobol en minuscule (_mois , etc)  




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
- concevoir la classe des zones groupes: FAIT
- Developper la prise en charge des clauses de formatage (exemple BLANK WHEN ZERO):  A FAIRE
- Prendre en charge les clauses redefine : FAIT
- Prendre en charge les FILLERS: A FAIRE
- Prendre en charge les clauses OCCURS : A FAIRE

Merci

Eric German

Journal
=======

Le 27/12/22:
Mise en place de la documentation avec SPHINX
Publication de la documentation sur le site read the docs
Refactorisations profondes

Le 23/11/2022:
--------------
Refactorisation encore et encore
Fin du developpement des zones groupes mais il reste le probleme de la retropropagation
Developpment d'une méthode d ajout dynamique à l'espace de nommage: les zones COBOL sont accessibles préfixées par un '_'


Le 28/10/2022:
--------------
Refactorisation du code.

Reorganisation du dépot.

Début du developpement des zones groupes.


Le 08/10/2022: 
--------------
Ajout d'un repertoire COBOL qui contiendra des sources COBOL pour étudier le comportement 
de GnuCOBOL 

Developpement du premier exemple de programme utilisant pycobol qui mnanipule des zones de niveau 77

