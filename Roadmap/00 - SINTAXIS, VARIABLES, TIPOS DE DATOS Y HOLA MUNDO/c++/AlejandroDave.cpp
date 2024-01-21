// https://isocpp.org

// Se puede realizar un comentario de una linea utilizando doble diagonal
/* Puedo realizar comentarios de mas de una linea
   encerrando el texto entre /*...*/


#include <iostream>  // Para poder trabajar con c++ necesitamos importar la biblioteca iostream

using namespace std;
// El comando anterior nos ayuda a acortar la escritura de los comandos principalmente de entrada y salida de consola

// En c++ podemos declarar constantes
const int ct = 10;

int main(){

// Variables principales
int i = -40;
float fl = 34.5;
char c = 'C';
string st = "Hola";
double db = 34535364;

// C++ Permite tener una amplia variedad de tipos de variables derivadas de las principales utilizando terminos como "long" o "unsigned" entre otros
unsigned int ui= 455;
long long int lli = 2342353464564;

string lenguaje = "C++";

cout<<"Hola "<<lenguaje<<"!"<<endl;


return 0;
}
