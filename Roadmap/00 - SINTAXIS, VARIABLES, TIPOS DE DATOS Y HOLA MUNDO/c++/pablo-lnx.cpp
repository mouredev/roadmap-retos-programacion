#include <iostream>
#include <string>
using namespace std;

/* 
Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
Representa las diferentes sintaxis que existen de crear comentariosen el lenguaje (en una línea, varias...).
Crea una variable (y una constante si el lenguaje lo soporta).
Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
*/

// Web Oficial de C++ -> https://isocpp.org/ 

/* Inicio del 
código */

// Tipos de datos
    
// 'int'
int myInt = 112; 

// 'float'
float myFloat = 7.9234;

// 'double'
double myDouble = 7.834758923745;

// 'char'
char myChar = 'p';

// 'string'
string myString = "Aprendiendo C++";

int main(){
    // Ejemplo práctico:
    
    // Creación de una constante: const type variableName = value;
    const float PI = 3.141516;

    // Creación de una varible: type variableName = value;
    int radio = 15;
    double area = radio * radio * PI;

    // Imprime el resultado en la terminal
    cout << "Area: "<< area << endl;

    // Muestra en pantalla "Hola C++"
    string language = "C++";
    cout << "Hola " << language;

    return 0;
}