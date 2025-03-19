// URL del sitio web oficial de C++: https://isocpp.org/   
// Generado por Chatgpt

// Comentarios en una línea

/*
   Comentarios
   en varias
   líneas
*/

#include <iostream> // Para poder usar std::cout
#include <string>   // Para poder usar el tipo std::string

// Constante (en C++)
const double PI = 3.14159;

int main() {
    // Variables con diferentes tipos de datos primitivos
    int numeroEntero = 42;
    float numeroDecimal = 3.14f;
    double numeroDoble = 2.718281828;
    bool esVerdadero = true;
    char letra = 'C';
    std::string cadenaDeTexto = "¡Hola, C++!";

    // Imprimir por terminal
    std::cout << "¡Hola, C++!" << std::endl;

    // Imprimir el valor de las variables
    std::cout << "Número Entero: " << numeroEntero << std::endl;
    std::cout << "Número Decimal (float): " << numeroDecimal << std::endl;
    std::cout << "Número Doble (double): " << numeroDoble << std::endl;
    std::cout << "Booleano: " << (esVerdadero ? "Verdadero" : "Falso") << std::endl;
    std::cout << "Carácter: " << letra << std::endl;
    std::cout << "Cadena de Texto: " << cadenaDeTexto << std::endl;

    return 0;
}
