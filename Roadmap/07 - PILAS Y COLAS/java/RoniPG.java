import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

// @Roni
public class PILAS_Y_COLAS_07 {

	public static void main(String[] args) {
		/*
		 * EJERCICIO: Implementa los mecanismos de introducción y recuperación de
		 * elementos propios de las pilas (stacks - LIFO) y las colas (queue - FIFO)
		 * utilizando una estructura de array o lista (dependiendo de las posibilidades
		 * de tu lenguaje).
		 */

		// PILA(STACK)

		Stack<Integer> pila = new Stack<>();

		// Insertar datos

		pila.push(1);
		pila.push(2);
		pila.add(3);
		pila.push(4);
		pila.add(5);
		System.out.println("Contenido de la pila: " + pila);

		// Borrar datos

		pila.remove(1); // ---> Borrar dato en la posicion deseada
		// pila.clear(); ---> Eliminar(limpiar) todos los datos de la lista
		System.out.println("Contenido de la pila: " + pila);
		int elementoCima = pila.pop(); // ---> Borrar dato en la cima de la pila con un return del dato
		System.out.println("Contenido de la pila: " + pila);
		System.out.println("Elemento en la cima de la pila: " + elementoCima);

		// Actualizar datos

		System.out.println("Contenido de la pila: " + pila);
		pila.set(0, 2);
		System.out.println("Contenido de la pila: " + pila);

		// Ordenar datos

		pila.push(8);
		pila.push(5);
		pila.push(7);
		System.out.println(pila);
		Collections.sort(pila);
		System.out.println(pila);

		// COLA(QUEUE)

		// Creamos una cola usando LinkedList (también podemos usar PriorityQueue)
		Queue<String> cola = new LinkedList<>();

		// Agregamos elementos a la cola
		cola.add("Elemento 0");
		cola.offer("Elemento 1");
		cola.offer("Elemento 2");
		cola.offer("Elemento 3");

		// Mostramos la cola
		System.out.println("Cola: " + cola);

		// Eliminamos y mostramos el primer elemento de la cola
		String firstElement = cola.poll();
		System.out.println("Primer elemento de la cola: " + firstElement);

		// Mostramos la cola actualizada
		System.out.println("Cola actualizada: " + cola);

		// Obtenemos pero no eliminamos el primer elemento de la cola
		String peekedElement = cola.peek();
		System.out.println("Primer elemento de la cola (sin eliminar): " + peekedElement);

		// Mostramos la cola nuevamente (sin cambios)
		System.out.println("Cola actualizada (sin cambios): " + cola);
		/*
		 * DIFICULTAD EXTRA (opcional): - Utilizando la implementación de pila y cadenas
		 * de texto, simula el mecanismo adelante/atrás de un navegador web. Crea un
		 * programa en el que puedas navegar a una página o indicarle que te quieres
		 * desplazar adelante o atrás, mostrando en cada caso el nombre de la web. Las
		 * palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta
		 * como el nombre de una nueva web.
		 */

		Programa1();
		/*
		 * - Utilizando la implementación de cola y cadenas de texto, simula el
		 * mecanismo de una impresora compartida que recibe documentos y los imprime
		 * cuando así se le indica. La palabra "imprimir" imprime un elemento de la
		 * cola, el resto de palabras se interpretan como nombres de documentos.
		 */
		Programa2();
	}

	public static void Programa1() {
		Scanner entradaDatos = new Scanner(System.in);
		Stack<String> url = new Stack<>();
		url.add("www.google.com");
		url.add("www.twitter.com");
		url.add("www.gmail.com");
		String texto = "";
		int pos = 0;

		do {
			System.out.println("\n*******Navegación web*******\n");
			System.out.println("Escribe la url de la página web para dirigirte a ella.");
			System.out.println("Si la url no existe se creara una nueva web");
			System.out.println("Escribe 'adelante' para ir a la siguiente web.");
			System.out.println("Escribe 'atras' para ir a la web anterior.");
			System.out.println("Escribe 'salir' para cerrar el programa.");
			System.out.println("Escribe aquí: ");
			texto = entradaDatos.nextLine();
			if (texto.equalsIgnoreCase("adelante")) {
				if (pos + 1 >= url.size()) {
					System.out.println("Ya te encuentras en la url del final");
					System.out.println("La url es:\n" + url.get(pos));
				} else {
					System.out.println("Avanzamos");
					System.out.println("La siguinente url es:\n" + url.get(pos + 1));
					pos += 1;
				}
			} else if (texto.equalsIgnoreCase("atras")) {
				if (pos - 1 < 0) {
					System.out.println("Ya te encuentras en la url del principio");
					System.out.println("La url es:\n" + url.get(pos));
				} else {
					System.out.println("Retrocedemos");
					System.out.println("La url anterior es:\n" + url.get(pos - 1));
					pos -= 1;
				}
			} else if (url.contains(texto)) {
				System.out.println("Encontramos url");
				pos = url.indexOf(texto);
				System.out.println("La url es:\n" + url.get(pos));
			} else if (texto.equalsIgnoreCase("Salir")) {
				System.out.println("Vuelva pronto");
			} else {
				System.out.println("Creamos web");
				url.add(texto);
				System.out.println("La url es:\n" + url.lastElement());
				pos = (int) Math.round(url.size() / 2);
			}
		} while (!(texto.equalsIgnoreCase("salir")));
	}

	public static void Programa2() {
		Scanner entradaDatos = new Scanner(System.in);
		Queue<String> doc = new LinkedList<>();
		String texto = "";
		doc.add("Documento 1");
		doc.add("Documento 2");
		doc.add("Documento 3");

		do {
			System.out.println("\n*******Mecanismo de una impresora*******\n");
			System.out.println("Escribe 'imprimir' para ir a la imprimir el primer documento de la cola.");
			System.out.println("Si no, introduce el nombre del nuevo documento a imprimir y se añadira a la cola");
			System.out.println("Escribe 'salir' para cerrar el programa.");
			System.out.println("Escribe aquí: ");
			texto = entradaDatos.nextLine();
			if (texto.equalsIgnoreCase("imprimir")) {
				System.out.println("Procedemos a imprimir el documento: " + doc.poll());
			} else if (texto.equalsIgnoreCase("salir")) {
				System.out.println("Vuelva pronto");
			} else {
				System.out.println("Introducimos el nuevo documento");
				doc.add(texto);
			}

		} while (!(texto.equalsIgnoreCase("salir")));

	}
}
