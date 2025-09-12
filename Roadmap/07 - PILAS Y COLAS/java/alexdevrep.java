package _07_Pilas_y_Colas;
//Importamos las librerías necesarias para el ejercicio
import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Scanner;


/*
 * EJERCICIO:
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
public class _07_Pilas_y_Colas {
    //Pilas LIFO Last In, First Out
    //Creamos una pila
    static Stack<String> pilaelementos = new Stack<>();

    //Colas FIFO First In, First Out
    //Creamos una cola
    static Queue<String> colaelementos = new LinkedList<>();

    public static void main (String[] args){
        //Añadimos elementos a la pila
        pilaelementos.push("Hola");
        pilaelementos.push("Java");
        pilaelementos.push("alexdevrep");
        pilaelementos.push("Mundo");
        System.out.println(pilaelementos);
        //Recuperamos el último elemento añadido a la lista en este caso "Mundo"
        System.out.println(pilaelementos.pop());
        System.out.println(pilaelementos);

        System.out.println("----------------------------------");
        //Añadimos elementos a la cola
        colaelementos.add("Hola");
        colaelementos.add("Java");
        colaelementos.add("Mundo");
        System.out.println(colaelementos);
        //Recuperamos el primer elemento añadido a la cola en este caso "Hola"
        System.out.println(colaelementos.poll());
        System.out.println(colaelementos);

        //Dificultad EXTRA
        //Ejercicio Pilas
        Stack<String> pila_web = new Stack<>();
        Scanner scanner = new Scanner(System.in);

        System.out.println("###---NAVEGADOR WEB---###");
        System.out.println("Pestaña nueva");

        while (true) {
            System.out.println("Por favor escriba ADELANTE si quiere acceder a una URL nueva, ATRAS si quiere cerrar la última URL, o SALIR para salir: ");
            String comando = scanner.nextLine();
            accion(pila_web, comando);

            if (comando.equals("SALIR")) {
                break;
            }
        }


        //Ejercicio Colas
        Queue<String> documentos = new LinkedList<>();

        while(true){
            System.out.println("Por favor escriba el nombre del archivo para añadirlo a la cola de la impresión , IMPRIMIR para imprimirlo y SALIR para apagar la impresora: ");
            String archivo = scanner.nextLine();
            impresora(documentos, archivo);
            if (archivo.equals("SALIR")){
                scanner.close();
                System.exit(0);
            }
        }

    }

    public static void accion(Stack<String> pila_web, String comando) {
        if (comando.equals("ADELANTE")) {
            System.out.println("Por favor indique a qué web quiere acceder: ");
            String web = new Scanner(System.in).nextLine();
            pila_web.push(web);
            System.out.println("Ahora estás viendo: " + pila_web.peek());
        } else if (comando.equals("ATRAS")) {
            if (pila_web.size() > 1) {
                pila_web.pop();
                System.out.println("Ahora estás viendo: " + pila_web.peek());
            } else {
                System.out.println("No hay historial de navegación para retroceder");
            }
        } else if (comando.equals("SALIR")) {
            System.out.println("Cerrando el navegador web");
        } else {
            System.out.println("Comando no reconocido");
        }
    }
    public static void impresora(Queue<String> documentos,String archivo){
        if (archivo.equals("IMPRIMIR")){
            if(documentos.size()>=1){
                System.out.println("Impriendo archivo"+ documentos.poll());
            }else {
                System.out.println("No hay archivos para imprimir");
            }
        }else if(archivo.equals("SALIR")){
            System.out.println("Apagando la impresora");
        }else{
            documentos.add(archivo);
            System.out.println("Documento añadido a la cola de impresion");
        }

    }
}

