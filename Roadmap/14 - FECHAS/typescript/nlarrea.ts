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


const currentDate: Date = new Date()
const birthdayDate: Date = new Date('1998-06-29 09:25:00')

const getYearsDifference = (dateOne: Date, dateTwo: Date): number => {
    if (dateOne > dateTwo) {
        return dateOne.getFullYear() - dateTwo.getFullYear()
    }

    return dateTwo.getFullYear() - dateOne.getFullYear()
}

console.log(getYearsDifference(currentDate, birthdayDate))


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

const weekDays: Object = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday'
}

const months: Object = {
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
}

console.log(`1. ${birthdayDate.toDateString()}`)  // 1. Mon Jun 29 1998
console.log(`2. ${birthdayDate.toLocaleDateString()}`)  // 2. 29/6/1998
console.log(`3. ${birthdayDate.toLocaleString()}`)  // 3. 29/6/1998, 9:25:00
console.log(`4. ${birthdayDate.getHours()}:${birthdayDate.getMinutes()}:${birthdayDate.getSeconds()}`)  // 4. 9:25:0
console.log(`5. ${birthdayDate.toLocaleTimeString()}`)  // 5. 9:25:00
console.log(`6. ${birthdayDate.getDay()}`)  // 6. 1
console.log(`7. ${weekDays[birthdayDate.getDay()]}`)  // 7. Monday
console.log(`8. ${birthdayDate.getMonth() + 1}`)  // 8. 6
console.log(`9. ${months[birthdayDate.getMonth()]}`)  // 9. June
console.log(`10. ${birthdayDate.toJSON()}`)  // 10. 1998-06-29T07:25:00.000Z