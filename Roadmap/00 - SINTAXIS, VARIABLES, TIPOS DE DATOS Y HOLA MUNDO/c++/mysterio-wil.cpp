// EJERCICIO:
// - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
//   https://isocpp.org/

#include <iostream>
#include <string>

// - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

// Esto es un comentario de una línea

/*
Esto es un comentario
de varias líneas
*/

int main() {
    // - Crea una variable (y una constante si el lenguaje lo soporta).
    std::string myVariable = "Mi variable";
    const std::string MY_CONSTANT = "Mi constante";

    // - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
    int myInt = 10;
    float myFloat = 10.5f;
    double myDouble = 10.555;
    char myChar = 'a';
    bool myBoolean = true;
    std::string myString = "Cadena de texto"; // En C++, std::string es una clase, no un tipo primitivo.

    // - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
    std::cout << "¡Hola, C++!" << std::endl;

    return 0;
}
