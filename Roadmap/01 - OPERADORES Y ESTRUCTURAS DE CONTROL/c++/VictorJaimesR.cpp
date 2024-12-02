#include<iostream>

using namespace std;

int main(){

//Operadores aritméticos
int suma=10+3; cout<<suma<<endl;
int resta=10-3; cout<<resta<<endl;
int multiplicacion=10*3; cout<<multiplicacion<<endl;
int a=10;
float b=3;
float division = a/b; cout<<division<<endl;
int residuo=10%3; cout<<residuo<<endl;

//Operadores de comparación 

bool igualdad=10==10; cout<<"Igualdad es: "<< igualdad<<endl;
bool diferencia=10!=3; cout<<"Diferencia es: "<< diferencia<<endl;
bool mayorque=10>3; cout<<"Mayor que es: "<< mayorque<<endl;
bool menorque=10<3; cout<<"Menor que es: "<< menorque<<endl;
bool mayor_o_igual_que=10>=3; cout<<"Mayor o igual que es: "<< mayor_o_igual_que<<endl;
bool menor_o_igual_que=10<=3; cout<<"Menor o igual que es: "<< menor_o_igual_que<<endl;

//Operadores Lógicos

bool y= 10 >= 3 && 3<=10; cout<<"y es: "<<y<<endl;
bool o= 10 >= 3 || 3<=10; cout<<"o es: "<<o<<endl;
bool no= !(10 >= 3 && 3<=10); cout<<"no es: "<<no<<endl;

//Operadores de asignación

int numero=15;
numero+=2;cout<<numero<<endl;
numero-=2;cout<<numero<<endl;
numero*=2;cout<<numero<<endl;
numero/=2;cout<<numero<<endl;
numero%=2;cout<<numero<<endl;


//Operadores de bits
numero<<=2;cout<<numero<<endl;
numero>>=2;cout<<numero<<endl;
int x=5;
int k=3;
int z= x & k;cout<<"El numero es: "<<z<<endl;
int m=x|k;cout<<"El numero es: "<<m<<endl;
int p=~x;cout<<"El numero es: "<<p<<endl;
 
//Operadores de identidad no existen en c++
//Operadores de pertenencia no existen en c++

//estructuras de control

//condicionales

string nombre="victor";

if (nombre=="victor"){
    cout<<"Mi nombre es: "<<nombre<<endl;
}
else if (nombre=="Andres")
{
    cout<<"Mi nombre es"<<nombre;
}

else{
    cout<<"Ese no es tu nombre";
}

int opcion;
cout<<"Ingrese la opcion: "; 
cin>>opcion;

switch (opcion)
{
case 1:
    cout<<"Usted escogió la opcion 1";
    break;
case 2:
    cout<<"Usted escogió la opcion 2";
    break;
case 3:
    cout<<"Usted escogió la opcion 3";
    break;
default:
    cout<<"Usted escogió una opcion incorrecta";
    break;
}

cout<<endl;
//iterativas

for (int i = 0; i < 11; i++)
{
    cout<<i<<endl;
}

int j=0;
while (j<=10)
{
    cout<<j<<endl;
    j++;
    
}


cout<<endl;

//EJERCICIO DE DIFICULTAD EXTRA
for (int ks  = 10; ks <= 55; ks++)
{
    if((ks%2==0) && !(ks%3==0) && ks!=16)
    cout<<"["<<ks<<"]";
}
/*
cout<<endl;



for (int ki = 10; ki <=55; ki++)
{
    if (!(ki%3==0) && ki!=16)
    {
       cout<<"["<<ki<<"]";
    }
    
}


*/


    return 0;
}
