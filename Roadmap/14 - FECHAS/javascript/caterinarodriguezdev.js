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

const currentDate = new Date();
const myBirthDate = new Date(1999, 7, 12, 7, 30, 12);

console.log(`Han transcurrido ${currentDate.getFullYear() - myBirthDate.getFullYear()} años`);

const format1 = { day: 'numeric', month: 'numeric',  year: 'numeric' };
const format2 = { year: '2-digit', month: '2-digit', day: '2-digit' };
const format3 = { year: 'numeric', month: 'long', day: 'numeric' };
const format4 = { weekday: 'short', month: 'short'};
const format5 = { weekday: 'long', month: 'long', day: 'numeric' };
const format6 = { weekday: 'short', day: 'numeric', month: 'short' };
const format7 = { month: 'long', year: 'numeric' };
const format8 = { day: 'numeric', month: 'numeric' };
const format9 = { month: 'long'};
const format10 = { weekday: 'long'};

console.log(myBirthDate.toLocaleDateString('es-ES', format1));
console.log(`${myBirthDate.getHours()} horas, ${myBirthDate.getMinutes()} minutos y ${myBirthDate.getSeconds()} segundos`);
console.log(myBirthDate.toLocaleDateString('es-ES', format3));
console.log(myBirthDate.toLocaleDateString('es-ES', format4));
console.log(myBirthDate.toLocaleDateString('es-ES', format5));
console.log(myBirthDate.toLocaleDateString('es-ES', format6));
console.log(myBirthDate.toLocaleDateString('es-ES', format7));
console.log(myBirthDate.toLocaleDateString('es-ES', format8));
console.log(myBirthDate.toLocaleDateString('es-ES', format9));
console.log(myBirthDate.toLocaleDateString('es-ES', format10));