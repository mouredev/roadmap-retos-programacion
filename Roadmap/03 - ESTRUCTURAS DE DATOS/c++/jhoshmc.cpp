#include <iostream>
#include <vector>
#include <algorithm> // necesario para remove
using namespace std;

//* estructura 
/*
 una estructura es  es un tipo compuesto definido por el usuario. Se compone de campos o 
 de miembros que pueden tener diferentes tipos.
*/
struct PERSONA{  // nombre de la estructura(declarando la estructura)
// declarando los tipos de campos 
  int edad;
  string name;
  string last_name;
}miembros_de_la_familia; // definir el objeto de la estructura

//* Prototipos de funciones
void insert_Sort(vector<int>); // funcion de ordenmiento por inserción
void imprimir_vector(vector<int>);
void burbuja_simple(vector<int>); // fucion de ordeanmeinto por burbuja simple
void eliminar_por_posicion(vector<int> &, int);
void eliminar_por_valor(vector<int> &, int);

int main(){
  
  struct PERSONA hermana; // declarando una estructura al estilo C
  // ingresando los valores
  hermana.edad = 23;
  hermana.name = "berenice";
  hermana.last_name = " Morales Zapata";

  // cout << "hemana: " << hermana.name <<hermana.last_name<<" "<<hermana.edad<< endl;
  // Declarando estructuras al estilo c++
  PERSONA hermano = {14, "Matias", "Morales Zapata"};
  PERSONA papa = {40, "Pedro", "Morales"};
  PERSONA mama = {41, "Ana", "Zapata"};

  // cout << "hermano: " << hermano.name << " " << hermano.last_name << " edad: " << hermano.edad << endl;
  // cout << "papá: " << papa.name << " " << papa.last_name << " edad: " << papa.last_name << endl;
  // cout << "mama: " << mama.name << " " << mama.last_name << " edad: " << mama.edad << endl;

  vector<int> numeros = {2,5,3,7,1};
  // insert_Sort(numeros);
  // cout<<"vector original "<<endl;
  // imprimir_vector(numeros);
  // cout << "ordenaminto por burbuja simple: " << endl;
  // burbuja_simple(numeros);
  vector<int> numeros_2 = {4, 2, 9, 8, 5, 3};
  imprimir_vector(numeros_2);
  numeros_2.push_back(10); // se inserta un nuevo numeroal final del vector
  imprimir_vector(numeros_2);
  eliminar_por_posicion(numeros_2,3);
  eliminar_por_valor(numeros_2,5);

  //* begin() da el inicio del iterador, 0, el prinicipio, end() da el final , tamaño n
  numeros_2.insert((numeros_2.begin() + 3), 7);
  imprimir_vector(numeros_2);

  return 0;
}
void imprimir_vector(vector<int> numeros){
  for (int i = 0; i < numeros.size(); i++)
 {
   cout << numeros[i]<<", ";
 }
 cout << endl;
}

void insert_Sort(vector<int> numeros){
  /*
  * Pseudocodigo:
  * for j=1 hasta (tamaño) hacer
  *   key = vec[j]
  *   i= j-1
  *   while i>= 0 && vec[i]> key
  *     vec[i+1]= vec[i]
  *     i= i-1
  *   vec[i+1] = key 
  */
  int key;
  int i;
  for (int j = 1; j < numeros.size(); j++)
  {
     key = numeros[j];
     i = j - 1;
     while (i>= 0 && numeros[i]>key)
     {
       numeros[i + 1] = numeros[i];
       i = i - 1;
     }
     numeros[i + 1]= key;
 }

 imprimir_vector(numeros);
}

void burbuja_simple(vector<int> vec){

  /*
  *Pseudocodigo
  para i desde 0 hasta n-1 hacer
    para j desde 0 hasta n-i-1
     si vec[j] > vec[j+1] entonces
      intercambiar vec[j] y vec[j+1]
      fin_si
    fin_para
  fin_para
  */
  int aux=0;

  for (int i = 0; i < (vec.size()-1); i++)
  {
    for (int j = 0; j < (vec.size()-i-1); j++)
    {
      if (vec[j] > vec[j+1])
      {
        aux = vec[j];
        vec[j] = vec[j+1];
        vec[j+1] = aux;
      }
      
    }
 }

 imprimir_vector(vec);
}

void eliminar_por_posicion(vector<int>& vec, int pos){
   //* eliminar por un número por posición.
   //* estoy pasando el vector por referencia, asi que afecta al que fue creado en main
  vector<int>::iterator it = vec.begin() + pos;
  vec.erase(it);
  // *eliminando el valor de la posiicon ingresada
  imprimir_vector(vec);
}

void eliminar_por_valor(vector<int>& vec, int valor){
  //* eliminar por valor
  vec.erase(remove(vec.begin(), vec.end(), valor), vec.end());
  //* eliminando el valor ingresado
  imprimir_vector(vec);
}