// Sitio Oficial de C++: https://isocpp.org/

// Esto es un comentario de una línea

/* Y esto es un comentario
de varias líneas. */

// librería estandar de entrada y salida por terminal
#include <iostream>

// librería estandar de cadenas de texto
#include <string>

int main() {
  // una variable
  auto variable{101};

  // una constante
  const auto constante{42};

  // un valor constante en tiempo de compilación
  constexpr auto PI{3.141592653589};

  // booleano
  bool booleano{true};

  // numeros con signo
  short s{32767};
  int i{2147483647};
  long long l{9223372036854775807LL};

  float f{9.8F};
  double d{6.02E23};
  long double ld{1.000000000000001L};

  // numeros sin signo
  unsigned short us{65535U};
  unsigned int ui{4294967295U};
  unsigned long long ull{18446744073709551615ULL};

  // caracteres
  char c{'C'};

  // cadena de texto (definida en <string>)
  std::string mensaje{"Hola, C++!"};

  // para enviar variables a la salida de la terminal
  std::cout << mensaje;

  return EXIT_SUCCESS;
}
