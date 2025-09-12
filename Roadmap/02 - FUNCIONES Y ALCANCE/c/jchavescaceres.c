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

 #include <stdio.h>
 #include <stdarg.h>
 #include <string.h>

/*
En C las funciones pueden o no devolver un valor, pueden tener entre 0 y n parámetros de entrada
(no existen parámetros OUT o IN OUT, aunque con un puntero se puede obtener el mismo resultado
*/

/*
Funcion sin parámetro de entrada, también se puede dejar (), sin retorno 
*/
void funcionSinParametrosNiRetorno (void) {
	printf ("funcionSinParametrosNiRetorno\n");
};

/*
Funcion con varios parámetros de entrada, sin retorno
*/
void funcionConParametrosSinRetorno (int numero1, int numero2) {
	printf ("funcionConParametrosSinRetorno: numero1=%d, numero2=%d\n", numero1, numero2);
};

/*
Funcion con varios parámetros de entrada y retorno
*/
int funcionConParametrosYRetorno (int numero1, int numero2, const char* texto) {
	const int res = numero1 * numero2;
	printf ("funcionConParametrosYRetorno: texto %s, numero1=%d, numero2=%d, retorno %d\n", texto, numero1, numero2, res);
	return res;
};

/*
Se pueden crear funciones dentro de funciones (funciones anidadas), solo visibles desde la funcion principal
*/
void ejemploFuncionesAnidadas() {

	void funcionAnidada() {
		printf ("funcionAnidada\n");
	};

	printf ("ejemploFuncionesAnidadas\n");
	funcionAnidada;
};

/*
También se pueden definir funciones con parámetros de entradas variable, tanto en numero como tipo, (pero siempre tiene que tener el primero fijo)
Un ejemplo es la funcion printf
Solo lo he visto en ejemplos pero nunca en la vida real
Esta funcion puede reciber n pares de int y const char*, numArgs es el total de argumentos
*/
void funcionParametrosVariables (unsigned int numArgs, ...) {
	va_list listaParametros;
	va_start (listaParametros, numArgs);

	printf ("funcionParametrosVariables: \n");

	for (int i=0; i < numArgs/2; i++) {
		int numero = va_arg (listaParametros, int);
		const char* texto = va_arg (listaParametros, const char*);
		printf ("	%d, %s\n", numero, texto);
	};

	va_end (listaParametros);
};

/*
También existen punteros a funciones
*/
void funcionPuntero1 (int a) {
	printf ("funcionPuntero1 %d\n", a);
};

void funcionPuntero2 (int a) {
	printf ("funcionPuntero2 %d\n", a);
};

typedef void (*t_ptr_funcion)(int);
const t_ptr_funcion C_ARRAY_PTR_FUNCIONES [] = {
	funcionPuntero1,
	funcionPuntero2
}; 

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
*/
unsigned int dificultadExtra (const char* cadena1, const char* cadena2);



int variableGlobal=0;

void funcionVariableLocal() {
	
	/* si se llama igual que una variable global prevalece la variable local */
	/* int variableGlobal=2;*/
	int variableLocal = 3;

	variableGlobal++;

	printf("funcionVariableLocal : variableLocal=%d, variableGlobal=%d\n", variableLocal, variableGlobal);
};

void main () {

	int longitud = 0;

	/* Llamada a funcion sin parámetros ni retorno*/
	funcionSinParametrosNiRetorno ();

	/* Llamada a funcion con parámetros ni retorno*/
	funcionConParametrosSinRetorno (2, 3);

	/* Llamada a funcion con parámetros y retorno*/
	printf ("Llamada a funcionConParametrosYRetorno devuelve %d\n", funcionConParametrosYRetorno (2, -3, "hola"));

	/*Funciones anidadas*/
	ejemploFuncionesAnidadas();
	/* error porque solo es visible dentro del ámbito de ejemploFuncionesAnidadas*/
	/* funcionAnidada();*/

	/*Funcion con número y tipo parámetros variable */
	funcionParametrosVariables (4, 1, "uno", 2, "dos");
	/*Funcion con número y tipo parámetros variable */
	funcionParametrosVariables (6, 3, "tres", 4, "cuatro", 5, "cinco");

	/* llamada a una funcion ya creada en el lenguaje*/
	longitud = strlen ("Prueba");

	/* variables globales y locales */
	variableGlobal=5;
	printf ("variableGlobal=%d\n", variableGlobal);
	funcionVariableLocal();

	/*Puntero a funciones*/
	for (int i = 0, tam = sizeof (C_ARRAY_PTR_FUNCIONES) / sizeof (t_ptr_funcion); i < tam; i++) {
		C_ARRAY_PTR_FUNCIONES [i](i);
	};

	printf ("dificultadExtra devuelve %u\n", dificultadExtra ("cadena1", "cadena2"));


};

unsigned int dificultadExtra (const char* cadena1, const char* cadena2) {
	const unsigned int C_MIN = 1;
	const unsigned int C_MAX = 100;
	const unsigned int C_MULTIPLE_CADENA1 = 3;
	const unsigned int C_MULTIPLE_CADENA2 = 5;

	/* contador de veces que no se imprime ni cadena1 ni cadena2,
	   (suponemos que se refiere a eso porque los números siempre se imprimen (2º línea de instrucciones)
	*/
	unsigned int res = 0; 
	char seHaImpresoCadenas = 0;

	for (unsigned int num = C_MIN; num <= C_MAX; num++) {

		seHaImpresoCadenas = 0;

		printf ("%u ", num);

		if (num >= C_MULTIPLE_CADENA1 && (num % C_MULTIPLE_CADENA1) == 0) {
			printf (" %s", cadena1);
			seHaImpresoCadenas = 1;
		};
		if (num >= C_MULTIPLE_CADENA2 && (num % C_MULTIPLE_CADENA2) == 0) {
			printf (" %s", cadena2);
			seHaImpresoCadenas = 1;
		};

		if (!seHaImpresoCadenas) {
			res++;
		};

		printf ("\n");
	};
	return res;
};
