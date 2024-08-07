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

public class JesusEs1312 {
    //--- Variables globales ---
    String variableGlobal = "Soy una variable global";

    //--- Funciones básicas ---
    // Sin parámetros ni retorno
    public void funcionBasica() {
        System.out.println("Hola, soy una función básica sin parametros ni retorno");
    }

    // Con un parámetro
    public void funcionConParametro(String parametro) {
        System.out.println("Hola, soy una función con un parámetro: " + parametro);
    }

    // Con varios parámetros
    public void funcionConVariosParametros(String parametro1, String parametro2) {
        System.out.println("Hola, soy una función con varios parámetros: " + parametro1 + " y " + parametro2);
    }

    // Con retorno
    public String funcionConRetorno() {
        return "Hola, soy una función con retorno";
    }

    //--- Funciones dentro de funciones ---
    public void funcionPrincipal() {
        System.out.println("Hola, soy la función principal");
        funcionBasica();
    }

    public static void main(String[] args) {
        //--- Variables locales ---
        String variableLocal = "Soy una variable local";

        JesusEs1312 jesus = new JesusEs1312();
        jesus.funcionBasica();
        jesus.funcionPrincipal();
        jesus.funcionConParametro("parametro");
        jesus.funcionConVariosParametros(variableLocal, jesus.variableGlobal);
        System.out.println(jesus.funcionConRetorno());

        //--- funciones ya creadas en el lenguaje ---
        // Math.random() devuelve un número aleatorio entre 0.0 y 1.0
        System.out.println(Math.random());
        // UpperCase() convierte una cadena de texto a mayúsculas
        System.out.println(jesus.funcionConRetorno().toUpperCase());
        // LowerCase() convierte una cadena de texto a minúsculas
        System.out.println(jesus.funcionConRetorno().toLowerCase());
        // Length() devuelve la longitud de una cadena de texto
        System.out.println(jesus.funcionConRetorno().length());
        // Replace() reemplaza una cadena de texto por otra
        System.out.println(jesus.funcionConRetorno().replace("Hola", "Adios"));
        // Substring() devuelve una subcadena de texto
        System.out.println(jesus.funcionConRetorno().substring(0, 4));
        // Concat() concatena dos cadenas de texto
        System.out.println(jesus.funcionConRetorno().concat(" con concatenación"));
        // Equals() compara dos cadenas de texto
        System.out.println(jesus.funcionConRetorno().equals("Hola, soy una función con retorno"));

        //--- Dificultad extra ---
        System.out.println(jesus.funcionExtra("Fizz", "Buzz"));
    }

    //--- Dificultad extra ---
    public int funcionExtra(String parametro1, String parametro2) {
        int contador = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(parametro1 + parametro2);
            } else if (i % 3 == 0) {
                System.out.println(parametro1);
            } else if (i % 5 == 0) {
                System.out.println(parametro2);
            } else {
                System.out.println(i);
            }
            contador++;
        }
        return contador;
   } 
}
