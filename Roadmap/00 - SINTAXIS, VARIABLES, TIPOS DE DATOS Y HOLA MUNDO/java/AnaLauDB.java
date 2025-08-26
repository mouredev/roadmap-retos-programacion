// URL oficial de Java: https://www.java.com

/*
  Ejemplo de comentarios en Java:
  - Una sola línea: usando //
  - Varias líneas: usando /* ... *​/
  - Comentarios de documentación: usando /** ... *​/
*/

/**
 * Clase de ejemplo para el reto #00
 */
public class AnaLauDB {
    public static void main(String[] args) {
        // Constante para el valor de PI
        final double PI = 3.1416;

        // Variables con diferentes tipos de datos primitivos
        String texto = "Hola, mundo";
        int numeroEntero = 42;
        double numeroDecimal = 2.718;
        boolean valorBooleano = true;
        char caracter = 'A';
        byte numeroByte = 100;
        short numeroCorto = 32000;
        long numeroLargo = 123456789L;
        float numeroFlotante = 3.14f;

        // Imprimir por terminal el texto solicitado
        System.out.println("¡Hola, Java!");

        // Imprimir variables para verificar
        System.out.println("Texto: " + texto);
        System.out.println("Entero: " + numeroEntero);
        System.out.println("Decimal: " + numeroDecimal);
        System.out.println("Booleano: " + valorBooleano);
        System.out.println("Carácter: " + caracter);
        System.out.println("Byte: " + numeroByte);
        System.out.println("Short: " + numeroCorto);
        System.out.println("Long: " + numeroLargo);
        System.out.println("Float: " + numeroFlotante);
        System.out.println("Constante PI: " + PI);
    }
}
