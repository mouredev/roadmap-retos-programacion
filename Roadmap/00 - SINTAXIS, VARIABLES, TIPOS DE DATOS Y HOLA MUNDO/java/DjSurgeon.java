/*
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */

public class Java00 {
  // Esto es un comentario de una linea.
  // La web oficial de java es:
  // https://www.oracle.com/java/

  /*
  Esto es un comentario de varias lineas, todo lo que se encuentra en su interior
  no se ejecuta.
   */

  /**
   * Esto es un JavaDoc sirve para generar documentacion sobre tu código.
   */

  public static void main(String[] args) {
    /*
    La sintaxis básica de Java para una variable es la siguiente:
    tipoDeDato nombreDeLaVariable = valor;
    int edad = 42;
    Y los tipos de datos primitivos del lenguaje son:
    - Enteros:
    byte: Almacena números enteros con un tamaño de 8 bits.
    short: Almacena números enteros con un tamaño de 16 bits.
    int: Almacena números enteros con un tamaño de 32 bits, 42.
    long: Almacena números enteros con un tamaño de  64 bits.
    - Punto flotante:
    float: Se utiliza para almacenar números fraccionarios con una única precisión.
    double: Almacena números con decimales con doble precisión, 3.14.+
    - Otros tipos:
    char: Almacena un solo carácter 'a'.
    boolean: Almacena un valor, true o false.
     */
    int edad = 42;

    /*
    Las constantes son variables cuyo valor no puede ser cambiado después de su inicialización.
    final tipoDeDato NOMBRE_DE_LA_CONSTANTE = valor;
    final double PI = 3.14159;
     */

    // Las strings no son un tipo primitivo, y son conjuntos de char y sirven para almacenar texto.
    String nombre = "Sergio";

    System.out.println("Hola, Java!");
  }

}
