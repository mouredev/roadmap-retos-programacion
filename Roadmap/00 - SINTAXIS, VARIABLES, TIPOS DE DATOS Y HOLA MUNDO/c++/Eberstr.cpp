
// url: isocpp.org (no hay sitio oficial)

// Esto es un comentario

/* Esto también es un comentario  */

#include <iostream>
using namespace std;

#define constante 1

int main(){
    char variable = 'variable';
    const int constant2 = 2;

    int numero = 10;
    short numeroCorto = 5;
    long numeroLargo = 100000;
    long long numeroMuyLargo = 1000000000;
    unsigned int numeroPositivo = 100;

    char caracter = 'a';
    char string = 'string';
    wchar_t letraUnicode = L'Ω';
    
    bool verdad = true;
    bool falso = false;

    float flotante = 1.2f;
    double float_largo = 1.22222222; // 15 decimales o menos
    long double numeroLargoDoble = 3.14159265358979323846L;

    cout << "¡Hola, C++!";
    return 0;
}