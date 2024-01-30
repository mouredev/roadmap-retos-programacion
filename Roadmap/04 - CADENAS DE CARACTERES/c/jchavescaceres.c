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

void advanced();

/*
1 if a word is the same reading from left to right and from right to left, e.g. noon
*/
int isPalindrome (const char* inString1, const char* inString2);

/*
1 if both words are anagram: different word but with exactly same letters in a different order, e.g. night and thing
*/
int isAnagrame (const char* inString1, const char* inString2);

/*
1 if all letters of a word appear the same time, e.g. dialogue all letters appears just one, intestines all letters appears twice
*/
int isIsograme (const char* inString);

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

	advanced();


};

char* getWord() {
	const unsigned int MAX_BUFFER=200;
        char buffer [MAX_BUFFER];
        char *res = NULL;

        printf("\nNombre : ");
        fgets (buffer, MAX_BUFFER, stdin);
        buffer [strlen (buffer)-1] = '\0'; /* remove \n */
        res = malloc (strlen (buffer)+1);

        strcpy (res, buffer);

        return res;
};

void advanced() {

	char* words[2] ;


	printf ("Escribe primera palabra : ");
	words[0] = getWord();
	printf ("Escribe segunda palabra : ");
	words[1] = getWord();

	printf ("%s y %s %s son palíndromo\n", words[0], words[1], (isPalindrome (words[0], words[1]) ? "": "no"));
	printf ("%s y %s %s son anagramas\n", words[0], words[1], (isAnagrame (words[0], words[1]) ? "": "no"));
	printf ("%s %s es isograma\n", words[0], (isIsograme (words[0]) ? "": "no"));
	printf ("%s %s es isograma\n", words[1], (isIsograme (words[1]) ? "": "no"));


	free (words[0]);
	free (words[1]);
};

int isPalindrome (const char* inString1, const char* inString2) {
	int res = 1;

	if (strlen( inString1) == strlen (inString2)) {
		for (int i = 0, mySize1 = strlen (inString1), j = strlen (inString2)-1; i < mySize1, j >=0; i++, j--) {
	
				if (inString1 [i] != inString2 [j]) {
					/* Is not a palindrome */
					res = 0;
					break;
				}
		};
	}
	else {
		res = 0;
	};
	return res;
};

void orderWord (char* word) {

	const int sizeString = strlen(word);
	char temp=0;

	for (int i=1 ; i<sizeString ; i++) {
		for (int j= 0; j < sizeString-i ; j++)  {
			if (word[j] > word[j+1]) {
				temp=word[j];
				word[j]=word[j+1];
				word[j+1]=temp;
			}
		}
	}
}


int isAnagrame (const char* inString1, const char* inString2) {

	char* string1 = malloc (strlen (inString1)+1);
	char* string2 = malloc (strlen (inString1)+1);
	int res = 0;

	strcpy (string1, inString1);
	strcpy (string2, inString2);

	/* Order both words, if equal then they are anagrames */
	orderWord (string1);
	orderWord (string2);

	if (strcmp (string1, string2) == 0) {

		res = 1;
	};

	free (string1);
	free (string2);

	return res;
};

int isIsograme (const char* inString) {

	int firstCount = 0;
	int count = 0;
	char firstChar = 0;
	char lastChar = 0;
	char* string1 = malloc (strlen (inString)+1);

	int res = 1;

	strcpy (string1, inString);
	orderWord (string1);

	/* Count how many times each character appears */
	for (int i = 0, mySize = strlen (string1) ; i < mySize; i++) {

		if (firstChar == 0) {
			firstChar = string1 [i];
			firstCount = 1;
		}
		else if (string1 [i] == firstChar) {
			firstCount++;
		}
		else if (lastChar == 0) {
			lastChar = string1 [i];
			count = 1;
		}
		else if (lastChar == string1 [i]) {
			count++;
		}
		else if (lastChar != string1 [i]) {
			if (count != firstCount) {
				res=0;
				break;
			}
			else {
				lastChar = string1 [i];
				count = 1;
			};
		};
	};
	if (res == 1 && count != firstCount) {
		res = 0;
	};

	free (string1);
	return res;
};
