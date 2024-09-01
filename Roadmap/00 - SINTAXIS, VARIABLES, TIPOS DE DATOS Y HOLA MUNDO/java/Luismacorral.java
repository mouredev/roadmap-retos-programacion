public class Luismacorral {

    /**
     * @param args
     */
    public static void main(String[] args) {
        
        // Ejercicio #00

        // Página oficial de Java https://www.java.com/es/

        // Este es un comentario de una única linea.

        /*
         *
         * Este comentario 
         * abarca
         * varias lineas
         * de texto.
         * 
         * ¿Quieres ver a una pelota con vertigo caer al vacio? 
         * 
         * Mira que te gusta el morbo, ¿¿ehhh?? :
         * 
         *  .
         *  .
         *  .
         *  .
         *  .   - (¡¡Sooocooooorrrroooo!!)
         *  .  -
         *  . -
         *  °          -(Pa'mi que se mata, Paco.)
         *            -   -(¿Tu crees, Mariloli?)
         *           @  @
         * #####################################################       
         */


        // Pasemos a declarar una variable y una constante:

        int tipoEntera; // Declaración de una variable entera sin inicializar.
        tipoEntera = 25; // Inicializamos la variable después de haberla declarado.
        final int CONSTANTE = 100; // Constante declarada e inicializada.
        final String CONSTEXTO = "Heeyyy, que yo también soy una constante."; // Constante envidiosa de la clase String.

        // Declaración de variables con los diferentes tipos de datos primitivos

        // De tipo entero: 

        byte tipoByte = 100; // byte: entero de 8 bits. Rango: de -128 a 127.
        short tipoShort = 10000; // short: entero de 16 bits. Rango: de -32,768 a 32,767.
        int tipoInt = 100000; // int: entero de 32 bits. Rango: de -2,147,483,648 a 2,147,483,647.
        long tipoLong = 100000L; // long: entero de 64 bits. Rango: de -9,223,372,036,854,775,808 a 9,223,372,036,854,775,807.

        /*
         *                              |       -(Espero que tu próximo
         *        -(Paco...)            |      -    sueldo sea de tipo long.)
         *       -  -(Dime, Mariloli.)  |     -  -(Glups!)
         *      @  @                    |    @  @
         * #################################################################       
         */

        // De Punto Flotante:

        float tipoFloat = 10.5f; // float: Número de punto flotante de precisión simple de 32 bits.
        double tipoDouble = 10.5; // double: Número de punto flotante de doble precisión de 64 bits.

        // De tipo Booleano: Pueden tomar dos valores, verdadero o falso.

        boolean tipoBool = true; // Variable booleana inicializada a true.
        boolean tipoBool2 = false; // Variable booleana inicializada a false.

        // De tipo carácter:

        char tipoChar = 'A'; // Caracter Unicode de 16 bits. Siempre va entre comillas simples ' '.

        System.out.print("¡Hola, soy Java y de mayor quiero ser una serpiente! Una pitón verbenera a poder ser.");
    }
}