Tutorial PyCOBOL
================

Contexte
--------

PyCOBOL a été développé avec comme objectif principal d'avoir a mettre en place 
un projet de grande empleur. Le but est avant tout pédagogique: utlisation d'environnement virtuel
doctests, tests , couverture de code, documentation etc.

Le COBOL est un pretexte comme un autre mais je me suis pris au jeu.

L'idée n'etait pas d'ecrire un compilateur COBOL en Python mais 
de donner à un programmeur COBOL des structures se comportant comme les variables COBOL.

J'ai ajouté des parsers qui permettent à partir de lignes COBOL d'instancier des objets Python.

Un programme COBOL a principalement deux parties distinctes: la description des données et la partie procedure. On retourve dans PyCOBOL cette distinction.


Installation
------------

Il n'y a pas encore de paquet installable par la commande PIP
Aussi l'installation se fait par clonage du dépot github.

Contenu des répertoires
-----------------------

Le répertoire exemples contient des petits programmes d'essai.

Le répertoire cobol contient les sources de petits programmes cobol.
Ils peuvent etre compilés avec opencobol. 