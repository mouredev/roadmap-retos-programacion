public class P05 {

	public static void main(String[] args) {

		// EXPLICACION VALOR Y REFERENCIA
		explicacion();

		// OPCIONAL

		int numeroPequegno = 1;
		int numeromayor = 10;

		System.out.println("numero Pequegno:" + numeroPequegno + " Numero mayor: " + numeromayor);

		int[] cambio = cambioPorValor(numeroPequegno, numeromayor);

		System.out.println("numero Pequegno:" + cambio[0] + " Numero mayor: " + cambio[1]);

	}

	public static int[] cambioPorValor(int num1, int num2) {
		int aux = num1;
		num1 = num2;
		num2 = aux;
		return new int[] { num1, num2 };
	}

	private static void explicacion() {
		// Asignacion de variable por valor

		int numero = 5;
		// Vamos ha cambiar valor de la variable mediante una funcion.
		cambiarValorInt(numero);
		// Esto deberia imprimir 10, pero NO, Imprime 5 ja que se le pasa una copia de
		// la variable
		// y no se agrega el 10 a la variable original si no a la copia.
		System.out.println(numero);

		// Asignacion de variable por referencia
		int[] miArray = new int[3];

		miArray[0] = 10;
		miArray[1] = 20;
		miArray[2] = 30;

		// Modificamos el array.
		modificarArray(miArray);

		// Imprimimos el contenido de nuestro Array
		// Habra cambiado? SI, ya que el array funciona por referencia, cuando llamamos
		// a la funcion
		// modificaArray le pasamos el array original no una copia.

		for (int n : miArray) {
			System.out.println(n);
		}

		// Como funciona en objetos?
		// Vamos a probarlo.

		Persona p1 = new Persona("Angel", 18);

		System.out.println(p1.getNombre() + " " + p1.getEdad());

		p1.setNombre("PEPE");
		p1.setEdad(20);

		// Que imprimira?
		System.out.println(p1.getNombre() + " " + p1.getEdad());
		// Imprime a PEPE y a 20, ya que se pasa como referencia
	}

	private static void modificarArray(int[] miArray) {

		miArray[0] = 5;
		miArray[1] = 5;
		miArray[2] = 5;

	}

	private static void cambiarValorInt(int numero) {
		numero = 10;

	}

	public static class Persona {

		protected String nombre;
		protected int edad;

		public Persona(String nombe, int edad) {
			this.nombre = nombe;
			this.edad = edad;
		}

		public String getNombre() {
			return nombre;
		}

		public void setNombre(String nombre) {
			this.nombre = nombre;
		}

		public int getEdad() {
			return edad;
		}

		public void setEdad(int edad) {
			this.edad = edad;
		}

	}
}
