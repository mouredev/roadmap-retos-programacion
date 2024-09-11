public class martinaq {

    // Static variables have to be declared before any instance and can be shared among other instances.
    static final String myVar = "This is a const variable in Java"; 
    public static void main(String[] args) {
        /*
        * EJERCICIO:
        * - Crea un comentario en el código y coloca la URL del sitio web oficial del
        *   lenguaje de programación que has seleccionado.
        * - Representa las diferentes sintaxis que existen de crear comentarios
        *   en el lenguaje (en una línea, varias...).
        * - Crea una variable (y una constante si el lenguaje lo soporta).
        * - Crea variables representando todos los tipos de datos primitivos
        *   del lenguaje (cadenas de texto, enteros, booleanos...).
        * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
        *
        * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
        * debemos comenzar por el principio.
        */

        /* 1. Crea un comentario en el código y coloca la URL del sitio web oficial del
         *   lenguaje de programación que has seleccionado. */

        // https://www.java.com/es/

        /* 2. Representa las diferentes sintaxis que existen de crear comentarios
         *   en el lenguaje (en una línea, varias...). */

        /* Comentario en
         * varias
         * lineas. */

        // 3. Crea una variable (y una constante si el lenguaje lo soporta).
        String username = "martin-aq";
        System.out.println(username);

        // 4. Crea variables representando todos los tipos de datos primitivos.
        boolean a = true; // 1 bit
        char b = '$'; // 2 bytes, char uses 2 bytes due to the usage of Unicode.
        byte c = 120; // 1 byte
        short d = 250; // 2 bytes
        int e = 36432; // 4 bytes
        long f = 9223372036854775L; // 8 bytes
        float g = 36739.24f; // 4 bytes, same as int data type
        double h = 9223372036854775.12d; // 8 bytes, same as long data type

        System.out.printf("boolean: %s\nchar: %c\nbyte: %d\nshort: %d\nint: %d\nlong: %d\nfloat: %f\ndouble: %f\n", a,b,c,d,e,f,g,h);

        // 5. Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
        System.out.println("Hello Java!");
    }
}
