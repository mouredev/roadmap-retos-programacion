public class adrs1166ma {
    public static void main(String[] args) {
        // URL del sitio oficial Java: https://www.java.com/

        // - - - Tipos de comentario - - -

        // Una linea 1

        /* Una linea 2 */

        /*
         * Varias
         * lineas 1
         */

        /*
        Varias
        lineas 2
         */

        // -- -- Variables y Constantes -- --
        String miVariable = "Soy una variable";
        final String miConstante = "Soy una constante";

        // -- -- Tipos de datos primitivos -- --
        //   Caja[tipo]   =  Numero Maximo

        /* Primitivos Enteros */
        byte datoByte     = 127;
        short datoShort   = 32767;
        int datoInt       = 2147483647;

        /* Primitivos Flotantes */
        long datoLong     = 9223372036854775807L; // L al final
        float datoFloat   = 3.4028235E38F;        // F al final
        double datoDouble = 1.7976931348623157E308;

        /* Primitivos Character */
        char datoCharSimbolo = 'a';
        char datoCharDecimal = 80;

        /* Primitivos Booleano */
        boolean datoBoolean1 = true;
        boolean datoBoolean2 = false;

        String saludo = "¡Hola";
        final String lenguaje = "Java";
        System.out.println(saludo + ", " + lenguaje + "!");

    }

}
