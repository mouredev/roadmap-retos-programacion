/**
 * 00 - SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
 * @author martinbohorquez
 */
public class martinbohorquez {

    // https://www.oracle.com/java/

    // Esto es un comentario en una sola línea.

    /*
     * Esto es un comentario
     * usando varías líneas
     * para describir el código.
     */

    public static void main(String[] args){
        // Variable
        String saludo = "¡Hola, ";

        // Constante
        final String PROGRAMMING_LANGUAGE = "Java!";

        // Datos Primitivos
        char letter = 'M';
        printMessage("letter", letter);

        byte age = 29;
        printMessage("age", age);

        short year = 2024;
        printMessage("year", year);
        int quantity = 1234567890;
        printMessage("quantity", quantity);
        long large = 1234567890123456789L;
        printMessage("large", large);

        float pi = 3.1415926535f;
        printMessage("pi", pi);
        double e = 2.718281828459045235360d;
        printMessage("e", e);

        boolean esVerdadero = true;
        printMessage("esVerdadero", esVerdadero);
        boolean esFalso = false;
        printMessage("esFalso", esFalso);

        System.out.println(saludo + PROGRAMMING_LANGUAGE);

    }

    private static void printMessage(String string, Object object) {
        System.out.println("El valor de '" + string + "' es: " + object + ", y su tipo es: "
                + object.getClass().getSimpleName().toLowerCase());
    }
}
