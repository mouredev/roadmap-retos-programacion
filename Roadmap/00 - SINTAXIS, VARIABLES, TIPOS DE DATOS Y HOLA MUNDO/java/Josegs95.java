public class Josegs95 {
    // Sitio web oficial Java: https://java.com/es

    // Doble barra para un comentario en una línea

    /* Barra asterisco para empezar un comentario en varias líneas
       ... Aquí vendría la segunda línea del comentario ...
       Para finalizar el comentario, hay que usar asterisco barra.
    */


    public static void main(String[] args) {

        //Creo una variable con un valor
        int miVariable = 8;
        //Cambio el valor de la variable
        miVariable = 12;

        //Creo una constante
        final double NUM_PI = 3.14;
        //No se puede cambiar el valor de una variable final
        //El código no compilaría
        //NUM_PI = 3.1415;

        //Tipos primitivos
        byte miByte= 8;
        short miShort = 16;
        int miInt = 32;
        long miLong = 64;
        float miFloat = 32.0f; //Hay que especificar que es un float poniéndole la "f" al final
        double miDouble = 64.0;

        boolean miBoolean = true; //Solo admite dos valores, true o false.

        char miChar = 'a'; //Hay que usar comillas simples, las comillas dobles son para cadenas

        //El tipo String, que sirve para representar cadenas, no es un tipo primitivo en java
        //Aún así, por ser un tipo especial (no hay que usar new para crear un objeto String)
        //Pongo un ejemplo de como sería
        String miString = "Cadena";

        //Imprimir por consola usando el método println()
        System.out.println ("¡Hola, java!");
    }
}
