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

public class Alextc35 {
    public static void main (String[] args){

        // 1
        
        funcionVoidNoParams(); // No tiene parámetros y no retorna nada.

        funcionVoidSiParams("cat"); // Tiene un parámetro y no retorna nada.

        funcionVoidTwoParams(13, 22); // Tiene dos parámetros y no retorna nada.

        System.out.println("La suma de 21 + 196 es = " + funcionIntTwoParams(21, 196)); // Tiene dos parámetros y retorna un número.

        System.out.println("Mi nombre es: " + funcionStringSiParams("Alejandro")); // Tiene un parámetro y retorna una cadena de caracteres.

        // 2

        funcionDos(); // funcionUno dentro de la funcionDos.

        // 3

        System.out.println(numPar(8)); // Ejemplo de función ya existente. Si el número del parámetro es par dará 'True'.

        // 4

        int variable = 777; // Variable global que también está en la función 'variable', pero no son las mismas.

        int variableLocal = variable(); // Obtenemos la variable local y la almacenamos, siendo ahora una variable global.

        System.out.println("Variable global: " + variable + "\nVariable local: " + variableLocal); // No son iguales a pesar de haber compartido el nombre de la variable.

        // OPCIONAL

        System.out.println(funcionOpcional("Alejandro", "Tellez")); // Mostrará las cadenas un total de 47 veces, por ende nos debe retornar 53
        
    }
    
    // 1

    public static void funcionVoidNoParams (){ // Sin parámetros.
        System.out.println("Función que no tiene parámetros y no retorna nada.");
    } // No retorna nada.

    public static void funcionVoidSiParams (String word){ // Un parámetro de tipo cadena de texto.
        System.out.println("La palabra es " + word + ".");
    } // No retorna nada.

    public static void funcionVoidTwoParams (int number1, int number2){ // Dos parámetros, ambos de tipo númerico.
        System.out.println("La suma de " + number1 + " + " + number2 + " es = " + (number1+number2));
    } // No retorna nada.

    public static int funcionIntTwoParams (int number1, int number2){ // Dos parámetros, ambos de tipo númerico.
        int suma = number1 + number2;
        return suma; // Retorna la suma de los parámetros.
    }

    public static String funcionStringSiParams (String name){ // Un parámetro de tipo cadena de texto.
        String myName = name;
        return myName; // Retorna la cadena de texto.
    }

    // 2

    public static void funcionUno() { // Función número uno.
        System.out.println("Soy la función uno!");
    }
    
    public static void funcionDos() { // Función número dos.
        funcionUno(); // Función uno dentro de la función dos.
        System.out.println("Soy la función dos!");
    }

    // 3

    public static boolean numPar(int number){
        if (number % 2 == 0) { // Comprueba que el resto de dividir el número entre 2 es 0.
            return true; // En caso afirmativo, el número será par.
        }
        return false; // Si no, será impar.
    }

    // 4

    public static int variable(){
        int variable = 666; // Esta es la variable local, que no afecta a nuestra variable global.
        return variable;
    }

    // OPCIONAL

    public static int funcionOpcional(String cadena1, String cadena2){
        int num = 0;

        // Hacemos un bucle del 1 al 100.
        for (int i = 1; i <= 100; i++){
            // Comprobamos si es divisible entre 3
            if (i % 3 == 0) {
                System.out.println(cadena1);
            // Comprobamos si es divisible entre 5
            } else if (i % 5 == 0) {
                System.out.println(cadena2);
            // Comprobamos si es divisible entre 3 y 5
            } else if (i % 3 == 0 && i % 5 == 0){
                System.out.println(cadena1 + cadena2);
            } else {
            // Si no se cumple ninguna, sumamos una unidad a nuestra variable.
                num++;
            }
        }
        return num;
    }
}