
/*
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una lí­nea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
*/

// Para tener una línea comentada en java se usa el simbolo "//"

/* 
Para varias líneas se usa la combinacion barra "/" y Multiplicar "*" para abrir el comentario
y la combinación Multiplicar "*" barra "/" para cerrar el comentario. Las lí­neas intermedias
quedan comentadas
*/

/*
La página de referencia de java es https://www.java.com
La página para España es https://www.java.com/es/
*/

public class Rantamhack {
    public static void main (String[] args){


        // Constante de programa
        final int MY_CONSTANTE = 100;

        // Variables

        // Entera (int)
        int my_integer_variable = 16;

        // Decimal (float)
        float my_pi_variable = 3.14f;

        // Caracter(char)
        char my_char_variable = 'a';

        // Texto (string)
        String my_text_variable = "mi variable";

        // Booleana (bool)
        boolean my_bool_variable = true;

        // Mensaje de saludo al lenguaje
        String lenguage = "Java";

        // otras variable con menos uso
        // --byte-- para cantidades pequeÃ±as (de -128 a 127)
        byte my_byte_variable = 15;
        
        // --short-- para cantidades medianas ( de -32678 a 32677)
        short my_short_variable = 15000;

        // --long-- para numeros de -9223372036854775808 a 9223372036854775807
        long  my_long_variable = 92233720368547756L;

        // --double-- para decimales con gran numero de cifras donde no llegue float
        double my_double_variable = 0.111111111111111111111;


        System.out.println(MY_CONSTANTE);
        System.out.println(my_integer_variable);
        System.out.println(my_pi_variable);
        System.out.println(my_char_variable);
        System.out.println(my_text_variable);
        System.out.println(my_bool_variable);
        System.out.println("¡¡Hola, "+lenguage +"!!");
        System.out.println(my_byte_variable);
        System.out.println(my_short_variable);
        System.out.println(my_long_variable);
        System.out.println(my_double_variable);
        



    }
}
