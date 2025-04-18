/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
*/

#include <iostream>

using namespace std;

void conteoRecursivo(int);
//! ejercicio extra
void extra();
int factorialRecursivo(int);
int fibonacciRecursivo(int);

int main(){
  int numero = 100;
  conteoRecursivo(numero);
  extra();
  return 0;
}

void conteoRecursivo(int numero){
  //* este es el caso de finalizacion y finalizacion de la resurción
  if(numero == 0){
    cout << "numero: " << numero<<endl;
    return ;
  }
  if(numero > 0){
    //* se va imprimiendo el numero 
    cout << "numero: " << numero << endl;
    //* se va retornando la funcion con un número menor al ya impreso
    return conteoRecursivo(numero - 1);
    

  }
}

/*
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
*/

void extra(){
  int numeroFactorial;
  int resultadoFactorial;
  int posicionFibonacci;
  int resultadoFibonacci;
  cout << "\n\t factorial: \n";
  cout << "ingrese un numero para ver su factorial: ";
  cin >> numeroFactorial;
  resultadoFactorial = factorialRecursivo(numeroFactorial);
  cout << "el factorial del numero " << numeroFactorial << "! es: " << resultadoFactorial << endl;
  cout << "\n\t fibonacci: \n";
  cout << "ingrese la posicion fibonacci: ";
  cin >> posicionFibonacci;
  resultadoFibonacci = fibonacciRecursivo(posicionFibonacci);
  cout << "el numero fibonacci en la posicion: " << posicionFibonacci << " es : " << resultadoFibonacci << endl;
}

int factorialRecursivo(int numero){
  if(numero == 1){
    return 1;
  }
  if (numero >=1)
  {
    return numero * factorialRecursivo(numero - 1);
  }
  
}

int fibonacciRecursivo(int numero){
  if(numero == 0){
    return 0;
  }
  if(numero == 1){
    return 1;
  }

  return fibonacciRecursivo(numero - 1) + fibonacciRecursivo(numero - 2);
}