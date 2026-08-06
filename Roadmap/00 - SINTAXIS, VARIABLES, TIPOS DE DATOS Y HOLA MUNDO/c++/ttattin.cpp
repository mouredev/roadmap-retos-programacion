// https://isocpp.org/

// Esto es un comentario de una línea

/* Esto es un 
   comentario de
   varias líneas */

/* Esto es un 
 * comentario de
 * varias líneas
 * mas bonito */

#include <iostream>
#include <string>

int main() {
    const int a = 10; // esto es una constante
    bool b = true;    // esto es una variable booleana
    int c = 20;       // esto es una variable entera
    float d = 3.14;   // esto es una variable flotante
    double e = 3.14;  // esto es una variable doble
    char f = 'a';     // esto es una variable caracter
    std::string g = "hola"; // esto es una variable cadena. necesita la librería string

    std::cout << "¡Hola, C++!" << std::endl;
}