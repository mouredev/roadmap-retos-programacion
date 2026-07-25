/**
 * Clase Zugarramurdi donde se implementara el primer ejercicio del roadmap #00-SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
 * @author Zugarramurdi
 * @version 1.0
 * @date 05/04/2025
 */
// https://www.java.com/es/ - Web de Java
// https://docs.oracle.com/en/java/javase/24/ - Documentación de Java

public class Zugarramurdi {

    //Declaracion de una constante
    public static final String TEXTO_CONSTANTE = "Soy una constante"; // Se declaran en mayusculas y con guiones bajos y a nivel de clase

    public static void main(String[] args) {
        // Esto es un comentario de una línea

        /*
         * Esto es un comentario en bloque
         */

        /**
         * Esto es un comentario JavaDoc para generar documentacion
         */

        //Declaracion de variables
        // Sintaxis: tipo nombreVariable = valor;
        String texto = "Soy una variable de tipo String"; // Cadena de texto - valor entre comillas dobles
        boolean booleano = true; // Almacena valores true o false
        char caracter = 'A'; // Almacena un solo caracter - valor entre comillas simples
        byte numeroByte = 100; // Almacena un entero entre -128 y 127
        short numeroShort = 1000; // Almacena un entero entre -32,768 y 32,767
        int numeroInt = 10000; // Almacena un entero entre -2,147,483,648 y 2,147,483,647
        long numeroLong = 10000000; // Almacena un entero entre -9,223,372,036,854,775,808 y 9,223,372,036,854,775,807
        float numeroFloat = 100.0f; // Almacena un decimal de 4 bytes, hasta 7 decimales - valor con f al final
        double numeroDouble = 100.0d; // Almacena un decimal de 8 bytes, hasta 15 decimales

        //Impresion por terminal
        System.out.println("¡Hola, Java!");

    }
}
