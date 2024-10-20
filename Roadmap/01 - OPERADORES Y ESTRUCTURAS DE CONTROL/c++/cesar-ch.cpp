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
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
#include <iostream>
using namespace std;

int main()
{
    // Operadores aritméticos
    int a = 10, b = 5;
    int suma = a + b;
    int resta = a - b;
    int multiplicacion = a * b;
    int division = a / b;
    int modulo = a % b;

    cout << "Operadores aritméticos:" << endl;
    cout << "Suma: " << suma << endl;
    cout << "Resta: " << resta << endl;
    cout << "Multiplicación: " << multiplicacion << endl;
    cout << "División: " << division << endl;
    cout << "Módulo: " << modulo << endl;

    // Operadores lógicos
    bool x = true, y = false;
    bool and_logico = x && y;
    bool or_logico = x || y;
    bool not_logico = !x;

    cout << "\nOperadores lógicos:" << endl;
    cout << "AND lógico: " << and_logico << endl;
    cout << "OR lógico: " << or_logico << endl;
    cout << "NOT lógico: " << not_logico << endl;

    // Operadores de comparación
    bool igualdad = (a == b);
    bool desigualdad = (a != b);
    bool mayor_que = (a > b);
    bool menor_que = (a < b);
    bool mayor_igual = (a >= b);
    bool menor_igual = (a <= b);

    cout << "\nOperadores de comparación:" << endl;
    cout << "Igualdad: " << igualdad << endl;
    cout << "Desigualdad: " << desigualdad << endl;
    cout << "Mayor que: " << mayor_que << endl;
    cout << "Menor que: " << menor_que << endl;
    cout << "Mayor o igual: " << mayor_igual << endl;
    cout << "Menor o igual: " << menor_igual << endl;

    // Operadores de asignación
    int c = 10;
    c += 5;
    cout << "\nOperador de asignación:" << endl;
    cout << "Valor de c después de c += 5: " << c << endl;
    c -= 5;
    cout << "Valor de d después de c -= 5: " << c << endl;
    c *= 5;
    cout << "Valor de c después de c *= 5: " << c << endl;
    c /= 5;
    cout << "Valor de c después de c /= 5: " << c << endl;
    c %= 5;
    cout << "Valor de c después de c %= 5: " << c << endl;

    // Operadores a nivel de bits
    cout << "\nOperadores a nivel de Bits: \n";
    cout << "a & b = " << (a & b) << endl; // AND a nivel de bits
    cout << "a | b = " << (a | b) << endl; // OR a nivel de bits
    cout << "a ^ b = " << (a ^ b) << endl; // XOR a nivel de bits

    // Estructuras de control (Condicionales)
    cout << "\nEstructura de Control - Condicional: \n";
    if (a > b)
    {
        cout << "a es mayor que b\n";
    }
    else
    {
        cout << "a no es mayor que b\n";
    }

    // Estructuras de control (Iterativas)
    cout << "\nEstructura de Control - Bucle For: \n";
    for (int i = 0; i < 5; i++)
    {
        cout << "i = " << i << endl;
    }

    // Manejo de excepciones
    cout << "\nEstructura de Control - Manejo de Excepciones: \n";
    try
    {
        if (b == 0)
            throw "Error: División por cero";
        cout << "a / b = " << a / b << endl;
    }
    catch (const char *msg)
    {
        cout << msg << endl;
    }

    // DIFICULTAD EXTRA
    cout << "\nDificultad Extra:\n";
    for (int i = 10; i <= 55; i++)
    {
        if (i % 2 == 0 && i != 16 && i % 3 != 0)
        {
            cout << i << " ";
        }
    }
    cout << endl;
}