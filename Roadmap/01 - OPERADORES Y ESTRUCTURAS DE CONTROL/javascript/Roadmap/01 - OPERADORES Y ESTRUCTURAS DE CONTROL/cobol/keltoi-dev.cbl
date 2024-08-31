      * EJERCICIO:
      * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
      *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
      *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
      * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
      *   que representen todos los tipos de estructuras de control que existan
      *   en tu lenguaje:
      *   Condicionales, iterativas, excepciones...
      * - Debes hacer print por consola del resultado de todos los ejemplos.
      *
      * DIFICULTAD EXTRA (opcional):
      * Crea un programa que imprima por consola todos los números comprendidos
      * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

       IDENTIFICATION DIVISION.
       PROGRAM-ID. RETO-01.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       77  A PIC 99 VALUE 10.
       77  B PIC 99 VALUE 5.
       77  C PIC 99 VALUE 2.
       77  resultado PIC 9(4) VALUE ZERO.
       77  decimales PIC 99V99 VALUE ZERO.
       77  I PIC 99 VALUE ZERO.
       77  signo PIC S99 VALUE -15.

       PROCEDURE DIVISION.
       Aritmeticos.
      * Suma
           ADD A TO B GIVING resultado.
           DISPLAY A " + " B " = " resultado.
      * Resta
           SUBTRACT A FROM B GIVING resultado.
           DISPLAY A " - " B " = " resultado.
      * Multiplicacion
           MULTIPLY A BY C GIVING resultado.
           DISPLAY A " * " C " = " resultado.
      * Division
           DIVIDE B BY C GIVING decimales.
           DISPLAY B " / " C " = " decimales.
      * Division entera
           DIVIDE B BY C GIVING resultado.
           DISPLAY "El valor entero de " B " / " C " = " resultado.
      * Modulo (Resto)
           DIVIDE A BY 3 GIVING resultado REMAINDER decimales.
           DISPLAY "El resto de " A " / 3 = " decimales.
      * Calculos varios
           COMPUTE resultado = (A + B - C) * 4 / C.
           DISPLAY "(" A " + " B " - " C ") * 4 / " C " = " resultado.

      * Operadores de asigancion
           MOVE A TO resultado.
           DISPLAY "Ahora resultado vale: " resultado.
      * Operadores de comparacion
      * A IS EQUAL TO 10 o A = 10
      * A IS NOT EQUAL TO 10 o A <> 10
      * A IS GREATER TO 10 o A > 10
      * A IS LESS TO 10 o A < 10
      * A IS EQUAL OR GREATER TO 10 o A >= 10
      * A IS EQUAL OR LESS TO 10 o A <=  10

      * Operadores logicos
      * AND
      * OR

      * Estructuras de control
       Condicionales.
      * IF ... ELSE
           DISPLAY "IF ... ELSE".
           IF A IS EQUAL TO 10
               DISPLAY "Es igual a 10"
           ELSE
               DISPLAY "No es igual a 10"
           END-IF.

      * IF anidados
           DISPLAY "IF anidados".
           IF A > 9 AND B < 9
               DISPLAY "Se cumplen las dos condiciones"
           ELSE
               IF A > 9 OR C > 9
                   DISPLAY "Se cumple al menos una de las opciones"
               ELSE
                   DISPLAY "No se cumple ninguna de las opciones"
               END-IF
           END-IF.

      * IF de signos
           DISPLAY "IF de signos".
           IF C IS POSITIVE
               DISPLAY "El valor es positivo".

      * IF de clase
           DISPLAY "IF de clase".
           IF B IS NUMERIC
               DISPLAY "El valor es numerico".

           IF A IS ALPHABETIC OR A IS ALPHABETIC-LOWER
               OR A IS ALPHABETIC-UPPER
               DISPLAY "El valor es una letra"
           ELSE
               DISPLAY "El valor es un numero".

      * Evaluate
           DISPLAY "Evaluate".
           EVALUATE signo

               WHEN > 1
                   DISPLAY "El valor es positivo"

               WHEN < 0
                   DISPLAY "El valor es negativo"

               WHEN OTHER
                   DISPLAY "El valor es cero"

           END-EVALUATE.


      * Bucles
      * Equivalente al for en otros lenguajes
           PERFORM 10 TIMES
               DISPLAY "-*" WITH NO ADVANCING
           END-PERFORM.

           DISPLAY " ".
           DISPLAY "Perform Varying".

           PERFORM Bucle VARYING I FROM 1 BY 1 UNTIL I > 9.

           MOVE 0 to I.
           DISPLAY " ".
           DISPLAY "While".

      * While
           PERFORM Bucle-While WITH TEST BEFORE
           UNTIL I = 10.

           MOVE 0 to I.
           DISPLAY " ".
           DISPLAY "Do while".

      * Do Ahile
           PERFORM Bucle-While WITH TEST AFTER
           UNTIL I = 10.


      * DIFICULTAD EXTRA
       Dificultad-extra.
           DISPLAY " "
           DISPLAY "----- DIFICULTAD EXTRA -----".
           PERFORM Calculo VARYING I FROM 10 BY 2 UNTIL I > 55.

           STOP RUN.

       Calculo.
           DIVIDE I BY 3 GIVING B REMAINDER C.
           IF C NOT = 0 AND I NOT = 16
               DISPLAY I.


      * Rutinas para bucles varios
       Bucle.
           DISPLAY I " " WITH NO ADVANCING.

       Bucle-While.
           ADD 1 TO I.
           DISPLAY I " " WITH NO ADVANCING.


       END PROGRAM RETO-01.
