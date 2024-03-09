/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
 */

#include <vector>
#include <stack>
#include <iostream>

class MyExceptionType : public std::exception
{
	public:
 	virtual const char* what() const throw();
};

const char* MyExceptionType::what() const throw() {

	return "Mi propia excepción";
};

void testException (int throwOutOfRangeException, 
	int throwIntException, 
	int throwMyExceptionType) throw () {

	std::vector<int> myVector;
	MyExceptionType myException;
	
	if (throwOutOfRangeException) {

		std::cout << myVector.at (5) << "\n";

	} else if (throwIntException) {

		throw (2);

	} else if (throwMyExceptionType) {

		throw myException;
	};

	std::cout << "Fin funcion testException sin errores";
};

int main() {

	//In c++ no exception is thrown in divide by zero
	
	std::vector<int> myVector;

	try {
		//Error as vector is empty
		std::cout << myVector.at (5) << "\n";
	} catch (std::out_of_range& myException) {
		std::cout << myException.what() << "\n";
	};

	std::cout << "Programa continua\n";

	try {
		testException (0, 0 , 1);
	} catch (std::out_of_range& myOutOfRange) {
		std::cout << myOutOfRange.what() << "\n";
	} catch (MyExceptionType& myExceptionType) {
		std::cout << myExceptionType.what() << "\n";
	} catch (int& i) {
		std::cout << "Excepcion int " << i << "\n";
	};

	std::cout << "Fin\n";
}
