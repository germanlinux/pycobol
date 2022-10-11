       IDENTIFICATION DIVISION. 
       PROGRAM-ID. ESSAI1.
      * Ce programme teste le comportement
      * du mot cle ZERO ou ZEROS
      * Pas de difference 
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
         77 MADONNEE PIC X(10) VALUE 4.
         77 MADONNEE2 PIC X(10) VALUE "4".
         77 MADONNEE3 PIC X(10) value zero.
         77 MADONNEE4 PIC X(10) value space.
       PROCEDURE DIVISION.
            DISPLAY "BONJOUR ERIC".
            display  MADONNEE.
            display  MADONNEE2.
            display  MADONNEE3.
            display  MADONNEE4   MADONNEE3.
       STOP RUN.
 
