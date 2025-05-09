package roadmap;

public class WelcomeToJava {

    // Este es un comentario de una sola linea

    /*
    *  Este es un comentario multilinea
    * [LINK DE LA PAGINA OFICIAL DE JAVA --- https://www.oracle.com/java/technologies/downloads/]
    * [LINK DE LA PAGINA DE LA DOCUMENTACION -- https://docs.oracle.com/en/java/javase/21/docs/api/index.html]
    *
    *
    */


    /*
    * La funcion main es la parte mas importante de un programa en java
    * ya que todo nuestro codigo debe estar dentro de esta funcion para poder ser ejecutado
    **/
    public static void main(String[] args) {

        /* TIPOS DE DATOS

        En java existen los siguientes tipos de datos
           1: Primitivos
           2: Object
        * */

        // 1: DATOS PRIMITIVOS

        // ENTEROS          Tamaño                              Rango min y maximo que soporta
        byte num; // soporta un tamaño de 8 bits            [-128 | 128]
        short num2; // soporta un tamaño de 16 bits         [-32768 | 32768]
        int num3; // soporta 32 bits                        [-9223372036854775808 | 9223372036854775808]
        long num4; // soporta 64 bits

        // FLOTANTES        Tamaño                              Rango min y maximo que soporta
        float num5; // soporta 32 bits                      [+- 3.40282347E+38]
        double num6; // soporta 64 bits                     [+- 1.79769313486231570E+308 ]

        // CARACTER        Tamaño                              Rango min y maximo que soporta
        char caracter; // soporta 16 bits                   [\u0000 | \uFFFF]

        // BOOLEANOS        Tamaño                              Rango min y maximo que soporta
        boolean booleano; // soporta 1 bit, este tipo de variable solo pueden tener dos valores, true o false




        // 2: DATOS OBJECT

        /*
        Este tipo es una cadena de caracteres mas sin embargo es importante mencionar
        que estamos haciendo una instancia de la clase String, por ende a diferencia de las variables
        primitivas, esta comienza con la primera letra mayuscula.
        * */
        String cadena;
        String cadena2 = new String(); // Basicamente es como si hicieramos esta llamada a la instancia, de forma simplificada

        System.out.println("¡Hola!, Java"); // Esta es la forma de imprimir un mensaje en consola.
    }
}
