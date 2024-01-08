// Pagina web oficial: https://isocpp.org

/* Comentario
en varias
lineas */

// Utilizaré el paradigma Orientado a Objetos para practicar la Universidad

#include <iostream>

using namespace std;

class TipoVariables{
    private:
    int entero;
    float decimal;
    double muchosDecimales;
    bool booleano;
    string cadenaDeTexto;
    char caracter;
    
    public:
    TipoVariables(){
        // Constructor
        entero = 2;
        decimal = 2.12;
        muchosDecimales = 3.14157;
        booleano = true;
        booleano = false;
        cadenaDeTexto = "Cadena de texto";
        caracter = 'A';
    }
    void print(){
        cout << "Entero: " << entero << endl;
        cout << "Decimal: " << decimal << endl;
        cout << "Double: " << muchosDecimales << endl;
        cout << "Booleano: " << booleano << endl;
        cout << "String: " << cadenaDeTexto << endl;
        cout << "Caracter: " << caracter << endl;
    }
    void hola_lenguaje(string lenguaje){
        cout << "Hola, " << lenguaje << "!\n";
    }
};

int main(){
    TipoVariables variable;
    variable.print();
    variable.hola_lenguaje("C++");
    return 0;
}