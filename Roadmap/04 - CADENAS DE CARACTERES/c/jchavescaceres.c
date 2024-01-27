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
strcasestr 
strlen 
strerror 
strerror_r 
strerrordesc_np 
strerrorname_np 
strerror_l 
strsep 
strsignal 
stpcpy 
stpncpy 
strverscmp 
strfry 

strncpy 
strncat 
strncmp 
strndup 
strnlen 
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
	strcpy (buffer, string1);
	printf ("String1: %s, strcpy (buffer, string1), buffer: %s\n", string1, buffer);

	/* Concat */
	printf ("buffer: %s, string2: %s, strcat (buffer, string2), ", buffer, string2);
	strcat (buffer, string2);
	printf ("buffer: %s\n", buffer);

	/* Compare */
	strcpy (buffer, string1);
	printf( "String1: %s, buffer: %s, strcmp (buffer, string1) = %d\n", string1, buffer, strcmp (buffer, string1));

	/* Compare using locale LC_COLLATE */
	strcpy (buffer, string1);
	printf( "String1: %s, buffer: %s, strcoll (buffer, string1) = %d\n", string1, buffer, strcoll (buffer, string1));

	/* Duplicate string, memory allocated must be freed */
	ptr = strdup (string1);
	printf( "String1: %s, strdup: %s\n", string1, ptr);
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
	printf( "strtok (NULL, \",\"): %s\n", strtok (NULL, "-,"));


};

