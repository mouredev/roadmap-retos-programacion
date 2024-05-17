#include <iostream>
using namespace std;

int main()
{
    /*
        OPERADORES EN C++
    */

    //== Operadores aritméticos en C++
    cout << "Suma: 22 + 13 = " << 22 + 13 << endl;
    cout << "Resta: 22 - 13 = " << 22 - 13 << endl;
    cout << "Multiplicación: 22 * 13 = " << 22 * 13 << endl;
    cout << "División: 22 / 13 = " << 22 / 13 << endl;
    cout << "Módulo: 22 % 13 = " << 22 % 13 << endl;
    // NOTE: Operadores de incremento y decremento exiten en C++ y tienen formato ++n, n++, --n, n-- respectivamente;

    //== Operadores de comparación en C++
    cout << "Igualdad: 22 == 13 es " << (22 == 13) << endl;
    cout << "Desigualdad: 22 != 13 es " << (22 != 13) << endl;
    cout << "Mayor que: 22 > 13 es " << (22 > 13) << endl;
    cout << "Menor que: 22 < 13 es " << (22 < 13) << endl;
    cout << "Mayor o igual que: 22 >= 13 es " << (22 >= 13) << endl;
    cout << "Menor o igual que: 22 <= 13 es " << (22 <= 13) << endl;

    //== Operadores lógicos en C++
    cout << "AND (&&): 22 + 3 == 25 && 22 - 3 == 19 es "
    << ([]() { return (22 + 3 == 25 && 22 - 3 == 19); }() ? "Verdadero" : "Falso") << endl;
    cout << "OR (||): 22 + 3 == 25 || 22 - 3 == 19 es " 
    << ([]() { return (22 + 3 == 25 || 22 - 3 == 19); }() ? "Verdadero" : "Falso") << endl;
    cout << "NOT (!): !(22 + 3 == 25) es " 
    << ([]() { return !(22 + 3 == 25); }() ? "Verdadero" : "Falso") << endl;

    //== Operadores de asignación en C++
    int number= 42;
    cout << "Asignación: number = " << number << endl;
    number += 1;
    cout << "Suma y asignación: number += 1 " << '(' << number << ')' << endl;
    number -= 3;
    cout << "Resta y asignación: number -= 3 " << '(' << number << ')' << endl;
    number *= 3;
    cout << "Multiplicación y asignación: number *= 3 " << '(' << number << ')' << endl;
    number /= 3;
    cout << "División y asignación: number /= 3 " << '(' << number << ')' << endl;
    number %= 3;
    cout << "Módulo y asignación: number %= 3 " << '(' << number << ')' << endl;

    //Funciones integradas en C++
    cout << "El valor absoluto de -13 es " << abs(-13) << endl;
    cout << "El valor máximo entre 13 y 42 es " << max(13, 42) << endl;
    cout << "El valor mínimo entre 13 y 42 es " << min(13, 42) << endl;

    //Otros operadores en C++
    cout << "El tamaño de un int en bytes es " << sizeof(int) << endl;
    cout << "El tamaño de un char en bytes es " << sizeof(char) << endl;
    cout << "El tamaño de un float en bytes es " << sizeof(float) << endl;
    cout << "El tamaño de un double en bytes es " << sizeof(double) << endl;

    //Operadores de bits en C++
    cout << "Desplazamiento de bits a la izquierda: 1 << 3 = " << (1 << 3) << endl;
    cout << "Desplazamiento de bits a la derecha: 8 >> 2 = " << (8 >> 2) << endl;
    cout << "AND a nivel de bits: 5 & 3 = " << (5 & 3) << endl;
    cout << "OR a nivel de bits: 5 | 3 = " << (5 | 3) << endl;
    cout << "XOR a nivel de bits: 5 ^ 3 = " << (5 ^ 3) << endl;
    cout << "NOT a nivel de bits: ~5 = " << (~5) << endl;

    /*
        ESTRUCTURAS DE CONTROL EN C++
    */

    //== Estructura condicional if en C++
    int age = 18;
    if (age >= 18) {
        cout << "Eres mayor de edad" << endl;
    } else if (age >= 60){
        cout << "Eres un adulto mayor" << endl;
    } else {
        cout << "Eres menor de edad" << endl;
    }

    //== Estructura condicional switch en C++
    int day = 3;
    switch (day) {
        case 1:
            cout << "Lunes" << endl;
            break;
        case 2:
            cout << "Martes" << endl;
            break;
        case 3:
            cout << "Miércoles" << endl;
            break;
        case 4:
            cout << "Jueves" << endl;
            break;
        case 5:
            cout << "Viernes" << endl;
            break;
        case 6:
            cout << "Sábado" << endl;
            break;
        case 7:
            cout << "Domingo" << endl;
            break;
        default:
            cout << "Día no válido" << endl;
            break;
    }

    //== Estructura de repetición for en C++
    for (int i = 0; i < 5; i++) {
        cout << "Iteración (for) " << i << endl;
    }

    //== Estructura de repetición while en C++
    int i = 0;
    while (i < 5) {
        cout << "Iteración (while) " << i << endl;
        i++;
    }

    //== Estructura de repetición do-while en C++
    int j = 0;
    do {
        cout << "Iteración (do-while) " << j << endl;
        j++;
    } while (j < 5);

    //== Manejo de excepciones en C++
    // haz un try de 10/0 y si hay except se ejecuta el catch imprimiendo error
    try {
        int result = 10 / 0;
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }
    
    /*
        DIFICULTAD EXTRA
    */

    //== Ejercicio extra
    cout << "Ejercicio extra: La lista de números es ";
    for (int i = 10; i <= 55; i++) {
        if (i % 2 == 0 && i % 3 != 0 && i != 16) {
            cout << i << " ";
        }
    }
    cout << endl;

    return 0;
}   