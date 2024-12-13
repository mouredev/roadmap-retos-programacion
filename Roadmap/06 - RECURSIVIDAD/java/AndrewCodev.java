public class AndrewCodev {

	// Listar números del 100 al 0
	public static void listarNumeros(int numero) {
		if (numero >= 0) {
			System.out.println(numero);
			listarNumeros(numero - 1);
		}
	}

	// Calcular el factorial de un número
	public static int factorial(int numero) {
		if (numero < 0) {
			System.out.println("\nEl número no es valido para realizar la función factorial");
			return 0;
		} else if (numero == 0) {
			return 1;
		} else {
			return numero * factorial(numero - 1);
		}
	}

	// Buscar elemento de la serie de Fibonacci segun la posición enviada
	public static int posicionFibonacci(int posicion) {
		if (posicion == 0) {
			return 0;
		} else if (posicion == 1) {
			return 0;
		} else if (posicion == 2) {
			return 1;
		} else {
			return posicionFibonacci(posicion - 1) + posicionFibonacci(posicion - 2);
		}
	}

	public static void main(String[] args) {
		// Impresión del 100 al 0;
		int numero = 100;
		listarNumeros(numero);

		// Factorial
		int numero1 = 5;
		int factorial = factorial(numero1);
		if (factorial > 0) {
			System.out.println("\nEl factorial de: " + numero1 + " es: " + factorial);
		}
		// Posicion en la serie de Fibonacci
		int posicion = 9;
		if (posicion <= 0) {
			System.out.println(
					"\nEl número no es valido para realizar la función Fibonacci, debe ser un número mayor a 0");
		} else {
			int elemento = posicionFibonacci(posicion);
			System.out.println("\nLa posición: " + posicion + " en la serie de Fibonacci " + "corresponde al elemento: "
					+ elemento);
		}
	}
}