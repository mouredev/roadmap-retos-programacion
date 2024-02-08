// #06 RECURSIVIDAD

/**
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 */

function toZero(num) {
	if (num < 0) {
		return;
	} else {
		console.log(num);
		// num = num - 1;
		return toZero(num - 1);
	}
}

toZero(100);

/** DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 */
function nFactorial(num) {
	if (num === 0 || num === 1) {
		return 1;
	} else {
		return num * nFactorial(num - 1);
	}
}

nFactorial(4);
nFactorial(0);
nFactorial(1);
nFactorial(10);

/** - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
 */

const fibonacci = (position) => {
	if (position === 0) {
		return 0;
	} else if (position === 1) {
		return 1;
	} else {
		return fibonacci(position - 1) + fibonacci(position - 2);
	}
};

fibonacci(0);
fibonacci(1);
fibonacci(10);
fibonacci(26);
