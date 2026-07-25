//Sitio web de lengauje c++ https://isocpp.org/

//comentario de una linea

/*comentario 
de varias lineas*/

#include <iostream>
#include <string>

using namespace std;

int main()
{
    string miVariable = "Variable"; //variable
    miVariable = "Mi nueva variable"; //variable modificada
    
    const string variableConst = "Variable constante"; //variable constante

    //datos primitivos
    int num1 = 10; //entero
    float num2 = 3.14; //flotante
    double num3 = 3.14159; //double, el más usados para decimales
    char caracter = 'A'; //caracter
    bool booleano = true; //booleano
    string texto = "Hello, world!"; //cadena de texto

    cout << "Hello, C++" << endl;

    return 0;
}