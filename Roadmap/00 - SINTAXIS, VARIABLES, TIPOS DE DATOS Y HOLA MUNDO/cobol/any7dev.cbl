     /*
      *    -Crea un comentario en el código y coloca la URL del sitio
      *    web oficial del lenguaje de programación que has seleccionado
      *    -Representa las diferentes sintaxis que existen de crear
      *    comentarios en el lenguaje (en una línea, varias...).
      *    -Crea una variable (y una constante).
      *    -Crea variables representando todos los tipos de datos
      *    primitivos del lenguaje (cadenas de texto, enteros...)
      *    - Imprime por terminal el texto: "¡Hola, [y el nombre de tu
      *    lenguaje]!"
     */

      *    No es la oficial https://es.wikipedia.org/wiki/COBOL

      *    Esto es una forma de poner comentarios
      *>   Esta es otra forma de añadir comentarios

       IDENTIFICATION DIVISION.
       PROGRAM-ID. RETO-0.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
      *    Variable
           77 VAR PIC 9.
      *    Constante
           01 VAR-CONS CONSTANT AS 100.
      *    Variable numerica entera
           77 NUM-INT PIC 9.
      *    Variable numerica entera negativa
           77 INT-NEG PIC S9.
      *    Variable numerica decimal
           77 NUM-FLOAT PIC 9V99.
      *    Variable numerica decimal negativa
           77 FLOAT-NEG PIC S9V99.
      *    Cadena
           77 CADENA PIC X.
      *    Cadena sin numeros
           77 CAD-A PIC A.
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
            DISPLAY "¡Hola, COBOL!"
            STOP RUN.
       END PROGRAM RETO-0.
