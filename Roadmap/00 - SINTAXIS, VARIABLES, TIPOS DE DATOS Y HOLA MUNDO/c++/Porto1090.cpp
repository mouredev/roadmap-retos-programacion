#include <iostream>
using namespace std;

int main()
{
    // https://isocpp.org

    // Comentario de una sola línea

    /*
    Este es un comentario 
    compuesto
    de varias líneas
    */

    //VARIABLES
    int entero = 5;
    float flotante = 4.5f;
    string cadena = "Cadena en C++";
    double Double = 5.6;
    bool boolean = true;
    char caracter = 'D';

    //CONSTANTE
    const float constante = 3.14f;

    //SALIDA POR TERMINAL
    cout << entero << endl;
    cout << flotante << endl;
    cout << cadena << endl;
    cout << Double << endl;
    cout << boolean << endl;
    cout << caracter << endl;
    cout << constante << endl;

    //TERMINAL
    string cPlusPlus = "C++";
    cout << "Hola " + cPlusPlus << endl;

    return 0;
}