#include <iostream>
using namespace std;

int n = 0;
int a = 0;
int b = 1;

int imprimeNumeros(int inicio){
    if(inicio==0){
        cout<<inicio<<endl;
        return 0;
    }
    else
        cout<<inicio<<", ";
    return imprimeNumeros(inicio-1);
}


int factorial(int numero){
    if(numero<0){
        cout<<endl<<"Factorial - Numero negativo, no valido!"<<endl;
        return 0;
    }
    if(numero==0)
        return 1;
    else
        return numero * factorial(numero-1);
}

int fibonacci(int pos){
    if(pos<0){
        cout<<"Fibonacci, Posicion no valida!"<<endl;
        return 0;
    }
    if(pos==1)
        return n;
    
    n = a + b;
    b = a;
    a = n;
    return fibonacci(pos-1);
}

int main()
{
    //Ejercicio
    imprimeNumeros(100);
    
    //Extra
    int fact = 8;   
    int resultado = factorial(fact);
    if(fact>=0)
        cout<<endl<<"El Factorial de "<<fact<<" es: "<<resultado<<endl;
    
    int fibo = 11;
    int fib = fibonacci(fibo);
    if (fibo >0)
        cout<<"El valor fibonacci de "<<fibo<<" es: "<<fib<<endl;
    return 0;
}
