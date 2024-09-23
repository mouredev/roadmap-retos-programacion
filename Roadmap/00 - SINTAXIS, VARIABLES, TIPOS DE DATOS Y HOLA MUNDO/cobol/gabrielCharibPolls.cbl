      *    -Crea un comentario en el código y coloca la URL del sitio
      *    web oficial del lenguaje de programación que has seleccionado
      *    -Representa las diferentes sintaxis que existen de crear
      *    comentarios en el lenguaje (en una línea, varias...).
      *    -Crea una variable (y una constante).
      *    -Crea variables representando todos los tipos de datos
      *    primitivos del lenguaje (cadenas de texto, enteros...)
      *    - Imprime por terminal el texto: "¡Hola, [y el nombre de tu
      *    lenguaje]!"
      **************************************************************************
      *    commentaire  
      **************************************************************************
      *      Voici un commentaire en Cobol
      *      URL officielle de GnuCOBOL: https://gnucobol.sourceforge.io/
       IDENTIFICATION DIVISION.
       PROGRAM-ID. RETO-O.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
      **************************************************************************
      *    Variables 
      **************************************************************************
           77 MY-VARIABLE    PIC 9(5) VALUE 12345.
           77 MY-STRING      PIC X(20) VALUE "COBOL Language".
      **************************************************************************
      *    Type de données primitifs
      **************************************************************************
           77 MY-INTEGER     PIC 9(5) VALUE 12345.
           77 MY-TEXT        PIC X(20) VALUE "HOLA COBOL".
           77 MY-DECIMAL     PIC 99V99 VALUE 13.14.  
           77 MY-BOOLEAN     PIC X VALUE "T".
      **************************************************************************     
      * Afficher un message dans le terminal
      **************************************************************************
       PROCEDURE DIVISION.
           DISPLAY "***************************".
           DISPLAY "¡Hola, COBOL!".
           DISPLAY "Valor de MY-VARIABLE : " MY-VARIABLE.
           DISPLAY "Texto en MY-TEXT : " MY-TEXT.
           DISPLAY "Valor de MY-INTEGER : " MY-INTEGER.
           DISPLAY "Valor de MY-DECIMAL : " MY-DECIMAL.
           DISPLAY "Booleano MY-BOOLEAN : " MY-BOOLEAN.
           DISPLAY "***************************".
           STOP RUN.



      







 
