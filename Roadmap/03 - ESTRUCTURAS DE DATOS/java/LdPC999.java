package fundamentos;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;
import java.util.TreeSet;

public class Clase03 {
	/*
	 * CLASE 03 - ESTRUCTURAS DE DATOS
	 * 
	 * EJERCICIO
	 * 
	 * - Muestra ejemplos de creación de todas las estructuras soportadas por
	 * defecto en tu lenguaje. - Utiliza operaciones de inserción, borrado,
	 * actualización y ordenación.
	 *
	 * EXTRA
	 * 
	 * Crea una agenda de contactos por terminal. - Debes implementar
	 * funcionalidades de búsqueda, inserción, actualización y eliminación de
	 * contactos. - Cada contacto debe tener un nombre y un número de teléfono. - El
	 * programa solicita en primer lugar cuál es la operación que se quiere
	 * realizar, y a continuación los datos necesarios para llevarla a cabo. - El
	 * programa no puede dejar introducir números de teléfono no numéricos y con más
	 * de 11 dígitos. - También se debe proponer una operación de finalización del
	 * programa.
	 */

	// EXTRA
	public static final int MAX_DIGITS = 11;
	public static Map<String, String> contactos = new HashMap<>();

	public static void extra() {
		Scanner sc = new Scanner(System.in);
		boolean on = true;

		System.out.println("------ Bienvenido a la Agenda ------");

		while (on) {
			System.out.println("Menu: \n");
			System.out.println("Insertar contacto - Pulse 1");
			System.out.println("Buscar contacto - Pulse 2");
			System.out.println("Actualizar contacto - Pulse 3");
			System.out.println("Eliminar contacto - Pulse 4");
			System.out.println("Mostrar todos los contactos - Pulse 5");
			System.out.println("Salir - Pulse 6\n");
			System.out.println("Seleccione una opción");

			String option = sc.nextLine();

			switch (option) {
			case "1":
				insertarContacto(sc);
				break;
			case "2":
				buscarContacto(sc);
				break;
			case "3":
				actualizarContacto(sc);
				break;
			case "4":
				eliminarContacto(sc);
				break;
			case "5":
				mostrarTodos();
				break;
			case "6":
				on = false;
				System.out.println("Hasta pronto");
				break;
			default:
				System.out.println("Opción no válida");

			}
		}

		sc.close();
	}

	public static void insertarContacto(Scanner sc) {
		System.out.println("Introduzca el nombre del contacto: ");
		String nombre = sc.nextLine().trim();

		if (contactos.containsKey(nombre)) {
			System.out.println("El contacto introducido ya existe");
			return;
		} else {

			String telefono = "";
			while (true) {
				System.out.println("Introduzca el número de teléfono. (Escriba salir para volver al menú");
				telefono = sc.nextLine().trim();

				if (telefono.equalsIgnoreCase("salir")) {
					System.out.println("Volviendo al menú");
					return;
				}

				if (isValid(telefono)) {
					contactos.put(nombre, telefono);
					System.out.println("Contacto guardado correctamente");
					break;
				} else {
					System.out.println("Número no válido. Máximo 11 dígitos");
				}
			}

		}
	}

	public static void buscarContacto(Scanner sc) {
		System.out.println("Introduzca el nombre del contacto");
		String nombre = sc.nextLine().trim();

		if (contactos.containsKey(nombre)) {
			System.out.println("Contacto encontrado: " + nombre + " -> " + contactos.get(nombre));

		} else {
			System.out.println("Contacto no encontrado");
		}
	}

	public static void actualizarContacto(Scanner sc) {
		System.out.println("Introduzca el nombre del contacto a actualizar");
		String nombre = sc.nextLine().trim();

		if (contactos.containsKey(nombre)) {
			String telNuevo = "";
			while (true) {
				System.out.println(
						"Introduzca el nuevo número. Máximo 11 dígitos (Escribe salir para cancelar y volver al menú)");
				telNuevo = sc.nextLine().trim();

				if (telNuevo.equalsIgnoreCase("salir")) {
					System.out.println("Volviendo al menu");
					return;
				}

				if (isValid(telNuevo)) {
					contactos.put(nombre, telNuevo);
					System.out.println("Contacto actualizado");
					break;
				} else {
					System.out.println("Número de teléfono no válido. Máximo 11 dígitos");

				}
			}
		} else {
			System.out.println("Contacto no encontrado");
		}
	}

	public static void eliminarContacto(Scanner sc) {
		System.out.println("Introduzca el nombre del contacto");
		String nombre = sc.nextLine().trim();

		if (contactos.containsKey(nombre)) {
			contactos.remove(nombre);
			System.out.println("Contacto eliminado correctamente");
		} else {
			System.out.println("Contacto no encontrado");
		}
	}

	public static void mostrarTodos() {
		if (contactos.isEmpty()) {
			System.out.println("La agenda está vacía");
		} else {
			System.out.println("Lista de contactos");
			contactos.forEach((nombre, telefono) -> System.out.println(nombre + " -> " + telefono));
		}
	}

	public static boolean isValid(String telefono) {
		return telefono.matches("\\d{1," + MAX_DIGITS + "}");
	}

	public static void main(String[] args) {

		// ESTRUCTURAS DE DATOS - Formas de almacenar y organizar datos

		// 1.- ArrayList - Es un array redimensionable al que añadimos elementos y
		// accedemos a ellos por índices.
		// Creación new ArrayList<String>();
		ArrayList<String> nombres = new ArrayList<>();

		// Inserción - .add("");
		// Si lo queremos en alguna posición concreta .add(0,"");
		nombres.add("Luis");
		nombres.add("Pepe");
		nombres.add("Juan");
		nombres.add("Javier");
		nombres.add(0, "Álvaro");
		nombres.add("Alvaro");

		// Eliminación - .remove(index o elemento);
		nombres.remove(3);
		nombres.remove("Javier");

		// Actualizar - .set(0, elemento); Machacamos uno por otro
		nombres.set(0, "LoL");
		System.out.println("ArrayList: " + nombres);

		// Ordenar - Collections.sort(ArrayList)
		// Para orden inverso Collections.reverseOrder()
		Collections.sort(nombres);

		System.out.println("ArrayList: " + nombres);

		// 2.- HashSet
		/*
		 * Set no admita duplicados HashSet no es ordenado (Para eso TreeSet o
		 * LinkedHashSet)
		 */

		// Creación - HashSet<String> xxxx = new HashSet<String>();
		HashSet<String> mySet = new HashSet<>();

		// Insertar - .add()
		mySet.add("Luis");
		mySet.add("Wuizi");
		mySet.add("36");
		mySet.add("LoL");
		mySet.add("Wuizi"); // Aunque lo añada dos veces no lo duplica

		// Eliminar - .remove();
		mySet.remove("LoL");

		// Ordenación - No se puede, tendríamos que usar TreeSet
		TreeSet<String> myTreeSet = new TreeSet<>();
		myTreeSet.add("Wuizi");
		myTreeSet.add("Luis");
		myTreeSet.add("36");
		myTreeSet.add("LoL");
		System.out.println("TreeSet: " + myTreeSet);

		System.out.println("HashSet: " + mySet);

		// 3.- HashMap - Diccionario clave - valor (key/value)

		// Creación
		HashMap<String, String> capitalesPaises = new HashMap<>();

		// Inserción - .put(key, value)
		capitalesPaises.put("Inglaterra", "Londres");
		capitalesPaises.put("España", "Madrid");
		capitalesPaises.put("Francia", "Paris");
		capitalesPaises.put("Italia", "Turín");
		System.out.println("HashMap antes de actualizar: " + capitalesPaises);

		// Eliminar - .remove(Key);
		capitalesPaises.remove("Inglaterra");

		// Actualizar - .put(Key, value) Machacamos el valor de una clave
		capitalesPaises.put("Italia", "Roma");

		System.out.println("HashMap después de actualizar: " + capitalesPaises);

		// Ordenar - Hash no se puede ordenar, hay que usar Tree
		TreeMap<String, String> capitalesPaisesTree = new TreeMap<>();

		capitalesPaisesTree.put("Inglaterra", "Londres");
		capitalesPaisesTree.put("España", "Madrid");
		capitalesPaisesTree.put("Francia", "Paris");

		System.out.println("TreeMap: " + capitalesPaisesTree);

		// EXTRA
		extra();

	}

}
