package ejercicio06;

public class AndrewCodev {
	
	//Listar números del 100 al 0
	public static int listarNumeros(int numero) {
		if(numero == 0) {
			return 0;
		}else {
			System.out.println(numero);
			return listarNumeros(numero - 1);
		}
	}
	
	//Calcular el factorial de un número
	public static int factorial(int numero) {		
		if(numero == 0) {
			return 1;
		}else {
			return numero * factorial(numero - 1);
		}
	}
	
	//Buscar elemento de la serie de Fibonacci segun la posición enviada
	public static int posicionFibonacci(int posicion) {
		if(posicion == 0) {
			return 0;
		}else if(posicion == 1){
			return 1;
		}else {
			return posicionFibonacci(posicion - 1) + posicionFibonacci(posicion -2);
		}		
	}
	
	public static void main(String[] args) {
		//Impresión del 100 al 0;
		int numero = 100;
		int impresion = listarNumeros(numero);
		System.out.println(impresion);
		
		//Factorial
		int numero1 = 5;
		int factorial = factorial(numero1);
		System.out.println("\nEl factorial de: "+numero1+" es: "+factorial);
		
		//Posicion en la serie de Fibonacci
		int posicion  = 6;
		int elemento = posicionFibonacci(posicion);
		System.out.println("\nLa posición: "+posicion+" en la serie de Fibonacci "
				+ "corresponde al elemento: "+elemento);
	}
}