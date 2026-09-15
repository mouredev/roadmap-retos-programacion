/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
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

public class calebsdev {

    public static void main(String[] args){
        //Comentario de una sola linea en Java
        //Sitio Java
        //URL: https://www.java.com/es/
        /*
        Comentario de multiples lineas en Java
        */
        
        int year = 2022;
        final String ArtistName = "ADO";

        //Tipos de datos primitivos
        boolean isSinger = true;    //Boolean       // 1 bit        // true or false
        byte age = 24;              //Byte          // 8 bits       // -128 to 127
        short height = 175;         //Short         // 16 bits      // -32,768 to 32,767
        int salary = 50000;         //Integer       // 32 bits      // -2,147,483,648 to 2,147,483,647
        long distance = 10000000L;  //Long          // 64 bits      // -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
        float weight = 70.5f;       //Float         // 32 bits      // 1.4E-45 to 3.4028235E38
        double pi = 3.141592653589; //Double        // 64 bits      // 4.9E-324 to 1.7976931348623157
        char initial = 'A';         //Character     // 16 bits      // '\u0000' (or 0) to '\uffff' (or 65,535)

        //Tipos de datos no primitivos
        String name = "ABO";        //String        // Variable length // A sequence of characters
        //ArrayList<String> names = new ArrayList<>(); //ArrayList // Variable length // A resizable array
        //Class<?> myClass = calebsdev.class;         //Class // Variable length // A class object
        //Inteface myInterface = new MyInterface() {}; //Interface // Variable length // An interface object

        System.out.print("¡Hola, Java!");
    }
}
