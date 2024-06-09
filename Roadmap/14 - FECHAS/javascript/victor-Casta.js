/*
  * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
  * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
  * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
  * Calcula cuántos años han transcurrido entre ambas fechas.
*/

// Obtenemos la fecha actual y la fecha de nacimiento usando el objeto Date proporcionado por JavaScript
const actualDate = new Date(); // Fecha actual
const birthday = new Date('2002-12-17'); // Fecha de nacimiento

// Calculamos la edad restando el año de la fecha de nacimiento del año de la fecha actual
let age = actualDate.getFullYear() - birthday.getFullYear();

// Ajustamos la edad si el cumpleaños de este año aún no ha ocurrido
// Calculamos la diferencia de meses entre la fecha actual y la fecha de nacimiento
const monthDiff = actualDate.getMonth() - birthday.getMonth();

// Si la diferencia de meses es negativa, significa que aún no ha pasado el cumpleaños este año
// Si la diferencia de meses es cero, verificamos si el día del mes actual es menor que el día del cumpleaños
// Si cualquiera de las condiciones es verdadera, restamos 1 de la edad calculada previamente
if (monthDiff < 0 || (monthDiff === 0 && actualDate.getDate() < birthday.getDate())) {
  age--;
}

console.log(`Han transcurrido: ${age} años, desde ${birthday.getFullYear()} hasta ${actualDate.getFullYear()}`);


/*
  * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
  * 10 maneras diferentes. Por ejemplo:
  * - Día, mes y año.
  * - Hora, minuto y segundo.
  * - Día de año.
  * - Día de la semana.
  * - Nombre del mes.
  * (lo que se te ocurra...)
*/

// 1. DD/MM/YYYY
const format1 = `${String(birthday.getDate() + 1).padStart(2, '0')}/${String(birthday.getMonth() + 1).padStart(2, '0')}/${birthday.getFullYear()}`;
console.log(`DD/MM/YYYY: ${format1}`);

// 2. HH:MM:SS (hora, minuto y segundo)
const format2 = `${String(birthday.getHours()).padStart(2, '0')}:${String(birthday.getMinutes()).padStart(2, '0')}:${String(birthday.getSeconds()).padStart(2, '0')}`;
console.log(`HH:MM:SS: ${format2}`);

// 3. YYYY-MM-DD (formato ISO)
const format3 = birthday.toISOString().split('T')[0];
console.log(`YYYY-MM-DD: ${format3}`);

// 4. Día de la semana
const daysOfWeek = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
const format4 = daysOfWeek[birthday.getDay() + 1];
console.log(`Día de la semana: ${format4}`);

// 5. Nombre del mes
const monthsOfYear = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
const format5 = monthsOfYear[birthday.getMonth()];
console.log(`Nombre del mes: ${format5}`);

// 6. Día del año
const startOfYear = new Date(birthday.getFullYear(), 0, 1);
const dayOfYear = Math.floor((birthday - startOfYear) / (1000 * 60 * 60 * 24)) + 1;
const format6 = dayOfYear;
console.log(`Día del año: ${format6}`);

// 7. MM/DD/YYYY
const format7 = `${String(birthday.getMonth() + 1).padStart(2, '0')}/${String(birthday.getDate() + 1).padStart(2, '0')}/${birthday.getFullYear()}`;
console.log(`MM/DD/YYYY: ${format7}`);

// 8. DD Month YYYY
const format8 = `${String(birthday.getDate() + 1).padStart(2, '0')} ${monthsOfYear[birthday.getMonth()]} ${birthday.getFullYear()}`;
console.log(`DD Month YYYY: ${format8}`);

// 9. Día, Nombre del mes, Año
const format9 = `${daysOfWeek[birthday.getDay() + 1]}, ${birthday.getDate() + 1} de ${monthsOfYear[birthday.getMonth()]} de ${birthday.getFullYear()}`;
console.log(`Día, Nombre del mes, Año: ${format9}`);

// 10. Timestamp
const format10 = birthday.getTime();
console.log(`Timestamp: ${format10}`);
