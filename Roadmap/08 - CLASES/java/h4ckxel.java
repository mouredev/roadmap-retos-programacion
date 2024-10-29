import java.util.ArrayList;
import java.util.List;

class PersonaH4ckxel {
    private String nombre;
    private int edad;

    public PersonaH4ckxel(String nombre, int edad) {
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

class PilaH4ckxel {
    private List<Integer> pila;

    public PilaH4ckxel(List<Integer> pila) {
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

class ColaH4ckxel {
    private List<Integer> cola;

    public ColaH4ckxel(List<Integer> cola) {
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

class MainH4ckxel {
    public static void main(String[] args) {
        PersonaH4ckxel person1 = new PersonaH4ckxel("Juan", 30);
        person1.imprimirInformacion();
        person1.setNombre("Pedro");
        person1.setEdad(25);
        person1.imprimirInformacion();
        System.out.println(person1.getNombre());
        System.out.println(person1.getEdad());

        // Usa PilaH4ckxel en lugar de ColaH4ckxel para manejar una pila
        PilaH4ckxel pila1 = new PilaH4ckxel(new ArrayList<>());
        pila1.push(1);
        pila1.push(2);
        pila1.push(3);
        pila1.imprimir();
        System.out.println(pila1.pop());
        pila1.imprimir();

        // Usa ColaH4ckxel para manejar una cola
        ColaH4ckxel cola1 = new ColaH4ckxel(new ArrayList<>());
        cola1.enqueue(1);
        cola1.enqueue(2);
        cola1.enqueue(3);
        cola1.imprimir();
        System.out.println(cola1.dequeue());
        cola1.imprimir();
    }
}
