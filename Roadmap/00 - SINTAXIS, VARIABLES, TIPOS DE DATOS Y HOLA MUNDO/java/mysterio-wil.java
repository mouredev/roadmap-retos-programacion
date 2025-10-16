// EJERCICIO:
// - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
//   https://www.java.com/

// Nota: El nombre del archivo "mysterio-wil.java" no es un nombre de clase público válido en Java.
// Para que el código compile, la clase no es pública y se ha nombrado "mysterio_wil".
class mysterio_wil {

    public static void main(String[] args) {

        // - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

        // Esto es un comentario de una línea

        /*
        Esto es un comentario
        de varias líneas
        */

        /**
         * Esto es un comentario de documentación (Javadoc)
         */

        // - Crea una variable (y una constante si el lenguaje lo soporta).
        String myVariable = "Mi variable";
        final String MY_CONSTANT = "Mi constante";

        // - Crea variables representando todos los tipos de datos primitivos del lenguaje.
        byte myByte = 100;
        short myShort = 10000;
        int myInt = 100000;
        long myLong = 1000000000L;
        float myFloat = 10.5f;
        double myDouble = 10.55555;
        boolean myBoolean = true;
        char myChar = 'a';
        // String no es un tipo primitivo en Java, es un objeto.
        String myString = "Cadena de texto";


        // - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
        System.out.println("¡Hola, Java!");
    }
}
