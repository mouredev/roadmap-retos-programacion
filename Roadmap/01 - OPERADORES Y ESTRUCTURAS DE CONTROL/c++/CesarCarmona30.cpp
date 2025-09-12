#include <iostream>
#include <stdexcept> 
#include <typeinfo>
using namespace std;

int main(int argc, char const *argv[]) {
  // Operadores Aritméticos
  cout << "(+)Suma: 8 + 5 = " << 8 + 5 << endl;
  cout << "(-)Resta: 8 - 5 = " << 8 - 5 << endl;
  cout << "(*)Multiplicacion: 8 * 5 = " << 8 * 5 << endl;
  cout << "(/, si uno de los datos es float o se convierte a float)Division: 8 / 5 = " << (float) 8 / 5 << endl;
  cout << "(/)Division entera: 8 / 5 = " << 8 / 5 << endl;
  cout << "(%)Modulo: 8 % 5 = " << 8 % 5 << endl;
  int a = 5, b, c;
  b = ++a;
  cout << "(++n)Pre-incremento: a = 5, b = ++a " << "(a: " <<  a << ", b: " << b << ')' << endl;
  a = 5;
  c = a++;
  cout << "(n++)Pos-incremento: a = 5, c = a++ " << "(a: " <<  a << ", c: " << c << ')' << endl;
  a = 10;
  b = --a;
  cout << "(--n)Pre-decremento: a = 10, b = --a " << "(a: " <<  a << ", b: " << b << ')' << endl;
  a = 10;
  c = a--;
  cout << "(n--)Pos-decremento: a = 10, c = a-- " << "(a: " <<  a << ", c: " << c << ')' << endl;
  
  // Operador Ternario
  cout << "Expresion a evaluar ? resultado si es verdadero : Resultado si es falso" << endl;
  cout << "5 > 10 ? \"Verdadero\" : \"Falso\" = " << (5 > 10 ? "Verdadero" : "Falso") << endl;

  // Operadores Lógicos
  cout << "AND (&&):" << endl;
  cout << "true && true = " << (true && true ? "true" : "false") << endl;
  cout << "true && false = " << (true && false ? "true" : "false") << endl;
  cout << "false && false = " << (false && false ? "true" : "false") << endl;
  cout << "OR (||):" << endl;
  cout << "true || true = " << (true || true ? "true" : "false") << endl;
  cout << "true || false = " << (true || false ? "true" : "false") << endl;
  cout << "false || false = " << (false || false ? "true" : "false") << endl;
  cout << "NOT (!):" << endl;
  cout << "!true = " << (!true ? "true" : "false") << endl;
  cout << "!false = " << (!false ? "true" : "false") << endl;
  
  //Operadores de Comparación
  cout << "Igualdad: 15 == 5 es " << (15 == 5 ? "true" : "false") << endl;
  cout << "Desigualdad: 15 != 5 es " << (15 != 5 ? "true" : "false") << endl;
  cout << "Mayor que: 15 > 5 es " << (15 > 5 ? "true" : "false") << endl;
  cout << "Menor que: 15 < 5 es " << (15 < 5 ? "true" : "false") << endl;
  cout << "Mayor o igual que: 15 >= 155 es " << (15 >= 155 ? "true" : "false") << endl;
  cout << "Menor o igual que: 155 <= 155 es " << (155 <= 155 ? "true" : "false") << endl;

  //Operadores de Asignación
  int number = 50;
  cout << "Asignacion: numero = " << number << endl;
  number += 1;
  cout << "Suma y asignacion: numero += 1 " << '(' << number << ')' << endl;
  number -= 3;
  cout << "Resta y asignacion: numero -= 3 " << '(' << number << ')' << endl;
  number *= 3;
  cout << "Division y asignacion: numero *= 3 " << '(' << number << ')' << endl;
  number /= 4;
  cout << "Multiplicacion y asignacion: numero /= 4 " << '(' << number << ')' << endl;
  number %= 5;
  cout << "Modulo y asignacion: numero %= 5 " << '(' << number << ')' << endl;

  //Operadores bit a bit
  cout << "AND: 10 & 12 = " << (10 & 12) << endl;
  cout << "OR: 10 | 12 = " << (10 | 12) << endl;
  cout << "XOR: 10 ^ 12 = " << (10 ^ 12) << endl;
  cout << "NOT: ~12 = " << (~2) << endl;
  cout << "Desplazamiento a la derecha: 10 >> 2 = " << (10 >> 2) << endl;
  cout << "Desplazamiento a la izquierda: 10 << 2 = " << (10 << 2) << endl;
  
  //Condicionales
  string mi_lenguaje = "C++";
  cout << "Ejecutando estructura if: " << endl;
  if (mi_lenguaje == "JavaScript") {
    cout << "Estoy programando en JavaScript" << endl;
  } else if (mi_lenguaje == "Python") {
    cout << "Estoy programando en Python" << endl;
  } else {
    cout << "Estoy programando en " << mi_lenguaje << endl;
  }

  int dia = 5;
  cout << "Ejecutando estructura switch: " << endl;
  switch (dia) {
  case 1:
    cout << "Lunes" << endl;
    break;
  case 2:
    cout << "Martes" << endl;
    break;
  case 3:
    cout << "Miercoles" << endl;
    break;
  case 4:
    cout << "Jueves" << endl;
    break;
  case 5:
    cout << "Viernes" << endl;
    break;
  case 6:
    cout << "Sabado" << endl;
    break;
  case 7:
    cout << "Domingo" << endl;
    break;          
  default:
    cout << "No existe el dia" << endl;
    break;
  }

  //Iterativas

  cout << "Ejecutando estructura for: " << endl;
  for (int i = 1; i <= 10; i++) {
    cout << i << ", ";
  }
  cout << endl;
  string name = "cesar";
  int index = 0;
  cout << "Ejecutando estructura while: " << endl;
  while (index < name.length()) {
    cout << name[index] << "-";
    index++;
  }
  cout << "Ejecutando estructura do-while: " << endl;
  string alphabet = "ABCDEFGHIJKJLMNOPQRSTUVWXYZ", text = "";
  int letter = 0;
  do {
    text += alphabet[letter];
    cout << text << endl;
    letter++;
  } while (text.length() != alphabet.length());

  // Manejo de Excepciones
  class ZeroDivisionExcept : public std::exception {
    public:
      ZeroDivisionExcept(const char* message) : errorMessage(message) {}
      virtual const char* what() const noexcept override {
        return errorMessage;
      }
    private:
      const char* errorMessage;
  };
  cout << "Ejecutando estructura try-catch" << endl;
  cout << "5 / 0 = ..." << endl;
  try {
    throw ZeroDivisionExcept("Division por cero.");
  } catch (const ZeroDivisionExcept& err) {  
    cout << "Se produjo un error de tipo: " << typeid(err).name() << endl;
    cout << err.what() << endl;
    cout << "*Nota: Recuerda que la division por cero no esta definida." << endl;
  }

  /*
    EXTRA
  */

  for (int number = 10; number <= 55; number++) {
    if ((number % 2 != 0) || (number == 16) || (number % 3 == 0)){
      continue;
    }
    cout << number << " ";
  }
  return 0;

}
