#include <stdio.h>

int main()
{
  //Enteros
  int edad = 20;
  long poblacion = 8000000000;

  //Decimales
  float precio = 9.99;
  double pi = 3.14159265358979;

  //Caracteres y cadenas
  char letra = 'A';
  char nombre[] = "Johann";

  // Booleanos (requiere stdbool.h)
  #include <stdbool.h> //esto en general se lo coloca arriba
  bool activo = true;

  printf("Edad: %d\n", edad);

  printf("Pi: %.2f\n", pi);

  printf("Letra: %c\n", letra);

  printf("Nombre: %s\n",nombre);

  printf("-----------------------Mi reto-------------------------\n");

  int age = 17;
  double decimal = 2.7;
  char letter = 'J';
  char name[] = "Johann";

  printf("Edad = %d\n", age);
  printf("Decimal = %.1f\n", decimal);
  printf("Letra =  %c\n", letter);
  printf("Nombre = %s\n", name);

  return 0;
}
