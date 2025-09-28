/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 */

#include <stdio.h>
#include <stdbool.h>

int main() {
    printf("### OPERADORES ###\n");

    // Operadores Aritméticos
    printf("\n--- Aritméticos ---\n");
    int a = 10, b = 3;
    printf("Suma: 10 + 3 = %d\n", a + b);
    printf("Resta: 10 - 3 = %d\n", a - b);
    printf("Multiplicación: 10 * 3 = %d\n", a * b);
    printf("División: 10 / 3 = %d\n", a / b);
    printf("Módulo: 10 %% 3 = %d\n", a %% b);

    // Operadores Lógicos
    printf("\n--- Lógicos ---\n");
    printf("AND (true && false): %d\n", true && false);
    printf("OR (true || false): %d\n", true || false);
    printf("NOT (!true): %d\n", !true);

    // Operadores de Comparación
    printf("\n--- Comparación ---\n");
    printf("Igualdad (10 == 3): %d\n", 10 == 3);
    printf("Desigualdad (10 != 3): %d\n", 10 != 3);

    // Operadores de Asignación
    printf("\n--- Asignación ---\n");
    int x = 5;
    x += 2;
    printf("Suma y asignación: x += 2 -> x = %d\n", x);

    // Operadores de Bits
    printf("\n--- Bits ---\n");
    int p = 10; // 1010
    int q = 3;  // 0011
    printf("AND a nivel de bits (10 & 3): %d\n", p & q);
    printf("OR a nivel de bits (10 | 3): %d\n", p | q);

    /*
     * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
     *   que representen todos los tipos de estructuras de control que existan
     *   en tu lenguaje:
     *   Condicionales, iterativas, excepciones...
     */

    printf("\n### ESTRUCTURAS DE CONTROL ###\n");

    // Condicionales
    printf("\n--- Condicionales (if, else) ---\n");
    int edad = 18;
    if (edad < 18) {
        printf("Eres menor de edad.\n");
    } else {
        printf("Eres mayor de edad.\n");
    }

    // Iterativas
    printf("\n--- Iterativas (for) ---\n");
    for (int i = 1; i <= 3; i++) {
        printf("%d\n", i);
    }

    printf("\n--- Iterativas (while) ---\n");
    int contador = 3;
    while (contador > 0) {
        printf("%d\n", contador);
        contador--;
    }

    // Excepciones (C no tiene un sistema de excepciones try-catch)
    printf("\n--- Excepciones ---\n");
    printf("C no tiene manejo de excepciones try-catch. El manejo de errores se hace usualmente devolviendo códigos de error.\n");

    /*
     * DIFICULTAD EXTRA (opcional):
     * Crea un programa que imprima por consola todos los números comprendidos
     * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
     */

    printf("\n### DIFICULTAD EXTRA ###\n");
    for (int numero = 10; numero <= 55; numero++) {
        if (numero %% 2 == 0 && numero != 16 && numero %% 3 != 0) {
            printf("%d\n", numero);
        }
    }

    return 0;
}
