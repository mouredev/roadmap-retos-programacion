import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * #07 PILAS Y COLAS
 *
 * @author martinbohorquez
 */
public class matinbohorquez {
    private static final String DOMAIN_REGEX = "^(?:https?:\\/\\/)?(?:www\\.)?((?:[a-zA-Z0-9\\-]+\\.)+[a-zA-Z]{2,})(\\/[^\\s]*)?$";
    private static final Pattern DOMAIN_PATTERN = Pattern.compile(DOMAIN_REGEX);
    /**
     * Pila / Stack (LIFO)
     */
    private static Stack<Integer> pila = new Stack<>();
    /**
     * Cola / Queue (FIFO)
     */
    private static Queue<Integer> cola = new LinkedList<>();

    private static void webNavigator() {
        Stack<String> stack = new Stack<>();
        Stack<String> stackBackup = new Stack<>();

        outterLoop:
        while (true) {
            Scanner scanner = new Scanner(System.in);
            System.out.print("""
                    -----------------------------------------------------------
                    Bienvenido al navegador web, ingresar una de las siguientes opciones:
                    1. Escribir una URL válida para navegar a una página web.
                    2. "adelante" - para regresar a una página posterior.
                    3. "atrás" - para regresar a una página anterior.
                    4. "salir" - para cerrar el navegador.
                    -----------------------------------------------------------
                    """);
            System.out.print("Ingresar su opción: ");
            String action = scanner.nextLine();

            switch (action) {
                case "salir" -> {
                    System.out.println("Saliendo del navegador web!");
                    break outterLoop;
                }
                case "adelante" -> {
                    if (!stackBackup.isEmpty()) stack.push(stackBackup.pop());
                }
                case "atrás" -> {
                    if (!stack.isEmpty()) stackBackup.push(stack.pop());
                }
                default -> {
                    String formattedURL = formatURL(action);
                    String lastUrl = stack.isEmpty() ? null : stack.getLast();
                    if (formattedURL != null && !formattedURL.equals(lastUrl)) stack.push(formattedURL);
                    stackBackup = new Stack<>();
                }
            }
            if (!stack.isEmpty()) System.out.printf("Has navegado a la web: %s%n", stack.getLast());
            else System.out.println("Página de inicio!");
        }
    }

    private static String formatURL(String input) {
        Matcher matcher = DOMAIN_PATTERN.matcher(input);
        StringBuilder result = new StringBuilder();

        if (matcher.find()) {
            // Captura el dominio completo sin el protocolo, 'www.' y el path
            String domain = matcher.group(1);
            String path = matcher.group(2);

            // Verifica si el protocolo está presente, si no, añádelo
            if (!input.startsWith("http://") && !input.startsWith("https://")) result.append("http://");

            // Verifica si 'www.' está presente, si no, añádelo
            if (!"www.".contains(input)) result.append("www.");

            // Añade el dominio capturado
            result.append(domain);
            if (path != null) result.append(path);
            return result.toString();
        } else {
            System.out.printf("Formato del URL inválido: '%s'%n", input);
            return null;
        }
    }

    public static void printer() {
        Queue<String> cola = new LinkedList<>();

        outterLoop:
        while (true) {
            Scanner scanner = new Scanner(System.in);
            System.out.print("""
                    -----------------------------------------------------------
                    Bienvenido a la impresora, ingresar una las siguientes opciones:
                    1. Añadir un documento, escribir el nombre del documento.
                    2. "imprimir" - para imprimir el documento en cola.
                    3. "salir" - para cerrar la impresora.
                    -----------------------------------------------------------
                    """);
            System.out.print("Ingresar su opción: ");
            String action = scanner.nextLine();

            switch (action) {
                case "imprimir" -> {
                    if (!cola.isEmpty())
                        System.out.printf("Imprimiendo documento: %s%n", cola.poll());
                    else System.out.println("No hay documentos para imprimir!");
                }
                case "salir" -> {
                    break outterLoop;
                }
                default -> cola.offer(action);
            }
            System.out.println(cola);
        }
    }


    public static void main(String[] args) {
        //stack
        pila.push(1);
        pila.push(2);
        pila.push(3);
        System.out.println("La pila nueva es: " + pila);
        System.out.printf("Se elimina el elemento %d de la pila!%n", pila.pop());
        System.out.println("La pila actualizada es: " + pila);
        //queue
        cola.offer(10);
        cola.offer(20);
        cola.offer(30);
        System.out.println("La cola nueva es: " + cola);
        System.out.printf("Se elimina el elemento %d de la cola!%n", cola.poll());
        System.out.println("La pila actualizada es: " + cola);

        /*
         * DIFICULTAD EXTRA
         */
        webNavigator();
        printer();


    }
}
