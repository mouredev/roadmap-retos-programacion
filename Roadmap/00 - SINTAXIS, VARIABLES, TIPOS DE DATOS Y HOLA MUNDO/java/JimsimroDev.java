public class JimsimroDev {
  public static void main(String[] args) {
    // Sitio oficial de java licencia paga
    // https://www.oracle.com/java/technologies/downloads/

    /*
     * Licencia gratis es el openjdk
     * https://jdk.java.net/
     */

    // Tipos de datos primitivos son
    // boolean, byte, char, short, int, long, float, double
    int numero = 25;
    String nombre = "Jimmis J Simnaca";
    final long edad = 29; // constante en java
    short fecha = 2024;
    char letra = 'c';
    float num = 23;
    double decimal = 2.3;
    boolean esEstudiandte = true;
    String lenguaje = "[Java]";

    // Precedencia de operadores
    int precedencia = ((5 * 8) + 4) * 2; // el resultado es 88 primero se opera las multiplicacion dentro de los () y
                                         // luego las sumas
    System.out.printf("resultado %d ", precedencia);
    System.out.println("\n¡Hola, " + lenguaje);
  }
}
