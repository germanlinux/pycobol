       IDENTIFICATION DIVISION.
       PROGRAM-ID. ESSAI1.
      * Ce programme teste le comportement des mots cles 
      * SpaCE et SPACES : même comportement 
      * L'instruction LENGTH OF donne la longueur d une zone
      *
      *
      *
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
         77 MADONNEE PIC X(10) VALUE SPACE.
         77 MADONNEE2 PIC X(10) VALUE SPACES.
         77 MADONNEEX PIC X(3) VALUE "ABC".
         77 MADONNEE3 PIC X(10) VALUE "1234567890".
         77 MADONNEE4 PIC X(20) VALUE "12345678901234567890".
         77 AC PIC S9999 COMP.
       PROCEDURE DIVISION.
            DISPLAY "BONJOUR ERIC".
            move MADONNEE to MADONNEE3.
            display  MADONNEE3.
            move "1234567890" to MADONNEE3.
            move MADONNEE2 to MADONNEE3.
            display  MADONNEE3.
            move MADONNEE2 to MADONNEE4.
            display  MADONNEE4.
            move MADONNEEX to MADONNEE4.
            display  MADONNEE4 MADONNEE4.
            display length of MADONNEE " X " length of AC.
            STOP RUN.
      * BONJOUR ERIC
      *    
      *   
      *              
      *ABC                 ABC                 
      *10 X 2
      

