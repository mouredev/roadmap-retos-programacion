public class Main {

    public static final String LENGUAJE = "Java";

    /**
     * En Java las funciones pueden retornar un valor, o no retornar nada.
     * Pueden recibir uno o más parámetros, o no recibir ninguno.
     * Pueden ser llamadas sin la necesidad de instanciar un objeto.
     * Pueden ser llamadas desde otras funciones.
     * Pueden ser sobrecargadas, es decir, tener el mismo nombre pero diferentes parámetros.
     * Pueden ser sobreescritas, es decir, tener el mismo nombre y parámetros pero diferentes implementaciones.
     * static indica que la función pertenece a la clase y no a un objeto, por lo tanto no es necesario instanciar un objeto para llamarla.
     */

    /**
     * En Java existen los modificadores de acceso, los cuales son:
     * default: Visible dentro del mismo paquete
     * public: Visible desde cualquier parte del proyecto
     * private: Visible solo dentro de la clase
     * protected: Visible dentro del mismo paquete y en las clases hijas (herencia)
     */

    public static void main(String[] args) {
        saludar();
        mensaje("ASJordi");
        mensajeCompleto("Jorge", "Garcia");

        String saludo = saludar2();
        System.out.println(saludo);
        String saludo2 = mensaje2("Pedro");
        System.out.println(saludo2);
        int resultado = suma(2, 3);
        System.out.println("2 + 3 = " + resultado);
        double resultado2 = suma(2.5, 3.5);
        System.out.println("2.5 + 3.5 = " + resultado2);

        System.out.println(new Main().toString());

        // Ejemplo de función propia de Java
        System.out.println("2 elevado al cuadrado es: " + Math.pow(2, 2));

        /**
         * Una variable local es una variable que es declarada dentro de un scope (bloque de código) y solo puede ser accedida dentro de ese scope.
         * Una variable global es una variable que es declarada fuera de un scope y puede ser accedida desde cualquier parte del proyecto.
         */

        // Variable local
        int a = 2;

        // Variable global
        System.out.println("PI es una variable global: " + Math.PI);
        System.out.println("LENGUAJE es una variable global: " + LENGUAJE);

        // RETO
        System.out.println("-------------------- RETO --------------------");
        int res = retornarNumero("Java", "Roadmap");
        System.out.println("El número de veces que se ha mostrado por consola el número es: " + res);
    }

    /**
     * Funciones sin retorno
     * Cuando una función no retorna un valor en Java se utiliza la palabra reservada void.
     */

    // Función que no retorna nada y no recibe parámetros
    public static void saludar() {
        System.out.println("Hola mundo!");
    }

    // Función que no retorna nada y recibe un parámetro
    public static void mensaje(String nombre) {
        System.out.println("Hola " + nombre + "!");
    }

    // Función que retorna un valor y recibe múltiples parámetros
    public static void mensajeCompleto(String nombre, String apellido) {
        System.out.println("Hola " + nombre + " " + apellido + "!");
    }

    /**
     * Funciones con retorno
     * Cuando una función retorna un valor en Java se utiliza el tipo de dato que retorna la función.
     * El tipo de dato de retorno puede ser un tipo de dato primitivo o un objeto.
     */

    // Función que retorna un valor y no recibe parámetros
    public static String saludar2() {
        return "Hola mundo!";
    }

    // Función que retorna un valor y recibe un parámetro
    public static String mensaje2(String nombre) {
        return "Hola " + nombre + "!";
    }

    // Función que retorna un valor y recibe múltiples parámetros
    public static int suma(int a, int b) {
        return a + b;
    }

    /**
     * Funciones sobrecargadas
     * Las funciones sobrecargadas son funciones que tienen el mismo nombre pero diferentes parámetros.
     * En el siguiente ejemplo tiene el mismo nombre pero el tipo de datos de los parámetros es diferente.
     */

    public static double suma(double a, double b) {
        return a + b;
    }

    /**
     * Funciones sobreescritas
     * Las funciones sobreescritas son funciones que tienen el mismo nombre y parámetros pero diferentes implementaciones.
     */

    @Override
    public String toString() {
        return "Hola mundo!, esto es una función sobreescrita";
    }

    /**
     * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
     * La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
     * - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
     * - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
     * - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
     * - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
     */

    public static int retornarNumero(String a, String b) {
        int count = 0;

        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) System.out.println(a + " " + b);
            else if (i % 3 == 0) System.out.println(a);
            else if (i % 5 == 0) System.out.println(b);
            else {
                System.out.println(i);
                count++;
            }
        }


        return count;
    }
}
