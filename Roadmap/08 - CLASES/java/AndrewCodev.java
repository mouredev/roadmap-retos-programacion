
import java.util.*;

public class AndrewCodev {

	// Creando atributos
	private String nombre;
	private String apellido;
	private int edad;

	// Inicializamos los atributos en el constructor
	public AndrewCodev() {
		this.nombre = "Andres";
		this.apellido = "Lozano";
		this.edad = 29;
	}

	// Creamos los metodos Get y Set de cada atributo para acceder al valor de los
	// atributos en el constructor
	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getApellido() {
		return apellido;
	}

	public void setApellido(String apellido) {
		this.apellido = apellido;
	}

	public int getEdad() {
		return edad;
	}

	public void setEdad(int edad) {
		this.edad = edad;
	}

	public static void main(String[] args) {
		// creamos la instancia del objeto AndrewCodev y accedemos a sus métodos desde
		// el metodo main
		AndrewCodev andrewCodev = new AndrewCodev();
		// Imprimimos sus atributos
		System.out.println("Atributos inicializados");
		System.out.println("Nombre: " + andrewCodev.getNombre());
		System.out.println("Apellido: " + andrewCodev.getApellido());
		System.out.println("Edad: " + andrewCodev.getEdad());

		// Modificamos los atributos
		System.out.println("\nAtributos modificados");
		andrewCodev.setNombre("Felipe");
		System.out.println("Nombre: " + andrewCodev.getNombre());
		andrewCodev.setApellido("Mendoza");
		System.out.println("Apellido: " + andrewCodev.getApellido());
		andrewCodev.setEdad(30);
		System.out.println("Edad: " + andrewCodev.getEdad());

		// FIN DEL EJERCICIO BASE
	}

	// Creamos la clase que representa la estructura de PILAS
	static class ClsPilas {
		Stack<Integer> pila;

		// Creamos los métodos que ejecutarán las acciones de agregar, listar, remover,

		// Agregar elemento
		public Stack<Integer> agregar(Stack<Integer> pila, int numero) {
			pila.push(numero);
			return pila;
		}

		// Ver elemento superior en la pila
		public Stack<Integer> verUltimo(Stack<Integer> pila) {
			pila.peek();
			return pila;
		}

		// Listar todo
		public Stack<Integer> listarTodo(Stack<Integer> pila) {
			return pila;
		}

		// Eliminar elemento superior en la pila
		public Stack<Integer> eliminarUltimo(Stack<Integer> pila) {
			pila.pop();
			return pila;
		}

		// Eliminar todos
		public Stack<Integer> eliminarTodos(Stack<Integer> pila) {
			pila.clear();
			return pila;
		}
	}

	static class OrdenLlegada {
		Queue<Integer> cola;
		// Creamos los métodos que ejecutarán las acciones de agregar, listar, remover,

		// Agregar elemento
		public Queue<Integer> agregarPlato(Queue<Integer> cola, int numero) {
			cola.add(numero);
			return cola;
		}

		// Ver elemento superior en la pila
		public Queue<Integer> verUltimo(Queue<Integer> cola) {
			cola.peek();
			return cola;
		}

		// Ver elemento superior en la pila
		public Queue<Integer> verTodos(Queue<Integer> cola) {
			return cola;
		}

		// Eliminar elemento superior en la pila
		public Queue<Integer> eliminarUltimo(Queue<Integer> cola) {
			cola.remove();
			return cola;
		}

		// Eliminar todos
		public Queue<Integer> eliminarTodos(Queue<Integer> cola) {
			cola.clear();
			return cola;
		}
	}
}