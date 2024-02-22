/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */

#include <iostream>

class MyClass {

	private:

		int arg1;
		long arg2;

	public:

		MyClass (int inArg1, int inArg2);

		int getArg1 ();
		long getArg2 ();

		void setArg1 (int inArg1);
		void setArg2 (long inArg2);

		void print ();
};

MyClass::MyClass (int inArg1, int inArg2) :
	arg1 (inArg1), arg2 (inArg2) {
};

int MyClass::getArg1 () {
	return arg1;
};

long MyClass::getArg2 () {
	return arg2;
};


void MyClass::setArg1 (int inArg1) {
	arg1 = inArg1;

};

void MyClass::setArg2 (long inArg2) {
	arg2 = inArg2;
};

void MyClass::print () {
	std::cout << "MyClass : arg1:" << arg1 << ", arg2:" << arg2 << "\n";
};

int main () {

 	MyClass myObject (1, 2);

	myObject.setArg1 (3);
	myObject.setArg2 (4);
	myObject.print();

	return 0;
};
