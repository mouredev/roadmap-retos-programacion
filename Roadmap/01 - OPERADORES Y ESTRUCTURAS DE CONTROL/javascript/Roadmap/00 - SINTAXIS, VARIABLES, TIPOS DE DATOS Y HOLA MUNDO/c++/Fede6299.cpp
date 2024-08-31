//  Sitio oficial: https://isocpp.org

//  Comentario de una sola linea.

/*  comentario en 
    varias lineas*/

/*  El Header es necesario para poder hacer uso de los tipos de datos stream, en nuestro caso para dar uso a 
    std::cout (ouput stream).*/

#include <iostream>  

int main(){

    char letra = 'A';
    const unsigned ANIO {2024};

    /* Tipos de datos primitivos/fundamentales */

    // Flotaing Point: Un numero con parte fraccional, 3.14159

    float numero;
    double parte;
    long double fraccional;

    // Integral (Boolean) : true o false, true

    bool booleano;

    // Integral (Character) : Un caracter de texto, 'C'

    char un;
    wchar_t caracter;
    char8_t de;  // C++20
    char16_t texto; // C++11
    char32_t C; // C++11

    // Integral (Integer) : Numeros enteros, positivos y negativos (incluyen el 0), 24

    short enteros;
    int positivos;
    long negativos;
    long long cero;    // C++11

    /*  Integral: dado que cuando estas variables se convierten a binario, el compilador considera a estos
        tipos como numeros enteros */

    // Null Pointer : Puntero nulo, nullptr

    std::nullptr_t p;   // C++11

    // Void : sin tipo (vacio), n/a

    void HolaMundo(); 

    /*  Nota: void es el unico tipo de dato primitivo que con el cual no se pueden definir variables, el contexto
        del uso del void, es para funcion que no devuelvan valores. Como por ejemplo:
        
        void HolaMundo(){
            std::cout << "Hello, world!";
        }

        Dado que hay tipos de datos de C++20, el mismo archivo debe ser compilado en C++20.
        Terminal: g++ Fede6299.cpp -o Fede6299.exe -std=c++20
     
        Otros tipos de datos son los compuestos y tipos de datos definidos por el usuario. Un ejemplo de tipo
        de dato compuesto es el string que en otros lenguajes es un tipo de dato primitivo.
        
        El uso del sufijo _t, signfica type (tipo) que es parte de la nomenclatura estandar de las nuevas versiones
        de C++.*/

    std::cout << "¡Hola, C++!";
}