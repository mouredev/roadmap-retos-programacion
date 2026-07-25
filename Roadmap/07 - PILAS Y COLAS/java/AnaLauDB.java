import java.util.Scanner;

public class AnaLauDB {
    public static void main(String[] args) {
        // PILA (Stack - LIFO)
        int[] pila = new int[5];
        int tope = -1;

        // Push
        tope++;
        pila[tope] = 10;
        tope++;
        pila[tope] = 20;
        tope++;
        pila[tope] = 30;

        // Pop
        System.out.println("Pila (LIFO):");
        while (tope >= 0) {
            System.out.println(pila[tope]);
            tope--;
        }

        // COLA
        int[] cola = new int[5];
        int inicio = 0, fin = 0;

        // Enqueue
        cola[fin++] = 100;
        cola[fin++] = 200;
        cola[fin++] = 300;

        // Dequeue
        System.out.println("\nCola (FIFO):");
        while (inicio < fin) {
            System.out.println(cola[inicio]);
            inicio++;
        }

        // --- Simulación navegador web (pila de cadenas) ---
        Scanner sc = new Scanner(System.in);
        String[] historial = new String[10];
        String[] adelante = new String[10];
        int topeHist = -1, topeAdel = -1;
        String paginaActual = null;

        System.out.println(
                "\nSimulación navegador web (escribe 'atrás', 'adelante' o nombre de web, 'salir' para terminar):");
        while (true) {
            System.out.print("> ");
            String entrada = sc.nextLine();
            if (entrada.equalsIgnoreCase("salir"))
                break;

            if (entrada.equalsIgnoreCase("atrás")) {
                if (topeHist >= 0) {
                    if (paginaActual != null) {
                        adelante[++topeAdel] = paginaActual;
                    }
                    paginaActual = historial[topeHist--];
                    System.out.println("Página actual: " + paginaActual);
                } else {
                    System.out.println("No hay páginas atrás.");
                }
            } else if (entrada.equalsIgnoreCase("adelante")) {
                if (topeAdel >= 0) {
                    historial[++topeHist] = paginaActual;
                    paginaActual = adelante[topeAdel--];
                    System.out.println("Página actual: " + paginaActual);
                } else {
                    System.out.println("No hay páginas adelante.");
                }
            } else {
                if (paginaActual != null) {
                    historial[++topeHist] = paginaActual;
                    topeAdel = -1; // Se pierde el historial de adelante
                }
                paginaActual = entrada;
                System.out.println("Página actual: " + paginaActual);
            }
        }

        // --- Simulación impresora compartida (cola de cadenas) ---
        String[] colaDocs = new String[10];
        int inicioDoc = 0, finDoc = 0;

        System.out.println("\nSimulación impresora (escribe nombre de documento o 'imprimir', 'salir' para terminar):");
        while (true) {
            System.out.print("> ");
            String entrada = sc.nextLine();
            if (entrada.equalsIgnoreCase("salir"))
                break;

            if (entrada.equalsIgnoreCase("imprimir")) {
                if (inicioDoc < finDoc) {
                    System.out.println("Imprimiendo: " + colaDocs[inicioDoc]);
                    inicioDoc++;
                } else {
                    System.out.println("No hay documentos en cola.");
                }
            } else {
                if (finDoc < colaDocs.length) {
                    colaDocs[finDoc++] = entrada;
                    System.out.println("Documento añadido a la cola: " + entrada);
                } else {
                    System.out.println("La cola está llena.");
                }
            }
        }
        sc.close();
    }
}
