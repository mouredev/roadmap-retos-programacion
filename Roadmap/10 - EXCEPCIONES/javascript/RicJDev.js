console.log('\n---CONTROL DE EXCEPCIONES---');

try {
	console.log('\nIniciando comprobación de errores...');
	console.log(variableInexistente);
} catch (error) {
	// console.log(`\nSe ha producido un error:\n${error.name}`); ---> Nombre del error
	// console.log(`\nSe ha producido un error:\n${error.message}`); ---> Mensaje con detalles del error
	// console.log(`\nSe ha producido un error:\n${error.stack}`); ---> Pila de llamadas actual. Utilizado para fines de depuración.
	console.log(`\nSe ha producido un error:\n${error}`);
} finally {
	console.log('\nComprobación de errores terminada :D');
}

console.log('\nEsta string se muestra porque no se ha detenido el programa');

console.log('\n---PROCESANDO PARÁMETROS---');

class CustomError extends Error {
	constructor(message) {
		super(message);
		this.name = 'Usuario baneado';
	}
}

const bannedUser = ['Peg Lewack', 'Abby Constantine', 'Richie Trelawney'];

function comprueba(user, password) {
	console.log('\n* Iniciando comprobación de usuario...');
	try {
		if (arguments.length < 2) {
			throw new Error('Debe ingresar un usuario y una contraseña numérica');
		}
		if (typeof user !== 'string' || typeof password !== 'number') {
			throw new Error(
				'El primer argumento debe ser una cadena de texto y el segundo debe ser un número'
			);
		}
		if (bannedUser.includes(user)) {
			throw new CustomError(
				`${user} ha sido baneado por no cumplir las normas comunitarias`
			);
		}
		console.log('\nNo se detectaron errores.');
		console.log(`\nBienvenido, ${user}!`);
	} catch (error) {
		console.log(
			`\nTipo de error:\n${
				error instanceof CustomError ? 'Custom error' : 'Normal error'
			}`
		);
		console.log(`\nSe produjo un error:\n${error}`);
	} finally {
		console.log('\n* Ha concluido la comprobación :D\n');
	}
}
console.log('\nPrueba 1:');
comprueba('Peg Lewack', 92344);

console.log('\nPrueba 2:');
comprueba(123, 345);

console.log('\nPrueba 3:');
comprueba('Damiano', '1234');

console.log('\nPrueba 4:');
comprueba('Fred');

console.log('\nPrueba 5:');
comprueba('Ric', 2356);
