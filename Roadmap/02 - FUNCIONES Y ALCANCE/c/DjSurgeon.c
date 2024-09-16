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

// Funciones básicas del sistema

#include <stdio.h>

// Función que no devuelve nada (void) y sin parametros.

void texto() {
  printf("Esto es un churro de texto.\n");
  printf("Esta funcion no tiene parametros.\n");
  printf("Y no devuelve nada, por eso es void.\n");
}

// Función con un parametro, pero sin retorno.

void imprimeNumero(int num) {
  printf("El parametro ingresado es: %d.\n", num);
}

// Función con varios parametros, sin retorno.

void sumaNumeros(int num1, int num2) {
  printf("La suma de %d y %d es igual a: %d.\n", num1, num2, num1 + num2);
}

// Funcion con parametro y que retorna un int.

int multiplicacion(int num1, int num2) {
  return num1 * num2;
}

// Funcion con parametros que retorna un float.

float division(float num1, float num2) {
  return num1 / num2;
}

// Funcion que retorna un char.

char primerCaracter(char *cadena) {
  return cadena[0];
}

// Variables Globales y Locales
// Variables Globales: Las variables globales se definen fuera de cualquier función y son accesibles desde cualquier función en el archivo.

char saludo[] = "Hola mundo";

// Variables loclaes: Las variables locales se definen dentro de una función y solo son accesibles dentro de esa función.

void saludar() {
  char saludoLocal[] = "Hola que ase";
  printf("Variable local: '%s'\n", saludoLocal);
}

// Extra ==================

void funcionExtra(char* cadena1, char* cadena2) {
  int contador = 0;
  for (int i=1; i <= 100; i++) {
    if(i % 3 == 0 && i % 5 == 0) {
      printf("%s%s\n", cadena1, cadena2);
    }
    else if (i % 5 == 0) {
      printf("%s\n", cadena2);
    }
    else if (i % 3 == 0) {
      printf("%s\n", cadena1);
    }
    else {
      printf("%i\n", i);
      contador++;
    }
  }
  printf("Numero de numeros: %i\n", contador);

}

/* =============================================================== */
int main() { // Esta funcion es la base de C y a partir de aqui es donde empieza el desarrollo del sistema.
// Dentro de main no se pueden crear funciones solo se pueden invocar.

texto();
imprimeNumero(10);
sumaNumeros(5,8);

printf("El resultado de multiplicar 5 * 3 es: %d.\n", multiplicacion(5,3));
// Se puede almacenar el resultado tb en una variable.

int resultadoMultplicacion = multiplicacion(10, 3);
printf("El resultado de multiplicar 10 * 3 es: %d.\n", resultadoMultplicacion);

printf("El resultado de la división 123 entre 23 es: %.4f\n", division(123,23));

printf("El primer caractér de 'Hola' es: %c.\n", primerCaracter("Hola"));

printf("Variable global: '%s'\n", saludo);
saludar();

// Extra ==============
funcionExtra("hola", "mundo");

return 0;
}
