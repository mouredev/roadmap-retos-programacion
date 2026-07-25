public class Excepciones {

	public static void main(String[] args) throws ExcepcionPersonal {

		new Ejercicio10().manejoExcepciones();
		
		System.out.println();
		
		new Ejercicio10_DificultadExtra().procesamientoParametros();

	}

}

/*
 	* EJERCICIO:
 		* Explora el concepto de manejo de excepciones según tu lenguaje.
 		* Fuerza un error en tu código, captura el error, imprime dicho error
 		* y evita que el programa se detenga de manera inesperada.
 		* Prueba a dividir "10/0" o acceder a un índice no existente
 		* de un listado para intentar provocar un error. 
 */

public class Ejercicio10 {
	
	public void manejoExcepciones() {
		
		try {
			
			System.out.println(calculoDivision(10, 7));
			
			System.out.println(calculoDivision(10, 0));
			
		} catch (ArithmeticException e) {
			
			System.err.println(e.getMessage());
			
		}
		
		System.out.println();
		
		String[] frase = {"Haciendo", "pruebas", "de", "manejo", "de", "excepciones" };
		
		try {
			
			System.out.println(palabraEnArray(frase, frase.length - 1));
			
			System.out.println(palabraEnArray(frase, frase.length));
			
		} catch (ArrayIndexOutOfBoundsException e) {
			
			System.err.println(e.getMessage());
			
		}
		
		
	} 
	
	private double calculoDivision(double numerador, double denominador) {
		
		if(denominador == 0) throw new ArithmeticException("No está permitida la división entre 0.");
		
		return numerador / denominador;
		
	}
	
	private String palabraEnArray(String[] frase, int i) {
		
		if (i < 0 || i > frase.length - 1) throw new ArrayIndexOutOfBoundsException("El índice buscado está fuera de rango del Array.");
		
		return frase[i];

	}

}

import javax.naming.NamingException;

/*
 	* DIFICULTAD EXTRA (opcional):
 		* Crea una función que sea capaz de procesar parámetros, pero que también
		* pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
		* corresponderse con un tipo de excepción creada por nosotros de manera
		* personalizada, y debe ser lanzada de manera manual) en caso de error.
			* - Captura todas las excepciones desde el lugar donde llamas a la función.
			* - Imprime el tipo de error.
			* - Imprime si no se ha producido ningún error.
			* - Imprime que la ejecución ha finalizado. 
 */

public class Ejercicio10_DificultadExtra {
	
	public void procesamientoParametros() {
		
		System.out.println(imprimirCapturaExcepciones(-5, "ejercicio10_DificultadExtra", "prueba 1"));
		System.out.println(imprimirCapturaExcepciones(3, "ejercicio10_Difícil", "prueba 2"));
		System.out.println(imprimirCapturaExcepciones(5, "ejercicio10_dificultadExtra", ""));
		System.out.println(imprimirCapturaExcepciones(9, "ejercicio10_dificultadextra", "prueba 4"));
		System.out.println(imprimirCapturaExcepciones(10, "ejercicio10_dificultadextra", "prueba 5"));
		
		System.out.println("\nLa ejecución ha finalizado.");
		
	}
	
	private String imprimirCapturaExcepciones(int i, String nombreClase, String palabra) {
		
		String captura;
		
		try {
			
			captura =  capturaExcepciones(i, nombreClase, palabra);
			
		} catch (ArrayIndexOutOfBoundsException | NamingException | ExcepcionPersonal e) {
			
			captura = e.getClass().getSimpleName();
			
		}
		
		return captura;
		
	}
	
	private String capturaExcepciones(int i, String nombreClase, String palabraPersonal) throws NamingException, ExcepcionPersonal {
		
		if(i < 0 || i >= 10) throw new ArrayIndexOutOfBoundsException();
		
		if(!nombreClase.equalsIgnoreCase(this.getClass().getSimpleName())) throw new NamingException();
		
		if(palabraPersonal == null || palabraPersonal.isBlank()) throw new ExcepcionPersonal();
		
		return "No se ha producido ningún error.";
		
	}

}

public class ExcepcionPersonal extends Exception {
	
	public ExcepcionPersonal() {	
	}

}
