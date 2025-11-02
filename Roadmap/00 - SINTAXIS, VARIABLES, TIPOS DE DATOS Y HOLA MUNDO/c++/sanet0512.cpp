// https://isocpp.org/
// Comentario de una linea

/* Comentario 
  de
  multiples
  Lineas */

//Variable

int numero = 9 ; 

//Constante 

const tipo nombre = valor;

/* 
tipo: Especifica el tipo de datos de la constante.
nombre: Es el nombre único que se le da a la constante.
valor: Es el valor constante que se asigna a la constante. 
*/

const double PI = 3.14159;

std::cout << PI << std::endl; // Imprime: 3.14159

PI = 3.5; // ❌ Esto dará un error, no puedes reasignar una constante

//Tipos de Variables 

int edad = 0;
float altura = 0.0f;
double peso = 0.0;
char inicial = '\0';
bool esEstudiante = false;

//Para imprimir por la terminal el texto

#include <iostream>

int main() {
    // Imprime la cadena de texto en la terminal.
    std::cout << "¡Hola, C++!" << std::endl;
    
    // Opcional: También puedes usar '\n' en lugar de std::endl, a menudo es más rápido.
    // std::cout << "¡Hola, C++!\n";

    return 0; 
}
