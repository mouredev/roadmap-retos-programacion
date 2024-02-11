package com.dm4.roadmap;

/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
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


public class Roadmap02_FuncionYAlcance {

    /**
     * Variable global: Resultan visibles y disponibles para todas las sentencias de un script
     */
    static int cont = 0; // Variable Global

    public static void main(String[] args) {
        sinParametrosNiRetorno();
        saludar("JAVA");
        mostrarCoordenadas(3, 7, 5);
        calcularAreaCirculo(6);
        imprimir("Hola", "JAVA");

    }

    /**
     * Funcion sin parámetros ni retorno, con uno o varios parámetros.
     */
    public static void sinParametrosNiRetorno() {
        System.out.println();
        System.out.println(" ** Funcion sin parametros ni retorno");
        System.out.println("Esta funcion no devuelve ningun valor, no tiene parametros ni retorno");
        System.out.println("--------------------------------------------------------------------------");
    }

    /**
     * Funcion con un parametro y sin retorno.
     */

    public static void saludar(String nombre) {
        System.out.println();
        System.out.println(" ** Funcion con un parametro");
        System.out.println("Hola, " + nombre + "!");
        System.out.println("--------------------------------------------------------------------------");
    }

    /**
     * Funcion con varios parámetros, sin retorno.
     */

    public static void mostrarCoordenadas(int x, int y, int z) {
        System.out.println();
        System.out.println(" ** Funcion con mas de un parametro");
        System.out.println("Coordenadas: (" + x + "," + y + "," + z + ")");
        System.out.println("--------------------------------------------------------------------------");
    }
    /**
     * Funcion con retorno y con un parametro.
     */

    public static double calcularAreaCirculo(double radio) {
        /*
         * Variable Local: Solo resultan visibles y disponibles dentro de la
         * función en la que están definidas.
         */
        double area = 0;

        System.out.println();
        System.out.println(" ** Funcion con retorno y con un parametro");
        area = Math.PI * Math.pow(radio, 2);
        System.out.println("Area del Circulo : " + area + " cm");
        System.out.println("--------------------------------------------------------------------------");
        return area;

    }

    /**
     *  DIFICULTAD EXTRA (opcional)
     */

    public static int imprimir(String cadena1, String cadena2) {
        System.out.println();
        System.out.println(" ** Dificultad extra");
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(i +  " : " + cadena1 + " " + cadena2 );
            } else if (i % 3 == 0) {
                System.out.println(i + " : " + cadena1);
            } else if (i % 5 == 0) {
                System.out.println(i + " : " + cadena2);
            } else  {
                System.out.println(i);
                cont++;
            }
        }
        System.out.println("--------------------------------------------------------------------------");
        return cont;
    }
}
