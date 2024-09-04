//Reto #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO;


public class Ainoaran {

    public static void main(String[] args) {

        //URL Sitio oficial JAVA: https://docs.oracle.com/javase/8/docs/api/

        /*Comentarios:
        - Los comentarios de una sola línea se realizan utilizando "//"
        - Los comentarios en varias líneas se inicializan con "/*" y se finaliza con '* /'
         */

        //VARIABLES:

        String variable = "Es una variable";
        final String constante = "Es una constante";

        //DATOS PRIMITIVOS:

        // Byte: Ocupa 8 bits (1 byte). Valores de -128 a 127 (inclusive).
        byte age = 25;

        // Short: Ocupa 16 bits (2 bytes). Valores de -32,768 a 32,767 (inclusive).
        short year = 2024;

        // int: Numero entero. Ocupa 32 bits (4 bytes). Valores de -2,147,483,648 a 2,147,483,647 (inclusive).
        int population = 8200000 ;

        // long: Número entero largo. Ocupa 64 bits (8 bytes). Valores de -9,223,372,036,854,775,808 a 9,223,372,036,854,775,807 (inclusive).
        long distance= 1000000000L;

        // float: Número de punto flotante de precisión simple. Ocupa 32 bits (4 bytes).
        float height = 1.75f;

        // double: Número de punto flotante de doble precisión. Ocupa 64 bits (8 bytes).
        double decimal = 6371.0;

        // char: Un solo carácter Unicode. Ocupa 16 bits (2 bytes).
        char character = 'A';

        // boolean: Valor booleano, true o false. Ocupa 1 bit.
        boolean isAdult = true;

        // Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

        System.out.println("¡Hola, Java!");
    }
}
