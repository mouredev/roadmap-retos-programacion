#include <iostream>
#include <string>

int main() {
  // Link a la web oficial de C++: https://isocpp.org/

  // Este es un comentario de una sola linea.

  /*
    Este es un comentario
    de multiples lineas.
  */

  // Esto es una variable
  int variable = 10;

  // Esta es una constante
  constexpr int constante = 5;

  // Los diferentes tipos de variables en C++
  // Entero, permite almacenar valores enteros.
  int entero = 1;

  // Double, decimal con 15 digitos de precision. Ocupa 8 bytes en memoria.
  double decimal_doble = 3.141592653589793;

  // Flotante, decimal con 7 digitos de precision. Ocupa 4 bytes en memoria.
  float decimal_flotante = 3.1415926f;

  // Caracter, almacena una sola letra o simbolo entre comillas simples.
  char caracter = 'a';

  // Booleano, almacena un valor verdadero o falso.
  bool booleano = true;

  // Cadena, almacena una cadena de texto entre comillas dobles.
  std::string cadena = "Hola";

  // Salida de texto usando libreria iostream

  std::cout << "¡Hola C++!\n";

  return 0;
}
