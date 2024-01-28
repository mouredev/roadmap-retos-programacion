public class vixxtory {
    public static void main(String[] args) {
        // https://www.java.com/es/

        // Comentario de una sola linea

        /* Comentario
            de
            multiples
            lineas
         */

        /** Comentarios de documentacion o JavaDocs
         * Estos comentarios no solo documentan el código fuente, sino el proyecto como tal.
         * Tambien indican los componentes del código fuente, tales como parámetros, tipos de retorno, entre otros.
         * Estos componentes se preceden por un @, por ejemplo en el metodo main:
         * @param args[] es un arreglo con los parámetros que reciba por consola.
         */

        // Las VARIABLES se almacenan en un espacio de memoria de la computadora y se utilizan para manejar y/o manipular información dentro de un sistema
        // Declaración de Variable constante: una vez asignado el valor inicial no se puede cambiar durante la ejecucion del programa
        final double IVA = 21.5;
        //Variable: Pueden cambiar su valor a los largo del tiempo.
        int edad = 29;

        // TIPOS DE DATOS PRIMITIVOS
        /**
         * Numericos Enteros
         */
        //byte: 8 bits de almacenamiento | valores en el rango [-128, 127]
        byte miByte = 5;
        //short: 2 bytes de almacenamiento | valores en el rango [-32.768, 32.767]
        short miShort = 12596;
        //int: 4 bytes de almacenamiento | valores en el rango  [-2 elevado 31 a 2 elevado 31-1]
        int miInt = 10;
        //long: 8 bytes de almacenamiento | valores en el rango  [-2 elevado a 63 a 2 elevado 63-1]
        long miLong = 1000000000;
        /**
         * Numericos de tipo punto flotante
         */
        //float: 4 bytes de almacenamiento | valores en el rango [1.4x10 elevado -45 a 3.4028235x10 elevado 38]
        float miFloat = 10.58f;
        //double: 8 bytes de almacenamiento | valores en el rango 4.9x10 elevado -324 a 1.7976931348623157x10 elevado 308.
        double miDouble = 10.58;
        /**
         * Booleanos y caracteres
         */
        //boolean: 1 byte de almacenamiento | valores porsibles [true/false]
        boolean miBoolean = false;
        //char: 2 bytes de almacenamiento | valores posibles [caracteres simples]
        char miChar = 'P';
        /**
         * Datos Estructurados
         */
        //String: cadena de caracteres
        String miString = "Hola Mundo";

        System.out.println("¡Hola, Java!");

    }
}
