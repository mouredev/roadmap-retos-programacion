/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

package javaExample_;
import java.util.Scanner;

public class Operadores_Estructuras_de_Control_01 {
	
	//Excepción Customizada
	static void largo_cadena(String nombre) {
		String identidad = nombre;
		int cadena = identidad.length();
		System.out.println(cadena);

		if(cadena > 3) {
			throw new ArithmeticException("La cadena excede la cantidad de caracteres");
		}else {
			System.out.println("Largo de cadena correcto");
		}
		}
	
	public static void main(String args[]) {
		
		//OPERADORES
		/* Asignación: =, +=, -=, *=, /=, %=, **=, etc..
		 * Aritméticos: +, -, *, /, %, **, etc..
		 * Comparasión: <, >, <=, >=, ==, !=
		 * Lógicos:&&(and),||(or), !(not)
		 * */
		
		//OPERADORES_ARITMETICOS
		System.out.println("--- Operadores Aritméticos ---");

		int x = 23;
		int y = 34;
		
		int Suma = x + y;
		int Resta = x - y;
		int Multiplicacion = x * y;
		int Division = x / y;
		int Modulo = x % y;
		int Incremento = x ++;
		int Decremento = y --;


		System.out.println("Resultado: "+ x + " + "+ y + "= "+ Suma);
		System.out.println("Resultado: "+ x + " - "+ y + "= "+ Resta);
		System.out.println("Resultado: "+ x + " * "+ y + "= "+ Multiplicacion);
		System.out.println("Resultado: "+ x + " / "+ y + "= "+ Division);
		System.out.println("Resultado: "+ x + " % "+ y + "= "+ Modulo);
		System.out.println("Resultado incremento de: "+ x + "= "+ Incremento);
		System.out.println("Resultado decremento de: "+ y + "= "+ Decremento);
		
		
		//OPERADORES DE ASIGNACION
		System.out.println("--- Operadores de asignación ---");
		
		int num_1 = 4;
		int num_2 = 6;
		int num_3 = 7;
		int num_4 = 5;
		int num_5 = 4;
		int num_6 = 9;
		
		num_1 = 6; //Se le asigna un nuevo valor a num_1
		num_2 += 2; // Se le suma 2 unidades a num_1
		num_3 -= 4; // Se le restan 4 unidades a num_1
		num_4 *= 3; // Se multiplica num_1 por 3
		num_5 /= 2; // Se divide num_1 entre 2
		num_6 %= 3; // Se obtiene el modulo de num_1 entre 3 

		System.out.println("Re-asignación de num_1: "+ num_1);
		System.out.println("Suma de 2 a num_2: "+ num_2);
		System.out.println("Se le resta 4 a num_3: "+ num_3);
		System.out.println("Se multiplica num_4 por 3: "+ num_4);
		System.out.println("Se divide num_5 entre 2: "+ num_5);
		System.out.println("Se obtiene el modulo de 9 entre 3: "+ num_6);

		//OPERADORES_COMPARACION
		
		System.out.println("--- Operadores de Comparación ---");
		int num_7 = 45;
		int num_8 = 55;
		
		System.out.println(num_7 == num_8); //Operador igualdad
		System.out.println(num_7 != num_8); //Operador desigualdad
		System.out.println(num_7 > num_8); //Operador igualdad
		System.out.println(num_7 < num_8); //Operador igualdad
		System.out.println(num_7 >= num_8); //Operador igualdad
		System.out.println(num_7 <= num_8); //Operador igualdad

		
		
		//EXCEPCIONES
		System.out.println("--- Excepciones ---");
		float number_1 = 4;
		float number_2 = 3;
				
		try {
			float number_3 = number_1 / number_2;
			System.out.println(number_3);
		}catch(Exception e) {
			System.out.println("Los valores son incorrectos");
		}finally {
			System.out.println("Programa terminado");
		}
		
		// Excepciones_Customizadas
		
		//largo_cadena("Nombre de persona"); //Código para probar excepción customizada (método en la cabezera))
		
		
			
		//ESTRUCTURA_DE_CONTROL_DE_SELECCION_O_TOMA_DE_DESICION
		System.out.println("--- Estructuras de control ---");
		int a = 34;
		int b = 56;
		
		//Estructura_IF_ELSE-IF_ELSE
		if(a >= b){
			System.out.println("A is major than B: " +  a + " > " + b);
		}
		else if(a <= b){
			System.out.println("B is major than A: " +  b + " > " + a);
		}
		else{
			System.out.println("Numbers are Equal");
		}
		
		//Estructura_SWITCH
		System.out.println("--- Estructura Switch ---");
		int option = 8;
		switch(option){
		case 1:
			System.out.println("Number selected is 1");
			break;
		case 2:
			System.out.println("Number selected is 2");
			break;
		case 3:
			System.out.println("Number selected is 3");
			break;
		case 4:
			System.out.println("Number selected is 4");	
			break;
		default:
			System.out.println("Number not recognized");	
		}
		
		//ESTRUCTURA_DE_CONTROL_DE_REPETICION
		
		//Bucle_FOR
		
		
		System.out.println("--- Bucle For ---");
		for(int i=1; i <= 10; i++) {
			System.out.println(i);
		}
		
		//Bucle_WHILE
		int f = 0;
		System.out.println("--- Bucle While ---");
		while(f < 10) {
			f += 1;
			System.out.println(x);
		}

	}
}
