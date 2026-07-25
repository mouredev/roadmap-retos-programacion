/**
 * Clase principal que incluye ejemplos de funciones en Java, variables globales y locales,
 * recursividad, encapsulación y la resolución de un ejercicio extra.
 */
public class AFOXJONES {

    // Variable global (accesible en toda la clase)
    private static final String variableGlobal = "SOY GLOBAL";

    /**
     * Método principal de ejecución.
     */
    public static void main(String[] args) {
        // Variable local (solo accesible dentro de este método)
        String variableLocal = "SOY LOCAL";

        System.out.println("Variable local: " + variableLocal);

        System.out.println("Variable global: " + variableGlobal);

        // Ejemplo de funciones nativas de Java
        System.out.println("\nEjemplo de funciones ya creadas por el lenguaje:");
        String exampleString = "pepe";
        System.out.println("compareToIgnoreCase: " + exampleString.compareToIgnoreCase("PEPE"));
        System.out.println("concat: " + exampleString.concat(" Gutierrez"));

        // Llamadas a los métodos de la clase
        sinRetorno();
        sinRetornoConParametro("¡Hola, mundo!");
        sinRetornoConParametros("Texto", 42);

        String retorno = conRetorno();
        System.out.println("\nResultado de conRetorno: " + retorno);

        int resultadoSuma = conRetornoConParametro(10);
        System.out.println("Resultado de conRetornoConParametro: " + resultadoSuma);

        System.out.println("\nLlamada recursiva:");
        funcionRecursiva(0);

        // Ejercicio extra
        System.out.println("\nEjercicio extra:");
        int count = extra("Fizz", "Buzz");
        System.out.println("Números impresos como números: " + count);
    }

    /**
     * Método sin retorno ni parámetros.
     */
    public static void sinRetorno() {
        System.out.println("Función sin retorno ni parámetros");
    }

    /**
     * Método público sin retorno, con un parámetro.
     *
     * @param param Parámetro de entrada de tipo String.
     */
    public static void sinRetornoConParametro(String param) {
        System.out.println("Función sin retorno con el parámetro: " + param);
    }

    /**
     * Método público sin retorno, con múltiples parámetros.
     *
     * @param param1 Primer parámetro de tipo String.
     * @param param2 Segundo parámetro de tipo int.
     */
    public static void sinRetornoConParametros(String param1, int param2) {
        System.out.println("Función sin retorno con los parámetros: " + param1 + " y " + param2);
    }

    /**
     * Método público con retorno y sin parámetros.
     *
     * @return Cadena de texto que indica el resultado de la función.
     */
    public static String conRetorno() {
        return "Función con retorno sin parámetros";
    }

    /**
     * Método público con retorno y un parámetro.
     *
     * @param param Número entero de entrada.
     * @return Número incrementado en 3.
     */
    public static int conRetornoConParametro(int param) {
        return param + 3;
    }

    /**
     * Ejemplo de método privado: solo se usa dentro de esta clase.
     * Representa una función recursiva.
     *
     * @param count Contador que determina la profundidad de la recursión.
     */
    private static void funcionRecursiva(int count) {
        System.out.println("Antes de la recursión: " + count);
        if (count < 5) {
            funcionRecursiva(count + 1);
        }
        System.out.println("Después de la recursión: " + count);
    }

    /**
     * Ejercicio extra: imprime números y textos según condiciones.
     *
     * @param text1 Texto a mostrar si el número es múltiplo de 3.
     * @param text2 Texto a mostrar si el número es múltiplo de 5.
     * @return Cantidad de números impresos como números (ni múltiplos de 3 ni de 5).
     */
    public static int extra(String text1, String text2) {
        int count = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(text1 + text2);
            } else if (i % 3 == 0) {
                System.out.println(text1);
            } else if (i % 5 == 0) {
                System.out.println(text2);
            } else {
                System.out.println(i);
                count++;
            }
        }
        return count;
    }
}
