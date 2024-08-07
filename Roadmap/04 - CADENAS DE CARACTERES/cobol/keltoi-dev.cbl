      * EJERCICIO:
      * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
      * en tu lenguaje. Algunas de esas operaciones podrÃ­an ser (busca todas las que puedas):
      * - Acceso a caracteres especÃ­ficos, subcadenas, longitud, concatenaciÃ³n, repeticiÃ³n, recorrido,
      *   conversiÃ³n a mayÃºsculas y minÃºsculas, reemplazo, divisiÃ³n, uniÃ³n, interpolaciÃ³n, verificaciÃ³n...
      *
      * DIFICULTAD EXTRA (opcional):
      * Crea un programa que analice dos palabras diferentes y realice comprobaciones
      * para descubrir si son:
      * - PalÃ­ndromos
      * - Anagramas
      * - Isogramas

       IDENTIFICATION DIVISION.
       PROGRAM-ID. RETO-04.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SPECIAL-NAMES.
           CLASS a-z IS "a" THRU "z", SPACE, "ñ".
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       77  texto PIC X(11) VALUE "Hola COBOL!".
       77  cadena PIC X(15) VALUE "Hola mundo!".
       77  palabra-1 PIC X(15).
       77  palabra-2 PIC X(15).
       77  palabra-3 PIC X(15).
       77  concatenado PIC X(60).
       77  contador PIC 99 VALUE ZERO.
       77  largo PIC 99 VALUE ZERO.
       77  largo2 PIC 99 VALUE ZERO.
       77  corte PIC 9 VALUE ZERO.
       77  I PIC 99 VALUE ZERO.
       77  J PIC 99 VALUE ZERO.
       77  K PIC 99 VALUE ZERO.

       PROCEDURE DIVISION.
       Operaciones-con-strings.

      * Longitud de la cadena
       DISPLAY FUNCTION LENGTH-AN(texto).
       INSPECT texto TALLYING contador FOR CHARACTERS.
       DISPLAY "Tiene " contador " caracteres".

      * Contando cuantas veces se repite una letra
       MOVE ZERO to contador.
       INSPECT cadena TALLYING contador FOR ALL "o".
       DISPLAY "Tiene " contador " letras 'o'".

      * Contando cuantos hay antes del primer espacio
       MOVE ZERO to contador.
       INSPECT texto TALLYING contador FOR CHARACTERS BEFORE
           INITIAL " ".
       DISPLAY "Tiene " contador " letras antes del espacio".

      * Contando cuantos hay despues del primer espacio
       MOVE ZERO to contador.
       INSPECT texto TALLYING contador FOR CHARACTERS AFTER
           INITIAL " ".
       DISPLAY "Tiene " contador " letras despues del espacio".

      * Buscando una letra en la cadena
       MOVE ZERO to contador.
       INSPECT texto TALLYING contador FOR LEADING "Hola".
       DISPLAY "Tiene la cadena contiene 'Hola'? 0=no y 1=si: "contador.

      * Reemplaza todos los caracteres por otro
       INSPECT texto REPLACING CHARACTERS BY "*".
       DISPLAY texto.
       MOVE "Hola COBOL!" to texto.

      * Reemplaza todas las o por i
       INSPECT cadena REPLACING ALL "o" BY "i".
       DISPLAY cadena.
       MOVE "Hola mundo!" to cadena.

      * Reemplaza la palabra Hola por Bye si esta antes del primer espacio
       INSPECT cadena REPLACING ALL "Hola" BY "Bye " BEFORE INITIAL " ".
       DISPLAY cadena.
       MOVE "Hola mundo!" to cadena.

      * Cambiar todo a mayusculas
       DISPLAY FUNCTION UPPER-CASE(cadena)

      * Cambiar todo a minusculas
       DISPLAY FUNCTION LOWER-CASE(cadena)

      * Invertir una cadena
       DISPLAY FUNCTION REVERSE(cadena)

      * Mostrar el tercer caracter de la cadena
       DISPLAY cadena(4:1)

      * Division de cadenas
       MOVE "Juan-Jose-Pedro" TO cadena.
       UNSTRING cadena DELIMITED BY "-" INTO
               palabra-1
               palabra-2
               palabra-3.
       DISPLAY "Se dividio la cadena '" cadena "' en estas plabras".

       DISPLAY palabra-1.
       DISPLAY palabra-2.
       DISPLAY palabra-3.

      * Union de cadenas
       STRING "Nombre 1: ", palabra-1, "Nombre 2: ", palabra-3
           DELIMITED BY SIZE INTO concatenado.

       DISPLAY concatenado.

      * DIFICULTAD EXTRA
       Comienzo.
           PERFORM Toma-palabra.
           MOVE palabra-3 TO palabra-1

           PERFORM Toma-palabra.
           MOVE palabra-3 TO palabra-2.

           DISPLAY "--- Palindromos ---".
           PERFORM Palindromos.

           MOVE palabra-1 TO palabra-3.
           DISPLAY "--- Isogramas ---".
           PERFORM Isogramas.
           IF corte = 1
               DISPLAY "La palabra " palabra-1 " NO es un isograma"
           ELSE
               DISPLAY "La palabra " palabra-1 " es un isograma".

           MOVE palabra-2 TO palabra-3.
           PERFORM Isogramas.
           IF corte = 1
               DISPLAY "La palabra " palabra-2 " NO es un isograma"
           ELSE
               DISPLAY "La palabra " palabra-2 " es un isograma".

           DISPLAY "--- Anagramas ---".
           PERFORM Anagramas.


           STOP RUN.

       Toma-palabra.
           DISPLAY "Ingrese una palabra (sin acentos)"
           ACCEPT palabra-3.
           MOVE FUNCTION LOWER-CASE(palabra-3) TO palabra-3.

           IF palabra-3 is NOT a-z
               DISPLAY "El dato ingresado es erroneo"
               PERFORM Toma-palabra.

      * Palabras que se leen igual al derecho y al reves
       Palindromos.
           MOVE FUNCTION REVERSE(palabra-1) TO palabra-3.
           IF FUNCTION TRIM(palabra-1) = FUNCTION TRIM(palabra-3)
               DISPLAY "La palabra " palabra-1 " es un palindromo"
           ELSE
               DISPLAY "La palabra " palabra-1 " NO es un palindromo".

           MOVE FUNCTION REVERSE(palabra-2) TO palabra-3.
           IF FUNCTION TRIM(palabra-2) = FUNCTION TRIM(palabra-3)
               DISPLAY "La palabra " palabra-2 " es un palindromo"
           ELSE
               DISPLAY "La palabra " palabra-2 " NO es un palindromo".

      * Isograma tienen todas las letras distintas
       Isogramas.
           MOVE ZERO TO corte.
           MOVE ZERO TO largo.
           INSPECT palabra-3 TALLYING largo FOR CHARACTERS
                   BEFORE INITIAL " ".
           PERFORM Vuelta-1 VARYING I FROM 1 BY 1 UNTIL I = largo.

       Vuelta-1.
           COMPUTE K = I + 1
           PERFORM Vuelta-2 VARYING J FROM K BY 1 UNTIL J > largo.

       Vuelta-2.
           IF palabra-3(I:1) = palabra-3(J:1)
               MOVE 1 TO corte.

      * Anagrama palabras distintas con las mismas letras
       Anagramas.
           MOVE ZERO TO largo.
           MOVE ZERO TO largo2.

           INSPECT palabra-1 TALLYING largo FOR CHARACTERS
                   BEFORE INITIAL " ".
           INSPECT palabra-2 TALLYING largo2 FOR CHARACTERS
                   BEFORE INITIAL " ".

           MOVE ZERO TO corte.

           IF largo = largo2
               PERFORM Recorre VARYING I FROM 1 BY 1 UNTIL I > largo.
           IF corte = 0
               DISPLAY "La palabra " palabra-1
                   "es un anagrama de la palabra " palabra-2
           ELSE
               DISPLAY "La palabra " palabra-1
                   "NO es un anagrama de la palabra " palabra-2.

       Recorre.
           MOVE ZERO TO J.
           MOVE ZERO TO K.
           INSPECT palabra-1 TALLYING J FOR ALL palabra-1(I:1).
           INSPECT palabra-2 TALLYING K FOR ALL palabra-1(I:1).
           IF J NOT = K
               MOVE 1 TO corte.

       END PROGRAM RETO-04.
