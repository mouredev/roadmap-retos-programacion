import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.InputMismatchException;
import java.util.LinkedHashSet;
import java.util.Scanner;
import java.util.Stack;
import java.util.TreeSet;

// @Roni

public class ESTRUCTURAS_DE_DATOS_03 {

	public static void main(String[] args) {

		// Arrays

		// Array estatico

		int numeros[] = { 1, 2, 3, 4, 5 }; // Instanciamos con variables asignadas
		int numeros2[] = new int[5]; // Instaciamos con cantidad de variables

		// Acceder y modificar datos del array

		System.out.println(numeros2[0] = 1); // Asignamos el valor 1 en la posicion 0
		System.out.println(numeros2[1] = 2); // Asignamos el valor 2 en la posicion 1
		System.out.println("Valor de la primera posicion en el array numeros: " + numeros[0]); // Asignamos el valor 1
																								// en la posicion 0
		System.out.print("Valor de la primera posicion en el array numeros: ");
		System.out.println(numeros[0] = 6); // Asignamos el valor 6 en la posicion 0
		for (int i : numeros) { // --->Foreach
			System.out.print(i + ",");
		}
		System.out.println();
		for (int i = 0; i < numeros.length; i++) {
			System.out.print(numeros[i] + ",");
		}
		System.out.println();

		// Ordenar

		numeros[0] = 3;
		numeros[1] = 1;
		numeros[2] = 5;
		numeros[3] = 2;
		numeros[4] = 4;
		for (int i : numeros) {
			System.out.print(i + ",");
		}
		System.out.println();
		Arrays.sort(numeros); // --> Ordena el array que le pases como parametro
		for (int i : numeros) {
			System.out.print(i + ",");
		}
		System.out.println();

		// Array dinamico (ArrayList)

		ArrayList<String> nombres = new ArrayList<>();// Creamos el array dinamico

		// Insertar datos

		nombres.add("Hola"); // Se a├▒ade a la primera posicion disponible
		nombres.add("Mundo"); // Se a├▒ade al final de la lista
		nombres.add("Nuevo");

		// Borrar datos

		System.out.println("La lista contiene " + nombres.size() + " posiciones");
		System.out.println("Este el el dato en la posicion 3 : " + nombres.get(2));
		nombres.remove(2); // Eliminamos le dato que esta en la posici├│n 2
		// System.out.println("Este el el dato en la posici├│n 2 : "+nombres.get(2)); -->
		// Una vez eliminado el dato, la posicion deja de existir
		System.out.println("La lista contiene " + nombres.size() + " posiciones");

		// Actualizar datos

		System.out.println(nombres);
		nombres.add(2, "Nuevo");
		System.out.println("Dato en la posicion 3: " + nombres.get(2));
		nombres.set(2, "Viejo");
		System.out.println("Dato en la posicion 3: " + nombres.get(2));
		System.out.println(nombres);

		// HashSet , TreeSet y LinkedHashSet

		/*
		 * Estas tres estructuras de datos evitan que se introuduzcan datos repetidos y
		 * cada uno contiene su forma de ordenar los datos. En el HashSet los datos no
		 * garantizan un orden especifico En TreeSet se ordena de menor a mayor, y el
		 * LinkedHashSet mantiene el orden de inserccion
		 */

		HashSet<Integer> noRepsHS = new HashSet<>();
		TreeSet<Integer> noRepsTS = new TreeSet<>();
		LinkedHashSet<Integer> noRepsLHS = new LinkedHashSet<>();

		// Insertar datos

		noRepsHS.add(4);
		noRepsTS.add(4);
		noRepsLHS.add(4);
		noRepsHS.add(2);
		noRepsTS.add(2);
		noRepsLHS.add(2);
		noRepsHS.add(1);
		noRepsTS.add(1);
		noRepsLHS.add(1);
		noRepsHS.add(3);
		noRepsTS.add(3);
		noRepsLHS.add(3);
		noRepsHS.add(1);
		noRepsTS.add(1);
		noRepsLHS.add(1); // ---> A├▒adimos datos repetidos

		System.out.println(noRepsHS);
		System.out.println(noRepsTS);
		System.out.println(noRepsLHS);

		for (Integer numero : Arrays.asList(9, 6, 8, 7, 5)) { // --Otro metodo de inserccion de datos
			noRepsHS.add(numero);
			noRepsTS.add(numero);
			noRepsLHS.add(numero);
		}
		System.out.println(noRepsHS);
		System.out.println(noRepsTS);
		System.out.println(noRepsLHS);

		// Borrar datos

		/*
		 * Con estos metodos podemos eliminar(limpiar) todos los datos de la lista
		 * 
		 * noRepsHS.clear(); noRepsTS.clear(); noRepsLHS.clear();
		 */

		int begin = 1;
		int desirable = 2;

		System.out.println(noRepsHS);
		for (Integer numero : noRepsLHS) {
			if (begin == desirable) {
				System.out.println(numero); // --->Podemos acceder la posicion que deseemos (desirable)
				break;
			}
			begin++;
		}
		noRepsHS.remove(2); // ---> Borrar dato en la posicion deseada
		System.out.println(noRepsHS);

		System.out.println(noRepsTS);
		System.out.println(noRepsLHS);

		int beginB = 1;
		for (Integer numero : noRepsTS) {
			if (begin == desirable) {
				noRepsHS.remove(numero); // ---> Borrar dato en la posicion deseada
				for (Integer num : noRepsLHS) {
					if (beginB == desirable) {
						noRepsLHS.remove(num); // ---> Borrar dato en la posicion deseada
						System.out.println(num);
						break;
					}
					beginB++;
				}
				System.out.println(numero); // --->Podemos acceder la posicion que deseemos (desirable)
				break;
			}
			begin++;
		}
		System.out.println(noRepsTS);
		System.out.println(noRepsLHS);

		// Las estructuras set no se pueden ordenar por naturaleza.

		// Pilas (Stacks)

		Stack<String> pila = new Stack<>();

		// Insertar datos

		pila.push("A");
		pila.push("B");
		pila.push("C");

		System.out.println("Contenido de la pila: " + pila);

		// Borrar datos

		pila.remove(1); // ---> Borrar dato en la posicion deseada
		// pila.clear(); ---> Eliminar(limpiar) todos los datos de la lista
		System.out.println("Contenido de la pila: " + pila);
		String elementoCima = pila.pop(); // ---> Borrar dato en la cima de la pila con un return del dato
		System.out.println("Contenido de la pila: " + pila);
		System.out.println("Elemento en la cima de la pila: " + elementoCima);

		// Actualizar datos

		System.out.println("Contenido de la pila: " + pila);
		pila.set(0, "B");
		System.out.println("Contenido de la pila: " + pila);

		// Ordenar datos

		pila.push("C");
		pila.push("D");
		pila.push("A");
		System.out.println(pila);
		Collections.sort(pila);
		System.out.println(pila);

		// HashMap , TreeMap y LinkedHashMap

		/*
		 * Podemos ordenar los datos con clave-valor, en donde la clave nos permitira
		 * acceder/locacalizar el valor Estas tres estructuras de datos evitan que se
		 * introuduzcan datos repetidos y cada uno contiene su forma de ordenar los
		 * datos. En el HashSet los datos no garantizan un orden especifico En TreeSet
		 * se ordena de menor a mayor, y el LinkedHashSet mantiene el orden de insercion
		 */

		HashMap<String, String> persona = new HashMap<>();

		// Insertar datos

		persona.put("023909R", "Pedro");
		persona.put("903828A", "Juan");
		persona.put("270842B", "Alberto");
		System.out.println(persona);

		// Borrar datos

		System.out.println(persona);
		persona.remove("903828A");
		System.out.println(persona);
		// persona.clear(); ---> Eliminar(limpiar) todos los datos de la lista

		// Actualizar datos

		System.out.println("Contenido de persona: " + persona);
		persona.replace("023909R", "Ronaldo");
		System.out.println("Contenido de persona: " + persona);

		// Las estructuras map no se pueden ordenar por naturaleza.

		/*
		 * DIFICULTAD EXTRA (opcional): Crea una agenda de contactos por terminal. -
		 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
     * - Cada contacto debe tener un nombre y un número de teléfono.
     * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
     *   los datos necesarios para llevarla a cabo.
     * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
     *   (o el número de dígitos que quieras)
     * - También se debe proponer una operación de finalización del programa.
     */

		Scanner entradaDatos = new Scanner(System.in);
		int opcion = 0;
		long numero;
		String nombre;
		HashMap<String, Long> agenda = new HashMap<>();

		do {
			opcion = Menu(opcion, entradaDatos);

			if (opcion == 1) {
				
				VerAgenda(agenda);
				
			} else if (opcion == 2) {
				System.out.println("Introduzca el nombre del contacto: ");
				nombre = entradaDatos.nextLine();
				NuevoContacto(nombre, entradaDatos, agenda);

			} else if (opcion == 3) {
				
				VerAgenda(agenda);
				
				System.out.println("Decida la opcion que quiera realizar: ");
				System.out.println();
				System.out.println("Opcion 1: Actulizar nombre");
				System.out.println("Opcion 2: Actualizar numero");
				int subOpcion = entradaDatos.nextInt();
				entradaDatos.nextLine();
				if (subOpcion ==1 ) {
					try {
						System.out.println("Introduzca el numero del contacto: ");
						numero = entradaDatos.nextLong();// ---> No tiene en cuenta los 0 a la izquierda
						entradaDatos.nextLine();
						String countNum = String.valueOf(numero);
						if (countNum.length() > 11) {
							System.out.println("Ha excedido el limite de digitos, intente de nuevo: ");
						}else {
							System.out.println("Indrozca el nuevo nombre del contacto: ");
							nombre = entradaDatos.nextLine();
							agenda.put(nombre, numero);
							VerAgenda(agenda);
						}
					} catch (InputMismatchException e) {
						System.out.println("No ha introduciodo un numero, intente de nuevo: ");
						entradaDatos.nextLine();
					}
				}else if (subOpcion == 2) {
					System.out.println("Introduzca el nombre del contacto: ");
					nombre = entradaDatos.nextLine();
					if (agenda.containsKey(nombre)) {
						ActualizarContacto(nombre, entradaDatos, agenda);
						VerAgenda(agenda);
					}
					else {
						System.out.println("El nombre del contacto no existe");
					}
					
				}else {
					System.out.println("Opcion erronea");
				}
			} else if (opcion == 4) {
				VerAgenda(agenda);
				System.out.println("Introduzca el nombre de contacto que quiera eliminar: ");
				nombre = entradaDatos.nextLine();
				agenda.remove(nombre);
				System.out.println("Contacto eliminado");
				VerAgenda(agenda);
			} else if (opcion == 5) {
				System.out.println("Programa finalizado");
				break;
			}

		} while (opcion != 5);

	}

	public static int Menu(int opcion, Scanner entradaDatos) {

		System.out.println("\n*************Agenda de Contactos*************");
		System.out.println();
		System.out.println("Decida la opcion que quiera realizar: ");
		System.out.println();
		System.out.println("Opcion 1: Buscar contacto");
		System.out.println("Opcion 2: Nuevo contacto");
		System.out.println("Opcion 3: Actualizar contacto");
		System.out.println("Opcion 4: Eliminar contacto");
		System.out.println("Opcion 5: Salir");
		System.out.println();
		System.out.println("Intruzca el numero de la opcion que desee: ");
		try {
			opcion = entradaDatos.nextInt();
			entradaDatos.nextLine();
		} catch (InputMismatchException e) {
			System.out.println("No ha introduciodo un numero, intente de nuevo: ");
			entradaDatos.nextLine();
			opcion =0;
		}
		return opcion;
	}

	public static void NuevoContacto(String nombre, Scanner entradaDatos, HashMap<String, Long> agenda) {
		try {
			System.out.println("\nIntroduzca el numero del contacto (max 11 digitos): ");
			Long numero = entradaDatos.nextLong();// ---> No tiene en cuenta los 0 a la izquierda
			entradaDatos.nextLine();
			String countNum = String.valueOf(numero);
			if (countNum.length() > 11) {
				System.out.println("Ha excedido el limite de digitos, intente de nuevo: ");
				NuevoContacto(nombre, entradaDatos, agenda);
			} else {
				agenda.put(nombre, numero);
				System.out.println("Nuevo contacto creado: Nombre " + nombre + " | Numero " + numero);
			}
		} catch (InputMismatchException e) {
			System.out.println("No ha introduciodo un numero, intente de nuevo: ");
			entradaDatos.nextLine();
			NuevoContacto(nombre, entradaDatos, agenda);
		}


	}
	
	public static void VerAgenda(HashMap<String, Long> agenda) {

		System.out.println("NOMBRE\t\t\tTelefono");
		agenda.forEach((key, value) -> System.out.println(key + "\t\t\t" + value));
	}
	public static void ActualizarContacto(String nombre, Scanner entradaDatos, HashMap<String, Long> agenda) {
		try {
			System.out.println("\nIntroduzca el nuevo numero del contacto (max 11 digitos): ");
			Long numero = entradaDatos.nextLong();// ---> No tiene en cuenta los 0 a la izquierda
			entradaDatos.nextLine();
			String countNum = String.valueOf(numero);
			if (countNum.length() > 11) {
				System.out.println("Ha excedido el limite de digitos, intente de nuevo: ");
				ActualizarContacto(nombre, entradaDatos, agenda);
			} else {
				agenda.replace(nombre, numero);
				System.out.println("Contacto acutalizado: Nombre " + nombre + " | Numero " + numero);
			}
		} catch (InputMismatchException e) {
			System.out.println("No ha introduciodo un numero, intente de nuevo: ");
			entradaDatos.nextLine();
			ActualizarContacto(nombre, entradaDatos, agenda);
		}

	}
}
