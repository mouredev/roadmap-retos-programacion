import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class GustavoGomez19{

    public static void main(String[] args) {
        /* Ejercicio: Implementa los mecanismos de introducción y recuperación propios de las
         * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
         * o lista.
         */

         // Pilas (stack - LIFO)
        Deque<Integer> pila = new ArrayDeque<>();

        System.out.println("**** PILAS (STACK - LIFO) ****");
        // Intorducción de elemanto en una pila (stack)
        pila.push(1);
        pila.push(2);
        pila.push(3);
        System.out.println("Pila: " + pila);
        pila.addLast(4);
        System.out.println(pila);
        pila.addFirst(5);
        System.out.println(pila);

        // Recuperación de elemento en una pila (stack)
        int elementoRecuperado = pila.poll();
        System.out.println("Elemento recuperdado: " + elementoRecuperado);
        int elementoRecuperado2 = pila.peek();
        System.out.println("Elemento recuperado 2: " + elementoRecuperado2); // Permite ver el elemento en la parte superior de la fila sin eliminarlo
        System.out.println(pila.reversed()); // Permite recuperar la pila en oreden invertido
        System.out.println(pila.getLast()); // Permite recuperar el último elemento de la pila
        System.out.println(pila);
        System.out.println();

        System.out.println("**** COLAS (QUEUE - FIFO) ****");
        // Colas (queue - FIFO)
        Queue<Integer> cola = new LinkedList<>();

        // Introducción de elementos 
        cola.add(1);
        cola.add(4);
        cola.add(2);
        cola.add(3);
        System.out.println("Cola: " + cola);
        
        // Recuperación de elemento
        System.out.println("Elemento recuperado: " + cola.peek());
        int elementoRecuperadoCola = cola.poll(); // Método poll recupera y elimina el elemento
        System.out.println("Elemento recuperado: " + elementoRecuperadoCola);
        System.out.println("Cola: " + cola);
        System.out.println(cola.remove(5)); // Remueve la primer concidencia encontrada según el número especificado, devuelve true si lo borró o false si no los borró

        /* DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos. */

        // Simulación de navegador
        System.out.println("*** NAVEGADOR ***");
        Deque<String> browser = new ArrayDeque<>();
        Scanner sc = new Scanner(System.in);
        String url = "";
        while (!url.equals("salir")) {
            System.out.print("Dirección URL: ");
            url = sc.nextLine();
            switch (url) {
                case "atras":
                    if (browser.size() > 1) {
                        browser.add(browser.poll());
                        System.out.println("Regresando a la pagina anterior " + browser.peek());
                    } else {
                        System.out.println("No existen más paginas para avanzar.");
                    }
                    break;

                case "adelante":
                    if (browser.size() > 0) {
                        browser.push(browser.poll());
                        System.out.println("Usted se encuentra en la siguiente pagina " + browser.peek());
                    } else {
                        System.out.println("No existen más paginas para avanzar.");
                    }
                    break;

                case "salir":
                    System.out.println("Cerrando el navegador.....");
                    break;
            
                default:
                    browser.push(url);
                    System.out.println("Se visitó la pagina " + browser.peek());
                    break;
            }
        }
        System.out.println();

        // Simulación de impresora
        System.out.println("*** FUNCIONAMIENTO DE IMPRESORA ***");
        Queue<String> impresora = new LinkedList<>();
        String documento = "";

        while (!documento.equals("salir")) {
            System.out.print("Ingrese el documento para imprimir: ");
            documento = sc.nextLine();
            if (!documento.equals("salir")) {
                switch (documento) {
                    case "imprimir":
                        if (impresora.size() > 0) {
                            System.out.println("Se esta imprimiendo el documento..." + impresora.poll());
                        } else {
                            System.out.println("No se tienen documentos para imprimir.");
                        }
                        break;

                    case "salir":
                        System.out.println("Apagando impresora...");
                        break;
                
                    default:
                        impresora.add(documento);
                        System.out.println("Documento " + documento + " agregado a la cola de impresión.");
                        break;
                }
            }
            
        }




    }

    
}