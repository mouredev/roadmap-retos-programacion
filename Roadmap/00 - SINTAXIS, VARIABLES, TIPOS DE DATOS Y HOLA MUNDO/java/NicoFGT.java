// URL: https://www.java.com/es/

/*
 * Esta sintaxis representa 
 * un comentario que es hecho en
 * varias lineas...
 */

//Esta sintaxis representa el comentario que es hecho en una sola linea 

public class NicoFGT {

    // VARIABLE asignada e inicilizada

    float precio = 1.16f;

    // CONSTANTE declarada e incilizada

    final int ProductoID = 692710;
    final String NOMBRE_PRDUCTO = "CAFE";

    // TIPOS DE DATOS PRIMITIVOS DEL LENGUAJE

    boolean Verdadero = true;
    boolean Falso = false;
    char Letra = 'N'; // introduce unicamente un solo caracter
    byte EnteroNgeativo = -45; // Enteros con signo
    short EnteroconSigno = -3444; // Entero con signo con mayor tamaño de caracteres
    int EnteroPostitivo = 1555567154; // Entero con mayor volumen de carcateres
    long PoblacionMundial = 8_000_000_000L; // Almacenar un número que excede la capacidad de un 'int'
    float PrecioProducto = 16.16f; // numeros decimales
    double pi = 3.141592653589793; // tambien almacena decimales

    // IMPRESION HOLA MUNDO
    public static void main(String[] args) {
        System.out.println("Hola, mundo Java");
    }

}
