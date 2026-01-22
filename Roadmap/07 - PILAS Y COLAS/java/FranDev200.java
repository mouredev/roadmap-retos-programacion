import java.util.ArrayList;
import java.util.Scanner;

public class FranDev200 {

    static ArrayList<Integer> arrayStack = new ArrayList<>();
    static ArrayList<Integer> arrayQueue = new ArrayList<>();

    static void main() {

        /*
            Implementa los mecanismos de introducción y recuperación de elementos propios de las
            pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
            o lista (dependiendo de las posibilidades de tu lenguaje).
        */

        // Añadimos elementos al Stack
        for(int i = 0; i < 5; i++){
            push(i);
        }

        // Añadimos elementos al Queue
        for(int i = 0; i < 5; i++){
            offer(i);
        }

        System.out.println("STACK");
        System.out.println(arrayStack);
        System.out.println("--------------");
        System.out.println("- Eliminamos y mostramos el primer elemento: " + pop());
        System.out.println("==============================================");
        System.out.println("STACK");
        System.out.println(arrayStack);
        System.out.println("--------------");
        System.out.println("- Eliminamos y mostramos el primer elemento: " + pop());
        System.out.println("==============================================");
        System.out.println("STACK");
        System.out.println(arrayStack);
        System.out.println("--------------");
        System.out.println("- Mostramos el primer elemento: " + peek());
        System.out.println("==============================================");
        System.out.println("STACK");
        System.out.println(arrayStack);
        System.out.println("--------------");
        System.out.println("- Esta vacio el stack: " + empty());
        System.out.println("- Numero de la posicion 3: " + search(3));
        System.out.println("- Numero de la posicion 5: " + search(5));
        System.out.println("=============================================\n\n");
        System.out.println("QUEUE");
        System.out.println(arrayQueue);
        System.out.println("--------------");
        System.out.println("- Eliminamos y mostramos el primer elemento: " + poll());
        System.out.println("==============================================");
        System.out.println("QUEUE");
        System.out.println(arrayQueue);
        System.out.println("--------------");
        System.out.println("- Eliminamos y mostramos el primer elemento: " + poll());
        System.out.println("==============================================");
        System.out.println("QUEUE");
        System.out.println(arrayQueue);
        System.out.println("--------------");
        System.out.println("- Mostramos el primer elemento: " + element());
        System.out.println("==============================================");
        System.out.println("QUEUE");
        System.out.println(arrayQueue);
        System.out.println("--------------\n\n\n\n");

/*
        DIFICULTAD EXTRA (opcional):
        * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
        *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
        *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
        *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
        *   el nombre de una nueva web.
*/
        Scanner scan = new Scanner(System.in);
        ArrayList<String> arrayStackWeb = new ArrayList<>();
        int endPointWeb = 1;
        boolean exit = false;

        System.out.println("==========================================");
        System.out.println("||     BIENVENIDO AL NAVEGADOR JAVA     ||");
        System.out.println("------------------------------------------");
        System.out.println("   Espero que su uso sea de su agrado.    ");
        System.out.println("==========================================");
        System.out.println("\nOpciones:");
        System.out.println("- - - - - - - - - - - - - - - - - - - - - -");
        System.out.println("- Navegar adelante --> Escribir \"adelante\".");
        System.out.println("- Navegar atras --> Escribir \"atras\".");
        System.out.println("- Para exit --> Escribir \"salir\".");
        System.out.println("- Navegar a una nueva pagina web --> Escribir \"nombre_de_la_web\".");
        System.out.println("===========================================");

        while(!exit){

            System.out.print("Respuesta: ");

            String respuesta = scan.next();

            switch (respuesta){

                case "salir":
                    System.out.println("  ---  Saliendo del navegador  ---  ");
                    exit = true;
                    break;

                case "adelante":

                    if(endPointWeb == 1){
                        System.out.println("No se puede ir más adelante.");
                        break;
                    }

                    endPointWeb--;
                    System.out.println("Pagina actual: " + arrayStackWeb.get(arrayStackWeb.size() - endPointWeb));
                    break;

                case "atras":

                    if(endPointWeb == arrayStackWeb.size()){
                        System.out.println("No se puede ir más atrás.");
                        break;
                    }

                    endPointWeb++;
                    System.out.println("Pagina actual: " + arrayStackWeb.get(arrayStackWeb.size() - endPointWeb));
                    break;

                default:
                    arrayStackWeb.add(respuesta);
                    endPointWeb = 1;
                    System.out.println("Pagina actual: " + arrayStackWeb.get(arrayStackWeb.size() - endPointWeb));
                    break;
            }

        }

/*
        - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
        *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
        *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
        *   interpretan como nombres de documentos.
*/

        ArrayList<String> arrayQueueImpresora = new ArrayList<>();
        exit = false;

        System.out.println("\n\n\n\n============================================");
        System.out.println("||     BIENVENIDO A LA IMPRESORA JAVA     ||");
        System.out.println("--------------------------------------------");
        System.out.println("    Espero que su uso sea de su agrado.     ");
        System.out.println("============================================");
        System.out.println("\nOpciones:");
        System.out.println("- - - - - - - - - - - - - - - - - - - - - -");
        System.out.println("- Añadir documento --> Escribir \"nombre\".");
        System.out.println("- Imprimir documento --> Escribir \"imprimir\".");
        System.out.println("- Imprimir todos los documento --> Escribir \"imprimir_todo\".");
        System.out.println("- Ver los documentos en cola --> \"cola\"");
        System.out.println("- Para exit --> Escribir \"salir\".");
        System.out.println("===========================================");

        while (!exit){

            System.out.print("Respuesta: ");
            String respuesta = scan.next();

            switch (respuesta){

                case "salir":
                    exit = true;
                    System.out.println(" --- Apagando impresora --- ");
                    break;

                case "imprimir":

                    if(arrayQueueImpresora.isEmpty()){
                        System.out.println("Primero añade un documento a la cola.");
                    }else{
                        System.out.println("Imprimiendo " + arrayQueueImpresora.getFirst());
                        arrayQueueImpresora.removeFirst();
                    }
                    break;

                case "cola":

                    if(arrayQueueImpresora.isEmpty()){
                        System.out.println("Primero añade un documento a la cola.");
                    }else{
                        System.out.println(arrayQueueImpresora);
                    }
                    break;

                case "imprimir_todo":

                    if(arrayQueueImpresora.isEmpty()){
                        System.out.println("Primero añade un documento a la cola.");
                    }else{
                        for(String document: arrayQueueImpresora){
                            System.out.println("Imprimiendo " + document);
                            arrayQueueImpresora.remove(document);
                        }

                    }
                    break;

                default:

                    arrayQueueImpresora.addLast(respuesta);
                    System.out.println("Documento añadido a la cola.");
                    break;

            }

        }

    }



    // METODOS PARA EL STACK
    public static void push(int i){

        arrayStack.addFirst(i);

    }

    public static int pop(){

        int result =  arrayStack.getFirst();

        if(!empty()){
            arrayStack.removeFirst();
            return result;

        }else{
            System.out.println("El stack esta vacio.");
            return 0;
        }

    }

    public static Integer peek(){

        if(!empty()){
            return arrayStack.getFirst();
        }else{
            System.out.println("El array esta vacio.");
            return null;
        }

    }

    public static boolean empty(){

        return arrayStack.isEmpty();

    }

    public static int search(int position){

        if(position > arrayStack.size()){
            System.out.println("Esa posición excede el tamaño del stack.");
            return 0;
        }

        return arrayStack.get(position - 1);

    }

    // METODOS PARA LA QUEUE
    public static boolean offer(int i){

        arrayQueue.addLast(i);
        return true;

    }

    public static Integer poll(){

        int result =  arrayQueue.getFirst();

        if(!empty()){
            arrayQueue.removeFirst();
            return result;

        }else{
            System.out.println("La cola esta vacio.");
            return null;
        }

    }

    public static Integer element(){

        if(!empty()){
            return arrayStack.getFirst();
        }else{
            System.out.println("El array esta vacio.");
            return null;
        }

    }

}
