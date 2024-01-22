// @RoniPG

#include <iostream>
#include <cmath>

using namespace std;

//Variables globales

//Declaraciones

//Al declarar una variable permitimos que sea vista por todo el programa
int a = 1;
//Funciones

//Declaraciones

//Al declarar una funcion permitimos que sea vista por todo el programa
void Resultados();
int X(string a, string b);

//Funcion de suma
/*
 * Las funciones pueden no recibir ningun parametro o pueden recibir varios parametros
 * Pueden tener un valor de retorno (return) que se devuelve al invocar la funcion
 * El return debe coincidir con el tipo de la funcion
 */

int Suma(int numA, int numB) {

	int result = numA + numB;

	return result;

}
int Resta() {
	/*int SegundaResta(int b) {
	 return 0;}
	 Podemos comprobra al descomentar este codigo que no podemos crear funciones dentro de funciones
	 */
	return 0;
}

//Llamadas a funciones dentro de funciones
int Resultsuma(int numA, int numB) {

	int result = numA + numB;
	Resultados(); // ---> Podemos realizar llamadas a funciones dentro otra que esten previamente declaradas
	return result;

}
int AccesoVariables() {
	int a = 0; // ---> Variable Local (Solo existe dentro de la funcion)
	return a;
}

//Funcion que no necesita valor de retorno
void Resultados() {
	cout << "El resultado de la suma es:" << Suma(2, 3) << endl;

}

int main() {

	//Llamadas a Funciones

	cout << Suma(2, 3) << endl;
	Resultados();
	cout << Resultsuma(2, 3) << endl;

	//Llamadas a Funciones predefinidas de C++

	cout << sqrt(16) << endl;

	//Comprobamos las variables locales y las globales

	cout << "Accedemos a la variable local a con valor : " << AccesoVariables() << endl;
	cout << "Comprobamos la variable global a : " << a << endl;

/*  DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
	cout << "Se ha impreso un numero: " << X("Soy multiplo de 3", "Soy multiplo de 5") << " veces" << endl;

	return 0;
}
int X(string a, string b) {
	int contador = 0;
	for (int i = 1; i < 100; i++) {
		if ((i % 5 == 0) && (i % 3 == 0)) {
			cout << a << " y tambien " << b << endl;
		} else if (i % 3 == 0) {
			cout << a << endl;
		} else if (i % 5 == 0) {
			cout << b << endl;
		} else {
			cout << i << endl;
			contador++;
		}

	}
	return contador;
}
