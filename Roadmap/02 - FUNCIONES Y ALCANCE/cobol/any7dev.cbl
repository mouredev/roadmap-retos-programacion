     /*
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
     */
       IDENTIFICATION DIVISION.
       PROGRAM-ID. RETO-02.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
      *Variables globales
           77 VAR-GLOBAL PIC 9 VALUE 7.
           77 CADENA1 PIC X(5) VALUE "Casi".
           77 CADENA2 PIC X(10) VALUE "Fizzbuzz".
           77 CADENA3 PIC X(20).
           77 CONTADOR PIC 9(2) VALUE 0.
           77 NUM PIC 9(3) VALUE 1.
           77 RESULTADO PIC 9(3).
           77 RESTO3 PIC 9.
           77 RESTO5 PIC 9.
       LOCAL-STORAGE SECTION.
      *Variables locales
           77 VAR-LOCAL PIC 9 VALUE 2.
       PROCEDURE DIVISION.
      *En COBOL no hay funciones, hay subrutinas y se usa el verbo PERFORM. No recibe parámetros
      *ni tiene retorno, ni se puede crear otra subrutina dentro. Se puede llamar a otra subrutina
      *dentro de otra
       SUBRUTINA.
           DISPLAY VAR-GLOBAL.
           DISPLAY VAR-LOCAL.
       OTRA-SUBRUTINA.
           PERFORM SUBRUTINA.

       EXTRA.
           STRING CADENA1 CADENA2 INTO CADENA3
           DISPLAY "           Dificultad extra"
           PERFORM 100 TIMES
           DIVIDE NUM BY 3 GIVING RESULTADO REMAINDER RESTO3
           DIVIDE NUM BY 5 GIVING RESULTADO REMAINDER RESTO5
           IF RESTO3 = 0 AND RESTO5 = 0
               DISPLAY CADENA3
           ELSE
               IF RESTO3 = 0
                   DISPLAY CADENA1
               ELSE
                   IF RESTO5 = 0
                       DISPLAY CADENA2
                   ELSE
                       DISPLAY NUM
                       ADD 1 TO CONTADOR
                   END-IF
               END-IF
           END-IF
           ADD 1 TO NUM
           END-PERFORM.
           DISPLAY "Numero de veces que se ha impreso el numero en "-
           "lugar de los textos: " CONTADOR.

       END PROGRAM RETO-02.
