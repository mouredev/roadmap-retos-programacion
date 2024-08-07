/*
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */

// https://cplusplus.com/

// Comentario de una linea

/*
Comentario
de
varias lineas
*/

#include <iostream>

using namespace std;

#define PI 3.1416; // Definimos una constante llamada PI

int main()
{
    string miVariable = "C++";

    // Tipos Enteros
    int myInt = 23;
    short myShort = 7;
    long myLong = 8888888888;
    long long myLongLong = 999999999999999;
    // Tipos de Punto Flotante
    float myFloat = 3.14;
    double myDouble = 33.3333;
    long double myLongDouble = 33333.333333;
    // Tipo Carácter
    char myChar = 'a';
    signed char mySignedChar = -65;
    unsigned char myUnsignedChar = 200;
    wchar_t myWideChar = L'Ω';
    // Tipo Booleano
    bool myBool = true;
    // Tipos de Caracteres Unicode
    char16_t myChar16 = u'Ω';
    char32_t myChar32 = U'Ω';

    cout << "¡Hola, C++!" << endl;
    return 0;
}