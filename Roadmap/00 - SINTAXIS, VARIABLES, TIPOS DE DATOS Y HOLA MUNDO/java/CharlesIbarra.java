package Java;

public class CharlesIbarra {
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
		 * - https://www.java.com/es/
		 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
		 *
		 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
		 * debemos comenzar por el principio.
		 */
		
		// Aquí va una larga lista de variables:
		// byte: Emplea un sólo byte (8 bits) de almacenamiento.
				// Esto permite almacenar valores entre [-128, 127].		
				byte numeroByte = 9;				
				//short: Emplea el doble almacenamiento que byte.
				//Esto permite almacenar valores entre [-32.767, 32.767].		
				short numeroShort = 32767;				
				//int: Emplea un tamaño mayor, 4 bytes (32 bits).
				//Esto permite almacenar valores entre [-2147483648, 2147483647].
				int numeroInt = 41825;
				//long: Emplea el tamaño mayor de todos los enteros, 8 bytes (64 bits).
				//Esto permite almacenar valores entre [-9223372036854775808, 9223372036854775807].
				long numeroLong = 926465464697266565L;
				
				//Número Flotantes:				
				//float: Emplea un tamaño de 32 bits (4 bytes).
				//Esto permite almacenar valores entre [-3.4028234E+8, 1.40239846E-45].
				float numeroFloat = 5976464F;
				//double: Emplea un tamaño de 64 bits (8 bytes).
				//Esto permite almacenar valores entre [-1.7976931348623157E+309, 4.94065645841246544E-324].
				double numeroDouble = 2654792142478F;
				
				//Booleanos y Caracteres:
				//boolean: Se empelan con la fialidad de trabajar con valores verdaderos/falsos (booleanos).
				//Se traducen sus valores en true/false
				boolean variableBoolean = true;				
				//char: Se emplea para almacenar caracteres individuales (letras, aunque puede contener números).
				//Utiliza 16 bits y se codifica sobre UTF-16 Unicode.
				char variableChar = 1;
				char variableChar1 = 'C';
				
				//Cadenas de caracteres:				
				//String: Se emplea creando una instancia de la CLASE String,
				//Aunque parezca trabajar con datos primitivos, esta CLASE u OBJETO se almacena en otro espacio de la memoria
				String variableString = "Hola Mundo.";
				
				// Vectores - arrays				
				//Vector - Arreglo: Se emplea para almacenar un grupo de datos del mismo tipo;				
				//Forma 1:
				int vectorNumeros1[] = new int[10];
				//Forma 2:
				int []vectorNumeros2 = new int[10];
				//Forma 3:
				int[] vectorNumeros3 = new int[10];
				//Forma 4:
				int vectorNumeros4[];
				//Forma 5:
				int vectorNumeros5[] = {};
				//Forma 6:
				int vectorNumeros6[] = {9,8,7,6,5,4,3,2,1,0};
				//Forma 7:
				int vectorNumeros7[] = new int[]{9,8,7,6,5,4,3,2,1,0};
				
				//Matriz: Se emplea para almacenar un grupo de datos del mismo tipo,
				//de forma bidimensional basados en [x],[y].				
				//Forma 1:
				int matrizNumeros1[][] = new int[4][5];
				//Forma 2:
				int [][]matrizNumeros2 = new int[4][5];
				//Forma 3:
				int[][] matrizNumeros3 = new int[4][5];
				//Forma 4:
				int matrizNumeros4[][];
				//Forma 5:
				int matrizNumeros5[][] = {};
				//Forma 6:
				int matrizNumeros6[][] = {{1,2},{3,4}};
				//Forma 7:
				int matrizNumeros7[][] = new int[][] {{5,6},{7,8}};
				
				// Wrappers:				
				//Estos tipos de datos son equivalentes a los primitivos pero en forma de objetos son:
				// Bytem, Short, Integer, Long, Float, Double, Boolean y Character.				
				//Representación de byte en Byte:
				Byte numeroByte1 = 1;				
				//Representación de short en Short;
				Short numeroShort1 = 2416;				
				//Representación de int en Integer;
				Integer numeroInteger = 95256712;				
				//Representación de long en Long;
				Long numeroLong1 = 5113714121L;				
				//Representación de float en Float;
				Float numeroFloat1 = 6591342543251F;				
				//Representación de double en Double;
				Double numeroDouble1 = 9.3;				
				//Representación de boolean en Boolean;
				Boolean variableBoolean1 = true;				
				//Representación de char en Character;
				Character variableCharacter = 'A';
				Character numeroCharacter = 24;
				
				//Aquí una sola constante:
				final double PI = 3.1416;
				
				System.err.println("¡Hola Java!");		
	}
}
