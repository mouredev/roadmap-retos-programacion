import java.util.Arrays;
import java.util.Scanner;

public class kleyner098 {

    public static void main(String[] args) {

        /*
         * EJERCICIO:
         * Implementa los mecanismos de introducción y recuperación de elementos propios
         * de las pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una
         * estructura de array o lista (dependiendo de las posibilidades de tu
         * lenguaje).
         */

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

        /*
         * DIFICULTAD EXTRA (opcional):
         * - Utilizando la implementación de pila y cadenas de texto, simula el
         * mecanismo adelante/atrás de un navegador web. Crea un programa en el que
         * puedas navegar a una página o indicarle que te quieres desplazar adelante o
         * atrás, mostrando en cada caso el nombre de la web.
         * Las palabras "adelante", "atras" desencadenan esta acción, el resto se
         * interpreta como el nombre de una nueva web.
         * - Utilizando la implementación de cola y cadenas de texto, simula el
         * mecanismo de una impresora compartida que recibe documentos y los imprime
         * cuando así se le indica.
         * La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
         * interpretan como nombres de documentos.
         */

        impresora();
        navegar();
    }

    static void navegar() {
        // variables
        Scanner sc = new Scanner(System.in);
        Pila<String> historial = new Pila();
        String pagina;
        String ultimaPagina = "";

        // Bucle que acaba cuando se escriba salir
        do {
            System.out.println(
                    "Escriba la url de la página, \"Adelante \" para avanzar de página ,\"Atras \" para retrocer de página o \"Salir\" para cerrar el programa");
            pagina = sc.nextLine();

            // Condición para avanzar de página
            if (pagina.equalsIgnoreCase("adelante")) {
                if (!(ultimaPagina.isEmpty())) {
                    historial.apilar(ultimaPagina);
                    System.out.println("Página: " + historial.cima() + "\n");
                    ultimaPagina = "";
                } else {
                    System.out.println("No hay más páginas para avanzar\n");
                }

                // Condición para retroceder de página
            } else if (pagina.equalsIgnoreCase("atras")) {

                if (historial.size() > 0) {
                    ultimaPagina = historial.desapilar();
                    String mensaje = (historial.size() > 0) ? "Página: " + historial.cima()
                            : "No hay páginas en el historial para retroceder";
                    System.out.println(mensaje + "\n");
                } else {
                    System.out.println("No hay páginas en el historial para retroceder\n");
                }

            } else {
                historial.apilar(pagina);
                System.out.println("Página actual: " + historial.cima() + "\n");
            }

        } while (!(pagina.equalsIgnoreCase("salir")));

        System.out.println("Cerrando navegador");
        
    }

    static void impresora() {
        // Variables
        Scanner sc = new Scanner(System.in);
        Cola<String> impresora = new Cola();
        String documento;
        String imprimiendo;

        // Bucle que acaba cuando se escriba salir
        do {
            System.out.println(
                    "Introduzaca el nombre del documento que quiere imprimir, escriba la \"Imprimir\" para imprimir el documento o \"Salir \" para cerrar el programa");
            documento = sc.nextLine();

            // Condición para imprimir
            if (documento.equalsIgnoreCase("imprimir")) {
                // Condición que imprime si la impresora tiene documentos
                if (impresora.size() > 0) {
                    imprimiendo = impresora.desencolar();
                    System.out.println("Imprimiendo documento: " + imprimiendo);
                } else {
                    System.out.println("No hay documento en la cola de la impresora");
                }
            } else {
                if (!(documento.equalsIgnoreCase("salir"))) {
                    impresora.encolar(documento);
                }

            }
            System.out.println("Documentos en la cola de la impresora: " + impresora + "\n");
        } while (!(documento.equalsIgnoreCase("salir")));
        System.out.println("Apagando impresora");
        
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
