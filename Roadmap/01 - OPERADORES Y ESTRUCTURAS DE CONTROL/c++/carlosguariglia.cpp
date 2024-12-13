/* # #01 OPERADORES Y ESTRUCTURAS DE CONTROL
> #### Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24

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
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

/* # #01 OPERADORES Y ESTRUCTURAS DE CONTROL
> #### Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24

 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje: Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
   */
// generado por Chatgpt


#include <iostream>
using namespace std;

int main() {
    // Operadores aritméticos
    int a = 10;
    int b = 3;
    cout << "Operadores aritméticos:" << endl;
    cout << "Suma: " << a + b << endl;
    cout << "Resta: " << a - b << endl;
    cout << "Multiplicación: " << a * b << endl;
    cout << "División: " << a / b << endl;
    cout << "Módulo: " << a % b << endl;

    // Operadores lógicos
    bool x = true;
    bool y = false;
    cout << "\nOperadores lógicos:" << endl;
    cout << "AND: " << (x && y) << endl;
    cout << "OR: " << (x || y) << endl;
    cout << "NOT: " << !x << endl;

    // Operadores de comparación
    cout << "\nOperadores de comparación:" << endl;
    cout << "a == b: " << (a == b) << endl;
    cout << "a != b: " << (a != b) << endl;
    cout << "a > b: " << (a > b) << endl;
    cout << "a < b: " << (a < b) << endl;
    cout << "a >= b: " << (a >= b) << endl;
    cout << "a <= b: " << (a <= b) << endl;

    // Operadores de asignación
    cout << "\nOperadores de asignación:" << endl;
    int c = 5;
    cout << "c = 5: " << c << endl;
    c += 3; // c = c + 3
    cout << "c += 3: " << c << endl;
    c *= 2; // c = c * 2
    cout << "c *= 2: " << c << endl;
    c -= 4; // c = c - 4
    cout << "c -= 4: " << c << endl;

    // Operadores de bits
    cout << "\nOperadores de bits:" << endl;
    int d = 5;  // 0101 en binario
    int e = 3;  // 0011 en binario
    cout << "AND binario (d & e): " << (d & e) << endl;
    cout << "OR binario (d | e): " << (d | e) << endl;
    cout << "XOR binario (d ^ e): " << (d ^ e) << endl;
    cout << "Shift izquierdo (d << 1): " << (d << 1) << endl;
    cout << "Shift derecho (d >> 1): " << (d >> 1) << endl;

    // Estructuras de control
    // Condicionales
    cout << "\nEstructuras de control - Condicionales:" << endl;
    if (a > b) {
        cout << "a es mayor que b" << endl;
    } else {
        cout << "a no es mayor que b" << endl;
    }

    // Bucle for
    cout << "\nEstructuras de control - Bucle for:" << endl;
    for (int i = 0; i < 5; i++) {
        cout << "i: " << i << endl;
    }

    // Bucle while
    cout << "\nEstructuras de control - Bucle while:" << endl;
    int count = 0;
    while (count < 3) {
        cout << "count: " << count << endl;
        count++;
    }

    // Bucle do-while
    cout << "\nEstructuras de control - Bucle do-while:" << endl;
    int num = 5;
    do {
        cout << "num: " << num << endl;
        num--;
    } while (num > 0);

    // DIFICULTAD EXTRA: imprimir los números pares entre 10 y 55 que no sean 16 ni múltiplos de 3
    cout << "\nDificultad extra: Números pares entre 10 y 55, excluyendo 16 y múltiplos de 3" << endl;
    for (int i = 10; i <= 55; i++) {
        if (i % 2 == 0 && i != 16 && i % 3 != 0) {       
            cout << i << " ";
        }
    }
    cout << endl;

    return 0;
}
