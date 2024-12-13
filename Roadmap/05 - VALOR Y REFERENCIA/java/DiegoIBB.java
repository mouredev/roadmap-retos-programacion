package Valor_y_Referencia_05;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

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

// CONTINUAR CON DIFICULTAD EXTRA METODOS CON DIFERENTES TIPOS DE DATOS	

//-------- REFERENCIAS --------	
// https://javarush.com/es/groups/posts/es.2642.tipos-de-datos-de-referencia-en-java
// https://somoshackersdelaprogramacion.es/paso-por-valor-y-paso-por-referencia-de-variables-en-java


//Ejemplo: Objeto como referencia
class Car{ 
	String brand;
	float milage;
	int cost;
}

public class Valor_Referencia_05 {
	
	/*Tipos primitivos (int, char, short, long, double, float, boolean, byte) siempre se pasan por VALOR en los métodos (mutables)
	 *las variables de tipos primitivos crean copias de dichas variables para que los métodos operen sobre las copias (valor) en lugar de
	 *las variables orignales, son elementos mutables.
	*/
	
	/*Los objetos o instancias de una clase siempre se pasan por REFERENCIA a los métodos (inmutables)
	los objetos pasan por referencia a un método, lo que quiere decir que al momento en que una instancia de un objeto entra a un método
	se cambia el valor original del objeto, no se crean copias.
	*/
	
	public static void main(String[]args) {
		
		//--------- PARAMETROS POR VALOR ---------
		
		/*Un parámetro por valor pasa una copia de la variable a un método y
		 * opera sobre ella, sin modificar la variable original, ya que trabajamos
		 * sobre direcciones de memoria diferentes*/
		
		int a = 45;
		int b = 34;
		
		System.out.println("Variable a sin modificar: " + a);
		System.out.println("Variable b sin modificar: " + b);
		System.out.println("Suma de elementos: " + suma(a, b));
		System.out.println("Copia de b al doble: " + doubl(b));
		System.out.println("Variable a: " + a);
		System.out.println("Variable b: " + b);
		
		//--------- PARAMETROS POR REFERENCIA ---------
		
		/* Los parámetros por referencia son aquellos parámetros que pasan la
		 * dirección de la variable orginal a un método y este actua sobre ella,
		 * modificando el valor interno de la variable referenciada*/
		
		String Estado = "Pensilvania";
		String Ciudad = "Filadelfia";
		
		System.out.println(Estado); // Cadena sin modificar
		System.out.println(Ciudad); // Cadena sin modificar
		System.out.println(upper(Estado)); // Cadena modificada, pasamos una copia de la variable State a la función
		System.out.println(Ciudad + "del estado de" + Estado);
		

		
		// Los datos usados como valor o referencia varían según el tipo de datos del que se trate
		
		//--------------------------------------------------------------------------------------
		//----------- DATOS PRIMITIVOS (INT, CHAR, BOOLEAN, FLOAT, DOUBLE) Mutables ------------
		//--------------------------------------------------------------------------------------
		// Estos datos son pasados por valor
		
		int entero = 12;
		char caracter = 'S';
		boolean booleano_1 = true;
		float flotante_1 = 34.5f;
		float flotante_2 = 14.8f;
		double Double = 45.6;
		
		// EJEMPLO CON DATO FLOTANTE (parámetro por valor)
		System.out.println("Resultado de la resta: " +(resta(flotante_1, flotante_2))); // El valor obtenido es gracias a las copias que entraron a la función
		System.out.println("Flotante 1 original: " + flotante_1); // La variable original no cambia
		System.out.println("Flotante 2 original: " + flotante_2); // La variable original no cambia
				
		// EJEMPLO CON DATO BOOLEANO (parámetro por valor)
		System.out.println(booleano_1);
		//boolean booleano_2 = bool(booleano_1); Si guardaramos el resultado de la función en otra variable lo estamos alojando en otro espacio de memoria
		System.out.println(bool(booleano_1));// El valor de la COPIA de booleano_1 pasado como parámetro cambia a false dentro del método
		System.out.println(booleano_1); //El valor original de booleano_1 permanece igual
		
		
		//--------------------------------------------------------------------------------------
		//----- DATOS DE REFERENCIA (hacen referencia a un objeto) (STRING) Inmutables ---------
		//--------------------------------------------------------------------------------------
		// Estos datos son pasados por referencia
		
		/*String no es un tipo de dato sino que es una clase, podemos crear objetos de tipo string*/
		
		String objeto_string = new String();
		objeto_string = "Este es un objeto";
		String variable_String = "Este tambien es un objeto";
		System.out.println(variable_String);

		variable_String = objeto_string;
		
		//Asignamos al objeto variable_string una copia de la dirección del objeto objeto_string
		//al hacer esto el objeto variable_String quedo sin variable que haga referencia a él (no podemos acceder a él)
		System.out.println(variable_String); // --> La variable original variable_String pese a que usa memoria  no tiene mayor utilidad
		System.out.println(objeto_string);
		
		
		/* IMPORTANTE:
		 * Los Arrays son un tipo de dato intermedio entre primitivos y objetos,
		 * y su paso siempre se realiza por referencia 
		 * */
		
		
		//-------------------------------------------
		//--------- OBJETOS COMO REFERENCIA ---------
		//-------------------------------------------
		
		/* Los objetos siempre son pasados por referencia dentro de una función, salvo los objetos inmutables 
		 * (aquel objeto en el que cada vez que se realiza una modificación sobre el mismo se crea una copia 
		 * automáticamente del mismo), un ejemplo clásico es el objeto String
		 * 
		 */

		Car auto_1 = new Car(); //Creamos una instancia u objeto de la clase Car llamado auto_1 y seteamos sus valores
		auto_1.brand = "Porsche";
		auto_1.milage = 24.5f;
		auto_1.cost = 150000;
		
		System.out.println(auto_1.brand);
		System.out.println(auto_1.milage);
		System.out.println(auto_1.cost);
		
		/* Creamos una referencia, no es un objeto, para que fuera un objeto debería tener la estructura
		 * "Car auto_2 = new Car();", esta podría considerarse como una clase vacia
		 * */
		Car auto_2;
		
		/* Le asignamos la referencia del objeto a la que declaramos anteriormente, ahora
		 * ambas tienen la misma dirección en la memoria
		 * */
		auto_2 = auto_1;
		
		//Vemos que al imprimir la referencia obtenemos los mismos valores de la referencia auto_1, al compartir la misma dirección sus valores son los mismos
		System.out.println(auto_2.brand);
		System.out.println(auto_2.milage);
		System.out.println(auto_2.cost);
		
		//Le asginamos nuevos valores a la referencia auto_2
		auto_2.brand = "BMW";
		auto_2.milage = 15.5f;
		auto_2.cost = 100000;
		
		//Imprimimos los valores que le dimos a la referencia y vemos que cambian, luego imprimimos los de la referencia auto_1
		System.out.println(auto_2.brand);
		System.out.println(auto_2.milage);
		System.out.println(auto_2.cost);
		
		//Vemos que al imprimir la referencia auto-1 sus valores cambian a los que le asignamos a la referencia auto_2
		System.out.println(auto_1.brand);
		System.out.println(auto_1.milage);
		System.out.println(auto_1.cost);
		
		/*Estos cambios se producen porque las referencias son las mismas debido a que comparten la misma locación en la 
		 * memoría, si una de las 2 sufre algún cambio dicho cambio afectará a la otra*/
		
		Car auto_3 = new Car(); //Creamos un objeto auto_3
		auto_3 = auto_1; // Le asignamos los mismos valores que auto_1

		// Al imprimir auto_3 vemos que conserva los mismos valores que auto_1
		System.out.println(auto_3.brand);
		System.out.println(auto_3.milage);
		System.out.println(auto_3.cost);
		
		// Si cambiamos sus valores al imprimirlos vemos que cambian
		auto_3.brand = "Audi";
		auto_3.milage = 20.8f;
		auto_3.cost = 90000;
		
		System.out.println(auto_3.brand);
		System.out.println(auto_3.milage);
		System.out.println(auto_3.cost);
		
		//Sinembargo al pasar la referencia del objeto auto_1 vemos que estos tambien cambiaron, ya que ambos comparten la misma dirección
		System.out.println(auto_1.brand);
		System.out.println(auto_1.milage);
		System.out.println(auto_1.cost);
		
		/*Conclusión: En JAVA los objetos creado por nosotros dentro del programa tienen paso por referencia
		*/
				
		/*
		 * DIFICULTAD EXTRA (opcional):
		 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
		 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
		 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
		 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
		 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
		 *   Comprueba también que se ha conservado el valor original en las primeras.
		*/
		
		// Programa_1: Pasa valores por referencia
		
		System.out.println("------ DIFICULTAD EXTRA ------");
		System.out.println("------- Parámetros por Referencia -------");
		String byRef1 = "Cadena referencia 1";
		String byRef2 = "Cadena referencia 2";
		
		System.out.println("Valor byRef1 original: " + byRef1);
		System.out.println("Valor byRef2 original: " + byRef2);
		String[]result_ref = byReference(byRef1, byRef2);
		System.out.println("Valor byRef1 modificado: " + result_ref[0]);
		System.out.println("Valor byRef2 modificado: " + result_ref[1]);
		System.out.println("Valor byRef1 original: " + byRef1);
		System.out.println("Valor byRef2 original: " + byRef2);
		
		System.out.println("------- Parámetros por Valor -------");
		int byVal1 = 435;
		int byVal2 = 211;
		//Valores originales
		System.out.println("Valor byVal1 original: " + byVal1);
		System.out.println("Valor byVal1 original: " + byVal2);
		int []result_val = byValue(byVal1, byVal2);
		//Valores invertidos
		System.out.println("Valor modificado byVal1: " + result_val[0]);
		System.out.println("Valor modificado byVal1: " + result_val[1]);
		//Valores originales conservados
		System.out.println("Valor byVal1 original: " + byVal1);
		System.out.println("Valor byVal1 original: " + byVal2);

	}
	
	//METODOS DE EJEMPLO
	
	static int suma(int x, int y) {
		int sum;
		sum = x + y;
		return sum;
	}
	
	static float resta(float e, float f) {
		float res;
		res = e - f;
		return res;
	}
	
	public static int doubl(int d) {
		int doub;
		doub = d * 2;
		return doub;
	}
	public static String upper(String x){
		String s;
		s = x.toUpperCase();
		return s;
	}
	public static boolean bool(boolean b) {
		boolean b_change = !b; // Negamos el valor de boolean b con el operador de negación "!", si es true pasa a false y viceversa 
		return b_change;
	}
	
	//DIFICULTAD EXTRA
	
//	static Map<String, Integer>[] programa_1 (String cadena, int entero) {
//		String var_aux = cadena;
//		int copiaCadena = entero;
//		String copiaEntero = var_aux;
//		
//		return Map[]{copiaEntero, copiaCadena};
//	}
	
	static int [] byValue(int i1, int i2){
		int iAux = i1;
		int int1 = i2;
		int int2 = iAux;
		
		int [] resultVal = {int1, int2};
		return resultVal;
	}
	
	//Investigar setter y getter para obtener valores por referencia en la función
	
	static String [] byReference(String s1, String s2) {
		String sAux = s1;
		String string_1 = s2;
		String string_2 = sAux;
		
		String [] resultRef = {string_1, string_2};
		return resultRef;
		
	}

}


