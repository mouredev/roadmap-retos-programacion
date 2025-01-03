
      * CMENTARIO PERSONAL: 
      * No conozco nada de COBOL, pero al verlo en el roadmap de midudev
      * me llamo la atención. 
      * Todo lo echo es a partir de la documentación de IBM, 
      * la IA de Gemini y los ejemplos de los usuarios.

      * 1. URL documentación no oficial: 
      * https://www.ibm.com/docs/es/i/7.3?topic=languages-cobol - IBM COBOL

       IDENTIFICATION DIVISION.
       PROGRAM-ID. ROADMAP-MIDUDEV-00.
       AUTHOR. LLONARDO798.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       
      * 2. Formas de añadir comentarios

      * Comentarios con * al inicio en la columna 7 de la linea.
      * hasta la columna 80.
      / Comentario que provoca un salto de página en el listado de compilación.
      *> Comentario flotante, todo lo puesto despues de *> es un comentario. 
      *> Se puede colocar en cualquier columna de la linea de codigo. 
      *REMARKS. 
      *    Este programa realiza cálculos matemáticos básicos.
      *    Fue creado el 20 de septiembre de 2023.
      * REMARKS no es soportado por todos los compiladores, aunque es parte del
      * estandar COBOL original.

      * 3. Variables y constantes
      * Variable numerica entera
      
      * En COBOL, las variables no existen de forma aislada. La declaración 01 
      * crea un registro o grupo de datos llamado VARIABLES.
       01  VARIABLES.
           03 WS-NOMBRE PIC X(20).

      * Variables CONSTANTES no hay en COBOL, pero se puede definir un valor
      * inicial con VALUE.
       
           03 NUM-CONST PIC 99 VALUE 100.

      * 4. Tipos de datos primitivos no existen, estos son los "fundamentales"
           03  WS-CADENA PIC X(20) VALUE "Cobol". 
           *> Cadena de texto de 20 caracteres

           03  WS-EDAD          PIC 9(3).    *> Número entero de hasta 3 dígitos
           03  WS-NUMERO        PIC 99.      *> Digitos numericos de 0-99
           03  WS-NEGATIVO      PIC S9.      *> Número entero negativo
           03  WS-SALARIO       PIC 9(7)V99. *> Números decimales 
                                             *> 7 enteros y 2 decimales
           03  WS-SALARIO-X     PIC 9V99.    *> Número decimal, la V indica la
                                             *> posición del punto decimal
           03  WS-ES-MAYOR-EDAD PIC A(3).    *> "SI" o "NO" (alfabético)
           03  WS-CODIGO-POSTAL PIC X(5).    *> Código postal (alfanumérico)
           03  WS-BINARIO       PIC 9(7)V9 COMP. 
           *> Número almacenado en memoria en formato binario 1/0

      * 5. Impresión por consola

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           MOVE "LEONARDO-AEDO" TO WS-NOMBRE.
           DISPLAY WS-NOMBRE.
           DISPLAY "¡Hola, " WS-CADENA "!".
           STOP RUN.
       END PROGRAM ROADMAP-MIDUDEV-00.