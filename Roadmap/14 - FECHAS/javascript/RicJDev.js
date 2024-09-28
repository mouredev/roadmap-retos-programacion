/*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
 */

const monthArr = [
	'Enero',
	'Febrero',
	'Marzo',
	'Abril',
	'Mayo',
	'Junio',
	'Julio',
	'Agosto',
	'Septiembre',
	'Octubre',
	'Noviembre',
	'Diciembre',
];

const daysArr = [
	'Domingo',
	'Lunes',
	'Martes',
	'Miércoles',
	'Jueves',
	'Viernes',
	'Sábado',
];

//EJERCICIO
console.log('\nFecha actual:');
let now = new Date();
console.log(now);

console.log('\nFecha de nacimiento:');
let birthDate = new Date(2002, 8, 22, 12, 0, 34, 676);
console.log(birthDate);

let age = Math.floor(
	(now.getTime() - birthDate.getTime()) / (365 * 24 * 60 * 60 * 1000)
);

console.log(`\nTengo ${age} años de edad`);

//EXTRA
console.log('\nFecha de nacimiento con distintos formatos:');

console.log(
	`\nDía, mes y año: ${birthDate.getDate()}.${
		birthDate.getMonth() + 1
	}.${birthDate.getFullYear()}`
);

console.log(
	`\nHora, minuto y segundo: ${birthDate.getHours()}:${birthDate.getMinutes()}.${birthDate.getSeconds()}`
);

dayAtTheYear = Math.floor(
	(birthDate - new Date(birthDate.getFullYear(), 0, 0)) / (24 * 60 * 60 * 1000)
);
console.log(`\nDía del año: ${dayAtTheYear}`);

console.log(
	`\nDía de la semana: ${daysArr[birthDate.getDay()]} ${birthDate.getDate()}`
);

console.log(`\nNombre del mes: ${monthArr[birthDate.getMonth()]}`);

console.log(`\nEn inglés: ${birthDate.toDateString()}`);

console.log(`\nHora local: ${birthDate.toLocaleTimeString()}`);

let UnixTimeYears = Math.floor(
	birthDate.getTime() / (365 * 24 * 60 * 60 * 1000)
);
console.log(
	`\nContando los años desde el 1 de enero de 1970 hasta esa fecha: ${UnixTimeYears} años`
);

let UnixTimeDays = Math.floor(birthDate.getTime() / (24 * 60 * 60 * 1000));
console.log(
	`\nContando los días desde el 1 de enero de 1970 hasta esa fecha: ${UnixTimeDays} días`
);

let myMomBirthDate = new Date(1978, 11, 25, 21, 15);
let diference = Math.floor(
	(birthDate.getTime() - myMomBirthDate.getTime()) / (365 * 24 * 60 * 60 * 1000)
);
console.log(`\nContando los años desde el nacimiento de mi mamá: ${diference} años`);
