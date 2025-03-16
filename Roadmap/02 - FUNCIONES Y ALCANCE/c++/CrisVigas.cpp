#include <cmath>
#include <cstdint>
#include <iostream>
#include <string>

// funcion sin retorno ni parametros
static void saludo() { std::cout << "Hola!\n"; }

// funcion con 1 parametros sin retorno
static void saludo(const std::string &name) {
  std::cout << "Hola " << name << "!\n";
}

// funcion con retorno
template <typename T>
static T cuadrado(T x) {
  return x * x;
}

// es mejor no usar variables globales... pero cada loco con su tema
static int32_t variableGlobal{5};

static void accesoGlobal() {
  std::cout << "La variable global es: " << ::variableGlobal << "\n";

  // modificamos la variable global
  ::variableGlobal += 100;

  std::cout << "La variable global modificada es: " << ::variableGlobal << "\n";

  // definimos una variable local con el mismo nombre
  int32_t variableGlobal{-1000};

  std::cout << "La variable ::global es: " << ::variableGlobal << "\n";
  std::cout << "La variable global es: " << variableGlobal << "\n";

  std::cout << "Cambiamos la variable global a 0\n";
  variableGlobal = 0;
  std::cout << "La variable ::global es: " << ::variableGlobal << "\n";
  std::cout << "La variable global es: " << variableGlobal << "\n";
}

static int64_t funcionExtra(const std::string &str1, const std::string &str2) {
  int32_t contador{0};

  for (int32_t i = 1; i < 101; ++i) {
    if (((i % 3) == 0) && ((i % 5) == 0)) {
      std::cout << str1 << str2 << "\n";
    } else if ((i % 3) == 0) {
      std::cout << str1 << "\n";
    } else if ((i % 5) == 0) {
      std::cout << str2 << "\n";
    } else {
      std::cout << i << "\n";
      ++contador;
    }
  }

  return contador;
}

int main() {
  ::saludo();
  ::saludo("Desarrollador");
  std::cout << "5 al cuadrado es: " << ::cuadrado(5) << "\n";

  // No es posible definir una funcion dentro de otra
  // int foo(int bar) { return bar + 1; }
  // ...pero podemos definir una expresion lambda
  auto foo = [](const int32_t bar) { return bar + 1; };
  std::cout << "5 + 1 = " << foo(5) << "\n";

  // funciones ya creadas
  std::cout << "raiz de 25 es: " << std::sqrt(25) << "\n";

  // variables globales
  ::accesoGlobal();

  // DIFICULTAD EXTRA
  std::cout << "======= DIFICULTAD EXTRA =======\n";
  std::cout << ::funcionExtra("Fizz", "Buzz");

  return EXIT_SUCCESS;
}
