import java.util.*;

public class AndrewCodev {

	public static void main(String[] args) {
		// Arrays
		int[] arNumeros = { 1, 2, 3, 4, 5 };
		String[] arCadenaTexto = { "Hola", "Hola Mundo", "Mundo" };

		AndrewCodev andrewCodev = new AndrewCodev();
		// Imprimiendo Array
		System.out.println("IMPRESIÓN DE Arrays");
		for (int i = 0; i < arNumeros.length; i++) {
			System.out.println("numero: " + arNumeros[i]);
		}
		System.out.println("\n");
		for (int i = 0; i < arCadenaTexto.length; i++) {
			System.out.println("Cadena de texto: " + arCadenaTexto[i]);
		}

		// Impresión de listas
		System.out.println("\nLISTAS DE DEPORTES - ArrayList\n");

		// Agregando datos a la lista
		// Listas ArrayList
		ArrayList<String> deportes = new ArrayList<>();
		deportes.add("NATACIÓN");
		deportes.add("FUTBOL");
		deportes.add("BALONCESTO");
		deportes.add("BESEBALL");

		// Imprimir la lista con los datos agregados
		for (int i = 0; i < deportes.size(); i++) {
			System.out.println(i + ": " + deportes.get(i));
		}

		// Editamos un dato de la lista
		System.out.println("\nMODIFICAMOS UN REGISTRO DE LA LISTA\n");
		deportes.set(0, "FUTBOL SALA");

		// Imprimir la lista con los datos editados
		for (int i = 0; i < deportes.size(); i++) {
			System.out.println(i + ": " + deportes.get(i));
		}

		// ORDENAR LISTA POR NOMBRE
		System.out.println("\nORDENANDO LA LISTA POR NOMBRE\n");
		Collections.sort(deportes);
		// Imprimir la lista con los datos agregados
		for (int i = 0; i < deportes.size(); i++) {
			System.out.println(i + ": " + deportes.get(i));
		}

		// Removemos un dato de la lista
		System.out.println("\nREMOVEMOS UN REGISTRO DE LA LISTA\n");
		deportes.remove(2);
		// Imprimir la lista con los datos agregados
		for (int i = 0; i < deportes.size(); i++) {
			System.out.println(i + ": " + deportes.get(i));
		}

		// Conjunto que no permite elementos duplicados
		HashSet<String> animales = new HashSet<>();
		System.out.println("\nCONJUNNTO DE DATOS - HashSet (No permite valores repetidos)");
		animales.add("Leon");
		animales.add("Tigre");
		animales.add("Elefante");
		animales.add("Leon");

		// Imprimir la lista con los datos agregados
		for (String animal : animales) {
			System.out.println(animal);
		}

		// Eliminar un elemento
		System.out.println("\nREMOVEMOS AL Elefante DE LA LISTA\n");

		animales.remove("Elefante");
		// Imprimir la lista con los datos agregados
		for (String animal : animales) {
			System.out.println(animal);
		}

		// HashMap
		System.out.println("\nLISTAS DE PERSONAS Y EDAD - HashMap\n");
		// HashMap
		HashMap<String, Integer> edades = new HashMap<>();
		edades.put("Ana", 30);
		edades.put("Luis", 25);
		edades.put("Carlos", 35);

		for (HashMap.Entry<String, Integer> edad : edades.entrySet()) {
			System.out.println(edad.getKey() + ": " + edad.getValue());
		}

		System.out.println("\nREMOVEMOS EL REGISTRO Ana - HashMap\n");
		edades.remove("Ana");
		for (HashMap.Entry<String, Integer> edad : edades.entrySet()) {
			System.out.println(edad.getKey() + ": " + edad.getValue());
		}

		// COLAS
		System.out.println("\nCOLAS - Queue - LinkedList \n");
		Queue<String> cola = new LinkedList<>();
		cola.add("Primer");
		cola.add("Segundo");
		cola.add("Tercero");

		System.out.println(cola.add("Cuarto")); // Elimina y retorna "Primer"

		System.out.println("\nPILAS - Queue - LinkedList \n");
		// PILA
		Stack<String> pila = new Stack<>();
		pila.push("Primero");
		pila.push("Segundo");
		pila.push("Tercero");

		System.out.println(pila.pop()); // Elimina y retorna "Tercero"

		ArrayList<AndrewCodev> agenda = new ArrayList<>();

		andrewCodev.inicioPrograma(agenda);
	}

	// INICIO DESARROLLO DE AGENDA
	String nombre;
	Long telefono;
	int codigo;

	public AndrewCodev() {
	}

	public AndrewCodev(String nombre, Long telefono) {
		this.nombre = nombre;
		this.telefono = telefono;
	}

	Scanner scanner = new Scanner(System.in);

	// ABRIMOS EL MENÚ
	public void menuAgenda(ArrayList<AndrewCodev> agenda) {
		String key = scanner.nextLine();
		try {

			int opcion = Integer.parseInt(key);

			switch (opcion) {
			case 1: {
				System.out.println("LISTA DE CONTACTO\n");

				listarContactos(agenda);
				inicioPrograma(agenda);
				break;

			}
			case 2: {

				System.out.println("CREANDO NUEVO CONTACTO\n");
				System.out.println("Ingrese el nombre");
				this.nombre = scanner.nextLine();

				System.out.println("Ingrese el numero de telefono");

				String telefono = scanner.nextLine();
				this.telefono = Long.parseLong(telefono);
				if (validarTelefono(telefono)) {

					nuevoContacto(agenda, this.nombre, this.telefono);

					System.out.println("El Contacto ha sido agregado correctamente: " + this.nombre + " Telefono: "
							+ this.telefono);
				} else {
					System.out.println("El número de telefono debe tener 11 digitos");
					inicioPrograma(agenda);
				}
				inicioPrograma(agenda);
				break;
			}
			case 3: {
				if (listarContactos(agenda)) {
					System.out.println("\nMODIFICAR CONTACTO\n");
					System.out.println("Escriba el Código del contacto que desea modificar");
					this.codigo = Integer.parseInt(scanner.nextLine());

					System.out.println("Modifique el nombre");
					this.nombre = scanner.nextLine();

					System.out.println("Modifique el telefono");
					String telefono = scanner.nextLine();
					this.telefono = Long.parseLong(telefono);

					if (validarTelefono(telefono)) {

						modificarContacto(agenda, this.codigo, this.nombre, this.telefono);

						System.out.println("El Contacto ha sido modificado correctamente: " + this.nombre
								+ " Telefono: " + this.telefono);
					} else {
						System.out.println("El número de telefono no debe tener mas de 11 digitos");
						inicioPrograma(agenda);
					}
				}
				inicioPrograma(agenda);
				break;
			}
			case 4: {

				if (listarContactos(agenda)) {
					System.out.println("\nELIMINAR CONTACTO\n");
					System.out.println("Escriba el Código del contacto que desea ELIMINAR");
					this.codigo = Integer.parseInt(scanner.nextLine());

					eliminarContacto(agenda, this.codigo);

				}
				inicioPrograma(agenda);
				break;
			}
			case 5: {
				scanner.close();
				System.err.println("EL PROGRAMA ESTÁ CERRADO");
				break;
			}
			default:
				System.out.println("La opción no se encuentra en el menú, intente nuevamente");
				inicioPrograma(agenda);
			}

		} catch (NumberFormatException e) {
			System.out.println("Los datos de entrada son invalidos inicie el proceso nuevamente");
			System.out.println("-----------------------------------------------------------------------");
			pintarMenu();
			menuAgenda(agenda);
		}
	}

	public void pintarMenu() {
		// DIFICULTAD EXTRA
		System.out.println("\nAGENDA DE CONTACTOS\n" + "\nPresiona 1 para LISTAR todos tus contactos"
				+ "\nPresiona 2 para AGREGAR un nuevo contacto" + "\nPresiona 3 para MODIFICAR un contacto"
				+ "\nPresiona 4 para ELIMINAR un contacto" + "\nPresiona 5 para CERRAR EL PROGRAMA");
	}

	// Función que crea y retorna la lista de contactos
	public static ArrayList<AndrewCodev> nuevoContacto(ArrayList<AndrewCodev> agenda, String nombre, Long telefono) {
		agenda.add(new AndrewCodev(nombre, telefono));
		return agenda;
	}

	public static ArrayList<AndrewCodev> modificarContacto(ArrayList<AndrewCodev> agenda, int codigo, String nombre,
			Long telefono) {
		for (int i = 0; i < agenda.size(); i++) {
			if (i == codigo) {
				System.out.println(
						"Vas a modificar el contacto: " + agenda.get(i).nombre + " - " + agenda.get(i).telefono);
				agenda.set(i, new AndrewCodev(nombre, telefono));
			}
		}
		return agenda;
	}

	public boolean listarContactos(ArrayList<AndrewCodev> agenda) {

		System.out.println("\nLISTA DE CONTACTOS ACTUALIZADA");
		if (agenda.size() != 0) {
			for (int i = 0; i < agenda.size(); i++) {
				System.out.println("\nCódigo: " + i + "\nNombre: " + agenda.get(i).nombre + "\nTelefono: "
						+ agenda.get(i).telefono);
			}
			return true;
		} else {
			System.out.println("Aun no has registrado contactos en tu agenda");
			return false;
		}
	}

	public static ArrayList<AndrewCodev> eliminarContacto(ArrayList<AndrewCodev> agenda, int codigo) {
		for (int i = 0; i < agenda.size(); i++) {
			if (i == codigo) {
				System.out.println(
						"EL contacto: " + agenda.get(i).nombre + " - " + agenda.get(i).telefono + ": Está eliminado");
				agenda.remove(i);
			}
		}
		return agenda;
	}

	public boolean validarTelefono(String telefono) {
		if (telefono.length() != 11) {
			return false;
		} else {
			return true;
		}
	}

	public void inicioPrograma(ArrayList<AndrewCodev> agenda) {
		System.out.println("-----------------------------------------------------------------------");
		pintarMenu();
		menuAgenda(agenda);
	}
}
/*
 * EJERCICIO: - Muestra ejemplos de creación de todas las estructuras soportadas
 * por defecto en tu lenguaje. - Utiliza operaciones de inserción, borrado,
 * actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional): Crea una agenda de contactos por terminal. -
 * Debes implementar funcionalidades de búsqueda, inserción, actualización y
 * eliminación de contactos. - Cada contacto debe tener un nombre y un número de
 * teléfono. - El programa solicita en primer lugar cuál es la operación que se
 * quiere realizar, y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y
 * con más de 11 dígitos. (o el número de dígitos que quieras) - También se debe
 * proponer una operación de finalización del programa.
 */