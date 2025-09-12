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

typedef struct {
	int value1;
	int value2;
} t_values;


t_values swapAsValue (int value1, int value2) {
	t_values res = {0, 0};
	int aux = value2;
	value2 = value1;
	value1 = aux;

	res.value1 = value1;
	res.value2 = value2;
	return res;
}

t_values swapAsReference (int* value1, int* value2) {
	t_values res = {0, 0};
	int aux = *value2;
	*value2 = *value1;
	*value1 = aux;
	
	res.value1 = *value1;
	res.value2 = *value2;
	return res;

}

 /*
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

void extra() {
	int initValueAsValue1 = 1;
	int initValueAsValue2 = 2;
	t_values resValuesAsValue;
	int endtValueAsValue1 = initValueAsValue1;
	int endtValueAsValue2 = initValueAsValue2;
	int initValueAsReference1 = 3;
	int initValueAsReference2 = 4;
	t_values resValuesAsReference;

	printf ("Intercambio por valor: \n");
	printf ("\tinitValue1 %d, initValue2 %d antes de llamar a función\n", initValueAsValue1, initValueAsValue2);
	resValuesAsValue = swapAsValue (initValueAsValue1, initValueAsValue2);
	printf ("\tresValue1 %d, resValue2 %d despues de llamar a función\n", resValuesAsValue.value1, resValuesAsValue.value2);
	printf ("\tinitValue1 %d, initValue2 %d despues de llamar a función\n", initValueAsValue1, initValueAsValue2);

	printf ("Intercambio por referencia: \n");
	printf ("\tinitValue1 %d, initValue2 %d antes de llamar a función\n", initValueAsReference1, initValueAsReference2);
	resValuesAsReference = swapAsReference (&initValueAsReference1, &initValueAsReference2);
	printf ("\tresValue1 %d, resValue2 %d despues de llamar a función\n", resValuesAsReference.value1, resValuesAsReference.value2);
	printf ("\tinitValue1 %d, initValue2 %d despues de llamar a función\n", initValueAsReference1, initValueAsReference2);




};


void main () {
	
	int value = 2;

	printf ("Valor inicial : %d, llamamos a funcion pasando valor\n", value);
	functionAsValue (value);
	printf ("Valor nuevo : %d\n", value);

	printf ("Valor inicial : %d, llamamos a funcion pasando referncia\n", value);
	functionAsReference (&value);
	printf ("Valor nuevo : %d\n", value);

	extra();

};
