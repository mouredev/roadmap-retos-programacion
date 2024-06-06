#include <iostream>
#include <math.h>

using namespace std;

// Función sin parámetros ni retorno
void greet(){
  cout << "Hi!" << endl;
}

// Función con parámetros sin retorno
void greetPerson(string name){
  cout << "Hello " << name << endl;
}

// Función con varios parámetros sin retorno
void add(int numberA, int numberB){
  cout << numberA << " + " << numberB << " = " << numberA + numberB<< endl;
}

// Función con varios parámetros con retorno
int subtract(int numberA, int numberB){
  return numberA - numberB;
}

// Función sin parámetros con retorno
string languageName(){
  return "C++";
}

// Función lambda
auto mult = [](int numberA, int numberB) -> int{
  return numberA * numberB;
};

// Función con parámetros variables
template<typename... Args>
double average(Args... args) {
    int sum = 0;
    // Procesar cada argumento
    ((sum += args), ...);
    return (static_cast<double> (sum))/sizeof...(Args);
}

/**
 * En C++ no se puede declarar una función dentro de otra,
 * pero si se puede crear una lambda dentro de una 
 * función normal
*/
int exteriorFunction(int x){
  // Función lambda
  auto interiorFunction = [](int y){
    return y * 2;
  };
  int result = x + interiorFunction(x);
  return result;
}

// Uso de funciones nativas
int exponentiate(int number, int base) {
  return pow(number, base);
}


// Variable global
string global = "Soy global";

void myFunction() {
  // Variable local
  string local = "Soy local";
  cout << "Accediendo a la variable global dentro de la funcion: " << global << endl;
  cout << "Accediendo a la variable local dentro de la funcion: " << local << endl;
  cout << "Fin de la funcion" << endl;
}

class LocalVariableAccessException : public exception {
public:
    const char* what() const noexcept override {
        return "Error: Acceso a variable local fuera de su ambito.";
    }
};

/**
 * EXTRA
*/

int printNumbers(string text1, string text2) {
  int printed_numbers = 0;
  for (int number = 1; number <= 100; number++) {
    if ((number % 3 == 0) && (number % 5 == 0)) {
      cout << text1 << " y " << text2 << endl;
    } else if (number % 3 == 0) {
      cout << text1 << endl;
    } else if (number % 5 == 0) {
      cout << text2 << endl;
    } else {
      cout << number << endl;
      printed_numbers += 1;
    }
  }
  return printed_numbers;
}

int main(){
  greet();
  greetPerson("Cesar");
  add(5, 8);
  cout << "175 - 123 = " << subtract(175, 123) << endl;
  cout << "5 * 8 = " << mult(5, 8) << endl;
  cout << "Promedio de 6, 4, 7 y 8 = " << average(6, 4, 7, 8) << endl;
  cout << "Promedio de 5, 2, 6, 8 y 9 = " << average(5, 2, 6, 8, 9) << endl;
  cout << "2 ^ 8 = " << exponentiate(2, 8) << endl;
  cout << "5 + (5 * 2) = " << exteriorFunction(5) << endl;
  cout << "Esto fue programado en " << languageName() << endl;
  myFunction();
  cout << "Accediendo a la variable global fuera de la funcion: " << global << endl;
  try{
    cout << "Accediendo a la variable local fuera de la funcion: " << endl;
    throw LocalVariableAccessException();
  } catch (const LocalVariableAccessException& err) {
    cerr << err.what() << endl;
  }

  cout << "EXTRA" << endl;
  int prints = printNumbers("Multiplo de 3", "Multiplo de 5 ");
  cout << "Numeros impresos: " << prints << endl;
  return 0;
} 