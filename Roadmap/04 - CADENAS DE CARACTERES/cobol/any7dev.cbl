     /*
      * EJERCICIO:
      * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
      * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
      * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
      *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
      *
      * DIFICULTAD EXTRA (opcional):
      * Crea un programa que analice dos palabras diferentes y realice comprobaciones
      * para descubrir si son:
      * - Palíndromos
      * - Anagramas
      * - Isogramas
      */

       IDENTIFICATION DIVISION.
       PROGRAM-ID. RETO-04.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
      *CADENAS PARA EJEMPLO
           77 CADENA1 PIC X(10) VALUE "HOLA MUNDO".
           77 CADENA2 PIC X(10).
           77 CADENA3 PIC X(5) VALUE "RETOS".
           77 CADENA4 PIC X(2) VALUE "DE".
           77 CADENA5 PIC X(12) VALUE "PROGRAMACION".
           77 CADENA6 PIC X(21).
           77 CADENA7 PIC X(12) VALUE "ROADMAP 2024".
           77 CADENA8 PIC X(10) VALUE "hola mundo".
      *ENTEROS PARA EJEMPLO
           77 CONTADOR PIC 9(2).
           77 LONG PIC 9(2).

      *CADENAS PARA EJERCICIO EXTRA
           77 PALABRA1 PIC X(20).
           77 PALABRA2 PIC X(20).
           77 CARACTER PIC X.
           77 PALABRA4 PIC X(20).
      *ENTEROS PARA EJERCICIO EXTRA
           77 REPE1 PIC 9.
           77 REPE2 PIC 9 VALUE 0.
           77 CONT PIC 9(2) VALUE 1.
           77 LONG1 PIC 9(2).
           77 LONG2 PIC 9(2).

       PROCEDURE DIVISION.

           DISPLAY SPACES.
           DISPLAY "---OPERACIONES CON CADENAS---".
           DISPLAY SPACES.

      *CONVERTIR EN MAYUSCULAS
       MAYUSCULAS.
           DISPLAY "-CONVERTIR EN MAYUSCULAS".
           DISPLAY CADENA8.
           DISPLAY FUNCTION UPPER-CASE(CADENA8).
      *Para guardar en variable
           MOVE FUNCTION UPPER-CASE(CADENA8) TO CADENA2.
           DISPLAY CADENA2.
           DISPLAY SPACES.

      *CONVERTIR EN MINUSCULAS
       MINUSCULAS.
           DISPLAY "-CONVERTIR EN MINUSCULAS".
           DISPLAY CADENA1.
           DISPLAY FUNCTION LOWER-CASE(CADENA1).
      *Para guardar en variable
           MOVE FUNCTION LOWER-CASE(CADENA1) TO CADENA2.
           DISPLAY CADENA2.
           DISPLAY SPACES.

      *EXTRAER LA LONGITUD DE UNA CADENA.
       LONGITUD.
           DISPLAY "-LONGITUD"
           DISPLAY CADENA1.
           MOVE FUNCTION LENGTH(CADENA1) TO LONG.
           DISPLAY LONG.
           DISPLAY SPACES.

      *INVERTIR CADENA
       INVERTIR.
           DISPLAY "-INVERTIR"
           DISPLAY CADENA1.
           MOVE FUNCTION REVERSE(CADENA1) TO CADENA2.
           DISPLAY CADENA2.
           DISPLAY SPACES.

      *INSPECCIONAR LA CADENA. NOS SIRVE PARA CONTAR O SUSTITUIR
       CONTAR.
           DISPLAY "-CONTAR"
           DISPLAY CADENA1.
      *Contar todos los caracteres.
           INSPECT CADENA1 TALLYING CONTADOR FOR CHARACTERS.
           DISPLAY CONTADOR.
           MOVE 0 TO CONTADOR.
      *Contar todas las "O"
           INSPECT CADENA1 TALLYING CONTADOR FOR ALL "O".
           DISPLAY CONTADOR.
           DISPLAY SPACES.
       SUSTITUIR.
           DISPLAY "-SUSTITUIR"
      *SUSTITUYE TODAS LAS LETRAS "A" POR 4.
           DISPLAY CADENA7.
           INSPECT CADENA7 REPLACING ALL "A" BY "4"
           DISPLAY CADENA7.
           DISPLAY SPACES.

      *EXTRAER LOS CANTIDAD DE CARACTERES QUE QUIERAS DE UNA CADENA DESDE EL PRINCIPIO
      *He elegido los primeros 7
       PREFIJO.
           DISPLAY "-PREFIJO"
           DISPLAY CADENA1.
           MOVE CADENA1(1:7) TO CADENA2.
           DISPLAY CADENA2.
           DISPLAY SPACES.
      *Se puede usar para sacar también los ultimos caracteres. He elegido los ultimos 3
       SUFIJO.
           DISPLAY "-SUFIJO"
           DISPLAY CADENA1.
           MOVE CADENA1(8:3) TO CADENA2.
           DISPLAY CADENA2.
           DISPLAY SPACES.

      *CONCATENAR VARIAS CADENAS EN OTRA
       CONCATENAR.
           DISPLAY "-CONCATENAR"
           DISPLAY CADENA3.
           DISPLAY CADENA4.
           DISPLAY CADENA5.
           STRING CADENA3 " " CADENA4 " " CADENA5
           DELIMITED BY SIZE INTO CADENA6.
           DISPLAY CADENA6.
           DISPLAY SPACES.

      *DIVIDIR CADENA EN VARIAS SUBCADENAS
       DIVIDIR.
           DISPLAY "-DIVIDIR"
           DISPLAY CADENA1.
           UNSTRING CADENA1 DELIMITED BY SPACE INTO CADENA2, CADENA6
           END-UNSTRING
           DISPLAY CADENA2.
           DISPLAY CADENA6.
           DISPLAY SPACES.


      *DIFICULTAD EXTRA
           DISPLAY SPACES.
           DISPLAY "-----DIFICULTAD EXTRA-----".
           DISPLAY SPACES.

       PALINDROMOS.
      *PENDIENTE DE TERMINAR


       ANAGRAMAS.
      *Una palabra es anagrama de otra si las dos tienen las mismas letras, con el mismo número de apariciones, pero en un orden diferente.
           DISPLAY "-ANAGRAMAS"
           DISPLAY "INTRODUCE LA PRIMERA PALABRA: ".
           ACCEPT PALABRA1.
           DISPLAY "INTRODUCE LA SEGUNDA PALABRA: ".
           ACCEPT PALABRA4.
           MOVE FUNCTION LOWER-CASE(PALABRA1) TO PALABRA1.
           MOVE FUNCTION LOWER-CASE(PALABRA4) TO PALABRA4.
           IF PALABRA1 = PALABRA4
               DISPLAY "NO SON ANAGRAMAS"
           ELSE
               COMPUTE LONG1 = FUNCTION LENGTH
                           (FUNCTION TRIM(PALABRA1, TRAILING))
               COMPUTE LONG2 = FUNCTION LENGTH
                           (FUNCTION TRIM(PALABRA4, TRAILING))
               IF LONG1 NOT EQUAL LONG2
                   DISPLAY "NO SON ANAGRAMAS"
               ELSE
                   MOVE FUNCTION REVERSE(PALABRA1) TO PALABRA2
                   IF CADENA2 = PALABRA4
                       DISPLAY "ANAGRAMAS"
                   ELSE
                       MOVE FUNCTION LENGTH(PALABRA1) TO LONG1
                       ADD 1 TO LONG1
                       PERFORM UNTIL CONT = LONG1
                           MOVE PALABRA1(CONT:1) TO CARACTER
                           INSPECT PALABRA4 TALLYING REPE1 FOR ALL
                           CARACTER REPLACING FIRST CARACTER BY SPACE
                           ADD 1 TO CONT
                           MOVE 0 TO REPE1
                       END-PERFORM
                       IF PALABRA4 EQUAL SPACES
                           DISPLAY "ANAGRAMAS"
                       ELSE
                           DISPLAY "NO SON ANAGRAMAS"
                       END-IF
                   END-IF
               END-IF
           END-IF.
           DISPLAY SPACES.

       ISOGRAMAS.
      *Un isograma es una palabra o frase en la que cada letra aparece el mismo número de veces.
           MOVE 1 TO CONT.
           DISPLAY "-ISOGRAMAS".
           DISPLAY "INTRODUCE PALABRA: ".
           ACCEPT PALABRA1.
           MOVE FUNCTION LOWER-CASE(PALABRA1) TO PALABRA1.
           COMPUTE LONG1 = FUNCTION LENGTH
                           (FUNCTION TRIM(PALABRA1, TRAILING))
           ADD 1 TO LONG1
           PERFORM UNTIL CONT = LONG1
               MOVE PALABRA1(CONT:1) TO CARACTER
               INSPECT PALABRA1 TALLYING REPE1 FOR ALL CARACTER
               IF REPE2 = 0
                   MOVE REPE1 TO REPE2
               END-IF
               IF REPE1 NOT EQUAL REPE2
                   DISPLAY "NO ISOGRAMA"
                   STOP RUN
               ELSE
                   ADD 1 TO CONT
                   MOVE 0 TO REPE1
               END-PERFORM
           DISPLAY "ISOGRAMA".
           STOP RUN.

       END PROGRAM RETO-04.
