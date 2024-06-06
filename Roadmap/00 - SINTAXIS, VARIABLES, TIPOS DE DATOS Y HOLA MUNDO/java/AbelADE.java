/**
 * Solución del reto #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO;
 * @author AbelADE
 */
public class AbelADE {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //Comentario con URL del sitio web oficial = https://docs.oracle.com/javase/8/docs/api/

        // Comentario de simple línea
        
        /*Comentario 
                de varias líneas*/
        
        /**
         * Comentario JavaDoc, para generar documentación oficial
         */
        
        // Crea una variable (y una constante si el lenguaje lo soporta).
        final String TEXTO = "Soy una constante";
        String textoVariable = "Soy una variable";
        
        
        //Crea variables representando todos los tipos de datos primitivos
        boolean datoLogico = true; // Almacena valores true o false
        char caracter = 'a'; // Caracteres unicode de 2 bytes
        byte numeroMuyPequeño = 100; // Entero entre -128 e 127
        short numeroPequeño = 25000; //  Entero entre -32768 y 32767
        int numero = 1000000; // Entero entre -2.147.483.648 y 2.147.483.647
        long numeroMasGrande = 2000000000L; // Entero entre -9.223.372.036.854.775.808 e 9.223.372.036.854.775.807
        float decimalPequeño = 15.6666F; // Decimal de 4 bytes
        double decimal = 15.269899; // Decimal de 8 bytes

        //Tipo de dato no primitivo (Objeto)
        String texto = "Soy un texto";
        
        //Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
        System.out.println("¡Hola, Java!");
    }

}
