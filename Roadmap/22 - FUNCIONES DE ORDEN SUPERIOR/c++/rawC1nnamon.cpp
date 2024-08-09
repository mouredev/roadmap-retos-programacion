/*
┌───────────────────────────────────┐
│  Autor: Camilo C.                 │
│  Lenguaje: C++                    │
└───────────────────────────────────┘
*/

#include <iostream>
#include <cmath>
#include <functional>

using namespace std;

/*                                          [Explicación básica]
                                           [Funciones superiores]                                      */

// Función que usa otra función como argumento con punteros:
void Q_sqrt(double (*func)(double), double value){
    cout << func(value) << endl;
}

// Función que tiene un lambda como parámetro:
void lambdaArgs(const function<int(int, int)>& func, int n1, int n2) {
    cout << func(n1, n2) << endl;
}

int main()
{
    Q_sqrt(sqrt, 5); // Se pasa como argumento sqrt que ya está definida en la biblioteca estándar de C/C++.
                     // También se debe pasar como argumento el número al que se le quiere sacar raíz. -> Devuelve 2.236
    lambdaArgs([](int x, int y) { return x + y; }, 5, 6); // Suma los dos argumentos -> Devuelve 11

    return 0;        
}


