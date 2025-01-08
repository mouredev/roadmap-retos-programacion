#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int resultado = 0;          //variable global

//Funcion con retorno y 2 parametros
int suma(int num1,int num2){
    return num1 + num2;
}

//Funcion sin parametros sin retorno
void resultadoSuma(void){
    cout<<"Resultado de la funcion suma es: "<<resultado<<endl;
}

//Funcion con parametros sin retorno
void resultadoResta(int resul){
    cout<<"Resultado de la funcion resta es: "<<resul<<endl;
}

//Funcion dentro de otra funcion, y con parametros y sin retorno
void resta(int num1,int num2){
    int res = num1 - num2;
    resultadoResta(res);
}

//Ejercicio Extra
int funcionExtra(string text1,string text2){
    int count = 0;
    for(int i=1;i<101;i++){
        if((i%5==0)&&(i%3==0))
            cout<<text1<<" "<<text2<<endl;
        else if(i%3==0)
            cout<<text1<<endl;  
        else if(i%5==0)
            cout<<text2<<endl;
        else
            count+=1;
    }
    return count;
}

int main()
{   
  resultado = suma(5,4);            
  resultadoSuma();
  cout<<"Raiz cuadrada: "<<sqrt(144)<<endl;       //ejemplo de funcion ya creadas por el lenguaje
  resta(10,5);
  int solucion = funcionExtra("uno","dos");
  cout<<"Resultado del ejercicio extra es: "<<solucion<<endl;
  
  return 0;
}
