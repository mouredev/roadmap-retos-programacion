/*
! EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
*/
/*
? sintaxis de una clase
* pareja(identificador o nombre de la clase )
class Pareja{ 
  *atributos (datos)
  int contador=0
  string nombre

  *especificador de acceso(opcional)
  *(public: accesibles desde cualquier lugar donde el objeto al que pertenece sea visible)
  *(private: solo son accesibles desde dentro de la clase )
  *(protected: miembros protegidos, solo pueden ser vistos por los demas miembros de la clase y de sus clases hijas o derivadas)
  public: 
  * metodos (funciones)
  string getNombre(){
    return nombre
  }
  int getContador(){
    return contador
  }
}
*/
#include<iostream>
#include<string>
#include<stack>
#include<vector>
#include<stdlib.h>

using namespace std;

class Mamifero{ 
  private:
    string especie;
    string nombre;
    int edad;
  public:
    Mamifero(string _especie,string _nombre,int _edad){
      especie = _especie;
      nombre = _nombre;
      edad = _edad;
    }
    void saludar(){
      if(especie == "humano"){
        cout << "\nhola me llamo " << nombre << " tengo " << edad << " años, mucho gusto" << endl;
      }else{

        cout << "\nme llamo " << nombre << " saludo dando la pata" << endl;
      }
    }
};
class Pila{
  private:
    vector<int> numeros;
    

  public:
    Pila(){
    }
    //* ver si la pila está vacia: true: vacia, false: tiene elementos
    bool empty(){
      return numeros.empty();
    }
    //* agregar elementos a la pila
    void push(int elemento){
      numeros.push_back(elemento);
    }
    //* devuelve el tamaño de la pila:
    int size(){
      return numeros.size();
    }
    //* eliminar el ultimo elemento de la pila y retornarlo
    int pop(){
      if(!numeros.empty()){

        int val = numeros.back();
        numeros.pop_back();
        return val;
      };
    }
    //* mostrar elementos de la pila
    void print(){
      if(!numeros.empty()){

        cout << "\n";
        for (int i = (numeros.size() -1); i >=0; i--)
        {
          cout << numeros[i] << " -> ";
        }
        cout << " Null\n";
      }else{
        cout << "\n la pila esta vacia" << endl;
      }
    }
    //* mostrar el ultimo elemento de la pila sin eliminarlo
    int end(){
      if(!numeros.empty()){

        return numeros[numeros.size() - 1];
      }
    }

};
class Cola{
  private:
    vector<int> numeros;
  public:
    Cola() {};
    //* ver si la cola esta vacia, true: vacia, false: tiene elementos
    bool empty() {
      return numeros.empty();
    };
    //* agregar elemento al final de la cola
    void push(int elemento) {
      numeros.push_back(elemento);
    };
    //* retornar el tamaño de la cola
    int size() {
      return numeros.size();
    };
    //* eliminar el primer elemento de la cola y retornarlo
    int pop() {
      if(!numeros.empty()){
        int var = numeros[0];
        numeros.erase(numeros.begin());
        return var;
      }
    };
    //* mostrar el primer elemento sin eliminarlo
    int front() {
      if(!numeros.empty()){
        return numeros[0];
      }
    };
    //* mostrar cola
    void print(){
      if(!numeros.empty()){
        cout << "\n";
        for (size_t i = 0; i < numeros.size(); i++)
        {
          cout<<numeros[i] << " <- ";
        }
        cout << " Null\n";
      }else{
        cout << "no hay elementos en la cola" << endl;
      }
    }
};
void ejercicio();
void extraPila();
void extraCola();
int main(){

  ejercicio();
  extraPila();
  extraCola();
  return 0;
}

void ejercicio(){
  //*creando objetos
  Mamifero miguel("humano", "miguel", 20);
  Mamifero chester("canina", "chester", 3);
  Mamifero laila("canina", "laila", 2);
  Mamifero lita("filina", "lita", 1);
  miguel.saludar();
  chester.saludar();
  laila.saludar();
  lita.saludar();
}

/*
 ! DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
*/

void extraPila(){
  Pila ePila;
  cout << "la pila esta vacia?: " << ePila.empty() << endl;
  cout << "agregando elementos a la pila: "<<endl;
  ePila.push(1);
  ePila.push(2);
  ePila.push(3);
  cout << "tamaño de la pila: " << ePila.size() << endl;
  cout << "mostrando pila: " << endl;
  ePila.print();
  cout << "mostrando ultimo elemento de la pila: " << ePila.end() << endl;
  cout << "eliminado ultimo elemento de la pila: " << ePila.pop() << endl;
  ePila.print();
  cout << "eliminado ultimo elemento de la pila: " << ePila.pop() << endl;
  ePila.print();
  cout << "eliminado ultimo elemento de la pila: " << ePila.pop() << endl;
  ePila.print();
  cout << "eliminado ultimo elemento de la pila: " << ePila.pop() << endl;
}
void extraCola(){
  Cola eCola;
  cout << "la cola esta vacia?: "<<eCola.empty() << endl;
  cout << "ingresando elementos a la cola: " << endl;
  eCola.push(1);
  eCola.push(2);
  eCola.push(3);
  cout << "tamaño de la cola: " << eCola.size() << endl;
  cout << "mostrando el primer elemento en la cola: " << eCola.front() << endl;
  cout << "mostrando cola: " << endl;
  eCola.print();
  cout << "sacando el primer elemento en la cola: " << eCola.pop() << endl;
  eCola.print();
  cout << "sacando el primer elemento en la cola: " << eCola.pop() << endl;
  eCola.print();
  cout << "sacando el primer elemento en la cola: " << eCola.pop() << endl;
  eCola.print();
}