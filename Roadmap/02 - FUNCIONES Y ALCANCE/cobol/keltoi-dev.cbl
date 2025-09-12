      * EJERCICIO:
      * - Crea ejemplos de funciones básicas que representen las diferentes
      *   posibilidades del lenguaje:
      *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
      * - Comprueba si puedes crear funciones dentro de funciones.
      * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
      * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
      * - Debes hacer print por consola del resultado de todos los ejemplos.
      *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
      *
      * DIFICULTAD EXTRA (opcional):
      * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
      * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
      *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
      *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
      *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
      *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
      *
      * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
      * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.

       IDENTIFICATION DIVISION.
       PROGRAM-ID. RETO-02.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       77  numero1 PIC 99 VALUE 10.
       77  numero2 PIC 99 VALUE 5.
       77  resultado PIC 9999 VALUE ZERO.
       77  dato1 PIC X(9) VALUE "Funcion 1".
       77  dato2 PIC X(9) VALUE "Funcion 2".
       77  resul-factor PIC 9(10).
       01  palabras.
           03 palabra-1 PIC X(4) VALUE "Fizz".
           03 FILLER PIC X VALUE " ".
           03 palabra-2 PIC X(4) VALUE "Buzz".
       77  I PIC 9(3).
       77  resto-3 PIC 9(2).
       77  resto-5 PIC 9(2).
       77  contador PIC 9(2) VALUE ZERO.

       PROCEDURE DIVISION.

      * En este lenguajes se usan las subrrutinas o parrafos en semajanza a
      * las funciones, tal como existen en otros lenguajes.
      * Al igual que las variables todas son globales, ya que se declaran en
      * la seccion working-storage. Por ello no se pasan como parametros a las
      * subrrutinas como en otros lenguajes.

       Inicio.
      * Funciones simples.
           DISPLAY "-- Funcion simple"
           PERFORM Funcion-simple.
      * Funcion dentro de otra funcion.
           DISPLAY "-- Funcion dentro de otra funcion"
           PERFORM Funcion-1.

      * Funcion recursiva.
           DISPLAY "-- Funcion recursiva"
           MOVE numero1 TO resul-factor.
           PERFORM Factoreo.
           DISPLAY "El resultado del factoreo es: " resul-factor.

      * Dificultad extra.
           DISPLAY "-- Dificultad extra".
           PERFORM Dificultad-extra VARYING I FROM 1 BY 1 UNTIL I = 100.
           DISPLAY "Se han impreso " contador " numeros.".

           STOP RUN.

       Funcion-simple.
           COMPUTE resultado = numero1 + numero2.
           DISPLAY numero1 " + " numero2 " = " resultado.

       Funcion-1.
           DISPLAY "Esta en la " dato1.
           PERFORM Funcion-2.
           DISPLAY "Esta de regreso en la" dato1.

       Funcion-2.
           DISPLAY "Esta en la " dato2.

       Factoreo.
           IF numero1 = 1 THEN
               DISPLAY numero1
           ELSE
               IF numero1 = 0 THEN
                   DISPLAY numero1
               ELSE
                   DISPLAY numero1
                   SUBTRACT 1 FROM numero1
                   COMPUTE resul-factor = resul-factor * numero1
                   PERFORM Factoreo
               END-IF
           END-IF.

       Dificultad-extra.
           DIVIDE I BY 3 GIVING resultado REMAINDER resto-3.
           DIVIDE I BY 5 GIVING resultado REMAINDER resto-5.
           IF resto-3 = 0 AND resto-5 = 0 THEN
               DISPLAY palabras
           ELSE
               IF resto-3 = 0 THEN
                   DISPLAY palabra-1
               ELSE
                   IF resto-5 = 0 THEN
                       DISPLAY palabra-2
                   ELSE
                       DISPLAY I
                       ADD 1 to contador
                   END-IF
               END-IF
           END-IF.

       END PROGRAM RETO-02.
