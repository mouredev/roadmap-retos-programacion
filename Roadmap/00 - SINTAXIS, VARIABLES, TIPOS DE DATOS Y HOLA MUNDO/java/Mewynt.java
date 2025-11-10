// https://developers.redhat.com/

// comentario en una linea
/* comentario en varias lineas

 */

public class Mewynt {
  public static void main(String[] args) {

    // CREACION DE VARIABLE

    String variable = "Hola soy una variable de JAVA";

    // CREACION VARIABLE CONSTANTE "final" Hace que la variable sea constante (no
    // modificable)

    final double DOLAR = 3.38; // Nombre en mayusculas Convención para distinguir constantes

    /// ==================== CREACIÓN DE VARIABLES ====================
    /// 
    int diasSemana = 7; // 4 bytes | -2,147,483,648 a 2,147,483,647 | Tipo entero más común.

    double pi = 3.141592; // 8 bytes | ±1.7×10³⁰⁸ (15 decimales) | Números decimales con más precisión.

    float precio = 5.75f; // 4 bytes | ±3.4×10³⁸ (6-7 decimales) | Números decimales pequeños (usa sufijo f).

    short numero = 3000; // 2 bytes | -32,768 a 32,767 | Entero más grande que byte pero menor que int.

    long distancia = 15000L; // 8 bytes | -2,147,483,648 a 2,147,483,647 | Enteros muy grandes (usa sufijo L).

    byte edad = 20; // 1byte (8 bits) | -128 a 127 | Entero pequeño, útil para ahorrar memoria.

    char letra = 'A'; // 2 bytes | Unicode (0 a 65,535) | Almacena un solo carácter.

    boolean activo = true; // 1 bit(aprox.) | true o false | Representa valores logicos.

    String nombre = "Guillermo"; // Variable | N/A | Cadena de texto (no primitivo, clase)

    // Imprimiendo algunas cosas
    System.out.print("yo siempre quise decir:" + variable);
  }
}
