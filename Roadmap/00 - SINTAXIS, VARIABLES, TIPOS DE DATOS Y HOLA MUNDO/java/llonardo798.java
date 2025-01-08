public class llonardo798 {

    public static void main(String[] args) {
        
        // 1. Documentación oficial en https://www.java.com/
        
        // 2. Tipos de comentarios.
        
        // Para comentarios de una sola línea

        /* 
         * para comentarios de
         * varias líneas
         */
        
        /**
         * para comentarios de
         * varias lineas pero es
         * formato de documentación
         * (JavaDoc).
         */ 
        
        // 3. Vairables y Constantes.
        String nombre = "Leonardo Aedo Jimenez";
        final int numeros = 21;

        // 4. Tipos de datos primitivos.
        byte edad = 30;                             // 8 bits, rango de valores permitidos -128 hasta 127
        short anoNacimiento = 1990;                 // 16 bits, rango de valores permitidos -32768 hasta 32767
        int poblacionCiudad = 5000000;              // 32 bits, rango de valores permitidos -2147483648 hasta 2147483647
        long distanciaTierraSol = 149600000000L;    // 64 bits, rango de valores permitidos -9223372036854775808 hasta 9223372036854775807
        float precioProducto  = 19.99f;             // 32 bits, rango de valores permitidos 1.4e-045 hasta 3.4e+038
        double gravedadTierra = 9.80665;            // 64 bits, rango de valores permitidos -1.79769313486232e308 hasta 1.79769313486232e308
        char primeraLetra = 'L';                    // 16 bits, rango de valores permitidos '\u0000' hasta '\uffff' (Caracteres Unicode)

        // 5. Imprimir en consola.
        System.out.println("Hola, Java!");

    }
    
}