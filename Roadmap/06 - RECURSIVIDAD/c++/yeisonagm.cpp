/* EJERCICIO #06: RECURSIVIDAD
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
 */
#include <iostream>

using namespace std;

// Imprime números de manera recursiva
void printNumbers(int n) {
    // Si n es menor a 0, termina la recursividad
    if (n < 0) {
        return;
    }

    cout << n << ", ";
    // Llamada recursiva
    printNumbers(n - 1);
}

// Factorial de un número
int factorial(int n) {
    // Si n es 0, el factorial es 1
    if (n == 0) return 1;

    // Llamada recursiva
    return n * factorial(n - 1);
}

// Elemento según la posición de la secuencia de Fibonacci
int fibonacci(int n) {
    // Si n es 0, el elemento es 0
    if (n == 0) return 0;
    // Si n es 1, el elemento es 1
    if (n == 1) return 1;

    // Llamada recursiva
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    cout << "EJERCICIO #06: RECURSIVIDAD" << endl;
    // Imprime números del 100 al 0
    cout << "Imprimiendo números del 100 al 0:" << endl;
    printNumbers(100);
    cout << endl;

    // Factorial de un número
    cout << "\nEjemplos de factoriales" << endl;
    for (int i = 0; i < 10; ++i) {
        cout << i << "! = " << factorial(i) << endl;
    }

    // Elemento según la posición de la secuencia de Fibonacci
    cout << "\nEjemplos de la secuencia de Fibonacci" << endl;
    for (int i = 0; i < 10; ++i) {
        cout << "Número de la posición " << i << " en la secuencia es " << fibonacci(i) << endl;
    }

    return 0;
}