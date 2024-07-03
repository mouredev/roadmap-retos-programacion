/*
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
 */

//EJERCICIO
/*
PRINCIPIO ABIERTO-CERRADO:

"Las entidades de software (clases, módulos, funciones, etc.) deben estar abiertas para su extensión, pero cerradas para su modificación"

*/

//EXTRA
class Calculator {
	display(operation, a, b) {
		const operationOptions = {
			add: this.add,
			susbtrac: this.susbtrac,
			multiplicate: this.multiplicate,
			divide: this.divide,
		};

		function defaultfun() {
			console.log('Operacion no soportada o inexistente');
		}

		const fun = operationOptions[operation] || defaultfun;

		fun(a, b);
	}

	add(a, b) {
		console.log(a + b);
	}

	susbtrac(a, b) {
		console.log(a - b);
	}

	multiplicate(a, b) {
		console.log(a * b);
	}

	divide(a, b) {
		console.log(a / b);
	}
}

const calculator = new Calculator();

calculator.display('add', 12, 10);
calculator.display('potencia', 12, 10);
