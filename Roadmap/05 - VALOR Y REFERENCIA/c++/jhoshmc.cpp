/*
 ! EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
*/

#include <iostream>
#include <tuple> 


void f_valor(int);
void f_referencia(int &);
//*------------ extra-------------
std::tuple<int,int> intercambiar_valor(int, int);
std::tuple<int,int> intercambiar_referencia(int&, int&);
void extra();

using namespace std;


int main(){
  
  // int numero = 2;
  // cout << "numero original: " << numero << endl;
  // f_valor(numero);
  // cout << "\n variable numero original: " << numero << endl;
  // f_referencia(numero);
  // cout << "\n variable texto original: " << numero << endl;
  // cout << "\n";

  
  extra();
  return 0;
}



void f_valor(int numero){
  /*
  * cuando se pasa una variable por valor, se pasa una copia del valor de esa variable
  * en este caso se pasa un string, dicho, se podria modificar, pero los cambios solo
  * se arian a la copia pasada, la variable original, segira tal y como fue declarada
  * en su scope
  */
  cout << "\nnumero pasado por valor: " << numero << endl;
  numero = 5;
  cout << "numero cambiado (por valor): " << numero << endl;
}

void f_referencia(int& numero){
  /*
  *cuando se pasa una variable por referencia, se está pasando la direccion de memoria 
  * donde está guardada esa variable, si se modifica , se estaria cambiando el valor 
  * de la variable original
  */
  cout << "\nnumero pasado por referencia: " << numero << endl;
  numero = 10;
  cout << "numero cambiado (por referencia): " << numero << endl;
}

/*
 ! DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
*/
void extra(){
  int p_1 = 2;
  int P_2 = 4;
  cout << "valor original de p_1: " << p_1 << endl;
  cout << "valor original de p_2: " << P_2 << endl;
  cout << "\n pasando valores por valor: " << endl;
  auto [copia_p_1, copia_p_2] = intercambiar_valor(p_1, P_2);
  cout << "el valor de la copia p_1: " << copia_p_1 << endl;
  cout << "el valor de la copia p_2: " << copia_p_2 << endl;
  cout << "\n pasando valores por referencia: " << endl;
  auto [ref_p1, ref_p2] = intercambiar_referencia(p_1, P_2);
  cout << " el valor por referencia de ref_1: " << ref_p1 << endl;
  cout << "el valor por referencia de ref_2: " << ref_p2 << endl;
  cout << "\n los valores de las variables originales: " << endl;
  cout << "valor de p_1: " << p_1 << endl;
  cout << "valor de p_2: " << P_2 << endl;
}

std::tuple<int,int>intercambiar_valor(int p_1,int p_2){

  int aux = p_1;
  p_1 = p_2;
  p_2 = aux;
  return std::make_tuple(p_1,p_2);
}

std::tuple<int,int> intercambiar_referencia(int& p_1, int& p_2){
  
  int aux = p_1;
  p_1 = p_2;
  p_2 = aux;
  return {p_1, p_2};
}