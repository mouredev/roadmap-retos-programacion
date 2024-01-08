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
(no existen parametros OUT o IN OUT, aunque con un puntero se puede obtener el mismo resultado
*/

/*
Funcion sin parametro de entrada, también se puede dejar (), sin retorno 
*/
void funcionSinParametrosNiRetorno (void) {
	printf ("funcionSinParametrosNiRetorno\n");
};

/*
Funcion con varios parametros de entrada, sin retorno
*/
void funcionConParametrosSinRetorno (int numero1, int numero2) {
	printf ("funcionConParametrosSinRetorno: numero1=%d, numero2=%d\n", numero1, numero2);
};

/*
Funcion con varios parametros de entrada y retorno
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
También se pueden definir funciones con parametros de entradas variable, tanto en numero como tipo, (pero siempre tiene que tener el primero fijo)
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

	funcionSinParametrosNiRetorno ();

	funcionConParametrosSinRetorno (2, 3);

	printf ("Llamada a funcionConParametrosYRetorno devuelve %d\n", funcionConParametrosYRetorno (2, -3, "hola"));

	ejemploFuncionesAnidadas();
	/* error porque solo es visible dentro del ámbito de ejemploFuncionesAnidadas*/
	/* funcionAnidada();*/

	funcionParametrosVariables (4, 1, "uno", 2, "dos");
	funcionParametrosVariables (6, 3, "tres", 4, "cuatro", 5, "cinco");

	/* llamada a una funcion ya creada en el lenguaje*/
	longitud = strlen ("Prueba");

	variableGlobal=5;
	printf ("variableGlobal=%d\n", variableGlobal);
	funcionVariableLocal();

};
