// Sitio web del lenguaje
// https://isocpp.org

// Comentario de línea

/*
  Esto es un comentario
  de varias líneas
*/

/**
 * Esto también es un 
 * comentario de varias
 * líneas
*/

#include <iostream>

using namespace std;

int main() {
  //variable
  int variable = 15;
  //constante
  const int constante = 20;

  // Datos primitivos
  short mi_short = 65535;         // 2 byte (16 bits)
  int mi_int = 321;               // 4 bytes (32 bits) hasta 8 bytes (64 bits)
  long mi_long = 4324;            // 8 bytes (64 bits)
  long long mi_dobleLong = 48329; // 16 bytes (128 bits)
  float mi_float = 321.4f;        // 4 bytes (32 bits)
  double mi_double = 43124.432l;  // 8 bytes (64 bits)
  bool mi_bool_ver = true;
  bool mi_bool_al = false;
  char mi_char = 'C';
  char mi_string[] = "cadena de texto";

  // Adicionalmente se pueden definir variables que solo sean positivas
  // utilizando unsigned antes del tipo de dato

  cout << "¡Hola C++!" << endl;

  return 0;
}