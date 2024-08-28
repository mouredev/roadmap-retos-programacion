import java.util.Scanner;
import java.util.Stack;
import java.util.LinkedList;
import java.util.Queue;

public class TofeDev {
/* EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */
    public class Navegador {

        public static void main(String[] args) {
            stackNavegacion();
        }
    
        public static void stackNavegacion() {
            Stack<String> historial = new Stack<>();
            Scanner scan = new Scanner(System.in);
            int pointerIndex = 0;
    
            while (true) {
                if (!historial.isEmpty()) {
                    System.out.println("---------------------------");
                    historial.forEach(h -> System.out.printf("%s | ", h));
                    System.out.println("\n" + "---------------------------");
                    System.out.print("Ingrese la 'página' o 'adelante' para avanzar, 'atras' para retroceder, o 'salir' para finalizar: ");
                } else {
                    System.out.println("Ingrese la página a visitar: ");
                }
                
                String comando = scan.next();
                
                switch (comando) {
                    case "adelante":
                        if (pointerIndex < historial.size() - 1) {
                            pointerIndex++;
                            System.out.printf("Visualizando la página %s\n\n", historial.get(pointerIndex));
                        } else {
                            System.out.println("No hay más historial hacia adelante\n\n");
                        }
                        break;
                        
                    case "atras":
                        if (pointerIndex > 0) {
                            pointerIndex--;
                            System.out.printf("Visualizando la página %s\n\n", historial.get(pointerIndex));
                        } else {
                            System.out.println("No hay más historial hacia atrás\n\n");
                        }
                        break;
                        
                    case "salir":
                        System.out.println("Saliendo del navegador");
                        scan.close();
                        System.exit(0);
                        break;
                        
                    default:
                        System.out.printf("Visualizando la página %s\n\n", comando);
                        historial.add(comando);
                        pointerIndex = historial.size() - 1;
                        break;
                }
            }
        }
    }

    public class Impresora {

        public static void main(String[] args) {
            colaImpresora();
        }
    
        public static void colaImpresora() {
            Queue<String> porImprimir = new LinkedList<>();
            Scanner scanner = new Scanner(System.in);
            
            System.out.println("******************************************************************");
            System.out.println("Ingrese 'agregar' para agregar un archivo a la cola de impresión");
            System.out.println("Ingrese 'imprimir' para empezar a imprimir un documento de la cola");
            System.out.println("Ingrese 'mostrar' para mostrar todos los documentos en la cola");
            System.out.println("Ingrese 'salir' para finalizar");
            System.out.println("******************************************************************");
    
            while (true) {
                System.out.print("Acción a realizar: ");
                String comando = scanner.next();
                
                switch (comando) {
                    case "mostrar":
                        System.out.println("-----------------------------------");
                        System.out.println(String.format("Documentos en cola (%d)", porImprimir.size()));
                        for (String doc : porImprimir) {
                            System.out.println("- " + doc);
                        }
                        break;
                        
                    case "agregar":
                        System.out.println("-----------------------------------");
                        System.out.print("Ingresa el nombre del documento: ");
                        String nombre = scanner.next();
                        porImprimir.add(nombre);
                        break;
                        
                    case "imprimir":
                        System.out.println("-----------------------------------");
                        if (porImprimir.isEmpty()) {
                            System.out.println("No hay nada para imprimir");
                            break;
                        }
                        System.out.println("Imprimiendo " + porImprimir.poll() + " ...");
                        try {
                            Thread.sleep(2000);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                        break;
                    case "salir":
                        System.out.println("Apagando la impresora");
                        scanner.close();
                        System.exit(0);
                        break;
                    default:
                        System.out.println("Comando no reconocido");
                        break;
                }
            }
        }
    }
}