/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */

 // 1.
 // Esta es la documentación oficial de Java https://dev.java/
 // Página web oficial de Java https://www.java.com

 public class Alextc35 {
    public static void main (String[] args){
        // 2.
        // Esto es un comentario de una línea.

        /* 
        * Esto es un comentario
        * de varias líneas.
        */

        // 3.
        // Variable;
        String cadenaTexto = "Esto es una cadena de texto";

        // Constante;
        final int IVA = 21; // Esta variable es una constante.

        // 4.
        // Datos primitivos.

        // Valores literales;
        // Valor booleano VERDADERO:
        boolean verdadero = true;

        // Valor booleano FALSO:
        boolean falso = false;

        // Letra A:
        char letraMayuscula = 'A';

        // Número 100:
        byte by = 100;

        // Número 1000:
        short sh = 1000;

        // Número 1000000:
        int in = 1000000;

        // Valor 26 en decimal
        int decVal = 26;

        // Valor 26 en hexadecimal
        int hexVal = 0x1a;

        // Valor 26 en binario
        int binVal = 0b11010;

        // Números enteros;
        // Comprendido entre [-128 , 127]:
        byte b = 35;
        
        // Comprendido entre [-32.768 , 32.767]:
        short s = 3500;
        
        // Comprendido entre [-2^31 , (2^31)-1]:
        int i = 35000;
        
        // Comprendido entre [-2^63 , (2^63)-1]:
        long l = 3_000_000_000L;

        // Números reales:
        // Precisión simple;
        float f = 0.25f;

        // Precisión doble;
        double PI = Math.PI;

        // 5.
        System.out.println("¡Hola, Java!");
    }
 }
