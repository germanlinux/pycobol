       IDENTIFICATION DIVISION. 
       PROGRAM-ID. ESSAI1.
      * Ce programme teste le comportement
      * du mot cle ZERO ou ZEROS
      * Pas de difference 
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SPECIAL-NAMES. 
       decimal-point is comma.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 nivsup.
          05 NEE2 PIC 999.
          05 MADONNEE3 PIC 999.
  

       PROCEDURE DIVISION.
            display  nivsup.
            move 1234 to nivsup.
            DISPLAY "BONJOUR ERIC".
            display  nivsup "suite".
            display nivsup.
            display  nivsup "suite".
            display  NEE2"suite".
            display  MADONNEE3"suite".
            

       STOP RUN.
 
