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

// Ejercicio 1
const fechaActual = new Date();
console.log(fechaActual);

const fechaNacimiento = new Date(1998, 10, 5, 1, 0, 0);
console.log(fechaNacimiento);

const tiempoTranscurrido =
  fechaActual.getFullYear() - fechaNacimiento.getFullYear();
console.log(`\nHan transcurrido ${tiempoTranscurrido} años.`);

// Ejercicio extra
const nacimiento = new Date("1998-11-05T04:05:12Z");

const year = nacimiento.getFullYear();
const day = nacimiento.getDay();
const month = nacimiento.getMonth();

const hour = nacimiento.getHours();
const minutes = nacimiento.getMinutes();
const seconds = nacimiento.getSeconds();

const daysOfWeek = [
  "Domingo",
  "Lunes",
  "Martes",
  "Miércoles",
  "Jueves",
  "Viernes",
  "Sábado",
];
const monthsOfYear = [
  "Enero",
  "Febrero",
  "Marzo",
  "Abril",
  "Mayo",
  "Junio",
  "Julio",
  "Agosto",
  "Septiembre",
  "Octubre",
  "Noviembre",
  "Diciembre",
];
const dayOfWeek = daysOfWeek[nacimiento.getDay()];
const monthOfYear = monthsOfYear[nacimiento.getMonth()];

const startOfYear = new Date(nacimiento.getFullYear(), 0, 1);
const diffInTime = nacimiento - startOfYear;
const dayOfYear = Math.floor(diffInTime / (1000 * 60 * 60 * 24)) + 1;

console.log(`\n${day}/${month}/${year}`);
console.log(`0${hour}:0${minutes}:${seconds}`);
console.log(`${dayOfYear}`);
console.log(`${dayOfWeek}`);
console.log(`${monthOfYear}`);
