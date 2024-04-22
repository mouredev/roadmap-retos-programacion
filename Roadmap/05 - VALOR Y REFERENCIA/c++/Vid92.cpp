#include <iostream>
#include <vector>

using namespace std;


void funcionValor(int dato){
    int nuevo = 35;
    dato = nuevo;
}

void funcionReferencia(int &dato){
    int nuevo = 20;
    dato = nuevo;
}

vector<int> cambioValor(int a, int b){
    int tmp = a;
    a = b;
    b = tmp;
    
    vector <int> temporal = { a, b };
    
    return temporal;
}


vector<int> cambioReferencia(int &a,int &b){ 
    int tmp = a;
    a = b;
    b = tmp;
    
    vector <int> temporal = { a, b };
    
    return temporal;
}


int main()
{
    cout<<"--------------------Variables por Valor-----------------"<<endl;
    int x = 5;
    int y = x;
    
    cout<<"Valor de x = "<<x<<endl;
    cout<<"Valor de y = "<<y<<endl;
    cout<<"Suma de (x + y) = "<<(x+y)<<endl;
    
    y = 10;
    cout<<"Valor de x al modificar y = "<<x<<endl;
    cout<<"Nuevo valor de y = "<<y<<endl;
    cout<<"Suma de (x + y) = "<<(x+y)<<endl;
    
    cout<<endl<<"-------------Variables por Referencia------------"<<endl;
    int i = 5;
	int &j = i;
	cout<<"El valor de i: "<<i<<endl;
	cout<<"El valor de j: "<<j<<endl;
	cout<<"Suma de (i + j) = "<<(i+j)<<endl;
	
	j = 10;
	cout<<"El valor de i al modificar j: "<<i<<endl;
	cout<<"El nuevo valor de j: "<<j<<endl;
	cout<<"Suma de (i + j) = "<<(i+j)<<endl;
    
    cout<<endl<<"-------------Funciones por Valor----------------"<<endl<<endl;
    int value = 15;
    cout<<"Valor de value antes de funcionValor: "<<value<<endl;
    funcionValor(value);
    cout<<"Valor de value despues de funcionValor: "<<value<<endl;
    
    
    
    cout<<endl<<"-----------Funciones por Referencia--------------"<<endl<<endl;
    int num = 10;
    cout<<"Valor de num antes de funcionReferencia: "<<num<<endl;
    funcionReferencia(num);
    cout<<"Valor num despues de funcionReferencia: "<<num<<endl;
    
    
    //Ejercicio extra
    int a = 10;
    int b = 20;
    
    
    vector<int> resultadoValor = cambioValor(a,b);
    int c = resultadoValor[0];
    int d = resultadoValor[1];
    
    cout<<endl<<"---------------------Valor-------------------"<<endl;
    cout<<"Valor de A: "<<a<<endl;
    cout<<"Valor de B: "<<b<<endl;
    cout<<"Valor de C: "<<c<<endl;
    cout<<"Valor de D: "<<d<<endl;
    
    
    
    vector<int> resultadoReferencia = cambioReferencia(a, b);
    int &e = resultadoReferencia[0];
    int &f = resultadoReferencia[1];
  
    cout<<endl<<"---------------------Referencia-----------------"<<endl;
    cout<<"Valor de A: "<<a<<endl;
    cout<<"Valor de B: "<<b<<endl;
    cout<<"Valor de E: "<<e<<endl;
    cout<<"Valor de F: "<<f<<endl;
    
    return 0;
}
