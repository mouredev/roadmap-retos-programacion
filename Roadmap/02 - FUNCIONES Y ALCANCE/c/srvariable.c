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

// Inclusión de librerías
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/* === 1 === */
// Sin parámetros ni retorno

/*
 * Función tipo 'void' llamada "hello_world".
 *
 * No recibe parámetros.
 *
 * No retorna nada porque la función es void.
 *
 * NOTA: Cuando la función no tiene parámetros
 * es recomendable poner void, para asegurar que
 * al llamar a la función si se le introducen
 * parámetros dé un error.
 */
void	hello_world(void)
{
	printf("¡Hola mundo!\n");
	return ; // (Opcional) return sin parámetros ya que la función es de tipo 'void'.
}

// Con uno o varios parámetros
/*
 * Función tipo 'void' llamada "conversor".
 * 
 * Recibe tres parámetros:
 * - temperature: Variable de tipo 'float'.
 * - unit: Variable de tipo 'char *'.
 * - unit2: Variable de tipo 'char *'.
 *
 * No retorna nada porque la función es void.
 */
void	conversor(float temperature, char unit, char unit2)
{
	float	result;

	if (unit == 'C')
	{
		if (unit2 == 'F')
			result = 9.0f / 5.0f * temperature + 32.0f;
		else if (unit2 == 'K')
			result = temperature + 273.15f;
		else
			return ;
	}
	else if (unit == 'F')
	{
		if (unit2 == 'C')
			result = 5.0f / 9.0f * (temperature - 32.0f);
		else if (unit2 == 'K')
			result = 5.0f / 9.0f * (temperature + 459.67f);
		else
			return ;
	}
	else if (unit == 'K')
	{
		if (unit2 == 'C')
			result = temperature - 273.15f;
		else if (unit2 == 'F')
			result = 9.0f / 5.0f * temperature - 459.67f;
		else
			return ;
	}
	else
		return ;
	printf("%f %c = %f %c\n", temperature, unit, result, unit2);
}

// Con retorno 
/*
 * Función tipo 'int' llamada "suma".
 *
 * Recibe dos parámetros:
 * - n1: Variable de tipo 'int'.
 * - n2: Variable de tipo 'int'.
 *
 * Retorna un 'int' que representa la suma de n1 y n2.
 */
int	suma(int n1, int n2)
{
	return (n1 + n2);
}

/* === 2 === */
// En el lenguaje C estándar no está soportado
// la definición de funciones dentro de funciones.
// Sin embargo, en GNU C, es posible, aunque no es
// recomendable usarlo.
void	hola(void)
{
	void	mundo(void)
	{
		printf(" mundo\n");
	}
	printf("Hola");
	mundo();
}

/* === 3 === */
/*
 * Función tipo 'char *' llamada pingpong.
 *
 * Recibe un parámetro:
 * - str: Variable de tipo 'char *'.
 *
 * Retorna:
 * - "ping" si el parámetro es "ping".
 * - "pingpong" si el parámetro no es "ping".
 */
char	*pingpong(char *str)
{
	// Función existente que compara dos "strings" y devuelve 0 si son iguales.
	// Para más información, buscar "man strcmp".
	if (strcmp(str, "ping") == 0)
		return ("pong");
	return ("pingpong");
}

/* === 4 === */
// Variable global
// Esta variable es posible utilizarla en cualquier scope a partir de esta línea.
// Es decir, si la intentamos usar en cualquier otra función anterior, no tendrá
// la referencia, ya que es secuencial.
const char	*g_githuburl = "https://github.com/mouredev/roadmap-retos-programacion";

// Declaración de la función fizzbuzz_tuneado
int		fizzbuzz_tuneado(char *str, char *str2);
void	is_fizzbuzz_tuneado(int (*f)(char *str, char *str2));
int		randomfunction(char *str, char *str2);

/* Función tipo 'int' llamada 'main'
 *
 * Recibe dos parámetros:
 * - argc: Variable de tipo 'int' que indica el número
 * de argumentos que se introducen al programa.
 * - argv: Variable de tipo 'char **' que almacena los
 * argumentos que se introducen al programa.
 *
 * Retorna:
 * - 0 si el programa se ejecuta correctamente.
 * - 1 si no se introducen al menos 2 argumentos.
 *
 * NOTA: Esta función es esencial si queremos crear un
 * programa.
 */
int	main(int argc, char **argv)
{
	// Variables locales
	const char	*texto = "El enlace al repositorio original es: ";
	char		u;
	char		u2;
	float		temperatura;

	if (argc < 2)
	{
		printf("Uso: %s <temperatura>", argv[0]); // Imprime el primer argumento, que es el nombre del programa.
		return (1);
	}
	printf("Función hello_world: ");
	hello_world();
	temperatura = (float)atof(argv[1]);
	printf("Introduce el primer carácter de la unidad de medida de la temperatura inicial: ");
	scanf(" %c", &u);
	printf("Introduce el primer carácter de la unidad de medida de la temperatura final: ");
	scanf(" %c", &u2);
	printf("Función conversor: ");
	conversor(temperatura, toupper(u), toupper(u2));
	printf("Función suma: %d\n", suma(1, 2));
	printf("Función pingpong: %s\n", pingpong("ping"));
	printf("Función pingpong: %s\n", pingpong("pong"));
	printf("Función fizzbuzz_tuneado:\n");
	printf("Número de veces que se imprimen números en lugar de texto: %d\n", fizzbuzz_tuneado("https://github.com", "/SrVariable"));
	printf("%s%s\n", texto, g_githuburl);

	// BONUS
	is_fizzbuzz_tuneado(fizzbuzz_tuneado);
	is_fizzbuzz_tuneado(randomfunction);
	return (0);
}

/*
 * Función tipo 'void' llamada "is_fizzbuzz_tuneado".
 *
 * Recibe un parámetro:
 * - f: Variable de tipo 'int *', es una función que recibe
 *   dos parámetros de tipo 'char *'.
 *
 * No retorna nada porque es una función tipo 'void'.
 */
void	is_fizzbuzz_tuneado(int (*f)(char *str, char *str2))
{
	if (f == fizzbuzz_tuneado)
		printf("Esta función es el fizzbuzz_tuneado\n");
	else
	{
		printf("Esta función no es el fizzbuzz_tuneado\n");
		printf("Devuelvo: %d\n", f(NULL, NULL));
	}
}

/*
 * Función tipo 'int' llamada "randomfunction".
 *
 * Recibe dos parámetros:
 * - str: Variable tipo 'char *'.
 * - str2: Variable de tipo 'char *'.
 *
 * Retorna:
 * - 0 si los dos parametros son NULL.
 * - 1 en cualquier otro caso.
 */
int	randomfunction(char *str, char *str2)
{
	if (!str && !str2)
		return (0);
	return (1);
}

/* === DIFICULTAD EXTRA === */
// Definición de la función fizzbuzz_tuneado
/*
 * Función tipo 'int' llamada "fizzbuzz_tuneado".
 *
 * Recibe dos parámetros:
 * - str: Variable de tipo 'char *'.
 * - str2: Variable de tipo 'char *'.
 * 
 * Retorna el número de veces que imprime un
 * número en lugar de texto.
 */
int	fizzbuzz_tuneado(char *str, char *str2)
{
	int	counter = 0; // Contador para aumentarlo cada vez que imprima un texto en lugar de un número

	for (int i = 1; i <= 100; i++)
	{
		// Hago primero la última condición, si es módulo de 3 y 5
		// para que no haya conflicto cuando sea módulo de 3 solamente,
		// o módulo de 5 solamente.
		if (i % 3 == 0 && i % 5 == 0) 
			printf("%s%s\n", str, str2); // Imprimo los dos "strings" juntos si es divisible entre  3 y 5.
		else if (i % 3 == 0)
			printf("%s\n", str); // Imprimo el primer "string" si es divisible entre 3.
		else if (i % 5 == 0)
			printf("%s\n", str2); // Imprimo el segundo "string" si es divisible entre 5.
		else
		{
			printf("%d\n", i); // Imprimo el número.
			counter++; // Aumento el contador cuando imprimo el número.
		}
	}
	return (counter);
}
