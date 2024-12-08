/*
        * - Crea ejemplos de funciones básicas que representen las diferentes
        *   posibilidades del lenguaje:
        *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
        * - Comprueba si puedes crear funciones dentro de funciones.
        * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
        * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
        * - Debes hacer print por consola del resultado de todos los ejemplos.
        *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
        * DIFICULTAD EXTRA (opcional):
        * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
        * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
        *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
        *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
        *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
        *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
        *
        * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
        * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
public class Funciones_Alcance {

    static String variableGlobal = "Esto es una variable Global"; //Variable Global, sin parámetro ni retorno

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        //Acceder a la variable Glogal:
        System.out.println(variableGlobal);

        //Acceder a la función sin parámetro:
        saludar();

        //Acceder al método con parámetros:
        saludarN("Ruth");

        //Acceder a la función con parámetros:
        double numero = 12;
        double raizC = raizCuadrada(numero);
        System.out.println("La raiz cuadrada de " + numero + " es " + raizC);

        //Acceder al método extra:
        String texto1 = "fizz";
        String texto2 = "Buzz";
        fizzBuzz(texto1, texto2);
    }

    public static void variables() {
        String variableLocal = "Esto es una variable local";

        //Acceder a la variable local
        System.out.println(variableLocal);

    }

    //Función con retorno sin parámetros:
    static String saludar() {
        String saludo = "Hola ";
        return saludo;
    }

    //método con parámetros:
    static void saludarN(String nombre) {
        System.out.println(saludar() + nombre);
    }

    //Función con parámetros + función ya creada:
    static double raizCuadrada(double numero) {
        return Math.sqrt(numero);
    }

    //Extra:
    static int fizzBuzz(String texto1, String texto2) {
        int count = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0) {
                System.out.println(texto1);
            } else if (i % 5 == 0) {
                System.out.println(texto2);
            } else if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(texto1 + texto2);
            } else {
                System.out.println(i);
            }
            count++;
        }
        return count;
    }
}
