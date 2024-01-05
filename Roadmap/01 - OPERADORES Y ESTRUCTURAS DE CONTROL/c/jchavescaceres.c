/*
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
 * DIFICULTAD EXTRA:
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

#include <stdio.h>

void main () {

	int a=10;
	int b=3;


	/* Dificultad extra */
	const unsigned int C_MIN=10;
	const unsigned int C_MAX=55;
	const unsigned int C_EXCLUDE=16;
	const unsigned int C_EXCLUDE_MULTIPLE = 3;
	
	/* Operadores artiméticos */
	printf ("Aritméticos:\n");
	printf ("a=%d, b=%d\n", a, b);
	printf ("Suma a+b : %d\n", a+b);
	printf ("Resta a-b : %d\n", a-b);
	printf ("Multiplicación a*b : %d\n", a*b);
	printf ("Divisioin a/b : %d\n", a/b);
	printf ("Módulo a%% b : %d\n", a%b);
	printf ("Incrementar primero y devolver nuevo valor ++a: %d, a: %d\n", ++a, a);
	printf ("Devolver valor e incrementar luego a++: %d, a: %d\n", a++, a);
	printf ("Decrementar primero y devolver nuevo valor --a: %d, a: %d\n", --a, a);
	printf ("Devolver valor y decrementar luego a--: %d, a: %d\n", a--, a);

	/* Operadores lógicos */
	printf ("\nLógicos:\n");
	a=1;
	b=0;
	printf ("Igualdad: a=%d, b=%d, a==b = %d\n", a, b, a==b);
	printf ("Negación: a=%d, b=%d, !a==b = %d a!=b = %d\n", a, b, !a==b, a!=b);
	printf ("AND: a=%d, b=%d, a && b = %d\n", a, b, a&&b);
	printf ("OR: a=%d, b=%d, a || b = %d\n", a, b, a||b);
	
	/* Operadores comparación */
	printf ("\nComparación:\n");
	printf ("a=%d, b=%d\n", a, b);
	printf ("a>b %s\n", a>b ? "true" : "false");
	printf ("a>=b %s\n", a>=b ? "true" : "false");
	printf ("a<b %s\n", a<b ? "true" : "false");
	printf ("a<=b %s\n", a<=b ? "true" : "false");
	
	/* Operadores asignación */
	printf ("\nAsignación:\n");
	printf ("a=%d, b=%d \n", a, b);
	b=a;
	printf ("b=a b: %d \n", b);
	a+=2;
	printf ("Sumar y asignar nuevo valor a+=2 : %d\n", a);
	a-=2;
	printf ("Restar y asignar nuevo valor a-=2 : %d\n", a);
	a*=2;
	printf ("Multiplicar y asignar nuevo valor a*=2 : %d\n", a);
	a/=2;
	printf ("Dividir y asignar nuevo valor a/=2 : %d\n", a);
	a%=2;
	printf ("Módulo y asignar nuevo valor a%%=2 : %d\n", a);
	printf ("Operador ternario (7 > 5 ? 3 : 2) : %d\n", (7 > 5 ? 3 : 2));
	printf ("Operador ternario (7 < 5 ? 3 : 2) : %d\n", (7 < 5 ? 3 : 2));

	/* Operador bits */
	a=4;
	b=5;
	printf ("\nbits:\n");
	printf ("Complemento a 1: a=%X, ~a %X\n", a, ~a);
	printf ("Desplazamiento a la izquierda 2 bits : a=%X, a<<2 %X\n", a, a<<2);
	printf ("Desplazamiento a la derecha 2 bits : a=%X, a>>2 %X\n", a, a>>2);
	printf ("AND: a=%X, b=%X, a&b=%X\n", a, b, a&b);
	printf ("OR: a=%X, b=%X, a|b=%X\n", a, b, a|b);
	printf ("XOR: a=%X, b=%X, a^b=%X\n", a, b, a^b);

	/* Operador sizeof */
	printf ("\nOtro:\n");
	printf ("sizeof (a): %lu, sizeof (long): %lu\n", sizeof(a), sizeof(long));
	
	/* Estructuras de control */
	printf ("\nEstructuras de control:\n");
	printf ("if, else sif , else :\n");
	if (a==5) {
		printf ("Dentro de if\n");
	} 
	else if (b==2) {
		printf ("Dentro de elsif\n");
	}
	else {
		printf ("Dentro de else\n");
	};

	a=3;
	printf ("do ... while\n");
	do {
		printf ("Dentro de do while %d\n", --a);
	} while (a>1);

	a=3;
	printf ("while ... \n");
	while (a>1) {
		printf ("Dentro de while %d\n", --a);
	};

	printf ("for (a=1; a<3; a++)\n");
	for (a=1; a<10; a++) {
		if (a==1) {
			printf ("Dentro del for continue\n");
			continue; 
		}
		else if (a==3) {
			printf ("Dentro del for break\n");
			break; 
		};
		printf ("Dentro del for %d\n", a);
	};

	a=3;
	printf("switch .. case\n");
	switch (a) {
		case 1:
			printf ("Dentro de case 1\n");
			break; /*hay que poner break o ejecutaría código a partir de aquí*/
		case 2:
			printf ("Dentro de case 2\n");
			break; /*hay que poner break o ejecutaría código a partir de aquí*/
		default:
			printf ("Dentro de default\n");
			break; /*hay que poner break o ejecutaría código a partir de aquí*/
	};

	printf ("Goto, MUY POCO ELEGANTE, NUNCA SE USA\n");
	a=1;
	if (a==2) {
		etiqueta:
		printf ("Dentro de label goto\n");
	}
	else {
		goto etiqueta;
	};

	/* C no tiene excepciones */


/*
 * DIFICULTAD EXTRA:
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/
printf("\nDificultad extra, imprimir por consola todos los números comprendidos entre \
%u y %u (incluidos), pares, y que no son ni el %u ni múltiplos de %u \n", C_MIN, C_MAX, C_EXCLUDE, C_EXCLUDE_MULTIPLE);

	for (unsigned int numero = C_MIN; numero <= C_MAX; numero++) {
		if ((numero != C_EXCLUDE) && (numero %2 == 0) && (numero %C_EXCLUDE_MULTIPLE != 0)) {
			printf("%u\n", numero);
		};
	};
};
