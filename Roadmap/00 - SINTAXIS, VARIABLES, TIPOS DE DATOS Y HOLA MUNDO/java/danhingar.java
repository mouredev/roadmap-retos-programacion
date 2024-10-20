//URL OFICIAL JAVA: https://www.java.com/es/

//Comentario en una linea

/*Comentarios
 en 
 varias 
 lineas 
 */

/**
 * Comentarios para generar documentación JAVADOC
 * 
 * Estos comentarios se utilizan para documentar los ficheros Java,
 * para ello utilizamos las siguientes etiquetas:
 * 
 * @author Daniel -> especifica el autor del fichero
 * 
 * @param name
 * @return String
 * @throws Exception
 * @since
 */

public class danhingar {

    // Para poder ejecutar algo en Java necesitamos tener definido un método main
    public static void main(String[] args) {

        /*
         * Datos primitivos
         * 
         * Tenemos tres tipo de datos: númericos, carácteres y booleanos
         */

        // Tipo primitivos númerico

        byte numero1 = 127; // Almacena un número hasta 8 bits(-127,127)
        short numero2 = 3242; // Almacena un número hasta 16 bits(-32768,32767)
        int numero3 = -235546234; // Almacena un número hasta 32 bits
        long numero4 = 716473841782738267l; // Almacena un número hasta 64 bits, obligatorio añadir 'l' al final
        float numero5 = 213123213.213f; // Almacena un número con decimales hasta 32 bits, obligatorio añadir 'f' al final
        double numero6 = -327163782136.2138762163876; // Almacena un número con decimales hasta 64 bits

        // Tipo primitivo boolean
        boolean condition = Boolean.TRUE;

        // Tipo primitivo caracter;
        char A = 'A';

        //Una constante se define usando 'final'
        final int constante= 23;

        // Para imprimir por terminal usamos:
        System.out.println("¡Hola,Java!");
    }

}