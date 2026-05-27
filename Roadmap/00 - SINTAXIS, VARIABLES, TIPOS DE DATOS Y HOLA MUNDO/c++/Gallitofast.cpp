// El lenguaje de c++ no tiene red oficial
// comentario de una linea
/*
comentario de varias lineas
aqui puedo decir lo que yo quiera
muchas gracias mouredev por el contenido gratuito
*/

#include <iostream>
#include <string>
using namespace std;
int main() {
  const string constante = "c++";
  string variable = "Hola, ";

  // Tipos de datos

  // hay diferentes valores numericos
  short corto = 65524; // este es de 16 bits
  int entero =
      4294967294; // este es de 32 bits o 16 bits dependiendo del compilador
  long largo = 4294967294;                  // este es de 32 bits
  long long gigante = 18446744073709551614; // este es de 64 bits
  float flotante = 3.141592;
  double doble = 3.141592653589793;
  long double giganteDoble = 1.000000000000001;
  float scientifico = 6.02E23; // el float también puede usar notación
                               // cientifica
  // cout<< corto;
  // cout<< corto;
  cout << corto << "\n";

  cout << entero << "\n";
  cout << largo << "\n";
  cout << variable + constante << "\n";

 cout<<"Hola mouredev";
}
