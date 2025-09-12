     /*
      *    EJERCICIO:
      *    - Crea ejemplos utilizando todos los tipos de operadores de
      *    tu lenguaje:
      *    Aritméticos, lógicos, de comparación, asignación, identidad,
      *     pertenencia, bits...
      *    Ten en cuenta que cada lenguaje puede poseer unos diferentes
      *    - Utilizando las operaciones con operadores que tú quieras,
      *     crea ejemplos
      *    que representen todos los tipos de estructuras de control
      *    que existan en tu lenguaje:
      *    Condicionales, iterativas, excepciones...
      *    - Debes hacer print por consola del resultado
      *     de todos los ejemplos.
      *
      *    DIFICULTAD EXTRA (opcional):
      *    Crea un programa que imprima por consola todos los números
      *    comprendidos entre 10 y 55 (incluidos), pares, y que no son
      *    ni el 16 ni múltiplos de 3.
      *
      *    Seguro que al revisar detenidamente las posibilidades has
      *    descubierto algo nuevo.
      */

       IDENTIFICATION DIVISION.
       PROGRAM-ID. RETO-02.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
           77 RESULTADO PIC 9(3).
           77 NUM1 PIC 99 VALUE 10.
           77 NUM2 PIC 99 VALUE 2.
           77 NUM3 PIC 99 VALUE 25.
           77 NUM-SALUDO PIC 99 VALUE 5.
           77 NUM-EXTRA PIC 99.
           77 RESTO PIC 99.
      *    Una variable diferente a las anteriores y que no estaba
      *    incluida en el ejercicio 00
           01 NUMERO PIC 9(6).
               88 UNA-CIFRA VALUE 0 THRU 9.
               88 DOS-CIFRAS VALUE 10 THRU 99.
               88 TRES-CIFRAS VALUE 100 THRU 999.
       PROCEDURE DIVISION.
       OPERADORES.
      *    -OPERACIONES ARITMETICAS CON COMPUTE
      *    Suma
           COMPUTE RESULTADO = NUM1 + NUM2.
           DISPLAY RESULTADO.

      *    Resta
           COMPUTE RESULTADO = NUM1 - NUM2.
           DISPLAY RESULTADO.

      *    Multiplicacion
           COMPUTE RESULTADO = NUM1 * NUM2.
           DISPLAY RESULTADO.

      *    Division
           COMPUTE RESULTADO = NUM1 / NUM2.
           DISPLAY RESULTADO.

      *    Potencia
           COMPUTE RESULTADO = NUM1 ** NUM2.
           DISPLAY RESULTADO.

      *    -OPERACIONES ARITMETICAS CON VERBOS
      *    Suma
           ADD NUM1 TO NUM2 GIVING RESULTADO.
           DISPLAY RESULTADO.

      *    Resta
           SUBTRACT NUM1 FROM NUM2 GIVING RESULTADO.
           DISPLAY RESULTADO.

      *    Multiplicacion
           MULTIPLY NUM1 BY NUM2 GIVING RESULTADO.
           DISPLAY RESULTADO.

      *    Division
           DIVIDE NUM1 BY NUM2 GIVING RESULTADO.
           DISPLAY RESULTADO.

      *    -OPERACIONES LOGICAS
      *    And
           IF NUM1 > NUM2 AND NUM2 < NUM3
               DISPLAY "Se cumple"

      *    Or
           IF NUM1 > NUM2 OR NUM2 < NUM3
               DISPLAY "Se cumple"

      *    Is not
           IF NUM1 IS NOT > 19
               DISPLAY "Se cumple"

      *    -OPERACIONES DE COMPARACION
      *    Igual con varias opciones
           IF NUM1 = 2
               DISPLAY "Se cumple"
           IF NUM1 EQUAL TO 2
               DISPLAY "Se cumple"
           IF NUM1 EQUAL 2
               DISPLAY "Se cumple"

      *    Menor que
           IF NUM1 < 2
               DISPLAY "Se cumple"

      *    Menor o igual
           IF NUM1 <= 2
               DISPLAY "Se cumple"

      *    Mayor que
           IF NUM1 > 2
               DISPLAY "Se cumple"

      *    Mayor o igual
           IF NUM1 >= 2
               DISPLAY "Se cumple"

      *    -ASIGNACION
           MOVE 7 TO NUM2.
           DISPLAY NUM2.

       ESTRUCTURAS-CONTROL.
      *    -CONDICIONALES
      *    If
           IF NUM1 = NUM3
               DISPLAY "Numeros iguales".
      *    Se puede finalizar con un punto o con END-IF

      *    If con else
           IF NUM1 = NUM2
               DISPLAY "Numeros iguales"
           ELSE
               DISPLAY "Numeros diferentes".

      *    Anidaciones
           IF NUM1 = NUM3
               DISPLAY "Numeros iguales"
                   IF NUM1 = NUM2
                       DISPLAY "Todos los numeros iguales"
                   ELSE
                       DISPLAY "Numeros 1 y 3 iguales pero diferentes "-
                       "con 2"
           ELSE
               DISPLAY "Numeros 1 y 3 diferentes".

      *    Evaluate
           EVALUATE NUM1

               WHEN 1 THRU 5
               DISPLAY "Numero entre los primeros 5"

               WHEN 6 THRU 10
               DISPLAY "Numero entre 6 y 10"

               WHEN OTHER
               DISPLAY "Numero fuera de rango"

           END-EVALUATE.

      *    Evaluate true
           DISPLAY "Introduce un numero".
           ACCEPT NUMERO.

           EVALUATE TRUE

               WHEN UNA-CIFRA
               DISPLAY "El numero tiene una cifra"

               WHEN DOS-CIFRAS
               DISPLAY "El numero tiene dos cifras"

               WHEN TRES-CIFRAS
               DISPLAY "El numero tiene tres cifras"

               WHEN OTHER
               DISPLAY "El numero tiene mas de tres cifras"

           END-EVALUATE.

      *    -ITERATIVAS
      *    Perform times
       REPETIR.
           PERFORM 3 TIMES
               DISPLAY "Hola"
           END-PERFORM.

      *    Necesario para los siguientes ejemplos
       SALUDO.
           DISPLAY "Hola " NUM-SALUDO.
           ADD 1 TO NUM-SALUDO.
           STOP-RUN.

       SALUDO2.
           DISPLAY "Hola " NUM-SALUDO.

      *    While
       WHILE.
           PERFORM SALUDO WITH TEST BEFORE UNTIL NUM-SALUDO = 10.

      *    Do-While
           MOVE 7 TO NUM-SALUDO.
       DO-WHILE.
           PERFORM SALUDO WITH TEST AFTER UNTIL NUM-SALUDO = 10.

      *    For
           PERFORM SALUDO2 VARYING NUM-SALUDO FROM 0 BY 1 UNTIL
           NUM-SALUDO = 10.
           STOP-RUN.

       EXTRA.
           DIVIDE NUM-EXTRA BY 3 GIVING RESULTADO REMAINDER RESTO.
           IF NUM-EXTRA NOT EQUAL 16 AND RESTO NOT EQUAL 0
               DISPLAY NUM-EXTRA.

       BUCLE.
           DISPLAY "Los numeros comprendidos entre 10 y 55(incluidos),"-
           "pares, y que no son ni el 16 ni multiplos de 3 son:"
           PERFORM EXTRA VARYING NUM-EXTRA FROM 10 BY 2 UNTIL
           NUM-EXTRA = 54.
           STOP-RUN.

       END PROGRAM RETO-02.
