public class IGuerreroV {
    //Reto de programacion por MoureDev

    /*

        EJERCICIO:
        - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
        - Representa las diferentes sintaxis que existen para crear comentarios en el lenguaje (en una línea, varias...).
        - Crea una variable (y una constante si el lenguaje lo soporta).
        - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
        - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!
    */

    // URL SITIO WEB OFICIAL: https://www.java.com/es/

    public static void main(String[] args) {

        // Variable
        var miVariable = "variable";

        // Constante
        final String miConstante = "Constante";

        // Datos primitivos
        byte datoPequeño = 8; // Almaneca valores pequeños
        short datoMasGrandeQueByte = 120; // Almcaena mas datos que byte
        int miEntero = 2000; // Es el mas comun
        long miEnteroGrande = 200000; // Es para almacenar enteros mas grandes
        double miFlotante = 120.5d; // Se usa para almacenar valores flotantes, mas precision
        float miDecimal = 120.6f; // Se usa para almacenar valores flotantes, menos precision
        char miChat = 'a'; // Se usa para almacenar caracteres (unicode) con comillas simples
        boolean miBoolean = true; // Se usa para almacenar valores de verdad (true / false)

        System.out.println("¡Hola, Java ");
    }
}
