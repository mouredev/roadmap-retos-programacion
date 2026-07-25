public class GuillermoMunoz {

    /*
     * EJERCICIO #00: Guillermo-Munoz
     * - Sintaxis, variables, tipos de datos y Hola mundo
     * - Lenguaje: Java
     */

    public static void main(String[] args) {
        
        // 1. URL oficial del lenguaje
        // https://www.oracle.com/java/
        
        // 2. Diferentes tipos de comentarios
        
        // Comentario de una línea
        
        /* Comentario
           de varias
           líneas */
        
        /**
         * Comentario de documentación JavaDoc
         * Útil para generar documentación automática
         */
        
        // 3. Variables y constantes
        final int CONSTANTE = 100;  // Las constantes se nombran en MAYÚSCULAS
        int variable = 12;
        
        // 4. Tipos de datos primitivos
        byte byteVar = 127;
        short shortVar = 32767;
        char charVar = 'a';
        long longVar = 9223372036854775807L;
        float floatVar = 2.2545445f;
        double doubleVar = 45.121212454;
        boolean booleanVar = true;
        
        // 5. Tipo referencia (no primitivo pero muy usado)
        String stringVar = "Java";
        
        // 6. Imprimir por terminal
        System.out.println("¡Hola, " + stringVar + "!");
    }
}
