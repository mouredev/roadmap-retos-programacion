#include <iostream>
#include <ostream>
#include <string.h>
#include <string>
//02 Funciones y saludarcance
//void son funciones que no van a retornar nada
//Funcion sin parametros ni retornos
void saludar(){
  std::cout<<"Hola, funcion de saludo"<<std::endl;
}

//Funcion con parametros y retorno 
int funcion_suma(int num1,int num2){
  return num1+num2;
}

//Funciones dentro de funciones no se pueden como tal en c++ pero investigue
//y con lambdas es posible, pero todavia no exploro ese concepto

//Experimento de variable global y global
int variable_global{20};
void funcion_global_local(){
 int variable_local{30}; //Esta variable solo podria usarla en esta funcion
 std::cout<<"La variable global: "<<variable_global<<" Se puede usar donde sea, en cambio la local: "<<
    variable_local<<" Solo en esta funcion"<<std::endl;

}

int ejercicio_extra(std::string ,std::string);
//Main es una funcion que siempre se va a ejecutar y es necesaria para compilar
int main(){
  saludar();
  std::cout<<"Funcion de suma: "<<funcion_suma(2,8)<<std::endl;
  funcion_global_local();

  int contador=ejercicio_extra("Hola","Mundo");
  std::cout<<contador<<": veces no se cumplieron las condiciones"<<std::endl;

return 0;
}


int ejercicio_extra(std::string cadena_de_texto1, std::string cadena_de_Texto2){
  int contador=0;
  for (int i=1;i<=100;i++){
    if (i%5==0 && i%3==0) std::cout<<i<<" ==> "<<cadena_de_texto1<<" "<<cadena_de_Texto2<<std::endl;
    else if (i%5==0) std::cout<<i<<" ==> "<<cadena_de_Texto2<<std::endl;
    else if (i%3==0) std::cout<<i<<" ==> "<<cadena_de_texto1<<std::endl;
    else{
       std::cout<<i<<std::endl;
       contador++;
    }
  }
 return contador;
}
