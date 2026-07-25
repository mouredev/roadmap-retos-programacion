      * TEST: https://www.jdoodle.com/execute-cobol-online CAMBIAR ESPACIOS AL
      * INICIO POR TABULACIONES
      * EJERCICIO:
      * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
      *   Aritméticos, lógicos, de comparación, asignación, identidad, 
      *   pertenencia, bits... (Ten en cuenta que cada lenguaje puede poseer 
      *   unos diferentes)
      * - Utilizando las operaciones con operadores que tú quieras, crea 
      *   ejemplos que representen todos los tipos de estructuras de control que
      *   existan en tu lenguaje:
      *   Condicionales, iterativas, excepciones...
      * - Debes hacer print por consola del resultado de todos los ejemplos.
      *
      *DIFICULTAD EXTRA (opcional):
      *Crea un programa que imprima por consola todos los números comprendidos
      *entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3

       IDENTIFICATION DIVISION.
       PROGRAM-ID. ROADMAP-MIDUDEV-01.
       AUTHOR. LLONARDO798.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.

       01 NUMEROS.
           03 NUM1 PIC 99 VALUE 10.
           03 NUM2 PIC 9 VALUE 5.
           03 NUM3 PIC 9 VALUE 3.
           03 COPIA PIC 9.
           03 TOTAL PIC 99.
           03 TOTALEXP PIC 999999.

       01 OTROS.
           03 COPIA PIC 9(3).
           03 MENSAJE PIC X(50).

       01 I PIC 99.
    
         

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
      *1. Operadores Aritméticos
           COMPUTE TOTAL = NUM1 + NUM2. *> Operador de suma
           DISPLAY "SUMA: " TOTAL. *> 15

           COMPUTE TOTAL = NUM1 - NUM2. *> Operador de resta
           DISPLAY "RESTA: " TOTAL. *> 5

           COMPUTE TOTAL = NUM1 * NUM2. *> Operador de multiplicación
           DISPLAY "MULTIPLICACIÓN: " TOTAL. *> 50

           COMPUTE TOTAL = NUM1 / NUM2. *> Operador de división
           DISPLAY "DIVISIÓN: " TOTAL. *> 2

           COMPUTE TOTALEXP = NUM1 ** NUM2. *> Operador de exponenciación
           DISPLAY "EXPONENCIACIÓN: " TOTALEXP. *> 100000

           *> No es una operación aritmética, pero como función se puede usar
           *> para obtener el resto de una división
           COMPUTE TOTAL = FUNCTION MOD(NUM1, NUM3). 
            DISPLAY "RESTO: " TOTAL. *> 1

      *2. Operadores Relacionales - Ejemplos usando IF

           IF NUM1 = NUM2 THEN
               DISPLAY "NUM1 es igual a NUM2"
           ELSE
                DISPLAY "NUM1 no es igual a NUM2"
           END-IF.

           IF NUM1 > NUM2 THEN
               DISPLAY "NUM1 es mayor que NUM2"
           ELSE
                DISPLAY "NUM1 no es mayor que NUM2"
           END-IF.

           IF NUM1 < NUM2 THEN
             DISPLAY "NUM1 es menor que NUM2"
           ELSE
              DISPLAY "NUM1 no es menor que NUM2"
           END-IF.

           IF NUM1 >= NUM2 THEN
               DISPLAY "NUM1 es mayor o igual que NUM2"
           ELSE
                DISPLAY "NUM1 no es mayor o igual que NUM2"
           END-IF.

           IF NUM1 <= NUM2 THEN
           DISPLAY "NUM1 es menor o igual que NUM2"
           ELSE
               DISPLAY "NUM1 no es menor o igual que NUM2"
           END-IF.

           IF NUM1 <> NUM2 THEN
           DISPLAY "NUM1 es distinto de NUM2"
           ELSE
               DISPLAY "NUM1 no es distinto de NUM2"
           END-IF.

      *3. Operadores Lógicos
           
           IF NUM1 = NUM2 AND NUM1 > NUM3 THEN
             DISPLAY "NUM1 es igual a NUM2 y mayor que NUM3"
           ELSE
              DISPLAY "NUM1 no es igual a NUM2 y mayor que NUM3"
           END-IF.
    
           IF NUM1 = NUM2 OR NUM1 > NUM3 THEN
             DISPLAY "NUM1 es igual a NUM2 o mayor que NUM3"
           ELSE
              DISPLAY "NUM1 no es igual a NUM2 o mayor que NUM3"
           END-IF.

           IF NOT NUM2 = 1  *> Se niega la condición
             DISPLAY "NUM 2 no es igual a 1"
           ELSE
             DISPLAY "NUM 2 es igual a 1"
           END-IF.
           

      *4. Otros Operadores
           
           MOVE 30 TO NUM1. *> Asignación usando MOVE
           DISPLAY "NUM1 Despues del MOVE: " NUM1.
           COMPUTE TOTAL = 25*2. *> Se calcula el valor usando COMPUTE
           DISPLAY "NUM1 Despues del COMPUTE: " NUM1.

           MOVE 17 TO COPIA OF OTROS.    
           *> Aunque se tienen dos variables con el mismo nombre en diferentes
           *> grupos, se puede acceder a la variable COPIA del grupo OTROS


      * DIFICULTAD EXTRA - Crea un programa que imprima por consola todos los 
      * números comprendidos entre 10 y 55 (incluidos) pares, y que no son ni el
      * 16 ni múltiplos de 3.

           PERFORM PRINT-NUMBERS VARYING I FROM 10 BY 2 UNTIL I > 55.


           STOP RUN.

       PRINT-NUMBERS.
           IF I <> 16 AND FUNCTION MOD(I, 3) <> 0 THEN
             DISPLAY I.

       END PROGRAM ROADMAP-MIDUDEV-01.