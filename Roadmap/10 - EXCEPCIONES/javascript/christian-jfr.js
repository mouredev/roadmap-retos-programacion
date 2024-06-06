// #10 EXCEPCIONES

/**
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 */
// Manejo de excepciones con try/catch + finally (Opcional)
function testProgram() {
	try {
		// forzar un TypeError
		console.lo('this message will not be displayed due to a TypeError');
	} catch (error) {
		console.error(error); // TypeError: Cannot read property 'lo' of undefined
	} finally {
		console.log('the "finally" block will always be executed');
	}
	// El programa se sigue ejecutando normalmente
	console.log('Program continues to run normally');
}

testProgram();

/* * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
 */

class InvalidCharacterError extends Error {
	constructor(message) {
		super(message);
		this.name = 'Invalid Character in Name';
	}
}

function validateUserData(id, name) {
	// Validación de tipo de dato
	if (typeof id !== 'number' || id <= 0) {
		throw new TypeError('ID must be a positive number');
	}
	if (typeof name !== 'string' || name.length === 0) {
		throw new Error('NAME must be a non-empty string');
	}

	// Validación de tipo de caracteres
	const validName = /^([a-zA-Z]+)\s([a-zA-Z]+)$/.test(name);
	if (!validName) {
		throw new InvalidCharacterError(
			'NAME must only contain alphabetic characters and spaces'
		);
	}

	// Si no hay errores, se crea el objeto user
	const user = {
		id: id,
		name: name,
	};

	return user;
}

// Usos

try {
	const user1 = validateUserData(1, 'Leia Organa'); // Sin errores
	console.log('User created:', user1);
} catch (error) {
	console.error('Error type:', error.name);
	console.error('Error message:', error.message);
} finally {
	console.log('The execution has ended.');
}

try {
	const user2 = validateUserData(true, 'Anakin Skywalker'); // TypeError
	console.log('User created:', user2);
} catch (error) {
	console.error('Error type:', error.name);
	console.error('Error message:', error.message);
} finally {
	console.log('The execution has ended.');
}

try {
	const user3 = validateUserData(123, ''); // Error
	console.log('User created:', user3);
} catch (error) {
	console.error('Error type:', error.name);
	console.error('Error message:', error.message);
} finally {
	console.log('The execution has ended.');
}

try {
	const user4 = validateUserData(-7, 'Han Solo'); // TypeError
	console.log('User created:', user4);
} catch (error) {
	console.error('Error type:', error.name);
	console.error('Error message:', error.message);
} finally {
	console.log('The execution has ended.');
}

try {
	const user5 = validateUserData(10, 'Luke Skywalker.08'); // InvalidCharacterError
	console.log('User created:', user5);
} catch (error) {
	console.error('Error type:', error.name);
	console.error('Error message:', error.message);
} finally {
	console.log('The execution has ended.');
}
