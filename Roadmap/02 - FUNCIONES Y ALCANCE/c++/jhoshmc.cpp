#include <iostream>
#include <string.h>
using namespace std;
const string variable_global = "hola, soy global";
// declaraciones de funciones
void hi(); // funcion sin parametro ni rotorno
void saludar(string nombre); // funcion con 1 parametro y sin retorno
void presentar(string, string); // funcion con 2 parametros y sin retorno
int suma_entera(int, int); // funcion con 2 parametros y con retorno
void funcion_anidada(int); // funcion que dependiendo el nuemro llama a una funcion o otra
int ejercicio_extra(string, string);
//* funcion principal
int main(){
  const string variable_local = "hola, soy local";
  int contador;
  hi();
  saludar("lucho");
  presentar("juan", "ana");
  cout << "la suma es " << suma_entera(4, 6)<<endl;
  funcion_anidada(2);
  cout << variable_local << " solo puedo ser llamada en mi scope,( mi entorno aislado)" << endl;
  contador = ejercicio_extra("biz","buzz");
  cout << "numero de veces que no se escribio un texto: " << contador<<endl;
  return 0;
}

//* desarrollo de las funciones declaradas
void hi(){
  cout << "hi, welcome to the jungle"<<endl;
  cout << variable_global << " me puede llamar en culaquier parte del codigo \t no rengo restincciones de scope ( entorno) :v"<<endl;
}

void saludar(string nombre){
  cout << "hola  "<<nombre << endl;
}

void presentar(string nombre_1, string nombre_2){
  cout << "hola " << nombre_1 << ", te presento a " << nombre_2 << endl;
}

int suma_entera(int n_1, int n_2){
  return n_1 + n_2;
}

void funcion_anidada(int numero){
  // funcion lambda
  auto dividir = [&]()
  {
    return numero / 2;
  };
  cout << "la divicion es: " << dividir() << endl;
}

int ejercicio_extra(string biz, string buzz){

  int contador = 0;
  for (int i=1; i <=100; i++)
  {
    if (i % 15 == 0)
    {
      cout << i<<" " << biz << " " << buzz << endl;
    }else if (i % 5 == 0)
    {
      cout<<i<<" " << buzz << endl;
    }else if ( i % 3 == 0)
    {
      cout<<i <<" "<< biz << endl;
    }else{
      contador++;
    }
    
    
  }

  return contador;
}