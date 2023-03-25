PyCOBOL was developed with the main objective of having to set up
a large-scale project. The goal is above all educational: use of virtual environment
doctests, tests, code coverage, documentation etc.

COBOL is a pretext like any other but I got caught up in the game.

The idea was not to write a COBOL compiler in Python but
to give a COBOL programmer structures that behave like COBOL variables.

I added parsers which allow from COBOL lines to instantiate Python objects.

A COBOL program mainly has two distinct parts: the data description and the procedure part. We return in PyCOBOL this distinction.


Installation
------------

The installation is done by cloning the github repository or by the *pip* command:

*pip install pycobol*