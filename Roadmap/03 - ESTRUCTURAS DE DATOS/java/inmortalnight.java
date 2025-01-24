// 03 - Java 
// Estructuras de datos

import java.util.*;

public class inmortalnight {
	public static void main(String[] args) {
		//Creación de estructuras de datos
		//NOTA: en Java, al declarar ya se establece un tipo de dato para toda la estructura.
        //Array, estructura de tamaño fijo 
		int[] array = {1, 2, 3, 4, 5}; //Operación de insercción
		array[0] = 1; //Operación de actualización
		Arrays.sort(array); //Operación de ordenación

		//Lista (ArrayList), estructura de tamaño variable de cualquier tipo
		ArrayList<Integer> lista = new ArrayList<Integer>();
		lista.add(1); //Operación de insercción
        lista.add(2);
        lista.remove(1); //Operación de borrado
        lista.set(0, 10); //Operación de actualización
        lista.sort(null); //Operación de ordenación
		
		//Set, estructura de valores únicos
		Set<Integer> set = new HashSet<Integer>();
		set.add(1); //Operación de insercción
		set.remove(1); //Operación de borrado

		//Map, estructura de clave-valor, donde la clave es única
		Map<String, Integer> map = new HashMap<String, Integer>();
		map.put("uno", 1); //Operación de insercción
		map.remove("uno"); //Operación de borrado
		map.put("uno", 10); //Operación de actualización

		//Queue, estructura de datos que sigue el orden FIFO
		Queue<Integer> queue = new LinkedList<Integer>(); 
		queue.add(1); //Operación de insercción
		queue.remove(); //Operación de borrado

		//Stack, estructura de datos que sigue el orden LIFO
		Stack<Integer> stack = new Stack<Integer>();
		stack.push(1); //Operación de insercción
		stack.pop(); //Operación de borrado

		//EXTRA: Crear una agenda de contactos
		EjercicioExtra();
	}

	public static void EjercicioExtra() {
		Scanner sc = new Scanner(System.in);
		Map<String, Integer> agenda = new HashMap<>();
		int opcion = 0;
		do {
			System.out.println("\n*** Agenda ***");
			System.out.println("Seleccione una opción:");
			System.out.println("1. Buscar Contacto");
			System.out.println("2. Nuevo Contacto");
			System.out.println("3. Actualizar Contacto");
			System.out.println("4. Eliminar Contacto");
			System.out.println("5. Salir");
			opcion = sc.nextInt();
			switch(opcion) {
				case 1:
					BuscarContacto(sc, agenda);
					break;
				case 2:
					NuevoContacto(sc, agenda);
					break;
				case 3:
					ActualizarContacto(sc, agenda);
					break;
				case 4:
					EliminarContacto(sc, agenda);
					break;
				case 5:
					System.out.println("Saliendo...");
					break;
				default:
					System.out.println("Opción no válida");
					break;
			}
		} while (opcion != 5);
		sc.close();
	}

	public static void BuscarContacto(Scanner sc, Map<String, Integer> agenda) {
        System.out.print("Ingrese el nombre del contacto: ");
        String nombre = sc.next();
        if (agenda.containsKey(nombre)) {
            System.out.println("Teléfono de " + nombre + ": " + agenda.get(nombre));
        } else {
            System.out.println("Contacto no encontrado.");
        }
    }

    public static void NuevoContacto(Scanner sc, Map<String, Integer> agenda) {
        System.out.print("Ingrese el nombre del nuevo contacto: ");
        String nombre = sc.next();
        System.out.print("Ingrese el número de teléfono: ");
        String telefono = sc.next();
        if (telefono.length() <= 11 && telefono.matches("\\d+")) {
            agenda.put(nombre, Integer.parseInt(telefono));
            System.out.println("Contacto agregado.");
        } else {
            System.out.println("Número de teléfono inválido. Debe ser numérico y no más de 11 dígitos.");
        }
    }

    public static void ActualizarContacto(Scanner sc, Map<String, Integer> agenda) {
        System.out.print("Ingrese el nombre del contacto a actualizar: ");
        String nombre = sc.next();
        if (agenda.containsKey(nombre)) {
            System.out.print("Ingrese el nuevo número de teléfono: ");
            String telefono = sc.next();
            if (telefono.length() <= 11 && telefono.matches("\\d+")) {
                agenda.put(nombre, Integer.parseInt(telefono));
                System.out.println("Contacto actualizado.");
            } else {
                System.out.println("Número de teléfono inválido. Debe ser numérico y no más de 11 dígitos.");
            }
        } else {
            System.out.println("Contacto no encontrado.");
        }
    }

    public static void EliminarContacto(Scanner sc, Map<String, Integer> agenda) {
        System.out.print("Ingrese el nombre del contacto a eliminar: ");
        String nombre = sc.next();
        if (agenda.containsKey(nombre)) {
            agenda.remove(nombre);
            System.out.println("Contacto eliminado.");
        } else {
            System.out.println("Contacto no encontrado.");
        }
    }
}