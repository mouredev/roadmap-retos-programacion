/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */


#include <iostream>
#include <vector>
#include <exception> // Para manejo de excepciones

using namespace std;

int main() {
    // ** Operadores aritméticos **
    int a = 10;
    int b = 3;

    cout << "Operadores aritméticos:" << endl;
    cout << "Suma: " << a + b << endl;         // Suma
    cout << "Resta: " << a - b << endl;        // Resta
    cout << "Multiplicación: " << a * b << endl; // Multiplicación
    cout << "División: " << a / b << endl;     // División
    cout << "Módulo: " << a % b << endl;       // Módulo
    cout << "Incremento: " << ++a << endl;     // Incremento
    cout << "Decremento: " << --b << endl;     // Decremento

    // ** Operadores de asignación **
    cout << "\nOperadores de asignación:" << endl;
    a = 5;
    cout << "a = 5 -> " << a << endl;
    a += 2;
    cout << "a += 2 -> " << a << endl;
    a -= 1;
    cout << "a -= 1 -> " << a << endl;
    a *= 3;
    cout << "a *= 3 -> " << a << endl;
    a /= 2;
    cout << "a /= 2 -> " << a << endl;
    a %= 3;
    cout << "a %= 3 -> " << a << endl;

    // ** Operadores de comparación **
    cout << "\nOperadores de comparación:" << endl;
    cout << "a == b: " << (a == b) << endl; // Igualdad
    cout << "a != b: " << (a != b) << endl; // Diferente
    cout << "a < b: " << (a < b) << endl;   // Menor que
    cout << "a > b: " << (a > b) << endl;   // Mayor que
    cout << "a <= b: " << (a <= b) << endl; // Menor o igual que
    cout << "a >= b: " << (a >= b) << endl; // Mayor o igual que

    // ** Operadores lógicos **
    cout << "\nOperadores lógicos:" << endl;
    bool x = true;
    bool y = false;
    cout << "x && y: " << (x && y) << endl; // AND lógico
    cout << "x || y: " << (x || y) << endl; // OR lógico
    cout << "!x: " << !x << endl;           // NOT lógico

    // ** Operadores de bits **
    cout << "\nOperadores de bits:" << endl;
    int c = 5;  // 0101 en binario
    int d = 9;  // 1001 en binario
    cout << "c & d: " << (c & d) << endl;   // AND a nivel de bits
    cout << "c | d: " << (c | d) << endl;   // OR a nivel de bits
    cout << "c ^ d: " << (c ^ d) << endl;   // XOR a nivel de bits
    cout << "~c: " << ~c << endl;           // NOT a nivel de bits
    cout << "c << 1: " << (c << 1) << endl; // Desplazamiento a la izquierda
    cout << "c >> 1: " << (c >> 1) << endl; // Desplazamiento a la derecha

    // ** Estructuras de control: Condicionales **
    cout << "\nEstructuras de control - Condicionales:" << endl;
    if (a > b) {
        cout << "a es mayor que b" << endl;
    }
    else {
        cout << "a no es mayor que b" << endl;
    }

    // ** Estructuras de control: Iterativas **
    cout << "\nEstructuras de control - Iterativas:" << endl;
    cout << "Bucle for:" << endl;
    for (int i = 0; i < 3; i++) {
        cout << "i = " << i << endl;
    }

    cout << "Bucle while:" << endl;
    int i = 0;
    while (i < 3) {
        cout << "i = " << i << endl;
        i++;
    }

    cout << "Bucle do-while:" << endl;
    i = 0;
    do {
        cout << "i = " << i << endl;
        i++;
    } while (i < 3);

    // ** Estructuras de control: Manejo de excepciones **
    cout << "\nEstructuras de control - Excepciones:" << endl;
    try {
        int divisor = 0;
        if (divisor == 0) {
            throw runtime_error("Error: División entre cero");
        }
        int resultado = 10 / divisor;
        cout << "Resultado: " << resultado << endl;
    }
    catch (const exception& e) {
        cout << e.what() << endl;
    }

    // ** Dificultad Extra **
    cout << "\nDificultad Extra:" << endl;

    int num = 10;
    while (num <= 55) {
        if (num % 2 == 0 && num % 3 != 0 && num % 16 != 0) {
            cout << num << " " << endl;
            num++;
        }
        num++;
    }
    return 0;
}
