// https://isocpp.org/

/*
    Solución al problema #00
    Permite familiarize con c++
*/

#include <iostream>
#include <cstring>
#include <string>

int main() {
    // Variable
    int miVariable = 6174;

    // Constante
    const float PI = 3.1416;

    // Enteros
    short nota = 8;
    unsigned short maximoShort = 65535;
    int anio = 2024;
    unsigned int enteroSinSigno = 4294967295;
    long distanciaSol = 150000000L; // Distancia en km
    unsigned long longSinSigno = 56389213233L;
    long long numeroGrande = 1234567890123456789;
    unsigned long long numeroGrandeSinSigno = 987123456789012345;

    // Punto flotante
    float numeroAureo = 1.618033f;
    double numeroEuler = 2.718281828459045;
    long double largePI = 3.14159265358979323846L;

    // Carácter
    char vocal = 'A';

    // Booleano
    bool verdadero = true;
    bool falso = false;
    bool mayor = 5 > 3;

    // Cadenas
    char nombre[] = "Yeison";
    char lenguaje[10];
    strcpy(lenguaje, "C++");
    std::string apellido = "Garcia";
    std::string nombreCompleto = apellido + " " + nombre;

    // Imprimir
    std::cout << "¡Hola, " << lenguaje << "!" << std::endl;

    // Retorno de la función
    return 0;
}
