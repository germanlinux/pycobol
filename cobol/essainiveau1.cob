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
          05 NEE2 PIC X(10) VALUE "4".
          05 MADONNEE3 .
             06  MADONNEE4 PIC X(10) value "ABCDEFGHIJ".
       77  MADONNEE PIC XXXXX value "ABCDE".

       PROCEDURE DIVISION.
            display  nivsup.
            move 12345678 to nivsup.
            DISPLAY "BONJOUR ERIC".
            display  nivsup "suite".
            display MADONNEE.
            MOVE "ER" to MADONNEE.
            display MADONNEE"suite".
            
       STOP RUN.
 
