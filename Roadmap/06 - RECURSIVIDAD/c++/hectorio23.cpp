#include <iostream>

/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */

/***********************************************
********** DECLARACION DE VARIABLES ************
************************************************/
int recursiveFoo(int);
int factorial(int);
int fibonacci(int);

int main() {
    int numeroCalcularFactorial = 3;
    int posicion = 10;
    int valor = fibonacci(posicion);

    /**************************************************************************
    ********** IMPRIME LOS NUMEROS DEL 100 - 0 DE MANERA RECURSIVA ************
    **************************************************************************/

    std::cout << "********* NUMEROS DEL 100 - 0 *********\n";
    recursiveFoo(100);
    std::cout << "\n";

    /**************************************************************************
    ********** IMPRIME EL FACTORIAL DE UN NUMERO DADO ************ ************
    **************************************************************************/
    std::cout << "El factorial de <<" << numeroCalcularFactorial << ">> es: " << factorial(numeroCalcularFactorial) << "\n";

    /***********************************************************************************************
    ********** IMPRIME EL VALOR DE UN NUMERO EN FUNCION A SU POSICION DENTRO ***********************
    ***********************+*** DE LA SERIE DE FIBONACCI ******************************************* 
    ************************************************************************************************/

    std::cout << "El valor en la posición " << posicion << " de la sucesión de Fibonacci es: " << valor << std::endl;

    return 0;
}

// LAS FUNCIONES RECURSIVAS PUEDEN LLAMARSE INFINITAMENTE SI NO SE TIENE CUIDADO AL MOMENTO DE 
// PROGRAMARLAS, PUEDEN SATURAR LA PILA DE LLAMADAS Y CAUSAR UN STACK OVERFLOW, AFORTUNADAMENTE
// LOS LENGUAJES COMO PYTHON, SU LIMITE DE RECURSIVIDAD ES DE 1,000 MIENTRAS QUE EN OTROS LENGUAJES
// ESTABLECEN UN LIMITE SIMILAR.

// Esta es una funcion recursiva que calculara (realmente imprimira) los valores
// de valor inicial a 0, es decir, imprime los valores que segun n >= 0, al momento
// de que el contador recursivo llega a cero, la funcion retorna un 0 y termina la
// recursividad.
int recursiveFoo(int valorInicial) {
    // En caso de que el contador recursivo llegue a -1.
    // La funcion finaliza su labor
    if (valorInicial == -1) return 0;
    std::cout << valorInicial << ", ";

    // Se llama a la misma funcion pero el contador recursivo valdra n - 1 
    return recursiveFoo(valorInicial - 1);
}

int factorial(int ivalue) {
    // En caso de que el contador recursivo llegue a 1.
    // La funcion finaliza su labor
    if (ivalue == 1) return 1; 

    // El valor se multiplica 100 * (n - 1) * (n - 2) * (n -3) * ... (n - n)
    return ivalue * factorial(ivalue - 1);
}

// Calcula el valor de la pocision dada al momento de llamar la funcion,
// finalmente retorna el valor, recordemos que la sucesion de fibonacci
// luce de la siguiente manera:
// 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377 
int fibonacci(int n) {
    if (n <= 0) {
        std::cout << "La posición debe ser un entero positivo" << std::endl;
        return -1; // o manejo de error según sea necesario
    }
    else if (n == 1) return 0;
    else if (n == 2) return 1;
    else {
        int a = 0, b = 1, temp;
        for (int i = 2; i < n; ++i) {
            temp = b;
            b = a + b;
            a = temp;
        }
        return b;
    }
}

/**************************************************************************
************************* OUTPUT EN EL TERMINAL ***************************
**************************************************************************/

/*
********* NUMEROS DEL 100 - 0 *********
100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 
76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 
52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 
28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 
2, 1, 0, 
El factorial de <<3>> es: 6
El valor en la posición 10 de la sucesión de Fibonacci es: 34

*/
