/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritm�ticos, l�gicos, de comparaci�n, asignaci�n, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que t� quieras, crea ejemplos
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
    // ** Operadores aritm�ticos **
    int a = 10;
    int b = 3;

    cout << "Operadores aritm�ticos:" << endl;
    cout << "Suma: " << a + b << endl;         // Suma
    cout << "Resta: " << a - b << endl;        // Resta
    cout << "Multiplicaci�n: " << a * b << endl; // Multiplicaci�n
    cout << "Divisi�n: " << a / b << endl;     // Divisi�n
    cout << "M�dulo: " << a % b << endl;       // M�dulo
    cout << "Incremento: " << ++a << endl;     // Incremento
    cout << "Decremento: " << --b << endl;     // Decremento

    // ** Operadores de asignaci�n **
    cout << "\nOperadores de asignaci�n:" << endl;
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

    // ** Operadores de comparaci�n **
    cout << "\nOperadores de comparaci�n:" << endl;
    cout << "a == b: " << (a == b) << endl; // Igualdad
    cout << "a != b: " << (a != b) << endl; // Diferente
    cout << "a < b: " << (a < b) << endl;   // Menor que
    cout << "a > b: " << (a > b) << endl;   // Mayor que
    cout << "a <= b: " << (a <= b) << endl; // Menor o igual que
    cout << "a >= b: " << (a >= b) << endl; // Mayor o igual que

    // ** Operadores l�gicos **
    cout << "\nOperadores l�gicos:" << endl;
    bool x = true;
    bool y = false;
    cout << "x && y: " << (x && y) << endl; // AND l�gico
    cout << "x || y: " << (x || y) << endl; // OR l�gico
    cout << "!x: " << !x << endl;           // NOT l�gico

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
            throw runtime_error("Error: Divisi�n entre cero");
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
