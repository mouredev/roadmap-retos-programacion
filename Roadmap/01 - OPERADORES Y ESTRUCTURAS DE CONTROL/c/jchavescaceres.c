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
 * DIFICULTAD EXTRA:
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

#include <stdio.h>

void main () {

int a=10;
int b=3;

printf ("Aritméticos:\n");
printf ("a=%d, b=%d\n", a, b);
printf ("Suma a+b : %d\n", a+b);
printf ("Resta a-b : %d\n", a-b);
printf ("Multiplicación a*b : %d\n", a*b);
printf ("Divisioin a/b : %d\n", a/b);
printf ("Módulo a%% b : %d\n", a%b);
printf ("Incrementar primero y devolver nuevo valor ++a: %d, a: %d\n", ++a, a);
printf ("Devolver valor e incrementar luego a++: %d, a: %d\n", a++, a);
printf ("Decrementar primero y devolver nuevo valor --a: %d, a: %d\n", --a, a);
printf ("Devolver valor y decrementar luego a--: %d, a: %d\n", a--, a);

printf ("\nComparación:\n");
printf ("a=%d, b=%d\n", a, b);
printf ("a>b %s\n", a>b ? "true" : "false");
printf ("a>=b %s\n", a>=b ? "true" : "false");

printf ("\nAsignación:\n");
printf ("a=%d, b=%d \n", a, b);
b=a;
printf ("b=a b: %d \n", b);
a+=2;
printf ("Sumar y asignar nuevo valor a+=2 : %d\n", a);
a-=2;
printf ("Restar y asignar nuevo valor a-=2 : %d\n", a);
a*=2;
printf ("Multiplicar y asignar nuevo valor a*=2 : %d\n", a);
a/=2;
printf ("Dividir y asignar nuevo valor a/=2 : %d\n", a);
a%=2;
printf ("Módulo y asignar nuevo valor a%%=2 : %d\n", a);
}
