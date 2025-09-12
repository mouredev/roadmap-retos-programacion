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
const bdayDate = new Date('1998-06-29 09:25:00');

const diffYears = (dateOne, dateTwo) => {
    let newestYear, oldestYear;
    if (dateOne > dateTwo) {
        newestYear = dateOne.getFullYear();
        oldestYear = dateTwo.getFullYear();
    } else {
        newestYear = dateTwo.getFullYear();
        oldestYear = dateOne.getFullYear();
    }

    return newestYear - oldestYear;
};
console.log(diffYears(currentDate, bdayDate));


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

const weekDays = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday'
};

const months = {
    0: 'January',
    1: 'February',
    2: 'March',
    3: 'April',
    4: 'May',
    5: 'June',
    6: 'July',
    7: 'August',
    8: 'September',
    9: 'October',
    10: 'November',
    11: 'December'
};

console.log(`1. ${bdayDate.toDateString()}`);
console.log(`2. ${bdayDate.toLocaleDateString()}`);
console.log(`3. ${bdayDate.toLocaleString()}`);
console.log(`4. ${bdayDate.getHours()}:${bdayDate.getMinutes()}:${bdayDate.getSeconds()}`);
console.log(`5. ${bdayDate.toLocaleTimeString()}`);
console.log(`6. ${bdayDate.getDay()}`);
console.log(`7. ${weekDays[bdayDate.getDay()]}`);
console.log(`8. ${bdayDate.getMonth() + 1}`);
console.log(`9. ${months[bdayDate.getMonth()]}`);
console.log(`10. ${bdayDate.toJSON()}`);