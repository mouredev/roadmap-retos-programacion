#include <iostream>
using namespace std;

void sinRet(){
    cout<<"Funcion sin parametros ni retorno"<<endl;
}

float retyPar(float a){
    return a*5.8;
}

int potencia(int a){
    return a*a;
}

int altaFun(int a, int b){
    int c = a+a;
    return c+ potencia(b);
}

int ejercicioFuncion(string a, string b){
    int s  = 0;
    for(int i=0;i<100;i++){
        if(i%3==0 && i%5 ==0){
            cout<<a<<" "<<b<<endl;
        }
        if(i%3==0){
            cout<<a<<endl;
        }
        if(i%5 ==0){
            cout<<b<<endl;
        }
        else{
            cout<<i<<endl;
            s++;
        }
        }
    return s;
    }


int main(){
     float f = retyPar(4.4);
     int af = altaFun(3,5);
     sinRet();
     cout<<"Funcion con parametro y retorno "<<f<<"\nFuncion que invoca otra funcion: "<<af<<endl;
     string a = "hola", b = "c++";
     int e = ejercicioFuncion(a,b);
     cout<<"El total de veces que aparecio el numero fue: "<<e<<endl;

return 0;}
