//#00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO;
/* EJERCICIO:
 * 1- Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * 2- Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * 3- Crea una variable (y una constante si el lenguaje lo soporta).
 * 4- Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * 5- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */
public class rballestercoll {

    // 1 - WEB OFICIAL DE JAVA : https://www.java.com/es/

    // 2 - DIFERENTES SINTAXIX PARA CREAR COMENTARIOS

        // Comentario de una línea con dos slash

        /*
         * Comentario en
         * varias líneas.
         * Con slash y asterisco.
         */

    public static void main(String[] args) {

        // 3 - CREA UNA VARIABLE Y UNA CONSTANTE

            int edad = 36; // (VARIABLE)Antes de JDK 10, las variables se escribian indicando el tipo.

            var meses = 12; // (VARIABLE) A partir de JDK 10 las variables indistintamente del tipo que sean pueden declararse con "var". solo pueden declararse dentro de métodos y bloques de inicialización, pero no como variables de instancia o estáticas.

            final double precio = 3.6; //(CONSTANTE) Las constantes como tal en Java no existen, se coloca la partícula "final" delante del tipo y la variable se vuelve inmutable.

        // 4 - CREA UN LISTADO DE VARIABLES CON TODOS LOS TIPOS DE DATOS PRIMITIVOS

            int temperatura = -6;
            boolean existe = true;
            byte amigos = 13;
            short fecha = 4567;
            char clase = 'B';
            long hectareas = 65L;
            float medida = 100F;
            double medidas = 23.789;

        // 5 - IMPRIME LA FRASE "HOLA MUNDO EN (JAVA)"

            String lenguajeProgramacion = "Java";
            System.out.println("Hola Mundo en " + lenguajeProgramacion);

    }
}
