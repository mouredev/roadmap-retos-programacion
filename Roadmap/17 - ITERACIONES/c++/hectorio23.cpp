// Author: Héctor Adán 
// GitHub: https://github.com/hectorio23 
#include <algorithm>
#include <iostream>
#include <cstdlib>

/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
*/

// Esta funcion imprimira el numero los 10 al 1
int recursive(int numero) {
    std::cout << numero << ", ";
    if (numero == 1) return 1;
    return numero * recursive(numero - 1);
}

int main() {
    // bucle for
    std::cout << "Forma 1 -> bucle for\n";
    for (int i = 1; i <= 10; i++) std::cout << i << ", ";
    std::cout << "\n";

    // bucle while
    std::cout << "Forma 2 -> bucle While\n";
    int n = 1;
    while (n <= 10) { std::cout << n << ", "; n++; }
    std::cout << "\n";

    // bucle do while
    std::cout << "Forma 3 -> bucle Do While\n";
    n = 1;
    do { std::cout << n << ", "; n++; } while (n <= 10);
    std::cout << "\n";

    // bucle for auto
    std::cout << "Forma 4 -> bucle for auto\n";
    int data[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    for (auto element : data) std::cout << element << ", ";
    std::cout << "\n";

    // bucle for indefinido
    std::cout << "Forma 5 -> bucle for indefinido\n";
    n = 1;
    for (;;) { std::cout << n << ", "; n ++; if (n == 11) break; };
    std::cout << "\n";

    // recursividad
    std::cout << "Forma 6 -> recursividad\n";
    recursive(10);
    std::cout << "\n";

    // bucle con iteradores
    std::cout << "Forma 7 -> bucle for con iteradores\n";
    int array[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    for (auto it = std::begin(array); it != std::end(array); ++it) {
        std::cout << *it << ", ";
    }
    std::cout << "\n";

    // bucle for_each usando funciones lambda o "anonimas" 
    std::cout << "Forma 8 -> bucle for_each con lambda/for each\n";
    std::for_each(std::begin(array), std::end(array), [](int value) {
        std::cout << value << ", ";
    });
    std::cout << "\n";

    // bucle for con indexacion de puntero 
    std::cout << "Forma 9 -> bucle con indexación de puntero\n";
    int* ptr = array;
    for (int i = 0; i < 10; ++i) {
        std::cout << *(ptr + i) << ", ";
    }
    std::cout << "\n";

    return EXIT_SUCCESS;
}
