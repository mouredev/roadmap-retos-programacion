import java.util.Scanner;

/**
 * - Crea ejemplos de funciones básicas que representen las diferentes
 * posibilidades del lenguaje:
 * Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 * (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne
 * un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 * - Si el número es múltiplo de 3, muestra la cadena de texto del primer
 * parámetro.
 * - Si el número es múltiplo de 5, muestra la cadena de texto del segundo
 * parámetro.
 * - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto
 * concatenadas.
 * - La función retorna el número de veces que se ha impreso el número en lugar
 * de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los
 * casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código
 * se entienda.
 * 
 * #### SINTAXIS DE UNA FUNCION ####
 * modificador tipoDatoDevuelto nombreDeFuncion (lista de parámetros de entrada)
 * {
 * return datoDevuelto;
 * }
 *
 * @version v1
 * 
 * @since 14/01/2024
 * 
 * @author Blas Barragán
 * 
 */
public class BlasBarragan {

    // Variables globales, pueden ser usada por todas las funciones y bloques.
    // Siempre iran precedidas del mosificador static. Y hay que evitar usarlas.
    static int mayor;
    static int c = 6;
    static int d = 3;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Hola, como te llamas?: ");
        String nombre = sc.nextLine();
        System.out.println("Y dime, cuantos años tienes?: ");
        int edad = sc.nextInt(); // Variale local, se define dentro de la funcion y solo se puede usar dentro de
                                 // la misma.
        funcionSinRetornoConParametros(nombre, edad);
        System.out.println(
                "Vamos a ver que numero es mayor, tu me das un numero \"a\" y yo pienso en otro \"b\" y vemos cual de los dos es mayor");
        System.out.println("Dime un numero: ");
        int a = sc.nextInt();
        System.out.println("El numero " + numeroMayor(a, 5) + " es el mayor.");
        System.out.println("Llamamos a la funcion mayorReturn con las variables globales c y d");
        System.out.println(mayorReturn(c, d));
        System.out.println(retornoSinParametros());
        System.out.println(dificultadExtra("cara", "cola"));
        sc.close();
    }

    // Funcion sin retorno ni parametros
    // - retorno: void. ("subprograma" (No devuelve resultado despues de ejecutar su
    // bloque y no necesita return))
    // - parametros(): vacio. (No recibe datos de entrada)
    public static void funcionSinRetornoNiParametros() {
        System.out.println("Esto es una funcion sin retorno ni parametros que imprime un mensaje");
    }

    // Funcion sin retorno con parametros
    // - retorno: void. ("subprograma" (No devuelve resultado despues de ejecutar su
    // bloque y no necesita return))
    // - parametros(): String nombre, int edad. (Los definimos en la funcion main
    // preguntando al usuario por consola)
    public static void funcionSinRetornoConParametros(String nombre, int edad) {
        System.out.println("Hola " + nombre + ", de verdad tienes " + edad + " años?");
    }

    // Funcion con retorno y parametros
    // - retorno: int mayor. (Utilizamos return para que nos devuelva el resultado
    // de las operaciones realizadas en la funcion)
    // - parametros: int a, int b. (En main, preguntamos al usuario por dos numeros
    // con los que inicializamos la funcion)
    public static int numeroMayor(int a, int b) {
        if (a >= b)
            mayor = a;
        else
            mayor = b;

        return mayor;
    }

    // La palabra reservada return, se puede usar en distintas partes de la funcion
    // segun necesitemos,
    // pero teniendo en cuenta que cuando se ejecuta el return se termina la
    // funcion.
    // Por ejemplo, la misma funcion que antes pero usando los return a nuestro
    // antojo.
    public static int mayorReturn(int c, int d) {
        if (c >= d)
            return c; // Si a es mayor que b, devolvemos a

        return d; // Si no, devuelve b
    }

    // Funcion con retorno sin parametros
    // - retorno: String (Utilizamos return para que nos devuelva el texto
    // introducido en la funcion)
    // - parametros(): vacio. (No recibe datos de entrada)
    public static String retornoSinParametros() {
        return "Soy una funcion con retorno sin parametros";
    }

    /**
     * DIFICULTAD EXTRA (opcional):
     * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne
     * un número.
     * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
     * - Si el número es múltiplo de 3, muestra la cadena de texto del primer
     * parámetro.
     * - Si el número es múltiplo de 5, muestra la cadena de texto del segundo
     * parámetro.
     * - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto
     * concatenadas.
     * - La función retorna el número de veces que se ha impreso el número en lugar
     * de los textos.
     */

    public static int dificultadExtra(String cadena1, String cadena2) {
        int i;
        int a = 0;
        for (i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                // System.out.println(cadena1+cadena2);
                a = a + 1;
            } else if (i % 5 == 0) {
                // System.out.println(cadena2);
                a = a + 1;
            } else if (i % 3 == 0) {
                // System.out.println(cadena1);
                a = a + 1;
            } else {
                // System.out.println("");}
            }
        }
        return a;
    }

}
