     /*
      * EJERCICIO:
      * Entiende el concepto de recursividad creando una función recursiva que imprima
      * números del 100 al 0.
      *
      * DIFICULTAD EXTRA (opcional):
      * Utiliza el concepto de recursividad para:
      * - Calcular el factorial de un número concreto (la función recibe ese número).
      * - Calcular el valor de un elemento concreto (según su posición) en la
      *   sucesión de Fibonacci (la función recibe la posición).
      */
       IDENTIFICATION DIVISION.
      *En COBOL hay que indicar que el programa es recursivo
       PROGRAM-ID. RETO-06 RECURSIVE.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
           77 NUMERO1 PIC 9(3) VALUE 0.
           77 NUMERO2 PIC 9(1) VALUE 7.
           77 FACT PIC 9(5) VALUE 0.
       LOCAL-STORAGE SECTION.
           77 NUM PIC 9(1).
       PROCEDURE DIVISION.
       RECURSIVIDAD.
           ADD 1 TO NUMERO1
           PERFORM UNTIL NUMERO1 > 100
               DISPLAY NUMERO1
      *Llamamos al programa para ejecutar la recursividad
               CALL "RETO-06"
           END-PERFORM.
           END PROGRAM RETO-06.

      *DIFICULTAD EXTRA

      *Precisamente como en COBOL es el programa entero recursivo y no la función (párrafo), no he conseguido que funcione el ejercicio
      *y la dificultad extra todo junto. Así que lo dejo en comentario como sería el factorial

      *IDENTIFICATION DIVISION.
      *PROGRAM-ID. FACTORIAL RECURSIVE.
      * DATA DIVISION.
      *FILE SECTION.
      *WORKING-STORAGE SECTION.
      *    77 NUMERO PIC 9(1) VALUE 7.
      *    77 FACT PIC 9(5) VALUE 0.
      *LOCAL-STORAGE SECTION.
      *    77 NUM PIC 9(1).
      *PROCEDURE DIVISION.
      *    MOVE NUMERO TO NUM.
      *    IF NUMERO = 0
      *        MOVE 1 TO FACT
      *    ELSE
      *        SUBTRACT 1 FROM NUMERO
      *        CALL "FACTORIAL"
      *        MULTIPLY NUM BY FACT
      *    END-IF.
      *    DISPLAY FACT.
      *END PROGRAM FACTORIAL.
