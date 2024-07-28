public class Main {

    /*Pila*/
    public static ArrayList<Integer> stack = new ArrayList<>();

    public static void showStack() {
        System.out.println("Stack:");
        String space = ", ";
        for (int i = 0; i < stack.size(); i++) {
            System.out.print(stack.get(i) + space);
            if (i == stack.size() - 2) {
                space = "\n";
            }
        }
        System.out.println();
    }

    public static void push(int number) {
        stack.add(number);
    }

    public static int pop() {
        int number = stack.get(stack.size() - 1);
        stack.remove(stack.size() - 1);
        return number;
    }

    /*Cola*/
    public static ArrayList<Integer> queue = new ArrayList<>();

    public static void showQueue() {
        System.out.println("Queue:");
        String space = ", ";
        for (int i = 0; i < queue.size(); i++) {
            System.out.print(queue.get(i) + space);
            if (i == queue.size() - 2) {
                space = "\n";
            }
        }
        System.out.println();
    }

    public static void enqueue(int number) {
        queue.add(number);
    }

    public static int dequeue() {
        int number = queue.get(0);
        queue.remove(0);
        return number;
    }

    public static void webBrowser(){
        boolean exit = false;
        ArrayList<String> stackBrowser = new ArrayList<>();
        do {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Bienvenido al navegador web: ");
            System.out.println("'adelante' - Para moverse adelante");
            System.out.println("'atrás' - Para moverse atrás");
            System.out.println("'salir' - Para salir del navegador");
            System.out.println("'URL' - Para cambiar de página" + "\n");

            System.out.print("Introduce el texto: ");

            String option = scanner.nextLine();

            switch (option) {
                case "adelante":
                    break;
                case "atrás":
                    if (stackBrowser.size() > 1) {
                        stackBrowser.remove(stackBrowser.size() - 1);
                    }
                    break;
                case "salir":
                    exit = true;
                    break;
                default:
                    stackBrowser.add(option);
            }
            if (stackBrowser.size() > 1) {
                System.out.println("Web actual: " + stackBrowser.get(stackBrowser.size() - 1));
            }else{
                System.out.println("Página de inicio");
            }

        } while (!exit);
    }

    public static void printer(){
        boolean exit = false;
        ArrayList<String> queuePrinter = new ArrayList<>();
        do{
            Scanner scanner = new Scanner(System.in);
            System.out.println("Bienvenido a la impresora: ");
            System.out.println("'imprimir' - Para imprimir un documento");
            System.out.println("'salir' - Para salir");
            System.out.println("'documento' - Para añadir un documento a la cola de impresión"+ "\n");

            String option = scanner.nextLine();

            switch (option) {
                case "imprimir":
                    if (queuePrinter.size() >= 1) {
                        System.out.println("Imprimiendo documento: " + queuePrinter.get(0) + "\n");
                        queuePrinter.remove(0);
                    }else {
                        System.out.println("No hay documentos para imprimir" + "\n");
                    }
                    break;
                case "salir":
                    exit = true;
                    break;
                default:
                    queuePrinter.add(option);
            }

        }while (!exit);
    }


    public static void main(String[] args) {
        /*Pila*/

        //Añadimos contenido a la pila
        push(0);
        push(1);
        push(2);
        push(3);
        push(4);
        push(5);

        //Mostramos el contenido de la pila
        showStack();

        //Desapilamos un elemento
        System.out.println("Elemento retirado: " + pop() + "\n");

        //Mostramos el contenido de la pila
        showStack();

        //Desapilamos un elemento
        System.out.println("Elemento retirado: " + pop() + "\n");

        //Mostramos el contenido de la pila
        showStack();

        System.out.println("---------------------------");

        /*Cola*/

        //Añadimos elementos a la cola
        enqueue(0);
        enqueue(1);
        enqueue(2);
        enqueue(3);
        enqueue(4);
        enqueue(5);

        //Mostramos el contenido de la cola
        showQueue();

        //Desencolamos un elemento
        System.out.println("Elemento retirado: " + dequeue() + "\n");

        //Mostramos el contenido de la cola
        showQueue();

        //Desencolamos un elemento
        System.out.println("Elemento retirado: " + dequeue() + "\n");

        //Mostramos el contenido de la cola
        showQueue();

        /*Dificultad Extra*/

        //Navegador web
        webBrowser();

        //Impresora
        printer();
    }
}
