// @Roni

public class RECURSIVIDAD_06 {
	// Variables Globales
	static int count = 100; 
	static int result = 1;
	static int resultado=0;
	static int resultado2=1;

	public static void imprimirNumeros() {

		if ((count > -1) && (count < 101)) {
			System.out.println(count + ",");
			count--;
			imprimirNumeros();
		} else {
			count = 0;
		}

	}

	public static void main(String[] args) {
		/*
		 * EJERCICIO:
     * Entiende el concepto de recursividad creando una función recursiva que imprima
     * números del 100 al 0.
		 */
		imprimirNumeros();
		/*
     * DIFICULTAD EXTRA (opcional):
     * Utiliza el concepto de recursividad para:
     * - Calcular el factorial de un número concreto (la función recibe ese número).
     * - Calcular el valor de un elemento concreto (según su posición) en la 
     *   sucesión de Fibonacci (la función recibe la posición).
		 */
		fibonacci(6); // 0 1 1 2 3 5 8
		factorial(6);
	
		
	}

	public static int factorial(int a) {

		if (count < (a - 1)) {
			result = result * (count + 2);
			count++;
			factorial(a);
		} else {
			System.out.print(a + "! = " + result);
			count = 0;
			return result;
		}
		return 0;
	}

	public static int fibonacci(int a) {

		if (a == 1) {
			System.out.println(0);
			return 0;
		} else if ((a == 2)||(a == 3)) {
			System.out.println(1);
			return 0;
		} else if (count +2 < a) {
			int x;
			x=resultado2+resultado;
			resultado=resultado2;
			resultado2=x;
			count++;
			fibonacci(a);
		} else if (count + 2 >= a) {
			System.out.println(resultado2);
			count = 0;
			return 0;
		}
		return 0;

	}

}
