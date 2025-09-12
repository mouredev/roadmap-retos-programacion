// Bibliotecas requeridas
#include <iostream>
#include <string>

// URL del sitio web oficial de C++
// https://isocpp.org/
// Comentarios de una línea

/*
Comentario que 
requiere de 
varias lineas 
*/

/* 
En c++ existen un monton de datos primitivos, cada uno se usa para cumplir con una necesidad,
sin embargo, los mas usados y conocidos son:
- int
- float
- double
- char
- string
- bool 
*/

// Variable
int unaSimpleVariable = 42;

// Constante
const double PI = 3.14159;

// Tipos de datos primitivos
// Enteros
int entero = 42;
unsigned int enteroSinSigno = 123;
short enteroCorto = 10;
unsigned short enteroCortoSinSigno = 20;
long enteroLargo = 12345;
unsigned long enteroLargoSinSigno = 67890;
long long enteroLargoLargo = 987654321;
unsigned long long enteroLargoLargoSinSigno = 876543210;

// Punto flotante
float puntoFlotante = 3.14f;
double puntoFlotanteDoble = 2.71828;
long double puntoFlotanteLargo = 0.123456789;

// Caracteres
char caracter = 'A';
unsigned char caracterSinSigno = 'B';
wchar_t caracterAmplio = L'C';

// Booleano
bool booleanoVerdadero = true;
bool booleanoFalso = false;

// Cadenas de texto
std::string cadenaDeTexto = "Hola, C++!";

// Punteros
int* punteroEntero = &entero;


int main() {
    // Imprimir por terminal
    std::cout << "¡Hola, C++!" << std::endl;

    return 0;
}
