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
         77 MADONNEE PIC X(10) VALUE 4.
         77 MADONNEE2 PIC X(10) VALUE "4".
         77 MADONNEE3 PIC X(10) value zero.
         77 MADONNEE4 PIC X(10) value space.
         77 MADONNEE5 PIC S9(4) value -1234.
         77 MADONNEE6 PIC S9(4)V99 value 1234,56 .
         77 MADONNEE7 PIC 9(6) value 111111.
         77 A PIC 99.

       PROCEDURE DIVISION.
            DISPLAY "BONJOUR ERIC".
            display  MADONNEE.
            display  MADONNEE2.
            display  MADONNEE3.
            display  MADONNEE4   MADONNEE3.
            display  MADONNEE5.
            move +12345 to MADONNEE5.
            display  MADONNEE5.
            move MADONNEE7 to MADONNEE6
            display  MADONNEE6.
            move -123 to A.
            display A.
       STOP RUN.
 
