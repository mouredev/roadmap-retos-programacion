#include <iostream>
using namespace std;

// operadores aritméticos

int suma = 1 + 2; // 3
int resta = 4 - 2; // 2
int multiplicar = 4 * 2; // 8
int division = 80 / 2; // 40
int modulo = 10 % 4; // resto es 2


// Conjunción (&&) chequeo de dos condiciones que se deben cumplir simultaneamente
// no olvidarse el camelCase al declarar
void mostrarValidacion()
{
	cout << "Esto es valido, ha funcionado";
}

// negación !
bool esFalso = !true; // false


int c = 1;
// Disyunción(|| ) : es igual al OR (si una de las dos se cumple, ejecuta)
bool opcionValida = (c == 1) || (c == 2); // true si c es 1 o 2




int main()
{
	cout << "esto funciona" << endl;
	cout << suma << endl;
	cout << resta << endl;
	cout << multiplicar << endl;
	cout << division << endl;
	cout << modulo << endl;
	cout << opcionValida << endl;
	if (multiplicar < 10 && modulo > 0)
	{
		mostrarValidacion();
	}



	return 0;
}
