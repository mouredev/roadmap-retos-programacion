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

#include <stdio.h>
#include <string.h>

void printCountDown (unsigned int inStart) {

	printf ("%u\n", inStart);

	/* If 0 stop recursive call */
	if (inStart != 0) {
		printCountDown (inStart-1);
	}

};

/*
factorial of 5 is 5*4*3*2*1*0, or 5 * factorial(4)
factorial of 1 is 1
factorial of 0 is 1
*/
unsigned long getFactorial (unsigned long inNumber) {

	unsigned long res = 1;

	if (inNumber != 1 && inNumber != 0) {
		res = inNumber * getFactorial (inNumber-1);
	};

	return res;
};

/*
Next numbers is got adding previos to previousPrevious
0,1,1,2,3,5,8,13,21,etc.
*/
unsigned long getFibonacciNumber (unsigned long inPosition) {
	unsigned long res = 0; 

	if (inPosition == 0 || inPosition == 1) {
		res = inPosition;
	} else {
		res =
			getFibonacciNumber (inPosition-1) +
			getFibonacciNumber (inPosition-2);
	};

	return res;
};

void main() {
	const unsigned int C_START = 100;

	const unsigned int MAX_BUFFER=200;
	char buffer [MAX_BUFFER];


	unsigned long factorial = 0;
	unsigned long posFibonacci = 0;

	/* Print count down starting from C_START */
	printCountDown (C_START);

	printf ("Calcular factorial de: ");
	fgets (buffer, MAX_BUFFER, stdin);
	buffer [strlen (buffer)-1] = '\0'; /* remove \n */
        if (strspn (buffer, "0123456789") != strlen (buffer)) {
		printf ("Número tiene que ser mayor o igual que 0\n");
	}
	else {
        	sscanf (buffer, "%lu\n", &factorial);
		printf ("El factorial de %lu es %lu\n", factorial, getFactorial (factorial));
	}

	printf ("Obtener el número de la sucesión de Fibonacci en la posición: ");
	fgets (buffer, MAX_BUFFER, stdin);
	buffer [strlen (buffer)-1] = '\0'; /* remove \n */
        if (strspn (buffer, "0123456789") != strlen (buffer)) {
		printf ("Número tiene que ser mayor o igual que 0\n");
	}
	else {
        	sscanf (buffer, "%lu\n", &posFibonacci);
		printf ("El número de la posición Fibonacci en la posición %lu es %lu\n", posFibonacci, getFibonacciNumber (posFibonacci));
	}

}
