public class Paiva {
    /** Comentarios de documentación */
     public static void main(String[] args) {
    // https://www.java.com/es/ -> Comentario en una linea
    /* Comentario en varias lineas */

// Variable: Puede cambiar su valor
 int edad = 21;
// Constante: Su valor no cambia una vez asignado y se pone final delante de la declaración
 final double PI = 3.1416;
// Tipo de datos primitivos
  byte b = 1; // 8 bits Rango: -128 a 127
  short s = 2; // 16 bits Rango: -32,768 a 32,767
  int i = 3; // 32 bits Rango: -2,147,483,648 a 2,147,483,647
  long l = 4; // 64 bits Rango: -9,223,372,036,854,775,808 a 9,223,372,036,854,775,807
  float f = 5.0f; // 32 bits Rango: -3.4028235E38 a 3.4028235E38
  double d = 6.0; // 64 bits Rango: -1.7976931348623157E308 a 1.7976931348623157E308
  char c = 'A'; // 16 bits Guarda solo una letra entre comillas simples
  boolean bl = true; // 1 bit Rango: true o false 

// Tipo objeto no es primitivo pero almacena texto en comillas dobles
    String t = "Reiner";

// Imprime con un salto de linea
    System.out.println("¡Hola, Java!");

// Imprime corrido
    System.out.print("Texto ");
    System.out.print("en una sola línea\n");

// Imprime con formato
    System.out.printf("Mi edad es %d años y mi nombre es %s.%n", edad, t);
}
}
