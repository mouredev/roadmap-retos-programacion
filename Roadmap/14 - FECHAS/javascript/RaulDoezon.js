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

console.log("+++++++++ EJERCICIO +++++++++");
var today = new Date();
var birthday = new Date(1992, 2, 31, 7, 30, 0, 999);
var msPerYear = 24 * 60 * 60 * 365 * 1000;
var years = (today.getTime() - birthday.getTime()) / msPerYear;

console.log(`Fecha actual: ${today}`);
console.log(`Fecha de nacimiento: ${birthday}`);
console.log(`Años transcurridos: ${years}`);

console.log("\n+++++++++ DIFICULTAD EXTRA +++++++++");
console.log(`DÍA: ${birthday.getDate()}`);
console.log(`MES: ${birthday.getMonth() + 1}`);
console.log(`AÑO: ${birthday.getFullYear()}`);
console.log(`DÍA DE LA SEMANA: ${birthday.getDay()}`);
console.log(`HORAS: ${birthday.getHours()}`);
console.log(`MINUTOS: ${birthday.getMinutes()}`);
console.log(`SEGUNDOS: ${birthday.getSeconds()}`);
console.log(`MILISEGUNDOS: ${birthday.getMilliseconds()}`);
console.log(`FECHA: ${birthday.getDate()}/${birthday.getMonth() + 1}/${birthday.getFullYear()}`);
console.log(`HORA: ${birthday.getHours()}:${birthday.getMinutes()}:${birthday.getSeconds()}`);
