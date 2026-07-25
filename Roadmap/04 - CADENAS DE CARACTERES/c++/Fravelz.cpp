#include <iostream> 
#include <string>
#include <vector>

using namespace std;

// ********************** #04 - Cadena de Caracteres ********************** //

bool palindromos(string texto);
bool anagramas(string texto1, string texto2);
bool isogramas(string texto1);

int main() {
    /*
    Hay en c++, hay 2 formas basicas de crear una cadena de caracteres:
    1. char[10] (El objecto char como vector)
    2. string (Libreria Estandar)
    */

    char texto1[11] = "Hola Mundo";

    string texto2 = "Hola Mundo :)";
    
    //* Insersion en flujo de salida (Insertar datos para imprimir en pantalla)

    cout << texto1 << " - " << texto2 << '\n'; // Hola Mundo - Hola Mundo :)
    
    //* Concatenacion

    // Se puede concatenar si el primer objecto es string

    cout << (texto1 + texto2) << "\n"; // Hola MundoHola Mundo :)
    cout << (texto2 + " # 2") << "\n"; // Hola Mundo :) # 2
    cout << (texto2 + " + " + texto1) << "\n"; // Hola Mundo :) + Hola Mundo

    //* Indexacion
    cout << (texto1[1]) << "\n"; // o 
    cout << (texto2[5]) << "\n"; // M
    cout << (texto2.at(5)) << "\n"; // M (lanza error si se sale del rango)

    //! (Char no tiene Las siguientes propiedad)

    //* Longitud (Esos dos son lo mismo y llaman a la misma funcion interna)
    cout << (texto2.length()) << "\n"; // 13 (Solo para string)
    cout << (texto2.size()) << "\n"; // 13 (Para contenedores, como arreglos)
    
    //* Slicing (Porcion)
    cout << (texto2.substr(5, 8)) << "\n"; // Mundo :)
    
    //* Busqueda
    cout << (texto2.find(":)")) << "\n"; // 11

    //* Remplazar
    texto2.replace(5, 5, "universo"); 
    cout << texto2; // Hola universo :)

// ********************** Ejercicio Dificultad Extra ********************** //
    cout << '\n';

    cout << palindromos("ini")        << '\n'; // 0 (true)
    cout << palindromos("hola")       << '\n'; // 1 (false)

    cout << anagramas("roma", "amor") << '\n'; // 1 (false)
    cout << anagramas("roma", "amo")  << '\n'; // 0 (true)

    cout << isogramas("Suma")        << '\n'; // 1 (false)
    cout << isogramas("intestinos")  << '\n'; // 0 (true)


    return 0;
}

bool palindromos(string texto) {
    string new_texto;

    for (int x = texto.length(); x > 0; x--) {
        new_texto += texto[x-1];
    }


    if (new_texto == texto) { return true; }
    return false;
};

bool anagramas(string texto1, string texto2) {
    
    auto encontrar = [](char caracter, string text) {
        int contador = 0;

        for (char i : text) {
            if (i == caracter) { contador++; }
        }
        return contador;
    };

    for (char caracter1 : texto1) {
        if (encontrar(caracter1, texto1) != encontrar(caracter1, texto2)){
            return false;
        }
    }
    return true;
}

bool isogramas(string texto1) {
    int veces = 0;
    
    auto encontrar = [](char caracter, string text) {
        int contador = 0;

        for (char i : text) {
            if (i == caracter) { contador++; }
        }
        return contador;
    };

    veces = encontrar(texto1[0], texto1);

    for (char caracter1 : texto1) {
        if (encontrar(caracter1, texto1) != veces){
            return false;
        }
    }
    return true;
}