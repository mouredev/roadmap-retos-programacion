/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
public class AngelSanchezT {
    public static int globalVariable = 5;

    public static void main(String[] args) {

        saludar();
        saludarPersona("AngelSanchezT");
        saludarPersona("Angel", "Sanchez");

        String saludo = getSaludo();
        saludarPersona(saludo);

        System.out.println("2 ** 2 es: " + elevarCuadrado(2));
        System.out.println("10 + 3 es: " + sumar(10, 3));
        System.out.println("1.5 + 2.5 es: " + sumar(1.5, 2.5));
        
        // Funciones del Lenguaje
        String username = "AngelSanchezT";
        
        System.out.println("Funciones de Java:");
        System.out.println("Longitud username:" + username.length());
        System.out.println("Usename minusculas:" + username.toLowerCase());
        System.out.println("Usename mayusculas:" + username.toUpperCase());

        // Variable local
        String pais = "Colombia";
        System.out.println("Variable Local: " + pais);

        System.out.println("Variable global: " + globalVariable);

        // EXTRA
        System.out.println("EXTRA:");
        int resultado = retornarNumero("Java", "Python");
        System.out.println("El número de veces que aparece el número es: " + resultado);

    }

    // Función que no retorna y no recibe parametros
    public static void saludar() {
        System.out.println("Hola Java ❤️!");
    }

    // Función que no retorna y recibe un parametro
    public static void saludarPersona(String nombre) {
        System.out.println("Hola, " + nombre + "!");
    }

    // Función que no retorna y recibe mas de un parametro
    public static void saludarPersona(String nombre, String apellido) {
        System.out.println("Hola, " + nombre + " " + apellido +"!");
    }

    // Función que no recibe parametros pero retorna un valor
    public static String getSaludo(){
        return "Hola Java!";
    }

    // Función que retorna un valor y recibe un parametro
    public static int elevarCuadrado(int numero) {
        return numero * numero;
    }

    // Función que retorna un valor y recibe múltiples parámetros
    public static int sumar(int a, int b) {
        return a + b;
    }

    // SobreCarga de Funciones.
    // La función sumar puede tener varias funciones con el mismo nombre pero con
    // parametros diferentes en numero y el tipos de datos. Y diferente tipo de retorno.
    public static double sumar(double a, double b) {
        return a + b;
    }

    public static int retornarNumero(String cadena1, String cadena2) {
        int count = 0;

        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) System.out.println(cadena1 + " " + cadena2);
            else if (i % 3 == 0) System.out.println(cadena1);
            else if (i % 5 == 0) System.out.println(cadena2);
            else {
                System.out.println(i);
                count++;
            }
        }


        return count;
    }



}