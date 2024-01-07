// Visita el sitio oficial de Java: https://www.oracle.com/java/


// Este es un comentario de una sola línea.

/*
   Este es un comentario
   que abarca varias líneas.
*/

/*
    Como ejecutar la siguiente clase de Java: 
    1. Instalación el JDK.

    2. Validar que este instalado con el comando: java -version

    3. Posicionar la terminal en la carpeta: 
    cd C:\DESARROLLO\git\roadmap-retos-programacion\Roadmap\00 - SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO\java

    4. Compilación de la clase Java, el proceso genera un archivo AngelSanchezT.class
        javac AngelSanchezT.java

    5. Ejecución de la clase Java: (Ejecución del archivo sin la extensión .class)
        java AngelSanchezT
 */

 public class AngelSanchezT {
    public static void main(String[] args) {
        // Declaración de una variable
        String mensaje = "¡Hola, Java!";

        // Declaración de una constante (final indica que es constante)
        final int CONSTANTE = 42;

        // Tipos de datos primitivos
        int entero = 10;
        double decimal = 3.14;
        char caracter = 'A';
        boolean booleano = true;

        // Imprimir por terminal
        System.out.println(mensaje);
    }
}