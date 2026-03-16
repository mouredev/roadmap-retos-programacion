#include <iostream>
#include <string>

using namespace std;
// c++ sin web oficial. //

//Esto es un comentario.//

/*
Esto tambien
pero entre
lineas.
*/

int main() { 
//CONST PARA REPRESENTAR UNA CONSTANTE, NO PUEDE CAMBIAR DURANTE EL PROGRAMA.
const int MAX_VIDAS = 5;

// Variables de c++

//INT, SHORT, LONG, LONG LONG, UNSIGNED VARIABLES PARA NUMEROS ENTEROS.
//el mas usado.
int edad = 25;
//entero mas chico, ocupa poca memoria.
short nivel = 5;
//entero mas grande, ocupa mas memoria.
long poblacion = 1000000;
//enteros muy grandes.
long long estrellas = 9999999999;
//solo numeros positivos, sin signo.
unsigned vida = 100;

//FLOAT Y DOUBLE VARIABLES PARA NUMEROS DECIMALES.
//para numeros no tan precisos.
float altura = 1.75;

//para numeros mas precisos.
double precio = 550.55;

//para numeros muy precisos.
long double distancia = 54321.87691;

//STRING Y CHAR VARIABLES PARA TEXTO.
//para solo un caracter.
char letra = 'T';

//para textos.
string nombre = "Tomas";

//BOOLEAN VARIABLE QUE CONTIENE SOLO DOS DATOS.
bool estaQuieto = true;
estaQuieto = false;

//COUT PARA IMPRIMIR EN CONSOLA.
cout << "Hola c++!\n";

//tambien se puede usar para imprimir en consola una variable. 
cout << "Mi edad es: " << edad;  
return 0;
}
