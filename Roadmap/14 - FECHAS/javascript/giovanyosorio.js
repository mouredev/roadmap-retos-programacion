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

// Fecha actual
const fechaActual = new Date();

const fechaNacimiento = new Date(1995, 9, 3, 12, 0, 0);


const edad = Math.floor((fechaActual - fechaNacimiento) / (1000 * 60 * 60 * 24 * 365));

console.log(`Mi edad es: ${edad} años.`);

// DIFICULTAD EXTRA
console.log(`Fecha de nacimiento: ${fechaNacimiento.toLocaleDateString()}`);
console.log(`Hora de nacimiento: ${fechaNacimiento.toLocaleTimeString()}`);
console.log(`Día del año: ${Math.floor((fechaNacimiento - new Date(fechaNacimiento.getFullYear(), 0, 0)) / (1000 * 60 * 60 * 24))}`); 
console.log(`Día de la semana: ${fechaNacimiento.toLocaleString('es-ES', { weekday: 'long' })}`); 
console.log(`Nombre del mes: ${fechaNacimiento.toLocaleString('es-ES', { month: 'long' })}`); 
console.log(`Año: ${fechaNacimiento.getFullYear()}`); 
console.log(`Mes (número): ${fechaNacimiento.getMonth() + 1}`); 
console.log(`Día del mes: ${fechaNacimiento.getDate()}`); 
console.log(`Hora: ${fechaNacimiento.getHours()}`);
console.log(`Minuto: ${fechaNacimiento.getMinutes()}`); 