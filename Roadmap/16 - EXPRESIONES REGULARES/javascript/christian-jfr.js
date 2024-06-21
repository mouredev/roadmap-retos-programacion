// #16 EXPRESIONES REGULARES

/**
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 */

const regex = /\d+/g;

const extractNumbers = (string) => {
	const numbers = string.match(regex);

	return numbers ? numbers : [];
};

console.log(extractNumbers('Hello World')); // -> []
console.log(extractNumbers('Y2024')); // -> [2024]
console.log(extractNumbers('Friday 31 May 2024')); // -> [31, 2024]

/**
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */

// Email
const emailRegex = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;

const validateEmail = (email) => {
	return emailRegex.test(email);
};

validateEmail('LkqZC@example.com'); // -> true

// Phone
const phoneRegex = /^3[0-9]{9}$/;

const validatePhone = (phone) => {
	return phoneRegex.test(phone);
};

validatePhone('123456789'); // -> false
validatePhone('3010101010'); // -> true

// Url
const urlRegex = /^https?:\/\/[\w\-]+(\.[\w\-]+)+[/#?]?.*$/;

const validateUrl = (url) => {
	return urlRegex.test(url);
};

validateUrl('https://retosdeprogramacion.com/roadmap'); // -> true
