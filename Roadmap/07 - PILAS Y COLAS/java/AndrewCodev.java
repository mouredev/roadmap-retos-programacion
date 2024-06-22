import java.util.*;

public class AndrewCodev {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		// EJEMPLO DE PILAS - STACKS estas siguen el principio LIFO (Last In, First Out)
		System.out.println("EJEMPLO DE PILAS - STACKS");
		ejemploPilas();

		System.out.println("\nEJEMPLO DE COLAS - QUEUE");
		// EJEMPLO DE COLAS - QUEUES sigue el principio FIFO (First In, First Out)
		ejemploColas();

		// SELECCIONA UNO DE LOS EJERCICIO DE LA DIFICULTAD EXTRA
		menuPrincipal(scanner);
	}

	// EJERCICIO DE EJEMPLO DE PILAS
	public static void ejemploPilas() {
		Stack<Integer> stack = new Stack<>();
		// Añadir elementos (push)
		stack.push(1);
		stack.push(2);
		stack.push(3);
		stack.push(4);
		System.out.println("Pila después de push: " + stack);

		// Remover el elemento superior (pop)
		int top = stack.pop();
		System.out.println("Elemento removido (pop): " + top);
		System.out.println("Pila después de pop: " + stack);

		// Ver el elemento superior (peek)
		top = stack.peek();
		System.out.println("Elemento en la cima (peek): " + top);
		System.out.println("Pila después de peek: " + stack);

		// Comprobar si la pila está vacía
		boolean isEmpty = stack.isEmpty();
		System.out.println("¿La pila está vacía? " + isEmpty);
	}

	// EJERCICIO DE EJEMPLO DE COLAS
	public static void ejemploColas() {
		Queue<Integer> queue = new LinkedList<>();

		// Añadir elementos (add)
		queue.add(1);
		queue.add(2);
		queue.add(3);
		queue.add(4);
		System.out.println("Cola después de add: " + queue);

		// Remover el primer elemento (remove)
		int first = queue.remove();
		System.out.println("Elemento removido (remove): " + first);
		System.out.println("Cola después de remove: " + queue);

		// Ver el primer elemento (peek)
		first = queue.peek();
		System.out.println("Primer elemento (peek): " + first);
		System.out.println("Cola después de peek: " + queue);

		// Comprobar si la cola está vacía
		boolean isEmpty = queue.isEmpty();
		System.out.println("¿La cola está vacía? " + isEmpty);
	}

	// DIFICULTAD EXTRA
	// EJERCICIO DIFICULTAD EXTRA

	// DEPURANDO
	// Se crea un menú principal para escoges el proyecto a correr Navegador o
	// Impresora
	public static void menuPrincipal(Scanner scanner) {
		Queue<String> impresora = new LinkedList<>();
		Stack<Integer> pagina = new Stack<>();

		System.out.println("____________________________________________________");
		System.out.println("\nMENÚ PRINCIPAL");
		System.out.println("Escriba (1) - NAVEGADOR WEB\nEscriba (2) - IMPRESORA\nEscribe (3) - FINALIZAR PROGRAMA");
		String navegacion = scanner.nextLine();

		switch (navegacion) {
		case "1": {
			// EJERCICIO DIFICULTAD EXTRA NAVEGADOR WEB
			navegadorWeb(pagina,scanner);
		}
		case "2": {
			// EJERCICIO DIFICULTAD EXTRA IMPRESORA
			dpImpre(impresora, scanner);
		}
		case "3": {
			finProceso();
		}
		default:
			System.err.println("Selección no valida");
			menuPrincipal(scanner);
		}
	}

	public static void navegadorWeb(Stack<Integer> pagina, Scanner scanner) {
		String navegacion = "";
		System.out.println("____________________________________________________");
		if (pagina.isEmpty()) {
			pagina.push(1);
			System.out.println("Estás en el Home página " + pagina.peek());
			System.out.println("Escribe (ADELANTAR)" + "\nEscribe (ATRAS)" + "\nEscribe (CERRAR para ir al menú principal)");
			System.out.println("____________________________________________________");
		}
		navegacion = scanner.nextLine();
		navegadorWeb(adelanteAtras(pagina, navegacion.toLowerCase(),scanner),scanner);

	}

	public static Stack<Integer> adelanteAtras(Stack<Integer> pagina, String navegacion, Scanner scanner) {
		switch (navegacion) {
		case "adelantar": {
			pagina.push(pagina.peek() + 1);
			System.out.println("Estás en lo página " + pagina.peek());
			return pagina;
		}
		case "atras": {
			pagina.pop();
			if (pagina.isEmpty()) {
				System.out.println("Redireccionado al Home");
			} else {
				System.out.println("Estás en lo página " + pagina.peek());
			}
			return pagina;
		}
		case "cerrar": {
			System.out.println("Navegador cerrado");
			pagina.clear();
			menuPrincipal(scanner);
			break;
		}
		default:
			System.err.println("La opción no es valida");
			return pagina;
		}
		return pagina;
	}
	
	// EJERCICIO DE IMPRESORA
	// Se crea el menú para el programa de impresora

	public static void dpImpre(Queue<String> impresora, Scanner scanner) {
		String opcion = "";
		System.out.println("____________________________________________________");

		if (impresora.isEmpty()) {
			System.out.println("\nEscribe (1) - ABRIR MENÚ DE LA IMPRESORA");
			System.out.println("Escribe (2) - MENÚ PRINCIPAL");
			System.out.println("Escribe (3) - FINALIZAR PROGRAMA");
			opcion = scanner.nextLine();
			switch (opcion) {
			case "1": {
				menuImpresora(impresora, scanner);
			}
			case "2": {
				menuPrincipal(scanner);

			}
			case "3": {
				finProceso();

			}
			default:
				System.err.println("La opción no es valida");
				dpImpre(impresora, scanner);
			}
		}
	}

	public static void menuImpresora(Queue<String> impresora, Scanner scanner) {
		String opcion = "";
		System.out.println("\nLa impresora no tiene archivos para imprimir");
		System.out.println("Escribe (1) - AGREGA UN NUEVO ARCHIVO");
		System.out.println("Escribe (2) - IMPRIMIR ARCHIVO");
		System.out.println("Escribe (3) - IMPRIMIR TODO");
		System.out.println("Escribe (4) - REMOVER ARCHIVO");
		System.out.println("Escribe (5) - REMOVER TODO");
		System.out.println("\nEscribe (6) - MENÚ PRINCIPAL");
		System.out.println("Escribe (7) - FINALIZAR PROGRAMA");

		opcion = scanner.nextLine();
		switch (opcion) {
		case "1": {
			System.out.println("Escribe el nombre del archivo");
			impresora.add(scanner.nextLine());
			System.out.println(impresora);
			menuImpresora(impresora, scanner);
		}
		case "2": {
			if (!impresora.isEmpty()) {
				System.out.println("El archivo: (" + impresora.peek() + ") fue impreso con éxito");
				impresora.remove();
				System.out.println("Pendientes: "+impresora);
			}			
			menuImpresora(impresora, scanner);
		}
		case "3": {
			if (!impresora.isEmpty()) {
				System.out.println("Los archivos: (" + impresora + ") fueron impresos con éxito");
				impresora.clear();
			}
			menuImpresora(impresora, scanner);
		}

		case "4": {
			if (!impresora.isEmpty()) {
				System.err.println("El archivo: (" + impresora.peek() + ") fue ELIMINADO con éxito");
				impresora.remove();
				System.out.println("Pendientes: "+impresora);
			}
			menuImpresora(impresora, scanner);
		}

		case "5": {
			if (!impresora.isEmpty()) {
				System.err.println("Los archivos: (" + impresora + ") fueron ELIMINADOS con éxito");
				impresora.clear();
			}
			menuImpresora(impresora, scanner);
		}case "6": {
			menuPrincipal(scanner);
		}
		case "7": {
			finProceso();
		}
		default:
			System.err.println("La opción no es valida");
			menuImpresora(impresora, scanner);
		}
	}
	
	public static void finProceso() {
		System.out.println("EJECUCIÓN FINALIZADA");
		System.exit(0);
	}
}