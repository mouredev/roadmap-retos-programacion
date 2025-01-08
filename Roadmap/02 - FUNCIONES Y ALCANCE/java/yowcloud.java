import java.lang.Math;
public class yowcloud {
    // Variable global
    static int globalVar = 42;
    public static void main(String[] args) {
        holaMundo();
        holaName("Cloud");
        addNumbers(4, 2);
        System.out.println("El producto es: " + multiplyNumbers(4, 2));
        System.out.println("El resultado de elevar 2 al cubo es: " + powerNumber(2, 4));
        testVariables();
        int result = dificultadExtra("Fizz", "Buzz");
        System.out.println("El número de veces que se ha impreso el número es: " + result);
    }  

    // Función sin parámetros ni retorno
    private static void holaMundo() {
        System.out.println("Función sin parámetros ni retorno");
        System.out.println("¡Hola mundo!");
    }

    // Función con un parámetro y sin retorno
    private static void holaName(String name) {
        System.out.println("Función con un parámetro y sin retorno");
        System.out.println("¡Hola " + name + "!");
    }

    // Función con varios parámetros y sin retorno
    private static void addNumbers(int num1, int num2) {
        System.out.println("Función con varios parámetros y sin retorno");
        int sum = num1 + num2;
        System.out.println("La suma es: " + sum);
    }

    // Función con retorno
    private static int multiplyNumbers(int num1, int num2) {
        System.out.println("Función con retorno");
        return num1 * num2;
    }

    // Función que utiliza una función ya creada en el lenguaje (Math.pow)
    private static double powerNumber(double base, double exponent) {
        System.out.println("Función que utiliza una función ya creada en el lenguaje");
        return Math.pow(base, exponent);
    }

    // Función que prueba el concepto de variable LOCAL y GLOBAL
    private static void testVariables() {
        System.out.println("Función que prueba el concepto de variable LOCAL y GLOBAL");
        int localVar = 21; // Variable local
        System.out.println("Variable global: " + globalVar);
        System.out.println("Variable local: " + localVar);
    }

    private static int dificultadExtra(String str1, String str2) {
        System.out.println("DIFICULTAD EXTRA");
        System.out.println("Función que recibe dos parámetros de tipo cadena de texto y retorna un número");
        int count = 0;
        for (int pos = 1; pos <= 100; pos++)
        {
            if (pos % 3 == 0 && pos % 5 == 0)
                System.out.println(str1 + str2);
            else if (pos % 3 == 0)
                System.out.println(str1);
            else if (pos % 5 == 0)
                System.out.println(str2);
            else
            {
                System.out.println(pos);
                count++;
            }
        }
        return count;

        
    }

    
}
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
