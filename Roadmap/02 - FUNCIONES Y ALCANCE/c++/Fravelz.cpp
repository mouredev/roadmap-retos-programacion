#include <iostream>

using namespace std;

// **************** Funciones y tipos, Alcance de variables, y Reto Extra **************** //


void nothing_(); // Funcion definida que no hace nada.

int al_cubo(int a); // Funcion definida que retorna un numero int.

int retoExtra(string a, string b) { // Funcion del reto Extra
    int contador = 0;

    for (int i = 1; i <= 100; i++) {

        if (i % 3 == 0 && i % 5 == 0) cout << "(" << a << b << ")"; 
        
        else if (i % 3 == 0) cout << "(" << a << ")"; 
        
        else if (i % 5 == 0) cout << "(" << b << ")"; 
        
        else {
            cout << i;
            contador++;
        }

        cout << endl;
    }
    
    return contador;
}


string variable1 = "GLOBAL"; // Variable Global

int main() {
    string variable2 = "Local"; // Variable Local

    cout << "\n4 a la 3 = " << al_cubo(4) << '\n';
    cout << endl;

    cout << "\nLos numeros se imprimen: " << retoExtra((string)"LaGran", (string)"Colombia") << " Veces.\n";

    return 0;
}

// Funcion que retorna un valor entero
int al_cubo(int a) {
    return a * a * a;
}