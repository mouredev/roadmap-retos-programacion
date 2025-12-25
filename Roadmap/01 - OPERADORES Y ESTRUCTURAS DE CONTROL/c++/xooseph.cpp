// Operadores

#include <iostream>

using namespace std;

void printNumbers() {
    /* EJERCICIO EXTRA
        Imprimir todos los números entre 10 y 55 (incluidos), pares, y que no 
        son ni el 16 ni múltiplos de 3.
    */
    cout << "Números del 10 al 55:\n";

    for (int i = 10; i <= 55; i++) {
        if (((i % 2) == 0) && (i != 16) && ((i % 3) != 0)) {
            cout << i << "\n";
        }
    }
}

int main() {
    int a = 10;
    int b = 5;

    cout << "OPERADORES ARITMÉTICOS\n\n";
    cout << "Suma: 10 + 5 = " << (a + b) << "\n";
    cout << "Resta: 10 - 5 = " << (a - b) << "\n";
    cout << "Multiplicación: 10 * 5 = " << (a * b) << "\n";
    cout << "División: 10 / 5 = " << (a / b) << "\n";
    cout << "Módulo: 10 % 5 = " << (a % b) << "\n";
    cout << "Incremento: +1 a 10 = " << ++a << "\n";
    cout << "Decremento: -1 a 5 = " << --b << "\n\n";

    a = 3;
    b = 5;

    cout << "OPERADORES LÓGICOS\n\n";
    cout << "a = 3\n";
    cout << "a > 2 and a < 5: " << (a > 2 && a < 5) << "\n";
    cout << "a > 2 or a > 10: " << (a > 2 || a > 10) << "\n";
    cout << "not a > 2: " << !(a > 2) << "\n\n";
    
    cout << "OPERADORES DE COMPARACIÓN\n\n";

    cout << "a = 3, b = 5\n";
    cout << "a == b: " << (a == b) << "\n";
    cout << "a != b: " << (a != b) << "\n";
    cout << "a > b: " << (a > b) << "\n";
    cout << "a < b: " << (a < b) << "\n";
    cout << "a >= b: " << (a >= b) << "\n";
    cout << "a <= b: " << (a <= b) << "\n\n"; 

    cout << "OPERADORES DE ASIGNACIÓN Y DE BIT\n\n";

    cout << "a = 8: " << (a = 8) << "\n";
    cout << "a = a + 2: " << (a += 2) << "\n";
    cout << "a = a - 3: " << (a -= 3) << "\n";
    cout << "a = a * 4: " << (a *= 4) << "\n";
    cout << "a = a / 3: " << (a /= 3) << "\n";
    cout << "a = a % 2: " << (a %= 2) << "\n";
    // AND bit a bit
    cout << "a = a & 3: " << (a &= 3) << "\n";
    // OR inclusivo bit a bit
    cout << "a = a | 2: " << (a |= 2) << "\n";
    // OR exclusivo bit a bit
    cout << "a = a ^ 5: " << (a ^= 5) << "\n";
    // Cambia el valor del primer operando a la derecha el número de bits 
    // especificado por el valor del segundo operando
    cout << "a = a >> 2: " << (a >>= 2) << "\n";
    // Cambia el valor del primer operando a la izquierda del número de bits 
    // especificado por el valor del segundo operando
    cout << "a = a << 2: " << (a <<= 2) << "\n\n"; 

    cout << "ESTRUCTURAS DE CONTROL\n\n";
    cout << "IF-ELSE:\n\n";

    a = 5;

    if (a == 5) {
        cout << "a es 5" << "\n";
    } 

    else {
        cout << "a no es 5" << "\n";
    }

    cout << "SWITCH:\n\n";

    switch (a){
        case 5:
            cout << "a es 5" << "\n";
            break;

        default:
            cout << "a no es 5" << "\n";
            break;
    }

    cout << "WHILE:\n\n";

    while (a > 0) {
        cout << a << "\n\n";
        --a;
    }

    cout << "DO-WHILE:\n\n";

    a = 5;

    do {
        cout << a << "\n\n";
        --a;
    } while (a > 0);

    cout << "FOR:\n\n";

    for (int i = 0; i < 5; i++) {
        cout << i << "\n\n";
    }

    cout << "EXCEPCIONES:\n\n";

    try {
        throw 12;
    }
    catch (int) {
        cout << "Se ha generado una excepción de tipo int.\n\n"; 
    }

    printNumbers();

    return 0;
}