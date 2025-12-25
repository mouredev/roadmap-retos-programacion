import java.util.ArrayList;

public class AnaLauDB {
    public static void main(String[] args) {
        Programador programador1 = new Programador("Alice", "Java", 5);
        programador1.Info();

        programador1.nombre = "Laura";
        programador1.lenguaje = "Java";
        programador1.experiencia = 4;
        programador1.Info();

        System.out.println("   ");
        Pila p1 = new Pila();
        p1.push(40);
        p1.push(50);
        p1.push(60);
        p1.print();
        p1.pop();
        p1.print();

        Cola c1 = new Cola();
        c1.enqueue(70);
        c1.enqueue(80);
        c1.enqueue(90);
        c1.print();
        c1.dequeue();
        c1.print();
    }

    // EJERCICIO
    public static class Programador {
        String nombre;
        String lenguaje;
        int experiencia;

        public Programador(String nombre, String lenguaje, int experiencia) {
            this.nombre = nombre;
            this.lenguaje = lenguaje;
            this.experiencia = experiencia;
        }

        public void Info() {
            System.out.println("Nombre: " + nombre);
            System.out.println("Lenguaje: " + lenguaje);
            System.out.println("Años de experiencia: " + experiencia);
            System.out.println("     ");
        }
    }

    // RETO EXTRA
    public static class Pila {
        private ArrayList<Integer> elementos = new ArrayList<>();

        public Pila() {
            this.elementos = new ArrayList<>();
        }

        public void push(int elemento) {
            elementos.add(elemento);
        }

        public int pop() {
            if (!elementos.isEmpty())
                return -1;
            return elementos.remove(elementos.size() - 1);
        }

        public int size() {
            return elementos.size();
        }

        public void print() {
            System.out.print("Pila: " + elementos);
            System.out.println();
        }

    }

    public static class Cola {
        private ArrayList<Integer> elementos = new ArrayList<>();

        public Cola() {
            this.elementos = new ArrayList<>();
        }

        public void enqueue(int elemento) {
            elementos.add(elemento);
        }

        public int dequeue() {
            if (!elementos.isEmpty())
                return elementos.remove(0);
            return -1;
        }

        public int size() {
            return elementos.size();
        }

        public void print() {
            System.out.print("Cola: " + elementos);
            System.out.println();
        }

    }
}
