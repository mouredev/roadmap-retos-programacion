// Este es un comentario de una línea

/*
 * Este es un comentario
 * de multiples
 * líneas
 */

/*
 * C no tiene un sitio web oficial
 *
 * Se puede acceder a la documentación de gcc:
 * https://man7.org/linux/man-pages/man1/gcc.1.html
 *
 * O al manual de referencia de C:
 * https://www.gnu.org/software/gnu-c-manual/
 */

#include <stdio.h> // Se incluye la librearía para manejor de I/O

#define PI 3.141592 // Esto es una directiva de preprocesador

int main() {
  // Una variable
  int variable = 15;

  // Una constante
  const int constante = -4;

  // Los tipos de datos primitivos
  char c = 'f';
  int i = 100;
  float f = 1.4;
  double d = -5.2;

  /*
   * Se pueden poner los siguientes modificadores a los tipos de datos
   * - signed
   * - unsigned
   * - short
   * - long
   */

  /*
   * En C no existe ni el tipo Boolean, ni el tipo String
   */
  
  printf("¡Hola, C!\n");
  printf("La directiva de preprocesador PI: %f\n", PI);
  printf("Variable: %d\n", variable);
  printf("Constante: %d\n", constante);
  printf("Los tipos de datos primitivos: %c, %d, %.2f, %.2f\n", c, i, f, d);

  return 0;
}
