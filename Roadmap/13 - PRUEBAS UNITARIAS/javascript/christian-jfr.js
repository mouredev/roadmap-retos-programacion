// #13 PRUEBAS UNITARIAS

/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 */

// Funciones para hacer las pruebas test() y assert()
function test(desc, fn) {
	try {
		fn();
		console.log('\x1b[32m%s\x1b[0m', '\u2714 ' + desc + ' PASSED');
	} catch (error) {
		console.log('\n');
		console.log('\x1b[31m%s\x1b[0m', '\u2718 ' + desc + ' FAILED');
		console.error(error);
	}
}

function assert(isTrue) {
	if (!isTrue) {
		throw new Error();
	}
}

function add(num1, num2) {
	if (typeof num1 !== 'number' || typeof num2 !== 'number') {
		return 'You must provide two numbers';
	} else {
		let result = Number((num1 + num2).toFixed(2));
		return result;
	}
}

// test que deberia pasar
test('add two numbers', function () {
	assert(add(1, 2) === 3);
});

// test que deberia fallar
test('add two numbers', function () {
	assert(add(1, 2) !== 3);
});

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
 */

const student = {
	name: 'Christian',
	age: 21,
	birth_date: {
		day: 1,
		month: 5,
		year: 2003,
	},
	programming_languages: ['JavaScript', 'Python', 'C++'],
};

const testFields = () => {
	if (
		student.name &&
		student.age &&
		student.birth_date &&
		student.birth_date.day &&
		student.birth_date.month &&
		student.birth_date.year &&
		student.programming_languages
	) {
		return true;
	} else {
		return false;
	}
};

const testValues = () => {
	if (
		typeof (student.name === 'string') &&
		typeof (
			student.age === 'number' &&
			Number.isInteger(student.age) &&
			student.age > 0
		) &&
		typeof (student.birth_date === 'object') &&
		typeof (
			student.birth_date.day === 'number' &&
			Number.isInteger(student.birth_date.day) &&
			student.birth_date.day > 0 &&
			student.birth_date.day < 32
		) &&
		typeof (
			student.birth_date.month === 'number' &&
			Number.isInteger(student.birth_date.month) &&
			student.birth_date.month > 0 &&
			student.birth_date.month < 13
		) &&
		typeof (
			student.birth_date.year === 'number' &&
			Number.isInteger(student.birth_date.year) &&
			student.birth_date.year > 0
		) &&
		typeof (student.programming_languages === 'object')
	) {
		return true;
	} else {
		return false;
	}
};

test('fields exist?', function () {
	assert(testFields());
});

test('values are correct?', function () {
	assert(testValues());
});
