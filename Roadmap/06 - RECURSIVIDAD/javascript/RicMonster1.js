/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 */

console.log("\nNUMEROS DEL 100 AL 0");
function cuentaAtras(n) {
	if (n >= 0) {
		console.log(n);
		cuentaAtras(n - 1);
	}
}

cuentaAtras(100);

/* DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
 */

console.log("\nFACTORIALES");
const factorial = (n) => {
	if (n < 0) {
		console.log("Numero no valido");
		return 0;
	} else if (n === 0) {
		return 1;
	} else {
		return n * factorial(n - 1);
	}
};

console.log(factorial(5));

console.log("\nSUCESIÓN DE FIBONACCI");
const fibonacci = (n) => {
	if (n <= 0) {
		console.log("Numero no valido");
		return 0;
	} else if (n === 1) {
		return 0;
	} else if (n === 2) {
		return 1;
	} else {
		return fibonacci(n - 1) + fibonacci(n - 2);
	}
};

console.log(fibonacci(23));
