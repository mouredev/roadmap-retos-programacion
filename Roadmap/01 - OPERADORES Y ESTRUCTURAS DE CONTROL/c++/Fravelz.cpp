#include <iostream>

using namespace std;

int main() {
    cout << endl;

    // **************** Operadores **************** //
    int a = 10, b = 20;

    // Operadores Aritmeticos
    cout << " > Incremento: " << a++ << '\n';
    cout << " > Decremento: " << a-- << '\n';
    
    cout << '\n';
    
    cout << " > Suma: "           << 20 + 10  << '\n';
    cout << " > Resta: "          << 20 - 10  << '\n';
    cout << " > Multiplicacion: " << 20 * 10  << '\n';
    cout << " > Division: "       << 625 / 25 << '\n';
    cout << " > Resto: "          << 101 % 2  << '\n';
    cout << endl;

    // Operadores de Asignacion
    int res = 0;

    res += a; // Suma (0 + 10 = 10) 
    res -= 8; // Resta (10 - 8 = 2)
    res *= 4; // Multipricacion (2 * 4 = 8)
    res /= 2; // Division (8 / 2 = 4)
    res %= 3; // Modulo o Resto (4 % 3 = 1)

    cout << " > El Resultado es: " << res << '\n';
    cout << endl;
    
    // Operadores Logicos de Comparacion 
    cout << " > Mayor que: "       << (a > b)   << '\n';
    cout << " > Menor que: "       << (a < b)   << '\n';
    cout << " > Igual que: "       << (a == b)  << '\n';
    cout << " > Mayor igual que: " << (a >= b)  << '\n';
    cout << " > Menor igual que: " << (a <= b)  << '\n';
    cout << " > Diferente que: "   << !(a == b) << '\n';
    cout << endl;

    // Operadores de Bit a Bit
    cout << "> OR: "                            << (a | b)  << '\n';
    cout << "> AND: "                           << (a & b)  << '\n';
    cout << "> XOR: "                           << (a ^ b)  << '\n';
    cout << "> NOT: "                           << (~a)     << '\n';
    cout << "> Desplazamiento a la izquierda: " << (a << 2) << '\n';
    cout << "> Desplazamiento a la derecha: "   << (a >> 3) << '\n';

    // **************** Bucles, Condicionales y Exepciones **************** //
    
    // Numeros Impares hasta el 11 (Bucle for, y Operador Ternario)
    for (int x = 1; x <= 11; x += 2) { 
        cout << x << (x != 11) ? ", " : ".";
    }

    cout << endl;

    // Suma de Numeros Pares (Bucle while y condicionales)
    int sum = 0, iter = 0;

    while (iter <= 10) {
        if (iter != 10) {
            cout << sum << ", ";

        } else {
            cout << sum << ". ";
        }
        
        sum += iter;
        iter++;
    }
    
    cout << endl;
    
    // Factorial de 5 (Bucle do while y condicionales) 
    // [Mucha cosa inesesaria se puede obtimizar :v]

    int factorial = 0, iter2 = 0;

    do {        
        factorial *= iter2;
        iter2++;

        if (iter2 != 10 && factorial != 0) {
            
            if (iter2 % 5 == 1 && iter2 != 0) {
                cout << factorial << ". ";
                break;
            } 

            else {
                cout << factorial << ", ";

            }
            
        
        } else if (factorial == 0) {
            factorial = 1;
            continue;

        } else {
            cout << factorial << ". ";
        }
        
    } while (iter2 <= 10);

    cout << endl;

    try { // Código que puede lanzar una excepción
        throw "Ocurrió un error";  // Lanzar excepción

    } catch (const char* msg) {
        cout << "\nError404: " << msg << " :v" << endl;
    }
    
    cout << endl;

    //* DIFICULTAD EXTRA (opcional):
    //* Crea un programa que imprima por consola todos los números comprendidos
    //* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
    //*
    //* Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

    cout << " [+] Reto de la dificultad Extra: ";
    
    for (int y = 10; y <= 55; y += 2) {

        if (y != 16 && y % 3 != 0) {
            cout << y << ( (y < 52) ? ", ": "." );
        }
        
    }

    cout << endl;

    return 0;
}
