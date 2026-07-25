/**
 * Solución del ejercicio #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
 * @author JOSE HAMMER
 */
public class josepilco7501{
    /**
     *
     * @param args
     */
    public static void main(String[] args) {

        //https://www.java.com/es/

        //Comentario de una linea

        /*
        Comentarios de
        varias lineas
         */

        /**
         * Comentario JavaDoc para documentacion de codigo fuente
         */

        /**
         * Creacion e inicializacion de una variable y un numero
         * @numeroA variable no iniciliazada
         * @numeroB constatnte inicializada
         */
        int numeroA; //Creacion de una variable de tipo entero llamada numeroA
        final double numeroB = 2.5; //Creacion e inicializacion de una constante llamada numeroB

        /**
         * - Crea variables representando todos los tipos de datos primitivos
         * del lenguaje (cadenas de texto, enteros, booleanos...).
         */

        /*
            | Tipo      | Tamaño  | Valor por defecto | Rango                                    | Descripción breve |
            | --------- | ------- | ----------------- | ---------------------------------------- | ----------------- |
            | `byte`    | 8 bits  | `0`               | -128 a 127                               | Entero pequeño    |
            | `short`   | 16 bits | `0`               | -32,768 a 32,767                         | Entero corto      |
            | `int`     | 32 bits | `0`               | -2³¹ a 2³¹-1                             | Entero estándar   |
            | `long`    | 64 bits | `0L`              | -2⁶³ a 2⁶³-1                             | Entero largo      |
            | `float`   | 32 bits | `0.0f`            | ±1.4e-45 a ±3.4e+38                      | Decimal simple    |
            | `double`  | 64 bits | `0.0d`            | ±4.9e-324 a ±1.7e+308                    | Decimal doble     |
            | `char`    | 16 bits | `'\u0000'`        | '\u0000' a '\uffff' (caracteres Unicode) | Carácter unicode  |
            | `boolean` | 1 bit   | `false`           | `true` o `false`                         | Lógico            |

         */

        byte edad = 25;
        short año = 2025;
        int poblacion = 1000000;
        long distancia = 9223372036854775807L;

        float temperatura = 36.6f;
        double pi = 3.14159265359;

        char inicial = 'J';
        boolean esJavaGenial = true;

        /**
         * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
         */

        System.out.println("¡Hola, java!");

    }
}