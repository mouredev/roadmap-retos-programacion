/* EJERCICIO : Crea un comentario en el código y coloca la URL del sitio web oficial del
            lenguaje de programación que has seleccionado.Representa las diferentes sintaxis que existen de crear comentarios
            en el lenguaje(en una línea, varias...)
            .Crea una variable(y una constante si el lenguaje lo soporta)
            .Crea variables representando todos los tipos de datos primitivos del lenguaje(cadenas de texto, enteros, booleanos...)
            .Imprime por terminal el texto : "¡Hola, [y el nombre de tu lenguaje]!" */

#include <iostream>
#include <stdio.h>

#define MaxValue 256 // Constante

using namespace std;

int main()
{
    int value = 3;         // enteros
    float pi = 3.14;       // decimales
    bool verdadero = true; // booleanos
    bool falso = false;
    char letter = 'a';            // de caracter
    string hello = "Hola C++!\n"; // cadena de caracteres

    cout << hello;

    system("pause");
    return 0;
}

/*
comentario
en varias
lineas
*/
