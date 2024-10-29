import java.util.Queue;
import java.util.Stack;
import java.util.LinkedList;

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

	// Métodos Get y Set
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
		AndrewCodev andrewCodev = new AndrewCodev();
		System.out.println("Atributos inicializados");
		System.out.println("Nombre: " + andrewCodev.getNombre());
		System.out.println("Apellido: " + andrewCodev.getApellido());
		System.out.println("Edad: " + andrewCodev.getEdad());

		andrewCodev.setNombre("Felipe");
		andrewCodev.setApellido("Mendoza");
		andrewCodev.setEdad(30);
		System.out.println("\nAtributos modificados");
		System.out.println("Nombre: " + andrewCodev.getNombre());
		System.out.println("Apellido: " + andrewCodev.getApellido());
		System.out.println("Edad: " + andrewCodev.getEdad());

		// Usando la clase de Pilas
		ClsPilas pila = new ClsPilas();
		pila.agregar(10);
		pila.agregar(20);
		System.out.println("\nPila después de agregar elementos:");
		pila.listarTodo();
		System.out.println("Elemento en la cima: " + pila.verUltimo());
		pila.eliminarUltimo();
		System.out.println("Pila después de eliminar el último elemento:");
		pila.listarTodo();

		// Usando la clase de Colas
		OrdenLlegada cola = new OrdenLlegada();
		cola.agregarPlato(1);
		cola.agregarPlato(2);
		System.out.println("\nCola después de agregar elementos:");
		cola.verTodos();
		System.out.println("Elemento en el frente de la cola: " + cola.verUltimo());
		cola.eliminarUltimo();
		System.out.println("Cola después de eliminar el primer elemento:");
		cola.verTodos();
	}

	// Clase para manejar Pila
	static class ClsPilas {
		Stack<Integer> pila;

		public ClsPilas() {
			pila = new Stack<>();
		}

		public void agregar(int numero) {
			pila.push(numero);
		}

		public int verUltimo() {
			return pila.peek();
		}

		public void listarTodo() {
			System.out.println("Pila completa: " + pila);
		}

		public void eliminarUltimo() {
			pila.pop();
		}

		public void eliminarTodos() {
			pila.clear();
		}
	}

	// Clase para manejar Cola
	static class OrdenLlegada {
		Queue<Integer> cola;

		public OrdenLlegada() {
			cola = new LinkedList<>();
		}

		public void agregarPlato(int numero) {
			cola.add(numero);
		}

		public int verUltimo() {
			return cola.peek();
		}

		public void verTodos() {
			System.out.println("Cola completa: " + cola);
		}

		public void eliminarUltimo() {
			cola.remove();
		}

		public void eliminarTodos() {
			cola.clear();
		}
	}
}
