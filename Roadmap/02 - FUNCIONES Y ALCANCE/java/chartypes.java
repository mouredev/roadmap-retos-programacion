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

public class chartypes {

  static String globalVar = "Global variable or Instance variable";

  class Functions {

    public static void noParamsNoReturn() {
      System.out.println("Function with no params and no returns");
    }

    public static void withParams(int number) {
      System.out.println("With params but no return. The number is: " + number);
    }

    public static String withReturn(String text) {
      return text;
    }

    public static void methodInside() {
      System.out.println(withReturn("Im inside of other method"));
    }

  }

  class BuiltInFunctions {

    public static void stringFunctions() {
      String hello = "Hello world";
      int length = hello.length();
      char first = hello.charAt(0);
      String subStr = hello.substring(6);
      String upperCase = hello.toUpperCase();
      String lowerCase = hello.toLowerCase();

      System.out.println("String buit-in functions! ");
      System.out.println(hello);
      System.out.println(length);
      System.out.println(first);
      System.out.println(subStr);
      System.out.println(upperCase);
      System.out.println(lowerCase);
    }

    public static void intFunctions() {
      int max = Math.max(4, 2);
      int min = Math.min(10, 15);
      int abs = Math.abs(-34);

      System.out.println("Int built-in functions! ");
      System.out.println(max);
      System.out.println(min);
      System.out.println(abs);
    }

  }

  class BonusEx {
    static int counter;

    public static int exercise(String text1, String text2) {
      for (int i = 0; i < 100; i++) {

        if (i % 3 == 0 && i % 5 == 0) {
          System.out.println(text1 + text2);

        }

        else if (i % 3 == 0) {
          System.out.println(text1);
        }

        else if (i % 5 == 0) {
          System.out.println(text2);
        }

        counter++;
      }
      return counter;
    }

  }

  public static void main(String[] args) {
    String localVar = "Local variable";

    System.out.println(chartypes.globalVar);
    System.out.println(localVar);

    Functions.methodInside();
    BuiltInFunctions.stringFunctions();
    BuiltInFunctions.intFunctions();

    System.out.println(BonusEx.exercise("fizz", "buzz"));

  }
}
