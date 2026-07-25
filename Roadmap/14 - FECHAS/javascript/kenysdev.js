/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#14 FECHAS
---------------------------------------
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
// ________________________________________________________
const { DateTime } = require("luxon");

const birthDate = DateTime.fromISO("1995-10-20T02:30:00");
const currentDate = DateTime.now();

// Diferencia precisa
const diff = currentDate.diff(birthDate, ["years", "months", "days"]);

console.log(`
Juanito tiene:
${Math.floor(diff.years)} años,
${Math.floor(diff.months)} meses y
${Math.floor(diff.days)} días.
`);

// ________________________________________________________
// DIFICULTAD EXTRA

console.log(`
    1. Predeterminado -> ${birthDate.toString()}
    2. dd/mm/yyyy     -> ${birthDate.toFormat("dd/MM/yyyy")}
    3. dd-mm-yyyy     -> ${birthDate.toFormat("dd-MM-yyyy")}
    4. Nombre del mes -> ${birthDate.toFormat("MMMM")}
    5. Mes abreviado  -> ${birthDate.toFormat("MMM")}
    6. Nombre dia     -> ${birthDate.toFormat("cccc")}
    7. Dia abreviado  -> ${birthDate.toFormat("ccc")}
    8. Hora(12 horas) -> ${birthDate.toFormat("hh:mm:ss a")}
    9. Hora(24 horas) -> ${birthDate.toFormat("HH:mm:ss")}
    0. personalizado  -> Born on ${birthDate.toFormat("cccc, dd 'of' MMMM yyyy at hh:mm:ss a")}
`);
