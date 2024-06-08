/* EJERCICIO #02: FUNCIONES Y ALCANCE
 * Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje
*/
#include <iostream>
#include <string>
#include <cmath>
#include <utility>

using namespace std;

// Variale global
std::string lenguajeProgramacion{"C++ 11"};

// Función que imprime un saludo
void saludo() {
    cout << endl << "Restos de programación con " << lenguajeProgramacion << endl;
}

// Función que determina si un número es primo
bool esPrimo(int n) {
    if (n <= 1) {
        return false;
    }

    for (int i = 2; i < n; i++) {
        if (n % i == 0) {
            return false;
        }
    }

    return true;
}

// Función que suma dos números
int suma(int a, int b) {
    return a + b;
}

// Declara la función de la dificultad extra
int dificultadExtra(std::string texto1, std::string texto2);


int main() {
    cout << "Lenguaje de programación: " << lenguajeProgramacion << endl;

    // Función sin parámetro ni retorno
    saludo();

    int n = 47;
    // Función con parámetro y retorno
    bool primo = esPrimo(n);
    cout << "El número " << n << (primo ? " es" : " no es") << " primo" << endl;

    int a = 5, b = 10;
    // Función con parámetros y retorno
    int sumaAB = suma(a, b);
    cout << "La suma de " << a << " + " << b << " es " << sumaAB << endl;

    // Función ya creada en la librería cmath
    auto potencia = pow(2.0, 3.0);
    cout << "2^3 = " << potencia << endl;

    // Función lambda
    auto actualizaVariableGlobal = [](std::string lenguaje) {
        lenguajeProgramacion = std::move(lenguaje);
        cout << "Variable global actualizada" << endl;
    };

    actualizaVariableGlobal("C++ 17");
    cout << "Lenguaje de programación: " << lenguajeProgramacion << endl;

    // Dificultad extra
    cout << endl << "Dificultad extra" << endl;
    int veces = dificultadExtra("Fizz", "Buzz");
    cout << "Se ha impreso el número en lugar de los textos " << veces << " veces" << endl;

    return 0;
}

/* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 *  - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *  - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *  - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *  - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *  - La función retorna el número de veces que se ha impreso el número en lugar de los textos.                                                                                                                                                                                                                                *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 */
int dificultadExtra(std::string texto1, std::string texto2) {
    int contador = 0;

    for (int i = 1; i <= 100; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            cout << texto1 + texto2 << ", ";
        } else if (i % 3 == 0) {
            cout << texto1 << ", ";
        } else if (i % 5 == 0) {
            cout << texto2 << ", ";
        } else {
            cout << i << ", ";
            contador++;
        }
    }

    cout << endl;
    return contador;
}