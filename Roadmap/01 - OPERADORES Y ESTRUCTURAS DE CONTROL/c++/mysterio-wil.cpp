/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 */

#include <iostream>
#include <string>
#include <vector>

int main() {
    std::cout << "### OPERADORES ###" << std::endl;

    // Operadores Aritméticos
    std::cout << "\n--- Aritméticos ---" << std::endl;
    int a = 10, b = 3;
    std::cout << "Suma: 10 + 3 = " << (a + b) << std::endl;
    std::cout << "Resta: 10 - 3 = " << (a - b) << std::endl;
    std::cout << "Multiplicación: 10 * 3 = " << (a * b) << std::endl;
    std::cout << "División: 10 / 3 = " << (a / b) << std::endl;
    std::cout << "Módulo: 10 % 3 = " << (a % b) << std::endl;

    // Operadores Lógicos
    std::cout << "\n--- Lógicos ---" << std::endl;
    std::cout << "AND (true && false): " << (true && false) << std::endl;
    std::cout << "OR (true || false): " << (true || false) << std::endl;
    std::cout << "NOT (!true): " << (!true) << std::endl;

    // Operadores de Comparación
    std::cout << "\n--- Comparación ---" << std::endl;
    std::cout << "Igualdad (10 == 3): " << (10 == 3) << std::endl;
    std::cout << "Desigualdad (10 != 3): " << (10 != 3) << std::endl;

    // Operadores de Asignación
    std::cout << "\n--- Asignación ---" << std::endl;
    int x = 5;
    x += 2;
    std::cout << "Suma y asignación: x += 2 -> x = " << x << std::endl;

    // Operadores de Bits
    std::cout << "\n--- Bits ---" << std::endl;
    int p = 10; // 1010
    int q = 3;  // 0011
    std::cout << "AND a nivel de bits (10 & 3): " << (p & q) << std::endl;
    std::cout << "OR a nivel de bits (10 | 3): " << (p | q) << std::endl;

    /*
     * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
     *   que representen todos los tipos de estructuras de control que existan
     *   en tu lenguaje:
     *   Condicionales, iterativas, excepciones...
     */

    std::cout << "\n### ESTRUCTURAS DE CONTROL ###" << std::endl;

    // Condicionales
    std::cout << "\n--- Condicionales (if, else) ---" << std::endl;
    int edad = 18;
    if (edad < 18) {
        std::cout << "Eres menor de edad." << std::endl;
    } else {
        std::cout << "Eres mayor de edad." << std::endl;
    }

    // Iterativas
    std::cout << "\n--- Iterativas (for) ---" << std::endl;
    for (int i = 1; i <= 3; ++i) {
        std::cout << i << std::endl;
    }

    std::cout << "\n--- Iterativas (while) ---" << std::endl;
    int contador = 3;
    while (contador > 0) {
        std::cout << contador << std::endl;
        contador--;
    }

    // Excepciones
    std::cout << "\n--- Excepciones (try, catch) ---" << std::endl;
    try {
        throw std::runtime_error("Este es un error de ejemplo");
    } catch (const std::exception& e) {
        std::cout << "Se capturó una excepción: " << e.what() << std::endl;
    }

    /*
     * DIFICULTAD EXTRA (opcional):
     * Crea un programa que imprima por consola todos los números comprendidos
     * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
     */

    std::cout << "\n### DIFICULTAD EXTRA ###" << std::endl;
    for (int numero = 10; numero <= 55; ++numero) {
        if (numero % 2 == 0 && numero != 16 && numero % 3 != 0) {
            std::cout << numero << std::endl;
        }
    }

    return 0;
}
