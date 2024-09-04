import java.util.ArrayList;

public class AndrewCodev {
	
	int numeroRef;
	int numeroRef2;
	
	public static void main(String[] args) {
		AndrewCodev andrewCodev = new AndrewCodev();
		//Asignación de Variable por valor		
		//EJEMPLO ASIGNACIÓN DE VARIBALE POR VALOR
		/*En Java, los tipos de datos primitivos se asignan por valor. 
		 *Esto significa que cuando asignas una variable a otra, se copia el valor 
		 * y no la referencia.
		 */
		//Asignación de Variable por valor
		int numeroVal = 5;
		int numeroVal2 = numeroVal; // b obtiene el valor 5
		numeroVal2 = 10; // cambiar b no afecta a

		System.out.println("a: " + numeroVal); // a sigue siendo 5
		System.out.println("b: " + numeroVal2); // b es 10
		
		//EJEMPLO ASIGNACIÓN DE VARIBALE POR REFERENCIA
		ArrayList<String> list1 = new ArrayList<>();
		list1.add("Elemento 1");

		ArrayList<String> list2 = list1; // list2 se refiere al mismo objeto que list1

		list2.add("Elemento 2"); // agregar un elemento a list2 afecta a list1

		System.out.println("list1: " + list1); // list1 contiene ["Elemento 1", "Elemento 2"]
		System.out.println("list2: " + list2); // list2 contiene ["Elemento 1", "Elemento 2"]
		
		
		//EJERCICIO DE ASIGNACIÓN DE VALOR Y REFERENCIA
		System.out.println("\n\nEJERCICIO DE ASIGNACIÓN DE VALOR");
		int num1 = 3;
		int num2 = 6;
		System.out.println("num1 = "+num1);
		System.out.println("num2 = "+num2);
		int[] intercambio = pasarValor(num1, num2);
		System.out.println("Se intercambian los numeros a través del método pasarValor(num1, num2) ");
		int num3 = intercambio[0];
		int num4 = intercambio[1];
		System.out.println("num3 = num1 con el valor de num2: "+num3);
		System.out.println("num4 = num2 con el valor de num1: "+num4);
		System.out.println("num1 = "+num1);
		System.out.println("num2 = "+num2);
		
		/*En Java, los objetos y arreglos se asignan por referencia.
		 *Esto significa que cuando asignas una variable a otra, ambas variables 
		 *se refieren al mismo objeto en la memoria.*/
		
		System.out.println("\n\nEJERCICIO DE ASIGNACIÓN DE REFERENCIA");
		andrewCodev.numeroRef = 5;
		andrewCodev.numeroRef2 = 10;
		System.out.println("numeroRef = "+andrewCodev.numeroRef);
		System.out.println("numeroRef2 = "+andrewCodev.numeroRef2);
		int[] intercambioR = andrewCodev.pasarPorReferencia(andrewCodev);
		System.out.println("\nSe intercambian los numeros a través del método "
				+ "\nandrewCodev.pasarPorReferencia(andrewCodev) "
				+ "\nrecibiendo como parámetro el objeto andrewCodev");
		int numeroRef3 = intercambioR[0];
		int numeroRef4 = intercambioR[1];
		System.out.println("numeroRef3 = numeroRef con el valor de numeroRef2: "+numeroRef3);
		System.out.println("numeroRef4 = numeroRef2 con el valor de numeroRef: "+numeroRef4);
		System.out.println("numeroRef = "+andrewCodev.numeroRef);
		System.out.println("numeroRef2 = "+andrewCodev.numeroRef2);
	}
	
	public static int[] pasarValor(int numeroVal, int numeroVal2) {
		numeroVal = numeroVal2;
		numeroVal2 = numeroVal;
		
		int[] arrEnteros = {numeroVal, numeroVal2};
		return arrEnteros;
	}
	
	public int[] pasarPorReferencia(AndrewCodev andrewCodev) {
		andrewCodev.numeroRef = andrewCodev.numeroRef2;
		andrewCodev.numeroRef2 = andrewCodev.numeroRef;
		
		int[] arrEnteros = {andrewCodev.numeroRef, andrewCodev.numeroRef2};
		return arrEnteros;
	}
}