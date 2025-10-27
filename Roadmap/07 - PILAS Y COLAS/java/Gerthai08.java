//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
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

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {

        /*
        //Pilas
        Stack<String> myStack =  new Stack<String>();

        //Método "empty" para saber si la pila está vacía
        System.out.println("Is my stack empty? " + myStack.empty());

        //Método "push" para agregar elementos
        myStack.push("Orange Ball");
        myStack.push("Violet Ball");
        myStack.push("Green Ball");

        //Imprimiendo elementos
        //"empty" y "isEmpty" son lo mismo, solo que hay una diferencia histórica, ya que el
        //Primero es propio de la clase Stack y el
        //Segundo es propio de la clase collection (version más moderna)
        System.out.println("Elements in stack: " + myStack);
        System.out.println("Is my stack empty? " + myStack.empty());
        while(!myStack.isEmpty()){
            myStack.pop();
            System.out.println("Elements in stack : " + myStack);
            System.out.println("Is my stack empty? " + myStack.empty());
        }

        //Colas
        Queue<String> myQueue = new LinkedList<>();

        //Método add para agregar elementos
        myQueue.add("ana");
        myQueue.add("Luis");
        myQueue.add("Marta");

        //Imprimir cola
        System.out.println("Cola inicial" + myQueue);

        //consultamos quién está primero
        System.out.println("Primero en la cola: " + myQueue.peek());

        //Mostramos en pantalla y eliminamos a la primér persona
        System.out.println("Mostramos y eliminamos: " + myQueue.poll());
        System.out.println("Cola después de mostrar y eliminar: " + myQueue);

        //consultamos quién está primero
        System.out.println("Primero en la cola: " + myQueue.peek());

        //Mostramos en pantalla y eliminamos a la primér persona
        System.out.println("Mostramos y eliminamos: " + myQueue.poll());
        System.out.println("Cola después de mostrar y eliminar: " + myQueue);

        //consultamos quién está primero
        System.out.println("Primero en la cola: " + myQueue.peek());

        //Mostramos en pantalla y eliminamos a la primér persona
        System.out.println("Mostramos y eliminamos: " + myQueue.poll());
        System.out.println("Cola vacía: " + myQueue);

        //si intento atender con poll en cola vacía, devuelve null
        System.out.println("Intentando atender mas: " + myQueue.poll());
        */

        //dificultad extra
        Scanner scanner = new Scanner(System.in);

        Stack<String> backStack = new Stack<>();
        Stack<String> fowardStack = new Stack<>();
        String actual = "Pagina de inicio";

        //Página inicial
        System.out.println("Navegador iniciado en: " + actual);

        while (true){
            System.out.println("\nEscribe una página, \"atras\", \"adelante\" o \"salir\"");
            String comando = scanner.nextLine().trim();

            if (comando.equalsIgnoreCase("salir")){
                System.out.println("Cerrando navegador...");
                break;
            }else if(comando.equalsIgnoreCase("atrás")){
                if (!backStack.isEmpty()){
                    fowardStack.push(actual);
                    actual = backStack.pop();
                }else{
                    System.out.println("No hay páginas atrás.");
                }
            } else if (comando.equalsIgnoreCase("adelante")) {
                if (!fowardStack.isEmpty()){
                    backStack.push(actual);
                    actual = fowardStack.pop();
                }else{
                    System.out.println("No hay páginas adelante.");
                }
            }else{
                //Navegar a una nueva pagina
                backStack.push(actual);
                actual = comando;
                fowardStack.clear();
            }

            System.out.println("Esats en: " + actual);
        }
        scanner.close();

        //Impresora
        Scanner sc = new Scanner(System.in);
        Queue<String> colaImpresion = new LinkedList<>();

        System.out.println("Impresora iniciada.");
        System.out.println("Escribe nombres de documentos o 'imprimir'. Escribe 'salir' para terminar.");

        while (true){
            System.out.println("Escribe un comando: ");
            String comando = sc.nextLine().trim();

            if (comando.equalsIgnoreCase("salir")){
                System.out.println("Apagando impresora...");
                break;
            }else if (comando.equalsIgnoreCase("imprimir")){
                if(!colaImpresion.isEmpty()){
                    String doc = colaImpresion.poll();
                    System.out.println("Imprimiendo: " + doc);
                }else {
                    System.out.println("No hay documentos en la cola");
                }
            } else {
                colaImpresion.offer(comando);
                System.out.println("Documento agregado: " + comando);
            }
            System.out.println("Cola actual: " + colaImpresion);
        }
        sc.close();
    }
}