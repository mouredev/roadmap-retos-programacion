#include <iostream>
#include <cmath>  
#include <ctime> 
using namespace std; 

int mis_cadenas (string cadena1, string cadena2); 



int x = 50; // declaracion de variable global
 
// funcion de tipo void, no regresa una variable
void funcion_no_ret1(){
    cout << "Esta funcion imprime solamente este mensaje." << '\n'; 
} 

/* funcion de tipo void, no regresa una variable pero toma un parametro y 
    lo imprime en pantalla. 
*/ 
void funcion_no_ret2(int numero){
    cout << "Esta funcion imprime un numero entero: " << numero << '\n';  
}

/* funcion void, que toma multiples parametros y no regresa ni uno de esos valores
solo los imprime en pantalla*/
float eq_cuadratica(float a, float b, float c){
  float equacion_1 = (-b + (sqrt(b*b) - (4 * a * c)) /  (2 * a)); 
  float equacion_2 = (-b - (sqrt(b*b) - (4 * a * c)) /  (2 * a)); 
    cout << "Esta funcion muestra el resultado de la equacion cuadratica: "   
        <<  equacion_1  << " y " << equacion_2 << '\n';   

  return equacion_1 && equacion_2;
} 
/* funcion de tipo entero(int), esta funcion si regresa los multiples parametros 
y regresa el valor de la suma a la funcion main*/
int suma(int numero1, int numero2, int numero3, int numero4){
    return numero1 + numero2 + numero3 + numero4; 
}




int main()
{
    int numero1; // variable local
    string cd1 = "multiplo de 3";
    string cd2 = "multiplo de 5"; 
    funcion_no_ret1(); // llamada de un parametro
    cout << '\n';  
    funcion_no_ret2(5); 
    cout << '\n'; 
    eq_cuadratica(5, 4, 10);
    cout << '\n';  

    numero1 = 35; 
    cout <<"El resultado de la suma es: " << suma(10, numero1, 27, x) << '\n'; 
    // x es una variable global y numero1 local
    cout << '\n'; 
    cout << "Ejercicio extra: "; 
    cout << mis_cadenas(cd1, cd2); 

    return 0; 
}

int mis_cadenas(string cadena1, string cadena2){
    int veces = 0;
    for (int i = 1; i < 100; i++){
        if (i % 3 == 0 && i % 5 == 0){ 
            cout << cadena1 << " y " << cadena2  << '\n';
        }
        else if (i % 3 == 0) { 
            cout << cadena1 << '\n'; 
            
        }
        else if (i % 5 == 0){
            cout << cadena2 << '\n'; 
        } 
        else{
            cout << i << '\n';
            veces++;  // si las condiciones de arriba no aplican, la variable veces suma a 1, hasta que 
            // las condiciones sean 
        }

         
    }
    return veces;
}
