/**
 * #02 FUNCIONES Y ALCANCE
 * @author clarancedev
 * @version %I%, %G%
 */

public class Clarancedev {

    // VARIABLE GLOBAL (accesible desde cualquier parte de la clase)
    static final String VARIABLE_GLOBAL = "Soy una variable global de la clase Clarancedev";

    // TIPOS DE FUNCIONES (TAMBIÉN DENOMINADOS MÉTODOS)

    // SIN PARÁMETROS Y SIN RETORNO
    /* No se especifica el tipo de dato que retorna la función,
     * en su lugar indicamos "void". Su contenido tampoco incluye
     * un "return", aunque puede incluir más de una función y
     * llamar a otras funciones de la misma clase */
        public static void variableLocal () {

            // VARIABLE LOCAL (accesible solo dentro de la función donde se declara)
            String variableLocal = "Soy una variable local de la función main()";

            System.out.println(variableLocal);
        }

        public static void cuentaAtrasDespegue () {
            for (int i = 10; i > 0; i--) {
                System.out.println(i);
            }
            System.out.println("¡Despegamos!");
        }

    // CON PARÁMETROS Y SIN RETORNO
    /* No debemos especificar el tipo de dato que retorna la función,
     * pero debemos especificar el tipo de dato de los parámetros
     * que recibe la función. Su contenido no incluye un "return" */
    public static void funcionConParSinRet (String nombre) {
        System.out.println("Hola, " + nombre + "!");
    }

    public static void funcionConParSinRet2 (int edadActual) {
        int nuevaEdad = edadActual + 5;
        System.out.println("Si ahora tienes " + edadActual + " años, dentro de 5 años tendrás " + nuevaEdad + ".");
    }

    // SIN PARÁMETROS Y CON RETORNO
    /* Debemos especificar el tipo de dato que retorna la función,
     * y su contenido debe incluir un "return" de dicho tipo de dato */
    public static String funcionSinParConRet () {
        return "Soy una función sin parámetros y con retorno";
    }

    public static int sumarUnoYDos() {
        return 1 + 2;
    }

    // CON PARÁMETROS Y CON RETORNO
    /* Debemos especificar el tipo de dato que retorna la función,
     * y su contenido debe incluir un "return" de dicho tipo de dato.
     * Ojo, dos métodos pueden tener el mismo nombre, siempre y cuando
     * los parámetros solicitados sean distintos, sea en cantidad o tipo */

    public static int multiplicarValores(int num1, int num2) {
        return num1 * num2;
    }

    public static double multiplicarValores(double num1, double num2) {
        return num1 * num2;
    }

    public static int multiplicarValores(int num1, int num2, int num3) {
        return num1 * num2 * num3;
    }

    // DIFICULTAD EXTRA

    public static int fizzBuzzInspired(String texto1, String texto2) {
        int counter = 0;

        System.out.println("Imprimiendo los números del 1 al 100, salvo los que son múltiples de 3 o de 5, para los cuales aparecerán las palabra Fizz y/o Buzz:");

        for (int i = 1; i <101; i++) {
            boolean esMultiploDe3 = i % 3 == 0;
            boolean esMultiploDe5 = i % 5 == 0;

            if (esMultiploDe3 && esMultiploDe5) {
                System.out.println(texto1 + texto2);
            } else if (esMultiploDe3) {
                System.out.println(texto1);
            } else if (esMultiploDe5) {
                System.out.println(texto2);
            } else {
                System.out.println(i);
                counter++;
            }
        }
        return counter;
    }

    public static void main(String[] args) {
        /* LA FUNCIÓN MAIN() ES UNA FUNCIÓN ESPECIAL,
         * ES LA PRINCIPAL DONDE SE EJECUTA EL PROGRAMA */

        // Imprimiendo variables LOCAL y GLOBAL
        variableLocal();
        System.out.println(VARIABLE_GLOBAL);

        // Imprimiendo la función SIN parámetros y SIN retorno cuentaAtrasDespegue()
        cuentaAtrasDespegue();

        // Imprimiendo las funciones CON parámetros y SIN retorno
        funcionConParSinRet("Java");
        funcionConParSinRet2(25);

        // Imprimiendo las funciones SIN parámetros y CON retorno
        System.out.println(funcionSinParConRet());
        System.out.println("La suma de 1 y 2 es igual a " + sumarUnoYDos());

        // Imprimiendo las funciones CON parámetros y CON retorno
        int int1 = 2;
        int int2 = 3;
        int int3 = 4;
        double double1 = 2.5;
        double double2 = 3.5;

        System.out.println(int1 + " * " + int2 + " = " + multiplicarValores(int1, int2));
        System.out.println(double1 + " * " + double2 + " = " + multiplicarValores(double1, double2));
        System.out.println(int1 + " * " + int2 + " * " + int3 + " = " + multiplicarValores(int1, int2, int3));

        // FUNCIONES DE JAVA CLASS LIBRARY
        /* Java Class Library es una biblioteca de clases que contiene
         * funciones predefinidas que podemos usar en nuestros programas.
         * Por ejemplo, la clase Math contiene funciones matemáticas
         * como Math.abs(), Math.sqrt(), Math.pow(), etc. */

        System.out.println("La raíz cuadrada de 9 es " + Math.sqrt(9));

        // Llamando a la función de dificultad extra

        int counter = fizzBuzzInspired("Fizz", "Buzz");
        System.out.println("El número de veces que no se imprimió Fizz o Buzz es: " + counter);
    }
}
