/* C17 gratuito con wayback machine:
   https://web.archive.org/web/20180118051003/http://www.open-std.org/jtc1/sc22/wg14/www/abq/c17_updated_proposed_fdis.pdf
*/

// Comentario de una linea

// Para las constantes máximas de cada dato
#include <limits.h>
// Libreria estandar para leer y escribir
#include <stdio.h>

// Un tipo de constante
#define PI 3.1416

int main() {
  // Otro tipo de constante de tipo caracter
  const char character = 'C';

  // VARIABLES EN SISTEMAS DE 64 BITS

  // Enteros y caracteres
  /* Puedes referenciarlo por caracter como 'A'
   *  o por su número correspondiente en ASCII,
   *  un char tiene 8 bits, por lo que sus
   *  valores posibles son desde
   *  -2^7 a (2^7)-1
   */
  char character2 = CHAR_MAX;
  printf("char: %c\n", character);   // Imprimir como texto
  printf("char: %hhd\n", character); // Imprimir como num

  /* 16 bits: de -2^15 a (2^15)-1
   * Se puede declarar como:
   * short int shortInteger = SHRT_MIN;
   * Pero abreviado es: */
  short shortInteger = SHRT_MIN;
  printf("short: %hd\n", shortInteger);

  // 32 bits: de -2^31 a (2^31)-1
  int integer = INT_MAX;
  printf("int: %d\n", integer);

  /* 64 bits: de -2^63 a (2^63)-1
   * Se puede declarar como:
   * long int longInteger = LONG_MIN;
   * Pero abreviado es: */
  long longInteger = LONG_MAX;
  printf("long: %ld\n", longInteger);

  // En sistemas de 32 bits se declaraban enteros de 64 bits se hacia con
  long long llinteger;
  printf("C rellenará las variables si no lo definimos nosotros");
  printf("No siempre tendrá el valor que queremos");
  printf("long long: %lld\n", llinteger);

  //ENTEROS SIN SIGNO

  /* Tenemos enteros que pueden tener signo positivo o negativo
   * por lo que el ultimo bit de nuestra variable se usa para
   * determinar si es positivo o negativo. Pero si no requerimos
   * datos negativos podemos usar todos los bits para representar
   * numeros. Para esto usamos la palabra reservada signed y 
   * unsigned, por defecto todos los tipos son signed
   *
   * int var == signed int  var*/
  unsigned short uShortInteger = USHRT_MAX;
  printf("ushort: %hu\n", uShortInteger);

  unsigned long uLongInteger = ULONG_MAX;
  printf("ushort: %lu\n", uLongInteger);

  // VARIABLES DE COMA FLOTANTE
  // Tiene 32 bits, pero el valor que contienen se calcula de forma más compleja
  float floatData = 2.0;
  printf("float: %f\n", floatData);
  printf("float limitando decimales impresos: %.2f\n", floatData);

  // Posee 64 bits
  double doubleData = 3.0;
  printf("float: %lf\n", doubleData);

  printf("Hola %c\n", character);
}
