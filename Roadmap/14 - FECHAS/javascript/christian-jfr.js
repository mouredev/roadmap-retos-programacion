// #14 FECHAS

/*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 */

let currentDate = new Date();
const birthDate = new Date('1987-09-26T03:15:00');

const millisecondsInYear = 1000 * 60 * 60 * 24 * 365;

let howManyYearsHavePassed = (currentDate - birthDate) / millisecondsInYear;
let yearsPassed = howManyYearsHavePassed.toFixed(2);

console.log(yearsPassed);

/*
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

// 1
const birthDateFormated1 = birthDate.toDateString();
console.log(birthDateFormated1); // Sat Sep 26 1987

// 2
const birthDateFormated2 = birthDate.toLocaleDateString('es-CO', {
	weekday: 'long',
	year: 'numeric',
	month: 'long',
	day: 'numeric',
});
console.log(birthDateFormated2); // sábado, 26 de septiembre de 1987

// 3
const birthDateFormated3 = birthDate.toLocaleDateString('es-CO', {
	weekday: 'short',
	year: 'numeric',
	month: 'numeric',
	day: 'numeric',
});
console.log(birthDateFormated3); // sáb, 26/9/1987

// 4
console.log(birthDate.toLocaleTimeString()); // 03:15:00 AM

// 5
console.log(birthDate.getDate()); // 26

// 6
const dayNames = [
	'Sunday',
	'Monday',
	'Tuesday',
	'Wednesday',
	'Thursday',
	'Friday',
	'Saturday',
];

console.log(dayNames[birthDate.getDay()]); // Saturday

// 7
const months = [
	'January',
	'February',
	'March',
	'April',
	'May',
	'June',
	'July',
	'August',
	'September',
	'October',
	'November',
	'December',
];

console.log(months[birthDate.getMonth()]); // September

// 8
const timePassed = Date.now() - birthDate.getTime();

const seconds = Math.floor(timePassed / 1000);
const minutes = Math.floor(seconds / 60);
const hours = Math.floor(minutes / 60);
const days = Math.floor(hours / 24);

console.log(
	`has been ${days} days, ${hours % 24} hours, ${minutes % 60} minutes and ${
		seconds % 60
	} seconds`
);

// 9
const january_1 = new Date(birthDate.getFullYear(), 0, 1);

const differenceInMilliseconds = birthDate.getTime() - january_1.getTime();

const dayOfYear =
	Math.floor(differenceInMilliseconds / (1000 * 60 * 60 * 24)) + 1;

console.log(`September 26, 1987 was the ${dayOfYear} day of the year.`);

// 10
console.log(birthDate.getFullYear()); // 1987
