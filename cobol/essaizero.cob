       IDENTIFICATION DIVISION. 
       PROGRAM-ID. ESSAI1.
      * Ce programme teste le comportement
      * du mot cle ZERO ou ZEROS
      * Pas de difference 
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
         77 MADONNEE PIC X(10) VALUE ZERO.
         77 MADONNEE2 PIC X(10) VALUE ZEROS.
         77 MADONNEE3 PIC X(10) VALUE "1234567890".
       PROCEDURE DIVISION.
            DISPLAY "BONJOUR ERIC".
            move MADONNEE to MADONNEE3.
            display  MADONNEE3.
            move MADONNEE2 to MADONNEE3.
            display  MADONNEE3.
               STOP RUN.
 
