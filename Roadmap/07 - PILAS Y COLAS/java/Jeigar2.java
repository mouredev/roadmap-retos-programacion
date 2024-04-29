import java.util.*;

public class Jeigar2 {
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
    public static void main(String[] args) {
        System.out.println("---pilas---");
        gestionPila();
        System.out.println("OK");
        System.out.println("---colas---");
        gestionCola();
        System.out.println("OK");
        int opcion = -1;
        do {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Qué acción quieres hacer");
            System.out.println("(1) Navegación por Internet");
            System.out.println("(2) Impresora");
            System.out.println("(0) Salir");
            try {
                opcion = scanner.nextInt();
                switch (opcion) {
                    case 1: {
                        navegar(scanner);
                        break;
                    }
                    case 2: {
                        imprimir(scanner);
                        break;
                    }
                    case 0: {
                        scanner.close();
                        System.exit(0);
                    }
                }
            }catch (InputMismatchException e) {
                System.out.println("Introduce el número de tu opción, por favor");
                opcion = -1;
            }
        }while (true);
    }

    private static void imprimir(Scanner scanner){
        Impresora impresora = Impresora.getInstance();
        String opcion = null;
        do {
            opcion = scanner.nextLine();
            System.out.println("Introduzca <acción> " + Impresora.IMPRIMIR + " o nombre del documento a imprimir");
            System.out.println("(0) Salir");
            if(!opcion.equals("0")){
                impresora.accion(opcion);
            }
        } while (!"0".equals(opcion));

//        impresora.accion("La Biblia");
//        impresora.accion("Don Quijote de la Mancha");
//        impresora.accion("El juicio de Cristo");
//        impresora.accion("El milagro del padre Stu");
//        impresora.accion(Impresora.IMPRIMIR);
    }

    private static void navegar(Scanner scanner) {
        int comando = -1;
        Navegador navegador = new Navegador();
        String pagina = null;
        do {
            do {
                System.out.println("Navegador, que accion quieres hacer");
                System.out.println("(1) Url");
                if(navegador.existeSiguentePagina()) {
                    System.out.println("(2) Adelante");
                }
                if(navegador.existeSiguenteAnterior()) {
                    System.out.println("(3) Atrás");
                }
                System.out.println("(0) Salir");
                scanner = new Scanner(System.in);
                try {
                    comando = scanner.nextInt();
                } catch (InputMismatchException e) {
                    System.out.println("Introduce el número de tu opción, por favor");
                    comando = -1;
                }
            }while (!(comando >= 0 && comando <= 3));

            switch (Navegador.Comando.values()[comando]){
                case URL_PAGINA -> {
                    do{
                        pagina = scanner.nextLine();
                        System.out.println("introducir URL: ");
                    } while (pagina == null || pagina.isEmpty() || pagina.isBlank());
                    navegador.nuevaPagina(pagina);
                    System.out.println("Pagina: " + pagina);
                }
                case ADELANTE -> System.out.println("Pagina: " + navegador.adelante());
                case ATRAS -> System.out.println("Pagina: " + navegador.atras());
                case SALIR -> {
                    System.exit(0);}
            }
        }while(true);
    }

    private static void gestionPila (){
        Stack<String> pila = new Stack<>();
        List<String> nombres = Arrays.asList("Adriana", "Jesús", "André", "Almudena");
        nombres.stream().forEach(pila::push);

        pila.stream().forEach(System.out::println);
        do {
            System.out.println(pila.pop());
        }while (!pila.isEmpty());
    }

    private static void gestionCola (){
        Queue<String> cola = new ArrayDeque<>();
        List<String> nombres = Arrays.asList("Adriana", "Jesús", "André", "Almudena");
        nombres.stream().forEach(cola::add);

        cola.stream().forEach(System.out::println);
        do {
            System.out.println(cola.remove());
        }while (!cola.isEmpty());
    }

    /*
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
}

class Navegador {
    public enum Comando {
        SALIR,
        URL_PAGINA,
        ADELANTE,
        ATRAS;
    }
    public String HOME = "Home";

    private Stack<String> pilaAvance;
    private Stack<String> pilaRetroceso;
    private String paginaActual;

    public Navegador(){
        pilaAvance = new Stack<>();
        pilaRetroceso = new Stack<>();
        paginaActual = HOME;
    }

    public boolean existeSiguentePagina(){
        return !pilaAvance.isEmpty();
    }
    public boolean existeSiguenteAnterior(){
        return !pilaRetroceso.isEmpty();
    }

    public void nuevaPagina(String pagina){
        // vaciamos las páginas siguientes porque hay nueva navegación
        while(!pilaAvance.isEmpty()) {
            pilaAvance.pop();
        }
        pilaRetroceso.push(paginaActual);
        paginaActual = pagina;
    }

    public String adelante(){
        if(!pilaAvance.isEmpty()){
            pilaRetroceso.push(paginaActual);
            paginaActual = pilaAvance.pop();
        }
        return paginaActual;
    }

    public String atras(){
        if(!pilaRetroceso.isEmpty()){
            pilaAvance.push(paginaActual);
            paginaActual = pilaRetroceso.pop();
        }
        return paginaActual;
    }
}

class Impresora {
    public static final String IMPRIMIR = "Imprimir";
    private static Impresora miImpresora;
    private Queue<String> cola = new ArrayDeque<>();

    private Impresora() {}

    public static Impresora getInstance() {
        if (miImpresora == null)
            miImpresora = new Impresora();
        return miImpresora;
    }

    public void accion(String documento) {
        if (IMPRIMIR.equals(documento)){
            cola.stream().forEach(doc -> System.out.println(cola.remove()));
        } else {
            cola.add(documento);
        }

        if(cola.isEmpty()){
            System.out.println("\n--- La cola de impresión está vacía ---\n");
        }
    }
}