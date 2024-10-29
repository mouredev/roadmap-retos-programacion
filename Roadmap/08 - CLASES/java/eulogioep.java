// Ejemplo de una clase en Java

/**
 * Clase Persona que representa a una persona con nombre y edad.
 */
class PersonaEulogio {
    // Atributos de la clase
    private String nombre;
    private int edad;

    // Constructor (inicializador)
    public PersonaEulogio(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    // Métodos getter y setter
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

    // Método para imprimir los datos de la persona
    public void imprimirDatos() {
        System.out.println("Nombre: " + nombre + ", Edad: " + edad);
    }
}

/**
 * Clase Pila que implementa una estructura de datos de tipo pila (LIFO).
 */
class PilaEulogio<T> {
    private java.util.LinkedList<T> elementos;

    public PilaEulogio() {
        elementos = new java.util.LinkedList<>();
    }

    public void push(T elemento) {
        elementos.push(elemento);
    }

    public T pop() {
        return elementos.pop();
    }

    public int size() {
        return elementos.size();
    }

    public void imprimirContenido() {
        System.out.println("Contenido de la pila: " + elementos);
    }
}

/**
 * Clase Cola que implementa una estructura de datos de tipo cola (FIFO).
 */
class ColaEulogio<T> {
    private java.util.LinkedList<T> elementos;

    public ColaEulogio() {
        elementos = new java.util.LinkedList<>();
    }

    public void enqueue(T elemento) {
        elementos.addLast(elemento);
    }

    public T dequeue() {
        return elementos.removeFirst();
    }

    public int size() {
        return elementos.size();
    }

    public void imprimirContenido() {
        System.out.println("Contenido de la cola: " + elementos);
    }
}

// Clase principal para probar las implementaciones
public class eulogioep {
    public static void main(String[] args) {
        // Prueba de la clase Persona
        PersonaEulogio persona = new PersonaEulogio("Juan", 30);
        persona.imprimirDatos();
        persona.setEdad(31);
        persona.imprimirDatos();

        // Prueba de la Pila
        PilaEulogio<Integer> pila = new PilaEulogio<>();
        pila.push(1);
        pila.push(2);
        pila.push(3);
        pila.imprimirContenido();
        System.out.println("Elemento extraído de la pila: " + pila.pop());
        pila.imprimirContenido();

        // Prueba de la Cola
        ColaEulogio<String> cola = new ColaEulogio<>();
        cola.enqueue("A");
        cola.enqueue("B");
        cola.enqueue("C");
        cola.imprimirContenido();
        System.out.println("Elemento extraído de la cola: " + cola.dequeue());
        cola.imprimirContenido();
    }
}