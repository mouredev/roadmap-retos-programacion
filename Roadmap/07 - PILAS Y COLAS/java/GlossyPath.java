import java.util.Arrays;
import java.util.Collections;
import java.util.InputMismatchException;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

/**
 * 
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 *  @version v1.0
 * 
 *  @since 09/07/2024
 * 
 * @author GlossyPath
 */

public class GlossyPath {

    
    public static void main(String[] args) {
        
        System.out.println("---------PILAS(STACK)--------"); //Last In, First Out
        Stack<String> frutas = new Stack<>();

        frutas.push("melon");
        frutas.push("fresa");
        frutas.push("manzana");

        frutas.remove(0);

        String elementoCima = frutas.pop();

        System.out.println(frutas.peek());

        frutas.set(0, "Melon griego");

        frutas.stream().forEach(System.out::println);

        System.out.println(frutas.peek());

        Collections.sort(frutas); //ordenar los objetos

        frutas.stream().forEach(System.out::println);

        System.out.println("---------COLAS(QUEUE)---------");//First In, First Out

        List<String> nom = Arrays.asList("Laura", "Maria", "Paco", "Luis");

        Queue<String> nombres = new LinkedList<>();

        nombres.addAll(nom);

        nombres.add("Jose");

        System.out.println("La lista de nombres esta vacia? " + nombres.isEmpty());

        nombres.remove("Laura");

        while(!nombres.isEmpty()){
           System.out.println(nombres.poll()); 
        }

/**
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

        System.out.println("-------DIFICULTAD EXTRA----------");

        Scanner sc = new Scanner(System.in);
        int opcion = -1;

        do {
            System.out.println("Escoge la opción que queires realizar(1,2,3): " +
            "\n1. Navegar por internet." +
            "\n2. Impresora" +
            "\n3. Salir");

            try {
                opcion = sc.nextInt();
                sc.nextLine();

                switch (opcion) {
                    case 1:
                        navegador(sc);
                        break;

                    case 2:
                        impresora(sc);
                        break;

                    case 3:
                        System.out.println("Saliendo...");
                        break;

                    default:
                        System.out.println("Opción no válida. Inténtalo de nuevo.");
                        break;
                }

            } catch (InputMismatchException e) {
                System.out.println("Introduce una opción válida");
                sc.nextLine(); // Limpiar el buffer
            }

        } while (opcion != 3);

        sc.close();
        }

        public static void navegador(Scanner sc) {

        Navegador navegador = new Navegador();
        String input;

        do {
            System.out.println("Introduce la acción que quieres realizar en el navegador (URL, adelante, atras o salir)");

            System.out.print("URL: ");
            input = sc.nextLine();

            if (input.equalsIgnoreCase("adelante")) {
                navegador.adelante();

            } else if (input.equalsIgnoreCase("atras")) {
                navegador.atras();

            } else if (!input.equalsIgnoreCase("salir")) {
                navegador.nuevaPagina(input);
            }

            navegador.mostrarEstado();

        } while (!input.equalsIgnoreCase("salir"));
    }

        static class Navegador {

        private Stack<String> pilaAdelante;
        private Stack<String> pilaAtras;
        private String paginaActual;

        public Navegador() {
            pilaAdelante = new Stack<>();
            pilaAtras = new Stack<>();
            paginaActual = "";
        }

        public boolean hayPaginaDelante() {
            return !pilaAdelante.isEmpty();
        }

        public boolean hayPaginaDetras() {
            return !pilaAtras.isEmpty();
        }

        public void nuevaPagina(String url) {
            if (!paginaActual.isEmpty()) {
                pilaAtras.push(paginaActual);
            }
            paginaActual = url;
            pilaAdelante.clear();
            System.out.println("Navegando a: " + url);
        }

        public void adelante() {
            if (hayPaginaDelante()) {
                pilaAtras.push(paginaActual);
                paginaActual = pilaAdelante.pop();
                System.out.println("Navegando a: " + paginaActual);
            } else {
                System.out.println("No hay páginas adelante.");
            }
        }

        public void atras() {
            if (hayPaginaDetras()) {
                pilaAdelante.push(paginaActual);
                paginaActual = pilaAtras.pop();
                System.out.println("Navegando a: " + paginaActual);
            } else {
                System.out.println("No hay páginas atrás.");
            }
        }

        public void mostrarEstado() {
            System.out.println("Página actual: " + paginaActual);
            System.out.println("Páginas atrás: " + pilaAtras);
            System.out.println("Páginas adelante: " + pilaAdelante);
        }
    }

        public static void impresora (Scanner sc){

            String accion;

            Impresora impresora = new Impresora();

            do{
                System.out.println("Introduce la acción que quieres realizar en la impresora (Imprimir o salir)");
                accion = sc.nextLine();

                if(accion.equalsIgnoreCase("Imprimir")){
                    impresora.imprimir();

                } else if(!accion.equalsIgnoreCase("salir")){
                    impresora.añadirDocumento(accion);
                }

                impresora.mostrarTodo();

            } while(!accion.equalsIgnoreCase("salir"));
        }

        static class Impresora {
            private Queue<String> colaImpresion;


            public Impresora(){
                colaImpresion = new LinkedList<>();
            }


            public void imprimir(){
                if(hayDocumento()){
                    String impresion = this.colaImpresion.remove();
                    System.out.println("Imprimiendo: " + impresion);
                }
            }


            public boolean hayDocumento(){
                return !colaImpresion.isEmpty();
            }


            public void añadirDocumento(String documento){
                colaImpresion.add(documento);
            }

            public void mostrarTodo(){

                System.out.println("Cola de impresion");
                for(String s: this.colaImpresion){
                    System.out.println(s);
                }


                
         }        
    }
}