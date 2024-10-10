//este lenguaje no tiene web oficial 
//comentario de una linea 
/*
    comentario de varias lineas
    todos los valres de bits que se ponen pueden ser variables dependiendo del compilador y arquitectura
    ¿hey brais puedes compartir los playlists de rock que usas para tus directos?

    este es el valor maximo que se puede representar con respecto a los bit que se maneja unsigned 
    8 bits  (1 byte)  = 255
    16 bits (2 bytes) = 65,535
    32 bits (4 bytes) = 4,294,967,295
    64 bits (8 bytes) = 18,446,744,073,709,551,615

    signed se puede manejar en estos rangos 
    8 bits  (1 byte)  = -128 a 127
    16 bits (2 bytes) = -32,768 a 32,767
    32 bits (4 bytes) = -2,147,483,648 a 2,147,483,647
    64 bits (8 bytes) = -9,223,372,036,854,775,808 a 9,223,372,036,854,775,807

    los valores de c++ son automaticamente signed 

*/
#include <iostream>
#include <string>
using namespace std;

int main() {
    const string constante = "C++";
    string variable = "¡Hola, ";

    //hay diferentes valores numericos
    short corto = 65524;//este es de 16 bits 
    int entero = 4294967294;//este es de 32 bits o 16 bits dependiendo del compilador
    long largo = 4294967294;//este es de 32 bits
    long long gigante = 18446744073709551614;//este es de 64 bits

    float flotante = 3.141592;
    double doble =  3.141592653589793;
    long double giganteDoble = 1.000000000000001;
    float scientifico = 6.02E23; //el float también puede usar notación cientifica

    //también se pueden declarar los valores sin signo
    unsigned short cortoSinSigno = 65535;
    //también está el constexpr que es un valor que se va a calcular mientras se conpila no mientras se corre
    constexpr float PI = 3.14159265358979323846;
    //y se puede usar el auto que lo detecta automatico
    auto autoDetectado = 3;
    
    //hay diferentes valores de texto
    char caracter = 'a';
    string texto = "Hola, C++";
    char ascii = 65; //el char también puede ser un valor ascii

    //y está el bool 
    bool booleano = true;

    cout << texto;
    return 0;
}