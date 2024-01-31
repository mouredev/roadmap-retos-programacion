/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

#include <stdio.h>

/*
Example of function with input parameter as value
*/
void functionAsValue (int inValue) {

	printf ("	functionAsValue parametro entrada %d, ", inValue);

	inValue *= 2;

	printf ("parametro modificado %d\n", inValue);
};

/*
Example of function with input parameter as reference.
Acutally this concept doesn't exist in (C) as it does in C++ or ADA,
but it can be emulated using pointers
*/
void functionAsReference (int* inValue) {

	printf ("	functionAsReference parametro entrada %d, ", *inValue);

	*inValue *= 2;

	printf ("parametro modificado %d\n", *inValue);
};

void main () {
	
	int value = 2;

	printf ("Valor inicial : %d, llamamos a funcion pasando valor\n", value);
	functionAsValue (value);
	printf ("Valor nuevo : %d\n", value);

	printf ("Valor inicial : %d, llamamos a funcion pasando referncia\n", value);
	functionAsReference (&value);
	printf ("Valor nuevo : %d\n", value);


};
