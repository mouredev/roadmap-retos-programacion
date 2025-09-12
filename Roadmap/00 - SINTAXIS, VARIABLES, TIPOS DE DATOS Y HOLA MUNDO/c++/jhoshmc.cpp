/*
? EJERCICIO:
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
//* citio que creo que es el oficial: https://cplusplus.com/
//* la sintaxis para un  comentaio de una sola línea se representa por dos barras

/*
 * En su contrario, la sintaxis para un comentario 
 *  de varias lieas se representa por un inicio de una barra seguido de un asterisco
 * y terminando de un asterirsco seguido por una barra, esto el text en medio
 
*/
// *esta es una variable de tipo entera, solo acepta numeros enteros
int variableEntera = 1; 
//* esta es una variable constante pero su tipo es flotante, acepta numeros flotantes y enteros
const float fl = 0.5;

int entero= 1; // hacepra valor entero
float flotante= 1.5; // acepta valores enteros y flotantes
bool booleano = true; // acepta solo dos valores, true o false;
double db = 1.6543; // es como un float pero con mayor cantidad de bits
char letra = 'a'; // hacepra un caracter
// hacepra una cadena de caracteres, va entre comillas dobles
//* string palabra = "hola a todos"; 
int array[5];// almacenamiento por celdas continuas en la memoria ram, puden ser números , caracteres, palabras, todo dependiendo del tipo en el que se declaren.

// Vector es como un array, pero con más funcionalidades, según yo :v
//* vector<string> vectorDePalabras(6);

#include <iostream>
#include <vector>
using namespace std;
int main()
{
  cout << "¡ Hola, C++ !" << endl;
  return 0;
}