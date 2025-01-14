/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

#include <stdio.h>
#include <stdbool.h>

  // Los principales operadores en c son los ariméticos, lógicos, comparación, de asignación, de bits y unarios.

int main() {
  
  int a = 5;
  int b = 9;

  // Operadores aritméticos

  // Suma
  printf("Suma: %d\n", a + b);
  //Resta
  printf("Resta: %d\n", a - b);
  //Multiplicación
  printf("Multiplicación: %d\n", a * b);
  //División
  printf("División: %d\n", a / b);
  //Módulo o Resto
  printf("Módulo: %d\n", a % b);
  //Incremento
  a++;
  printf("Incremento: %d\n", a);
  //Decremento
  b--;
  printf("Decremento: %d\n", b);

  // Operadores lógicos
  bool c = true, d = false;

  // AND
  printf("AND lógico: %d (0 = false, 1 = true)\n", c && d);
  // OR
  printf("OR lógico: %d (0 = false, 1 = true)\n", c || d);
  // NOT
  printf("NOT lógico: %d (0 = false, 1 = true)\n", !d);
  printf("NOT lógico: %d (0 = false, 1 = true)\n", !c);

  // Operadores de comparación
  int e = 5;
  int f = 8;
  
  // Igual a
  printf("Igual a: %d (0 false, 1 = true)\n", e == f);
  // Diferente de
  printf("Diferente de: %d (0 false, 1 = true)\n", e != f);
  // Mayor que
  printf("Mayor que: %d (0 false, 1 = true)\n", e > f);
  // Menor que
  printf("Menor que: %d (0 false, 1 = true)\n", e < f);
  // Mayor o igual que
  printf("Mayor o igual que: %d (0 false, 1 = true)\n", e >= f);
  // Menor o igual que
  printf("Menor o igual que: %d (0 false, 1 = true)\n", e <= f);

  //Operadores de asignación
  int g = 4;
  int h = 8;

  // Asignación =
  // Asignación con suma
  printf("Asignación con suma: %d\n", g += h);
  // Asignación con resta
  printf("Asignación con resta: %d\n", g -= h);
  // Asignación con multiplicación
  printf("Asignación con multiplicación: %d\n", g *= h);
  // Asignación con división
  printf("Asignación con división: %d\n", g /= h);
  // Asignación con módulo
  printf("Asignación con modulo: %d\n", g %= h);

  /*
  Existen otros operadores como los operadores de Bits, Unarios y Ternario.
  - Los operadores de bits realizan operaciones directamente sobre los bits individuales de los operandos. Estos son útiles en situaciones que requieren manipulación a nivel de bits, como en programación de sistemas, controladores de hardware, y algoritmos de criptografía.
  - Los operadores unarios son aquellos que operan sobre un solo operando. Estos operadores se utilizan comúnmente para operaciones aritméticas, lógicas y de punteros.
  - El operador ternario es una forma concisa de realizar una operación condicional. Es el único operador en C que toma tres operandos. La sintaxis es condicion ? expresion_si_true : expresion_si_false.
  */

  // Estructuras de control
  /* La principales estructuras de control en c serian:
  - Estructuras condicionales: Permite ejecutar u omitir bloques de código según se cumplan o no ciertas condiciones. if-else y switch
  - Estructuras de repetición o bucles: permiten ejecutar bloques de código repetidamente mientras se cumple una condición o hasta que se cumpla la condición. while, do-while y for
  - Estructuras de salto: Controlan el flujo del programa saltando a diferentes partes del código. break, continue, goto, return
  */

  // If-Else
  int num1 = 5;
  if (num1 > 0) {
    printf("El número %i es positivo\n", num1);
  }
  else {
    printf("El número %i es negativo\n", num1);
  }

  // Switch
  int num2 = 1;
  switch (num2)
  {
  case 2:
    printf("El número %i es 2.\n", num2);
    break;
  case 0:
    printf("El número %i es 0.\n", num2);
  default:
  printf("El número %i no es ni 0 ni 2.\n", num2);
  }

  // For
  int i;
  for (i = 0; i < 5; i++) {
    printf("El valor es %i por cada paso del bucle.\n", i);
  }
  // While
  i = 0;
  while (i < 6){
    printf("El valor de i es: %i.\n", i);
    i++;
  }
  //Do While
  i = 3;
  do{
    printf("El valor de i es: %i.\n", i);
    i++;
  }
  while(i < 6);

  // Ejercicio Extra

  printf("== Ejercicio Extra ==\n");

  for (i = 10; i <= 55; i++) {
    if (i % 2 == 0 && i !=16 && i % 3 != 0){
    printf("Números: %i\n", i);
    }
  }
}
