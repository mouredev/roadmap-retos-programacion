package org.roadmap.java;

public class Password1989 {

	public static void main(String[] args) {
		/*
		 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
		 * - Recuerda que todas las instrucciones de participación están en el
		 *   repositorio de GitHub.
		 *
		 * Lo primero... ¿Ya has elegido un lenguaje?
		 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
		 * - Este primer reto te servirá para familiarizarte con la forma de participar
		 *   enviando tus propias soluciones.
		 *
		 * EJERCICIO:
		 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
		 *   lenguaje de programación que has seleccionado.
		 * - Representa las diferentes sintaxis que existen de crear comentarios
		 *   en el lenguaje (en una línea, varias...).
		 * - Crea una variable (y una constante si el lenguaje lo soporta).
		 * - Crea variables representando todos los tipos de datos primitivos
		 *   del lenguaje (cadenas de texto, enteros, booleanos...).
		 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
		 *
		 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
		 * debemos comenzar por el principio.
		 */
		
		/* URL del sitio web oficial de JAVA: 
		 * https://www.java.com/es/
		 */
		
		/*
		 * Comentario de varias lineas
		 */
		
		//Comentario de una linea
		
		/*
		 * Ejercicio crea una variable:
		 */
		String variableJava = "Java";
		
		/*
		 * Ejercicio crea una constante:
		 */
		
		final String constanteJava = "Java";

		/*
		 * Datos primitivos en JAVA:
		 * El lenguaje Java da de base una serie de tipos de datos primitivos.
		 * 
		 * byte: 	Representa un tipo de dato de 8 bits con signo. De tal manera que puede almacenar los valores numéricos de -128 a 127 (ambos inclusive)
		 * short: 	Representa un tipo de dato de 16 bits con signo. De esta manera almacena valores numéricos de -32.768 a 32.767.
		 * int: 	Es un tipo de dato de 32 bits con signo para almacenar valores numéricos. Cuyo valor mínimo es -231 y el valor máximo 231-1.
		 * long:	Es un tipo de dato de 64 bits con signo que almacena valores numéricos entre -2 elevado 63 a 2 elevado a 63-1
		 * float:	Es un tipo dato para almacenar números en coma flotante con precisión simple de 32 bits.
		 * double:	Es un tipo de dato para almacenar números en coma flotante con doble precisión de 64 bits.
		 * char:	Es un tipo de datos que representa a un carácter Unicode sencillo de 16 bits.
		 * boolean:	Sirve para definir tipos de datos booleanos. Es decir, aquellos que tienen un valor de true o false. Ocupa 1 bit de información.
		 * 
		 * Primitivos
		 * Lista de tipos de datos primitivos en JAVA
		 * Tipo		Tamaño	Valor mínimo			Valor máximo
		 * byte		8 bits	-128					127
		 * short	16 bits	-32768					32767
		 * int		32 bits	-2147483648				2147483647
		 * long		64 bits	-9223372036854775808	9223372036854775807
		 * float	32 bits	-3.402823e38			3.402823e38
		 * double	64 bits	-1.79769313486232e308	1.79769313486232e308
		 * char		16 bits	 u000				ufff
		 */
		byte b = -128;
		short s = -32768;
		int i = -2147483648;
		long l = -9223372036854775808l;
		float f = -3.402823e38f;
		double d = -1.79769313486232e307d;
		char c;
		boolean bl = true;
		
		//Facil: System.out.println("¡Hola, " + variableJava + "!");
		System.out.println(String.format("¡Hola, %s!", variableJava));
		
		/*
		 * El título de la Pull Request también debe seguir este formato: "#[número] - [lenguaje_utilizado]". 
		 * En el ejemplo anterior sería "#00 - Python".
		 * 
		 * En mi caso seria: "#00 - Java"
		 */

	}

}
