public class AndrewCodev {

	public static void main(String[] args) {
		// EJEMPLO
		ejemploExcepcion();

		// DIFICULTAD EXTRA
		int[] miArreglo = { 10, 5, 8, 65, 87 };
		validarEdad(5, miArreglo);
	}

	public static void ejemploExcepcion() {
		try {
			// Intentamos realizar una operación que puede fallar
			int resultado = dividir(10, 0);
			System.out.println("Resultado: " + resultado);
		} catch (ArithmeticException e) {
			// Manejo de una excepción específica
			System.out.println("Error: " + e.getMessage());
		} catch (Exception e) {
			// Manejo de cualquier otra excepción
			System.out.println("Se produjo un error: " + e.getMessage());
		} finally {
			// Esto siempre se ejecuta
			System.out.println("Operación de división finalizada.");
		}
	}

	public static int dividir(int a, int b) throws ArithmeticException {
		return a / b;
	}

	// DIFICULTAD EXTRA

	// Función para validar que la edad no sea un número negativo
	public static void validarEdad(int edad, int[] miArreglo) {
		try {
			// Creamos una excepción manual con la palabra reservada throw
			if (edad < 0) {
				throw new IllegalArgumentException("La edad debe ser mayor o igual a 18.");
			} else {
				System.out.println("La edad es: " + edad);
			}
		} catch (Exception e) {
			// Manejo de cualquier otra excepción
			System.out.println("Error: " + e.getMessage());
		} finally {
			System.out.println("Validación edad finalizada");
		}

		// acceso a un índice no existente
		try {
			int posicion = miArreglo[10];
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("El índice no existe");
			e.printStackTrace();
		}
	}
}