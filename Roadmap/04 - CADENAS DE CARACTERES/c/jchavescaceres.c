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
/*
Functions defined in string.h:

strcpy 
strcat 
strcmp 
strcoll 
strxfrm (NOT COVERED)
strdup 
strchr 
strrchr 
strcspn 
strspn 
strpbrk 
strstr 
strtok 
strtok_r 
strlen 
strerror 
strerror_r 
strerrordesc_np (NOT COVERED) 
strerrorname_np  (NOT COVERED)
strerror_l 
strsep 
strsignal 
stpcpy 

strncpy 
strncat 
strncmp 
strndup 
strnlen 
stpncpy 
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

void main () {

	const char *string1 = "Cadena 1";
	const char *string2 = "Cadena 2";
	char *ptr = NULL;
	char buffer [200];
	char buffer2 [200];

	setlocale(LC_COLLATE, "es_ES.UTF-8");

	/* Copy */
	memset (buffer, 0, sizeof (buffer));
	strcpy (buffer, string1);
	printf ("String1: %s, strcpy (buffer, string1), buffer: %s\n", string1, buffer);

	/* Copy but n characters*/
	memset (buffer, 0, sizeof (buffer));
	strncpy (buffer, string1, 4);
	printf ("String1: %s, strncpy (buffer, string1, %d), buffer: %s\n", string1, 4, buffer);

	/* Concat */
	memset (buffer, 0, sizeof (buffer));
	strcpy (buffer, string1);
	printf ("buffer: %s, string2: %s, strcat (buffer, string2), ", buffer, string2);
	strcat (buffer, string2);
	printf ("buffer: %s\n", buffer);

	/* Concat n characters */
	memset (buffer, 0, sizeof (buffer));
	strcpy (buffer, string1);
	printf ("buffer: %s, string2: %s, strcat (buffer, string2, %d), ", buffer, string2, 4);
	strncat (buffer, string2, 4);
	printf ("buffer: %s\n", buffer);


	/* Compare */
	strcpy (buffer, string1);
	printf( "String1: %s, buffer: %s, strcmp (buffer, string1) = %d\n", string1, buffer, strcmp (buffer, string1));

	/* Compare n characters*/
	printf( "String1: %s, String2: %s, strncmp (string1, string2, %d) = %d\n", string1, string2, 4, strncmp (string1, string2, 4));

	/* Compare using locale LC_COLLATE */
	strcpy (buffer, string1);
	printf( "String1: %s, buffer: %s, strcoll (buffer, string1) = %d\n", string1, buffer, strcoll (buffer, string1));

	/* Duplicate string, memory allocated must be freed */
	ptr = strdup (string1);
	printf( "String1: %s, strdup: %s\n", string1, ptr);
	free (ptr);
	ptr = NULL;
	
	/* Duplicate string but n characters, memory allocated must be freed */
	ptr = strndup (string1, 4);
	printf( "String1: %s, strndup(%d): %s\n", string1, 4, ptr);
	free (ptr);
	ptr = NULL;

	/* Find position (pointer) of character in string */
	printf( "String1: %s, strchr (a): %s\n", string1, strchr (string1, 'a'));

	/* Find last position (pointer) of character in string */
	printf( "String1: %s, strrchr (a): %s\n", string1, strrchr (string1, 'a'));

	/* Search in string1 if it starts with "Cad" and return following position*/
	printf( "String1: %s, strspn (string1, \"Cad\"): %lu\n", string1, strspn (string1, "Cad"));

	/* Search in string1 the characters b, c or d, return first position found */
	printf( "String1: %s, strcspn (string1, \"bcd\"): %lu\n", string1, strcspn (string1, "bcd"));

	/* Search in string1 the characters b, c or d, return pointer first position found */
	printf( "String1: %s, strpbrk (string1, \"a\"): %s\n", string1, strpbrk (string1, "bcd"));

	/* Search in string1 the string2, return pointer first position found */
	printf( "String1: %s, strstr (string1, \"dena\"): %s\n", string1, strstr (string1, "dena"));

	/* Split a string into tokens, to get all tokens then call the function with NULL value after the first time */
	char testStrtok [] = "1, 2, 3 y 4";
	printf( "strtok (%s, \",\"): ", testStrtok);
	printf( "%s\n", strtok (testStrtok, "-,"));
	printf( "strtok (NULL, \",\"): %s\n", strtok (NULL, "-,"));

	/* Same as strtok but savePtr keep status in sucesive calls */
	char * savePtr = NULL;
	char testStrtok_r [] = "1, 2, 3 y 4";
	printf( "strtok_r (%s, \",\", &savePtr): ", testStrtok_r);
	printf( "%s\n", strtok_r (testStrtok_r, "-,", &savePtr));
	printf( "strtok_r (NULL, \",\", &savePtr): %s\n", strtok_r (NULL, "-,", &savePtr));
	printf( "strtok_r (NULL, \",\", &savePtr): %s\n", strtok_r (NULL, "-,", &savePtr));

	/* Another implementation of tokens separator, testStrsep is updated with rest of string after token */
	char *testStrsep = malloc (200); 
	char *copiaTestStrsep = testStrsep;
	strcpy (testStrsep , "1, 2, 3 y 4");
	printf( "strsep (%s, \",\"): ", testStrsep);
	printf( "%s\n", strsep (&testStrsep, "-,"));
	printf( "%s\n", testStrsep);
	free (copiaTestStrsep);

	/* String length without counting \0 at the end */
	printf( "String1: %s, strlen (string1): %lu\n", string1, strlen (string1));

	/* String length with a maximum characters without counting \0 at the end */
	printf( "String1: %s, strnlen (string1, %d): %lu\n", string1, 4, strnlen (string1, 4));
	printf( "String1: %s, strnlen (string1, %d): %lu\n", string1, 400, strnlen (string1, 400));
	
	/* System error message, several implementations */
	printf( "strerror 4 %s\n", strerror (4));
	strerror_r (4, buffer, sizeof (buffer) / sizeof (char));
	printf( "strerror 4 %s\n", buffer);
	printf( "strerror_l 4 %s\n", strerror_l (4, 0));

	/* Signal name as string */
	printf( "Signal %d, name %s \n", 15, strsignal (15));


};

