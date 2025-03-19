import java.util.Arrays;

public class kleyner098 {
    /*
     * EJERCICIO:
     * Explora el concepto de clase y crea un ejemplo que implemente un
     * inicializador, atributos y una función que los imprima (teniendo en cuenta
     * lasposibilidades de tu lenguaje).
     * Una vez implementada, créala, establece sus parámetros, modifícalos e
     * imprímelos utilizando su función.
     *
     * DIFICULTAD EXTRA (opcional):
     * Implementa dos clases que representen las estructuras de Pila y Cola
     * (estudiadas en el ejercicio número 7 de la ruta de estudio)
     * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
     * retornar el número de elementos e imprimir todo su contenido.
     * 
     */

    public static void main(String[] args) {
        Contador count = new Contador(1, 2);
        System.out.println(count.toString());
        count.setFin(10);
        System.out.println(count.toString());
        count.contar();


        // DIFICULTAD EXTRA (opcional):
        Pila<Integer> pila = new Pila();
        pila.apilar(1);
        pila.apilar(2);
        pila.apilar(3);
        System.out.println("Pila : " + pila);
        pila.desapilar();
        pila.desapilar();
        System.out.println("Pila : " + pila);
        Cola<Integer> cola = new Cola();
        cola.encolar(1);
        cola.encolar(2);
        cola.encolar(3);
        System.out.println("Cola :" + cola);
        cola.desencolar();
        cola.desencolar();
        System.out.println("Cola :" + cola);
    } 
}

class Contador {
    // Atributos
    private int inicio;
    private int fin;

    // Constructor
    Contador(int inicio, int fin) {
        this.inicio = inicio;
        this.fin = fin;
    }

    // Getters y setters
    public int getInicio() {
        return inicio;
    }

    public void setInicio(int inicio) {
        this.inicio = inicio;
    }

    public int getFin() {
        return fin;
    }

    public void setFin(int fin) {
        this.fin = fin;
    }

    // Método que imprime los números desde inicio hasta fin.
    public void contar() {
        for (int i = inicio; i < fin; i++) {
            System.out.println(i);
        }
    }

    // toString
    @Override
    public String toString() {
        return "Inicio: " + inicio + " | Fin: " + fin;
    }

}

class Pila<T> {
    private T[] pila;

    Pila() {
        pila = (T[]) new Object[0];
    }

    public void apilar(T elemento) {
        pila = Arrays.copyOf(pila, pila.length + 1);
        pila[pila.length - 1] = elemento;
    }

    public T desapilar() {
        T eliminado = pila[pila.length - 1];
        pila = Arrays.copyOf(pila, pila.length - 1);
        return eliminado;
    }

    @Override
    public String toString() {
        return Arrays.toString(pila);
    }

    public int size() {
        return pila.length;
    }

    public T cima() {
        return pila[pila.length - 1];
    }
}

class Cola<T> {
    private T[] cola;

    Cola() {
        cola = (T[]) new Object[0];
    }

    public void encolar(T elemento) {
        cola = Arrays.copyOf(cola, cola.length + 1);
        cola[cola.length - 1] = elemento;
    }

    public T desencolar() {
        T eliminado = cola[0];
        System.arraycopy(cola, 1, cola, 0, cola.length - 1);
        cola = Arrays.copyOf(cola, cola.length - 1);
        return eliminado;
    }

    @Override
    public String toString() {
        return Arrays.toString(cola);
    }

    public int size() {
        return cola.length;
    }

    public T finalCola() {
        return cola[cola.length - 1];
    }
}