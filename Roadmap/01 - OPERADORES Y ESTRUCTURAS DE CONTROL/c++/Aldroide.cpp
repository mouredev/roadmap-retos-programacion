//Operadores y extructuras de control
// Ejercicio crea ehemplos utilizando los tipos de operadores en tu lenguaje
// Aritmetico, lógicos, comparativos, asignación, identidad, pertenencia, bits.

#include <iostream>
#include <conio.h>

using namespace std;


int main(){
    // Ejemplos de operadores de asignación
    cout<<"Operadores de asignación"<<endl;
    int var =20;
    cout<<"Operador de asignación var = 20, "<<var<<endl;
    var +=5;
    cout<<"Suma 5 a la variable  var += 5, "<<var<<endl;
    var -= 10;
    cout<<"Resta 10 a la variable var -= 10, "<<var<<endl;
    var *= 2;
    cout<<"Multiplica 2 a la variable var *= 10, "<<var<<endl;
    var /= 5;    
    cout<<"Divide entre 5 a la variable var /= 5, "<<var<<endl;
    var %= 2;
    cout<<"Modulo entre 2 a la variable var = 2, "<<var<<endl;

     // Ejemplos de operadores aritmeticos
    cout<<"Operadores aritmeticos"<<endl;
    var = 10;
    cout<<"operador Signo negativo: "<< -var<<endl;
    cout<<"operador Incremento: "<< ++var<<endl;
    cout<<"operador Decremento: "<< --var<<endl;
    cout<<"operador Suma: 2 + 3 = "<< 2 + 3<<endl;
    cout<<"operador Resta: 3 - 2 = "<< 3 - 2<<endl;
    cout<<"operador Multiplicacion: 10 * 5 = "<< 10 * 5<<endl;
    cout<<"operador Division: 24 / 6 = "<< 24 / 6<<endl;
    cout<<"operador  Modulo: 30 % 11 = "<< 30 % 11<<endl;

    // Ejemplos de operadores relacionales
    cout<<endl<<"Operadores relacionales"<<endl;
    int a=10, b=20;
    cout<<"resultado a<b: "<<(a<b)<<endl;
    cout<<"resultado a>b: "<<(a>b)<<endl;
    cout<<"resultado de igualdad a==b: "<<(a==b)<<endl;
    cout<<"resultado de desigualdad a!=b: "<<(a!=b)<<endl;
    cout<<"resultado de mayor o igual que a>=b:"<<(a>=b)<<endl;
    cout<<"resultado de menor o igual que a<=b: "<<(a<=b)<<endl;

    // Ejemplos de operadores lógicos
    cout<<endl<<"Operadores lógicos"<<endl;
    a = 13;

    cout<<"AND a > 5 && a < 15: "<<(a > 5 && a < 15)<<endl;
    cout<<"OR a > 5 || a < 15: "<<(a > 5 || a < 15)<<endl;
    cout<<"NOT !(a > 5 && a < 15): "<< (!(a > 5 && a < 15)) <<endl;

// If and Else
    cout<<endl<<"Condicional if-else a>b"<<endl;
    if(a>b){
        cout<<"a es mayor que b"<<endl;
    }
    else{
        cout<<"a es menor que b"<<endl;
    }

// switch case
    cout<<endl<<"Switch Case"<<endl;
    int option = 2;
    switch (option)
    {
    case 1:
        cout<<"Realizar acción 1"<<endl;
        break;
    case 2:
        cout<<"Realizar acción 2"<<endl;
        break;    
    default:
        cout<<"No hay mas acciones"<<endl;
        break;
    }
    

    // for
    cout<<endl<<"Estructura for"<<endl;
    for(int i=0; i<=10;i++)
        cout<<i<<" ";

    // do While
    cout<<endl<<"Estructura do while"<<endl;
    do
    {
        cout<<"Ingresar 1 para salir"<<endl;
        cin>>option;
    } while (option!=1);
    

    // While
    cout<<endl<<"estructura while"<<endl;
    int c=1;
    while(c<=10){
        cout<<c<<" ";
        c++;
    }


// Dificultad Extra
    cout<<endl<<"Dificultad extra"<<endl;
    for (int i=1; i<=25; i++)
        if(i!=16 && i%2 ==0 && i%3 != 0)
            cout<<i<<" ";
    
    getch();
    return 0;
}