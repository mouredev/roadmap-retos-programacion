// Sitio web del lenguaje:
// https://docs.oracle.com/en/java/

// Comentario de línea

/**
 * Este es un comentario
 * de varias líneas
 */

/*
  Esto también es un
  comentario de
  varias líneas
 */

public class CesarCarmona30 {
  public static void main(String[] args) {
    
    // Variable
    String name = "Cesar";
    // Constante: se declaran con final
    final String GENDER = "MALE";

    // TIpos de datos primitivos
    byte numByte = 127;
    short numShort = 32767;
    int numInt = 2147483647;
    long numLong = 9223372036854775807L;
    float numFloat = 21.4f;
    double height = 1.75;
    boolean alive = true;
    boolean dead = false;
    char blood = 'O';
    String country = "México";

    String language = "Java";
    System.out.println("¡Hola, " + language + "!");
  }
}