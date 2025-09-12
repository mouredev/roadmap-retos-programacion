// Comentario en una linea

/*
Comentario
en varias
lineas
*/

#include <iostream>
#include <string>

using namespace std;

int main(){
    // Variable
    int variable = 9;
    // Constante
    const int constante = 8;

    //Tipos de datos primitivos
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
    string cadenaDeTexto = "En C++ tenemos cadenas";
    int *punteroEntero = &entero;

    string lenguaje = "C++";
    cout<<"Hola "<<lenguaje<<"!"<<endl;
}
