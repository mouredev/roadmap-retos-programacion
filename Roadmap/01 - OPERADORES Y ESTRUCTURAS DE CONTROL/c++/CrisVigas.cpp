/**
 * ESTANDAR MINIMO C++20
 * (Se debe usar -std=c++20 con soporte para <format>)
 */

#include <bitset>
#include <cstdint>
#include <format>
#include <iostream>
#include <string>
#include <vector>

static std::string binario(const uint8_t num) {
  return std::bitset<8>(num).to_string();
}

int main() {
  constexpr int32_t a{10'000};
  constexpr int32_t b{99};
  int32_t c{10'000};

  uint8_t m{0B1001'1001};
  uint8_t n{0B1010'1100};

  std::cout << "Ejecutando Operadores Aritmeticos:\n";
  std::cout << std::format("a = {}\n", a);
  std::cout << std::format("b = {}\n", b);
  std::cout << std::format("a + b = {}\n", (a + b));
  std::cout << std::format("a - b = {}\n", (a - b));
  std::cout << std::format("a * b = {}\n", (a * b));
  std::cout << std::format("a / b = {}\n", (a / b));
  std::cout << std::format("a % b = {}\n", (a % b));

  std::cout << "\nEjecutando Operadores de Bit:\n";
  std::cout << std::format("m\t= {}\n", ::binario(m));
  std::cout << std::format("n\t= {}\n", ::binario(n));
  std::cout << std::format("m | n\t= {}\n", ::binario(m | n));
  std::cout << std::format("m & n\t= {}\n", ::binario(m & n));
  std::cout << std::format("m ^ n\t= {}\n", ::binario(m ^ n));
  std::cout << std::format("~m\t= {}\n", ::binario(~m));
  std::cout << std::format("~n\t= {}\n", ::binario(~n));
  std::cout << std::format("n << 2\t= {}\n", ::binario(n << 2));
  std::cout << std::format("n >> 3\t= {}\n", ::binario(n >> 3));

  std::cout << "\nEjecutando Operadores de Comparacion:\n";
  std::cout << std::format("a = {}, b = {}, c = {}\n", a, b, c);
  std::cout << std::format("(a == b)\t= {}\n", a == b);
  std::cout << std::format("(a == c)\t= {}\n", a == c);
  std::cout << std::format("(a != b)\t= {}\n", a != b);
  std::cout << std::format("(a != c)\t= {}\n", a != c);
  std::cout << std::format("(a < b)\t\t= {}\n", a < b);
  std::cout << std::format("(a < c)\t\t= {}\n", a < c);
  std::cout << std::format("(a > b)\t\t= {}\n", a > b);
  std::cout << std::format("(a > c)\t\t= {}\n", a > c);
  std::cout << std::format("(a <= b)\t= {}\n", a <= b);
  std::cout << std::format("(a <= c)\t= {}\n", a <= c);
  std::cout << std::format("(a >= b)\t= {}\n", a >= b);
  std::cout << std::format("(a >= c)\t= {}\n", a >= c);

  std::cout << "\nEjecutando Operadores Logicos:\n";
  std::cout << std::format("!true\t\t= {}\n", !true);
  std::cout << std::format("!false\t\t= {}\n", !false);
  std::cout << std::format("true && true\t= {}\n", true && true);
  std::cout << std::format("true && false\t= {}\n", true && false);
  std::cout << std::format("false && false\t= {}\n", false && false);
  std::cout << std::format("true || true\t= {}\n", true || true);
  std::cout << std::format("true || false\t= {}\n", true || false);
  std::cout << std::format("false || false\t= {}\n", false || false);

  std::cout << "\nEjecutando Operadores de Asignacion:\n";
  std::cout << "Creamos una variable V sin inicializar:\tint32_t v;\n";
  int32_t v;
  std::cout << std::format("v = {}\n", v);
  std::cout << "El valor de v es indeterminado y pude ser cualquier cosa.\n";
  std::cout << "Asignamos el valor 42 a la variable V:\tv = 42;\n";
  v = 42;
  std::cout << std::format("v = {}\n", v);

  std::cout << "\nEjecutando Estructuras de Control (if):\n";
  if (true) {
    std::cout << "\tDentro de un if\n";
  }

  std::cout << "\nEjecutando Estructuras de Control (if/else):\n";
  if (false) {
    std::cout << "\tAhora esto no se ejecutara\n";
  } else {
    std::cout << "\tDentro de un else con condicion falsa\n";
  }

  std::cout << "\nEjecutando Estructuras de Control (switch):\n";
  switch (b) {
    case 98:
      std::cout << "\tEl valor es 98\n";
      break;
    case 99:  // la opcion correcta
      std::cout << "\tEl valor es 99\n";
      break;
    case 100:
      std::cout << "\tEl valor es 100\n";
      break;
    default:
      std::cout << "\tEl valor no es ninguno de los anteriores\n";
      break;
  }

  std::cout << "\nEjecutando Estructuras de Control (while sin break):\n";
  while (c != 10'005) {
    std::cout << std::format("\tc = {}\n", c);
    ++c;
  }

  std::cout << "\nEjecutando Estructuras de Control (while con break):\n";
  while (true) {
    std::cout << std::format("\tc = {}\n", c);
    if (c == 10'010) {
      std::cout << "\t\tAhora se ejecutara un break que terminara el while\n";
      break;
    }
    ++c;
  }

  std::cout << "\nEjecutando Estructuras de Control (for):\n";
  for (auto i{c}; i != 10'015; ++i) {
    std::cout << std::format("\ti = {}\n", i);
  }

  std::cout << "\nEjecutando Estructuras de Control (for con break):\n";
  for (auto i{c}; true; ++i) {
    std::cout << std::format("\ti = {}\n", i);
    if (i == 10'015) {
      std::cout << "\t\tAhora se ejecutara un break que terminara el for\n";
      break;
    }
  }

  std::cout << "\nEjecutando Estructuras de Control (for con continue):\n";
  std::cout << "\tAhora nos saltaremos miles de pasos, nos vemos en el futuro";
  for (auto i{c}; i != 10'000'005; ++i) {
    if (i < 10'000'000) {
      continue;
    }

    std::cout << std::format("\ti = {}\n", i);
  }

  std::cout << "\nEjecutando Estructuras de Control (for con iterable):\n";
  std::vector<char> vec{'H', 'o', 'l', 'a', '!', '*', 'e', 'r', 'r', 'o', 'r'};
  for (const auto& element : vec) {
    if (element == '*') {
      break;
    }
    std::cout << element;
  }
  std::cout << '\n';

  std::cout << "\nEjecutando excepcion con captura definida:\n";
  try {
    std::cout << "\tIntentaremos acceder fuera de rango en un vector\n";
    auto e{vec.at(50'000)};
    std::cout << "\tEsta linea solo se ejecutara si no hubo errores.\n";
  } catch (const std::out_of_range& error) {
    std::cout << std::format("\tError: {}\n", error.what());
    std::cout << "\tYa que sabemos el tipo de error, podemos tomar medidas\n";
    auto e{vec.back()};
  }

  std::cout << "\nEjecutando excepcion con captura generica:\n";
  try {
    int32_t e{std::stoi("F")};
    std::cout << e;
  } catch (...) {
    std::cout << "\tAlgo raro ha pasado!";
  }

  // DIFICULTAD EXTRA
  std::cout << "\n== DIFICULTAD EXTRA ==\n";
  for (int32_t i{10}; i <= 55; ++i) {
    if (((i % 2) == 0) && (i != 16) && ((i % 3) != 0)) {
      std::cout << i << '\n';
    }
  }

  return EXIT_SUCCESS;
}
