package javaExample_;
import java.util.Scanner;


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


//En Java las funciones son conocidas como métodos y se declaran dentro de la clase antes del bloque main


public class Funciones_alcance_02 {
	
	
	
	//-------- CONCEPTO DE VARIABLE LOCAL Y GLOBAL --------
	
	public static void var_local() {
		int horas_laborales = 5 * 24;
		int horas_fin_semana = 2 * 24;
		System.out.println("Cantidad de horas en la semana: " + horas_laborales);
		System.out.println("Cantidad de horas en fin de semana: " + horas_fin_semana);

	}
	
	
	public static void main(String[]args) {
		Scanner name = new Scanner(System.in);
		System.out.println("Put Your name: ");
		String nombre = name.nextLine();
		
		int []lista = {1, 2, 3, 4, 5, 6};
		int []punto_1 = {2,4};
		int []punto_2 = {7,9};
		
		
		//--- Resultados de funciones ---

		System.out.println(bienvenida());	
		Saludo(nombre);
		contador(lista);
		System.out.println("La distancia entre puntos: " + distancia_puntos(punto_1, punto_2));
		
		
		//-------- FUNCIONES EXISTENTES DENTRO DEL LENGUAJE -------

		// Función CONCAT(), devuelve la unión de dos cadenas
		String cadena_2 = "Hola ";
		String cadena_3 = "que tal todo";
		String cadena_final = cadena_2.concat(cadena_3);
		System.out.println(cadena_final);

		// Función LENGTH(), devuelve el largo de una cadena
		String cadena_1 = "Hola como estas";
		int largo = cadena_1.length();
		System.out.println(largo);


		//-------- CONCEPTO DE VARIABLE LOCAL Y GLOBAL --------
		var_local();
		//La variable local horas_laborales no se puede acceder de manera global
		//int horas_trabajo = horas_laborales - (8*5);
		
		
		//-------- DIFICULTAD EXTRA --------
		System.out.println(reto_extra(" multipo de 3", " multiplo de 5"));
		
	}	

	
	//-------- DIFERENTES TIPOS DE FUNCIONES --------
	
	//Ejemplo de Función sin retorno y con parámetro
	
	/* 
	 * Función con Modificador Public, dicho modificador permite que
	 * Se pueda acceder a esta función desde otras clases al momento de
	 * crear un objeto que utice dicha función
	*/
	public static void contador(int[]lista) {
		int counter =0;
		int total =0;
		int largo = lista.length;
		
		for(int i=0; i<largo; i++) {
			counter = lista[i];
			total = total + counter;
		}
		System.out.println("Largo de la lista: " + largo);
		System.out.println("Suma de todos los elementos de una lista: " + total);		

	}
	
	// Ejemplo de Función con retorno y con parámetro
	
	static String Saludo(String nombre){
		System.out.println("Hola " + nombre);
		return nombre;
	}
	
	// Ejemplo de Función con retorno y sin parámetro
	public static String bienvenida() {
		String mensaje = "------------------\n----BIENVENIDO----\n------------------";
		return mensaje;
	}
	
	// Ejemplo de Función con retorno y varios parámetros
	
	public static Double distancia_puntos(int[]pto1, int[]pto2) {
		int cateto_1 = pto1[0] - pto2[0];
		int cateto_2 = pto1[1] - pto2[1];
		double value_cateto_1 = Math.pow(cateto_1, 2);
		double value_cateto_2 = Math.pow(cateto_2, 2);
		double distancia = Math.pow(value_cateto_1 + value_cateto_2, 1/2);

		return distancia;
		
	}
	
	//-------- DIFICULTAD EXTRA --------
	
	public static int reto_extra(String cadenaR_1, String cadenaR_2) {
		int contador_3 = 0;
		int contador_5 = 0;
		int contador_comun = 0;

		for(int i=0; i<100; i++){
			if(i%5 == 0 && i%3 == 0){
				System.out.println( i + cadenaR_1 + cadenaR_2);
				contador_comun += 1;
			}else if(i%3 == 0){
				System.out.println(i + cadenaR_1);
				contador_3 += 1;
			}else if(i%5 == 0){
				System.out.println( i + cadenaR_2);
				contador_5 += 1;
			}
		}
		System.out.println("Los números multiplos de 3 son: " + contador_3);
		System.out.println("Los números multiplos de 5 son: " + contador_5);
		System.out.println("Los números multiplos de 3 y 5 son: " + contador_comun);

		return contador_comun;
	}

}
