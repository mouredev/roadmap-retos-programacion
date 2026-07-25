#include <iostream>
using namespace std;

// la web oficial es: https://isocpp.org/

/* otra forma de 
comentar */

//comentario de una linea


int vida = 52;
string perros = "doce";
double flotante = 22;
char letra = 'N';
bool falsito = false;
string lenguaje = "C++";


int numeroBalas = 25, armorTotal = 78, hpLeft = 62;
const int miConstante = 12;




int main()
{
    cout << "esto anda de 10" << ", Test si funciona" << endl;
    cout << "La vida int es: " << vida << endl;
    cout << "El string total de perros es: " << perros << endl;
    cout << "el numero float es: " << flotante << endl;
    cout << "La letra es: " << letra << endl;
    cout << "El booleano es: " << falsito << endl;
    cout << "Lo siguiente suma los valores de: numerosBalas, armorTotal y hpLeft \nestadisticas de un juego por ejemplo." << endl;
    cout << "La suma de los ints es: " << numeroBalas + armorTotal + hpLeft << endl;
    cout << "mi constante es:" << miConstante << endl;
    cout << "Hola, mi lenguaje es: " << lenguaje << ", y estoy encantado de ir aprendiendo." << endl;
    return 0;

}


