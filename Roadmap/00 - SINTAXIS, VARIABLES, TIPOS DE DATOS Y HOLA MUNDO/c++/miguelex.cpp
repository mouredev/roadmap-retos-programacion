// Documentación en https://devdocs.io/cpp/

// Comentario en una linea

/*
Comentario
en varias
lineas
*/

#include <iostream>
#include <string>

int main()
{

    // Declaramos una variable
    int unaSimpleVariable = 1;

    // Constante
    const double PI = 3.14159;

    // Tipos de datos primitivos
    int entero = 1;
    unsigned int enteroSinSigno = 120;
    short enteroCorto = 10;
    unsigned short enteroCortoSinSigno = 10;
    long enteroLargo = 123456789;
    unsigned long enteroLargoSinSigno = 876543210;
    long long enteroLargoLargo = 1236547899;
    unsigned long long enteroLargoLargoSinSigno = 999999999;
    float puntoFlotante = 3.1415f;
    double puntoFlotanteDoble = 2.71828;
    long double puntoFlotanteLargo = 0.123456789;
    char caracter = 'a';
    unsigned char caracterSinSigno = 'a';
    wchar_t caracterAmplio = L'a';
    bool Verdadero = true;
    bool Falso = false;
    std::string cadenaDeTexto = "En C++ tenemos cadenas";
    int *punteroEntero = &entero;

    // Impresión por consola
    std::cout << "Hola, C++!" << std::endl;
}