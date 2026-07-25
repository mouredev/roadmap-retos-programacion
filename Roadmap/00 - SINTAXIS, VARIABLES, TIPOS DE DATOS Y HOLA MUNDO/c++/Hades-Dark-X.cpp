# include <iostream>
# include <string>
using namespace std;

//-Sitio de C++: https://isocpp.org/

// - Esto es un comentario en un linea

/* -Esto
es un comentario
multilinea */

// - Tipos de datos números enteros
int edad= 16;                               //- Entero con signo
unsigned int puntosGanados= 1500;          //- Entero sin signo, solo valores positivos
short dias= 7;                             //- Entero corto
long poblacionCdmx= 9209944;              //- Entero largo

// - Tipos de datos números decimales
float temperatura= 36.15f;                 //- El sufijo 'f' para indicar que es un float y tiene menos pesición
double altura= 1.78;                       //- Decimal con mayor precisión
long double pi= 3.1415926535;              //- Decimal de alta precicisón

// - Tipos de datos caracter y cadena de carecteres
char miInicial= 'M';                       //- Un único caracter, se respetan las comillas simples
string miNombre= "Marcos";                 //- Es una cadena de texto

// - Tipo de dato booleano
bool aspiranteSelecionado= true;        //- Verdadero o falso

// - Constantes en C++
const string holaMundo= "Hola Mundo!";  //- Se ecribe: cosnt tipo de dato nombre y valor

int main(){

    // - Vamos a mostrar los valores de las variables en pantalla
    cout << "Una constante: " << holaMundo << endl;
    cout << "Nombre: " << miNombre << endl;
    cout << "Inicial: " << miInicial << endl;
    cout << "Edad: " << edad << endl;
    cout << "Temperatura: " << temperatura << endl;
    cout << "Altura: " << altura << endl;
    cout << "Puntos Ganados: " << puntosGanados << endl;
    cout << "Días de la semana: " << dias << endl;
    cout << "Población de CDMX: " << poblacionCdmx << endl;
    cout << "Número Pi: " << pi << endl;
    cout << "Asipirante Seleccionado: " << aspiranteSelecionado << endl;
    return 0;
}