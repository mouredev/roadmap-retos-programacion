import java.util.ArrayList;
import java.util.List;

class PersonaCesar {
    private String nombre;
    private int edad;

    public PersonaCesar(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    public void imprimirInformacion() {
        System.out.println("Nombre: " + this.nombre);
        System.out.println("Edad: " + this.edad);
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public int getEdad() {
        return this.edad;
    }
}

class PilaCesar {
    private List<Integer> pila;

    public PilaCesar(List<Integer> pila) {
        this.pila = pila;
    }

    public void push(int dato) {
        this.pila.add(dato);
    }

    public int pop() {
        int lastIndex = this.pila.size() - 1;
        int dato = this.pila.get(lastIndex);
        this.pila.remove(lastIndex);
        return dato;
    }

    public void imprimir() {
        System.out.println(this.pila);
    }
}

class ColaCesar {
    private List<Integer> cola;

    public ColaCesar(List<Integer> cola) {
        this.cola = cola;
    }

    public void enqueue(int dato) {
        this.cola.add(dato);
    }

    public int dequeue() {
        return this.cola.remove(0);
    }

    public void imprimir() {
        System.out.println(this.cola);
    }
}

class Main {
    public static void main(String[] args) {
        PersonaCesar person1 = new PersonaCesar("Juan", 30);
        person1.imprimirInformacion();
        person1.setNombre("Pedro");
        person1.setEdad(25);
        person1.imprimirInformacion();
        System.out.println(person1.getNombre());
        System.out.println(person1.getEdad());

        PilaCesar pila1 = new PilaCesar(new ArrayList<>());
        pila1.push(1);
        pila1.push(2);
        pila1.push(3);
        pila1.imprimir();
        System.out.println(pila1.pop());
        pila1.imprimir();

        ColaCesar cola1 = new ColaCesar(new ArrayList<>());
        cola1.enqueue(1);
        cola1.enqueue(2);
        cola1.enqueue(3);
        cola1.imprimir();
        System.out.println(cola1.dequeue());
        cola1.imprimir();
    }
}
