// Solución del reto #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO

// - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
// https://dev.java/    --->    Web oficial del lenguaje de programación Java

// - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
// Este es un comentario en 1 línea
/* Este es un
 * comentario en
 * varias líneas
 */
 /** Este comentario es para la herramienta de documentación JavaDoc */

 public class lautimorales{
    public static void main(String[] args){
        // - Crea una variable (y una constante si el lenguaje lo soporta).
        int edad;   // Una variable se crea solo con el tipo de dato ('int' en este caso) y el nombre de ('edad' en este caso)
        final int dni;  // Una constante se crea con la palabra reservada 'final'

        // - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
        byte enteroMuyPequenio = 110; // Valor mínimo -128 y valor máximo 127
        short enteroPequenio = 1100; // Valor mínimo -32.768 y valor máximo 32.767
        int entero = 11110000; // Valor mínimo -2.147.483.648 y valor máximo 2.147.483.647
        long enteroGrande = 111100000;  // Valor mínimo -9.223.372.036.854.775.808 y valor máximo 9.223.372.036.854.775.807
        char caracterSimple = 'A';    // Sirve para representar un caracter unicode
        float decimalMenorPrecision = 10.3232F;    // Se utiliza para representar números con decimales con menor precisión (32 bits)
        double decimalMayorPrecision = 10.64;   // Se utiliza para representar números con decimales con mayor precisión (64 bits)
        boolean booleano = true;   //Representa expresiones lógicas (verdadero o falso)

        // - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
        // Opción 1
        String saludo = "¡Hola, Java!";
        System.out.println(saludo);
        // Opción 2
        System.out.println("¡Hola, Java!");
    }
}