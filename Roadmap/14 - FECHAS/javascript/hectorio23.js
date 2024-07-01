// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23 

"use strict";

// npm install luxon
const { DateTime } = require('luxon');

/**
 * EJERCICIO:
 * Crea dos variables utilizando los objetos de fecha de tu lenguaje:
 * - Una primera que represente la fecha y hora actual.
 * - Una segunda que represente tu fecha de nacimiento (puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 * 
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatea y muestra su resultado de
 * 10 maneras diferentes.
 */

// Variables con la fecha actual y la fecha de nacimiento
const now = DateTime.now();
const birthDate = DateTime.fromObject({ year: 2004, month: 6, day: 28, hour: 12, minute: 59, second: 0 });

// Calculando la diferencia en años
const diffYears = now.diff(birthDate, 'years').toObject().years;

// Imprimiendo resultados del ejercicio básico
console.log(`Fecha actual: ${now.toFormat('dd/MM/yyyy  hh:mm:ss a')}`);
console.log(`Fecha de nacimiento: ${birthDate.toFormat('dd/MM/yyyy  hh:mm:ss a')}`);
console.log(`Han pasado aproximadamente ${diffYears.toFixed(2)} años desde tu nacimiento.`);

// Función para mostrar el resultado en 10 formas diferentes (ejercicio extra)
function showFormattedBirthDate() {
    console.log("\n**** Formateando la fecha de nacimiento en 10 formas distintas ****\n");
    console.log(`Fecha de nacimiento (dd/MM/yyyy): ${birthDate.toFormat('dd/MM/yyyy')}`);
    console.log(`Fecha de nacimiento (MM-dd-yyyy): ${birthDate.toFormat('MM-dd-yyyy')}`);
    console.log(`Fecha de nacimiento (dd-MM-yyyy): ${birthDate.toFormat('dd-MM-yyyy')}`);
    console.log(`Fecha de nacimiento (yyyy/MM/dd): ${birthDate.toFormat('yyyy/MM/dd')}`);
    console.log(`Fecha de nacimiento (dd/MM/yy): ${birthDate.toFormat('dd/MM/yy')}`);
    console.log(`Fecha de nacimiento (yy/MM/dd): ${birthDate.toFormat('yy/MM/dd')}`);
    console.log(`Fecha de nacimiento (hh:mm:ss): ${birthDate.toFormat('HH:mm:ss')}`);
    console.log(`Fecha de nacimiento (hh:mm): ${birthDate.toFormat('HH:mm')}`);
    console.log(`Fecha de nacimiento (mes dd, yyyy): ${birthDate.toFormat('MMMM dd, yyyy')}`);
    console.log(`Fecha de nacimiento (dd de mes de yyyy): ${birthDate.toFormat('dd \'de\' MMMM \'de\' yyyy')}`);
}

// Mostrar el resultado en 10 formas diferentes
showFormattedBirthDate();
