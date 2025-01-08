package paquete;

/*
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */
public class KGRC {

	// https://www.java.com/es/

	// SINTAXIS 1 DE COMENTARIO
	/* SINTAXIS 2 DE COMENTARIO MÚLTIPLE */
	/** SINTAXÍS 3 PARA ANOTACIONES EN EL CÓDIGO */

	int var = 1; // variable
	final double PI = 3.1416; // constante

	byte var_byte = -128;
	short var_short = -32768;
	int var_int = -2147483648;
	long var_long = 41324394823l; // REQUIERE "L" AL FINAL
	float var_float = 3.1365243f; // REQUIERE "F" AL FINAL
	double var_double = 3.2392482923209;
	char var_char = '\0';
	boolean var_boolean = true && false;

  System.out.println("¡Hola,Java!");

}
