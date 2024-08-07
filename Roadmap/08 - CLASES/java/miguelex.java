public class miguelex {

    static class Vehiculo {
        private String nombre;
        private int numRuedas;

        public Vehiculo(String nombre, int numRuedas) {
            this.nombre = nombre;
            this.numRuedas = numRuedas;
        }

        public String toString() {
            return "Vehiculo{" +
                    "nombre='" + nombre + '\'' +
                    ", numRuedas=" + numRuedas +
                    '}';
        }
    }

    static class Pila {
        private int[] elementos;
        private int tope;

        public Pila() {
            elementos = new int[10];
            tope = -1;
        }

        public void push(int elemento) {
            if (tope < elementos.length - 1) {
                elementos[++tope] = elemento;
            }
        }

        public int pop() {
            if (tope >= 0) {
                return elementos[tope--];
            }
            return -1;
        }

        public int size(){
            return tope + 1;
        }

        public void imprimir() {
            for (int i = 0; i <= tope; i++) {
                System.out.println(elementos[i]);
            }
        }
    }

    static class Cola {
        private int[] elementos;
        private int frente;
        private int fin;

        public Cola() {
            elementos = new int[10];
            frente = 0;
            fin = -1;
        }

        public void agregar(int elemento) {
            if (fin < elementos.length - 1) {
                elementos[++fin] = elemento;
            }
        }

        public int quitar() {
            if (frente <= fin) {
                return elementos[frente++];
            }
            return -1;
        }

        public int size(){
            return fin - frente + 1;
        }

        public void imprimir() {
            for (int i = frente; i <= fin; i++) {
                System.out.println(elementos[i]);
            }
        }
    }

    public static void main(String[] args) {
        Vehiculo coche = new Vehiculo("Coche", 4);
        Vehiculo bicicleta = new Vehiculo("bicicleta", 2);
        System.out.println(coche);
        System.out.println(bicicleta);

        Pila pila = new Pila();
        Cola cola = new Cola();

        pila.push(1);
        pila.push(2);
        pila.push(3);

        cola.agregar(1);
        cola.agregar(2);
        cola.agregar(3);

        pila.imprimir();
        pila.pop();
        pila.imprimir();
        System.out.println("Tamaño de la pila: " + pila.size());

        cola.imprimir();
        cola.quitar();
        cola.imprimir();
        System.out.println("Tamaño de la cola: " + cola.size());


    }
    
}
