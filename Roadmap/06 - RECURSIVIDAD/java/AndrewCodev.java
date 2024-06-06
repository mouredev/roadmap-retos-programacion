public class AndrewCodev {
	
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
		//Factorial
		int numero = 5;
		int factorial = factorial(numero);
		System.out.println("El factorial de: "+numero+" es: "+factorial);
		
		//Posicion en la serie de Fibonacci
		int posicion  = 6;
		int elemento = posicionFibonacci(posicion);
		System.out.println("La posición: "+posicion+" en la serie de Fibonacci "
				+ "corresponde al elemento: "+elemento);
	}
}