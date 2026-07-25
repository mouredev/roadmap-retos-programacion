#include <iostream>
#include <cmath>

using namespace std;

// Global variable
int anotherAge = 24;

void printUsername() {
    cout << "Mi nombre es xooseph." << endl;
}

void printAge(int age) {
    cout << "Tengo " << age << " años." << endl;
}

int printSum(int a, int b) {
    return a + b;
}

void printUsernameAndAge(int anotherAge) {
    printUsername();
    printAge(anotherAge);
}

/*
EJERCICIO EXTRA
Función que recibe dos parámetros de tipo cadena de texto y retorna un número.
 *   - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/

int multiples(string text1, string text2) {
    int numbersWithoutText = 0;

    for (int i = 1; i <= 100; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            cout << text1 << " " << text2 << endl;
        }
        else if (i % 3 == 0) {
            cout << text1 << endl;
        }
        else if (i % 5 == 0) {
            cout << text2 << endl;
        }
        else {
            cout << i << endl;

            numbersWithoutText++;
        }
    }

    return numbersWithoutText;
}

int main() {
    int age = 23, a = 2, b = 4, c = 121;
    int result, i;
    string text1 = "Hello", text2 = "World!";

    printUsername();
    printAge(age);
    result = printSum(a,b);

    cout << "La suma de 2 y 4 es " << result << endl;

    printUsernameAndAge(anotherAge);

    cout << "La raíz cuadrada de 121 es " << sqrt(c) << endl;

    cout << "\nEJERCICIO EXTRA" << endl;

    i = multiples(text1, text2);

    cout << "Se imprimieron " << i << " números en lugar de las cadenas de texto." << endl;

    return 0;
}