//* voy a poner codigo rapido, regresando de trabajar profundizo mas
#include<iostream>
#include <stdexcept> // Para excepciones estándar como invalid_argument y out_of_range
using namespace std;
void ejercicio();
void extra();
void procesarParametro(int);
int main(){
  // ejercicio();
  extra();
  return 0;
}

void ejercicio(){
  /*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
*/
  int a, b;
  float result;
  a = 10;
  b = 0;

  try{
    if (b == 0){
      throw "El divisor no puede ser 0";
    }
    result = a / b;
    cout << "resultado: " << result << endl;
  }catch(const char *error){
    cout << error << endl;
  }
  
  

}
/*
 ! DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
 
*/
//? 1. Definimos una clase de excepción personalizada
//*Creamos una clase que hereda de exception y sobreescribimos el método what() para mostrar un mensaje personalizado.
class CustomException : public exception {
public:
    const char* what() const noexcept override {
        return "soy un mensaje de una excepcion personalizada";
    }
};
//? 2. Función que puede lanzar 3 tipos de excepciones
/*
*lanza:
*invalid_argument si el valor es negativo.

*out_of_range si es mayor a 10.

*CustomException si el valor es exactamente 5 (esto es solo un ejemplo simbólico).
*/
void procesarParametro(int valor) {
    if (valor < 0) {
        throw invalid_argument("Valor no puede ser negativo.");
    } else if (valor > 10) {
        throw out_of_range("Valor excede el rango permitido (0-10).");
    } else if (valor == 5) {
        throw CustomException(); // Lanzamos nuestra excepción personalizada
    }

    // Si no hay excepción, mostrar que se procesó correctamente
    cout << "Parametro procesado correctamente: " << valor << endl;
}
//? bloque try-catch
/*
*Aquí capturamos cada excepción por tipo y mostramos el mensaje asociado usando e.what().

*También imprimimos un mensaje cuando no hay error y cuando finaliza la ejecución, para que quede claro el flujo del programa.
*/
void extra(){
  int valor;
  cout << "\ningresa un numero mayor a cero y menor a 10: ";
  cin >>valor;
  try {
        procesarParametro(valor);
        cout << "No se ha producido ningun error." << endl;
    }
    catch (const invalid_argument& e) {
        cerr << "Error: " << e.what() << endl;
    }
    catch (const out_of_range& e) {
        cerr << "Error: " << e.what() << endl;
    }
    catch (const CustomException& e) {
        cerr << "Error: " << e.what() << endl;
    }
    catch (...) {
        cerr << "Se produjo una excepcion desconocida." << endl;
    }

    cout << "La ejecucion ha finalizado.\n" << endl;

}



