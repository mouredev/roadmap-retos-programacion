#include <iostream>
#include <vector>

using namespace std;

// *************** *************** 05# - Valor y Referencia *************** *************** //

// ? Funciones

int funcion_por_valor(int x) {
    ++x; return x*x;
}

int funcion_por_referencia(int& x) {
    ++x; return x*x;
}

vector<int> programa1(int a, int b);
vector<int> programa2(int& a, int& b);

int main() {
    int numero = 10;

    cout << funcion_por_valor(numero) << '\n'; // 121
    cout << numero << '\n';                    // 10

    cout << funcion_por_referencia(numero) << '\n'; // 121
    cout << numero << '\n';                         // 11
   
    // ? Copia de una Variable
    string saludo = "> Hola Mundo!";
   
    string saludo2 = saludo;
    saludo2 = "Hola :v"; // Modifico la copia 2
    
    cout << saludo << " != " << saludo2 << '\n'; // Copia 2 es diferente a original

    string *saludo3 = &saludo;
    *saludo3 = "Hello :)"; // Modifico la copia 3
    
    cout << saludo << " == " << *saludo3 << '\n'; // Copia 3 es igual a original

    // *********************** Ejercicio DIFICULTAD EXTRA *********************** //
    
    int nueva_1, nueva_2, original_1 = 1, original_2 = 2;

    vector<int> result = programa1(original_1, original_2);

    nueva_1 = result[0];
    nueva_2 = result[1];

    cout << original_1 << ", " << original_2 << "\n";
    cout << nueva_1 << ", " <<  nueva_2 << "\n";

    nueva_1, nueva_2, original_1 = 1, original_2 = 2;

    cout << '\n' << "por Referencia :)" << '\n';

    result = programa2(original_1, original_2);

    nueva_1 = result[0];
    nueva_2 = result[1];

    cout << original_1 << ", " << original_2 << "\n";
    cout << nueva_1 << ", " <<  nueva_2 << "\n";

    return 0;
}

vector<int> programa1(int a, int b) {
    swap(a, b);
    return {a, b};
};

vector<int> programa2(int& a, int& b) {
    swap(a, b);
    return {a, b};
};
