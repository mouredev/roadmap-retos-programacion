import java.util.*;

public class Josegs95 {
    public static void main(String[] args) {
        //Pilas. En java existe una clase que representa una pila, la clase Stack.
        Stack<String> bag = new Stack<>();
        bag.push("Bola roja"); //Sirve para añadir un elemento al final de la pila
        bag.push("Bola negra");
        bag.push("Bola azul");
        System.out.println("La pila: " + bag); //Out: 'La pila: [Bola roja, Bola negra, Bola azul]'

        bag.pop(); //Sirve para sacar el último elemento de la pila
        System.out.println("La pila: " + bag); //Out: 'La pila: [Bola roja, Bola negra]'

            //Implementación de pila a través de un arrayList
        List<String> stack = new ArrayList<>();
        stack.add("Elemento 1");
        stack.add("Elemento 2");
        stack.add("Elemento 3");
        System.out.println("Mi stack: " + stack); //Out: 'Mi stack: [Elemento 1, Elemento 2, Elemento 3]'

        stack.remove(stack.size() - 1); //Borra y devuelve el último elemento, como si fuera una pila
        System.out.println("Mi stack: " + stack); //Out: 'Mi stack: [Elemento 1, Elemento 2]'

        //Colas. En java existe una clase que representa una pila, la clase Queue.
        Queue<String> processes = new LinkedList<>();
        processes.offer("Process 1"); //Añade un elemento
        processes.offer("Process 2");
        processes.offer("Process 3");
        System.out.println("La cola: " + processes); //Out: 'La cola: [Process 1, Process 2, Process 3]'

        processes.poll(); //Borra el primer elemento
        System.out.println("La cola: " + processes); //Out: 'La cola: [Process 2, Process 3]'

            //Implementación de cola a través de un arrayList
        List<String> queue = new ArrayList<>();
        queue.add("Elemento 1");
        queue.add("Elemento 2");
        queue.add("Elemento 3");
        System.out.println("Mi queue: " + queue); //Out: 'Mi queue: [Elemento 1, Elemento 2, Elemento 3]'

        queue.remove(0); //Borra y devuelve el primer elemento, como si fuera una cola
        System.out.println("Mi queue: " + queue); //Out: 'Mi queue: [Elemento 1, Elemento 2]'

        //Reto
        System.out.println("\n");
        retoFinalPila();
        retoFinalCola();
    }

    static Scanner sc;

    public static void retoFinalPila(){
        sc = new Scanner(System.in);
        int sitesSize;

        List<String> sites = new ArrayList<>();
        List<String> cachedSites = new ArrayList<>();
        sites.add("Inicio");

        app: while(true){
            sitesSize = sites.size();
            System.out.println("Página actual: " + sites.get(sites.size() - 1));
            System.out.print("Escribe el nombre de la web, Adelante/Atrás para moverte o Salir: ");
            String reply = sc.nextLine();
            switch (reply.toLowerCase()){
                case "adelante":
                    if (cachedSites.size() > 0)
                        sites.add(cachedSites.remove(cachedSites.size() - 1));
                    break;
                case "atrás", "atras":
                    if (sitesSize > 1)
                        cachedSites.add(sites.remove(sites.size() - 1));
                    break;
                case "salir":
                    break app;
                default:
                    sites.add(reply);
                    cachedSites.removeAll(cachedSites);
            }
        }
    }

    public static void retoFinalCola(){
        sc = new Scanner(System.in);

        List<String> printer = new ArrayList<>();

        app: while(true){
            System.out.println("Documentos para imprimir: " + printer.size());
            System.out.print("Escribe el nombre de un documento, Imprimir o Salir: ");
            String reply = sc.nextLine();
            switch (reply.toLowerCase()){
                case "imprimir":
                    if (printer.size() > 0)
                        System.out.println("Imprimiendo: " + printer.remove(0));
                    break;
                case "salir":
                    break app;
                default:
                    printer.add(reply);
            }
        }
    }
}
