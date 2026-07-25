public class Java01 {
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

  // Constante global
  public static final int EDAD = 42;

  /**
   * Saludos!!
   */
  public static void saluda() {
    System.out.println("Hola, Java!!");
  }

  /**
   * Saluda a una persona por su nombre.
   * @param nombre El nombre de la persona.
   */
  public static void nombra(String nombre) {
    System.out.printf("Hola, %s!!\n", nombre);
  }

  /**
   * Realiza una suma de dos números enteros.
   * @param sum1 El primer sumando.
   * @param sum2 El segundo sumando.
   * @return La suma total.
   */
  public static int suma(int sum1, int sum2) {
    int total;

    total = sum1 + sum2;
    return (total);
  }

  /*
  En Java no se pueden crear funciones dentro de funciones. Todos los metodos deben ser miembros de
  una clase.
   */

  /*
  En este ejemplo se estan usando funciones predefinidas del sistema como son println() y printf().
   */

  /*
    EJERCICIO EXTRA
   */

  public static int extra(String s1, String s2) {
    int total;

    total = 0;
    for (int i = 0; i < 100; i++) {
      if (i % 5 == 0 && i % 3 == 0) {
        System.out.println(s1 + " " + s2);
      } else if (i % 5 == 0) {
        System.out.println(s1);
      } else if (i % 3 == 0) {
        System.out.println(s2);
      } else {
        total++;
      }
    }
    return (total);
  }

  public static void main(String[] args) {
    int result;

    result = suma(3, 3);
    saluda();
    nombra("Sergio");
    System.out.printf("La suma de 3 + 3 es: %d.\n", result);
    System.out.printf("Mi edad es %d años.\n", EDAD);
    result = extra("Hola", "Java");
    System.out.printf("El total es: %d.\n", result);
  }
}
