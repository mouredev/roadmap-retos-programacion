      ******************************************************************
      * - Crea un comentario en el código y coloca la URL del sitio web oficial del
      *   lenguaje de programación que has seleccionado.
      * - Representa las diferentes sintaxis que existen de crear comentarios
      *   en el lenguaje (en una línea, varias...).
      * - Crea una variable (y una constante si el lenguaje lo soporta).
      * - Crea variables representando todos los tipos de datos primitivos
      *   del lenguaje (cadenas de texto, enteros, booleanos...).
      * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
      * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
      * debemos comenzar por el principio.
      ******************************************************************
      * https://www.ibm.com/docs/es/i/7.3?topic=languages-cobol
      * Se puede consultar documentacion sobre el lenguaje
      ******************************************************************

       IDENTIFICATION DIVISION.
       PROGRAM-ID. RETO-00.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01  TIPOS-DE-VARIABLES.
           03 LETRAS PIC A(11) VALUE "Alfabeticas".
           03 ALFANUMERICAS PIC X(10) VALUE "abc123#$_%".
           03 NUMEROS-NATURALES PIC 9999 VALUE 1234.
           03 NUMEROS-ENTEROS PIC S9999 VALUE -1234.
           03 RACIONALES-SIN-SIGNO PIC 99V99 VALUE 12.34.
           03 RACIONALES-CON-SIGNO PIC S99V99 VALUE -12.34.
      * Nombre del lenguaje.
           03 NOMBRE PIC X(5).
       01  CONSTANTE.
           03  FILLER PIC X(25) VALUE "-------------------------".
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           DISPLAY "Tipos de variables.".
           DISPLAY LETRAS ": Con solo letras".
           DISPLAY "alfanumericas: letras, numeros y simbolos "
           ALFANUMERICAS.
           DISPLAY "Con numeros enteros positivos: " NUMEROS-NATURALES.
           DISPLAY "Con numeros enteros positivos y negativos: "
           NUMEROS-ENTEROS.
           DISPLAY "Con numeros positivos con decimales: "
           RACIONALES-SIN-SIGNO.
           DISPLAY
           "Con numeros positivos y negativos con decimales: "
           RACIONALES-CON-SIGNO.
           MOVE "COBOL" TO NOMBRE.
           DISPLAY CONSTANTE.
           DISPLAY "Hola, " NOMBRE.
           STOP RUN.
       END PROGRAM RETO-00.
