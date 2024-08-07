

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


public class oixild {
    public static void main(String[] args) {

        int intValue = miInt();
        System.out.println("El valor devuelto de miInt es: " + intValue);

    //miString("miString imprimira esto y le cambiara el valor devuelto");
        System.out.println(miString("miString imprimira esto y le cambiara el valor devuelto"));

        miVoid();

        int finalValueDificultadExtra = dificultadExtra("Primera cadena", "Segunda cadena");
        System.out.println("Los numeros se han imprimido " + finalValueDificultadExtra + " veces");
    }

    public static int miInt() {
        return (1);
    }

    public static String miString(String str) {
        System.out.println("Printado en miString: " + str);
        str = "Printado en main: Al no ser una constante se le puede cambiar el valor";
        return (str);
    }

    public static void miVoid() {
        System.out.println("Void no retorna nada");
    }

    // APARTE DE PUBLIC TAMBIEN HAY PROTECTED Y PRIVATE, TAMPOCO ES NECESARIO QUE SEA STATIC, EN ESTE CASO SI
    // POR QUE LO LLAMAMOS DESDE UNA FUNCION ESTATICA public static void main

    public static int dificultadExtra(String str1, String str2) {
        int i = 0, count = 1;
        while(count <= 100) {
            if (count % 3 == 0 & count % 5 == 0) {
                System.out.println(str1 + str2);
            }
            else if (count % 3 == 0) {
                System.out.println(str1);
            }
            else if (count % 5 == 0) {
                System.out.println(str2);
            }
            else {
                System.out.println(count);
                i++;
            }
            count++;
        }

        return (i);
    }

}

