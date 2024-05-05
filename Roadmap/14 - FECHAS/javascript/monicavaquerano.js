// 14 FECHAS
// Monica Vaquerano
//  https://monicavaquerano.dev


/*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 */

// Now
let now = new Date();

// Day of Birth
let dob = new Date(1988, 9, 9, 19, 33);

// Difference
let dif = Math.abs(now - dob);
let days = dif / (1000 * 60 * 60 * 24);
let years = Math.floor(days / 365)

console.log(`Difference (Age) => ${years}`)

// Date Output - JavaScript Get Date Methods
// In JavaScript, date objects are created with new Date().
// new Date() returns a date object with the current date and time.

const MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
const WEEKDAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

console.log("Now: weekday, full version =>", WEEKDAYS[now.getDay()]);
console.log("Now: year =>", now.getFullYear())
console.log("DOB: day =>", dob.getDate())
console.log("DOB: month =>", dob.getMonth() + 1)
console.log("DOB: month name =>", MONTHS[dob.getMonth()])
console.log("DOB: year =>", dob.getFullYear())

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

let fullYear = dob.getFullYear();	// Get year as a four digit number (yyyy)
let year = fullYear.toString().slice(2); // Get year as a two digit number (yy)
let month = dob.getMonth() + 1;	// Get month as a number (0-11)
let monthName = MONTHS[dob.getMonth()];	// Get month fullname
let date = dob.getDate();	// Get day as a number (1-31)
let weekday = dob.getDay();	// Get weekday as a number (0-6)
let weekdayName = WEEKDAYS[dob.getDay()];	// Get weekday fullname
let hour = dob.getHours();	// Get hour (0-23)
let minutes = dob.getMinutes(); // Get minute (0-59)
minutes = minutes < 10 ? "0" + minutes : minutes;	// Adds a "0" if minutes is less than 10
let seconds = dob.getSeconds();	// Get second (0-59)
seconds = seconds < 10 ? "0" + seconds : seconds;	// Adds a "0" if seconds is less than 10
let milliseconds = dob.getMilliseconds(); // Get millisecond (0-999)
let time = dob.getTime(); // Get time (milliseconds since January 1, 1970)

// # - Día, mes y año.
console.log("Día, mes y año =>\t", `${date} ${monthName} ${year}`)
console.log("Día, mes y año =>\t", `${date}/${month}/${year}`)
console.log("Día, mes y año =>\t", `${date}/${month}/${fullYear}`)

// # - Hora, minuto y segundo.
console.log("Hora, minuto y segundo =>\t", `${hour}:${minutes}:${seconds}`)

function getTimeAMPM(dt) {
    let hours = dt.getHours();
    let minutes = dt.getMinutes();
    let seconds = dt.getSeconds();

    // PM or AM?
    let meridian = hours >= 12 ? "PM" : "AM";

    // 12-Hours Format
    hours = hours % 12;
    hours = hours ? hours : 12;

    // Adds a "0" if minutes or seconds are less than 10
    minutes = minutes < 10 ? "0" + minutes : minutes;
    seconds = seconds < 10 ? "0" + seconds : seconds;

    let format = `${hours}:${minutes}:${seconds} ${meridian}`
    return format
}

console.log("Hora, minuto y segundo =>\t", getTimeAMPM(dob))

// # - Día de año.
function getDayOfYear(dt) {
    // First day of that year
    let startOfYear = new Date(dt.getFullYear(), 0, 0);

    // Difference between date and start of that year
    let diff = dt - startOfYear;

    // Divide the difference between the milliseconds of a day (86400000)
    let dayOfYear = Math.floor(diff / 86400000);

    return dayOfYear;
}

console.log("Día del año =>\t", getDayOfYear(dob))

// # - Día de la semana.
console.log("Día de la semana =>\t", weekday)
console.log("Día de la semana =>\t", weekdayName.slice(0, 3))
console.log("Día de la semana =>\t", weekdayName)


// # - Nombre del mes.
console.log("Nombre del mes =>\t", month)
console.log("Nombre del mes =>\t", monthName.slice(0, 3))
console.log("Nombre del mes =>\t", monthName)

// # - (lo que se te ocurra...)
console.log(dob.toJSON()); // Returns the date as a string, formatted as a JSON date
console.log(dob.toString()); // Converts a Date object to a string
console.log(dob.toLocaleString()); // Converts a Date object to a string, using locale conventions
console.log(dob.toDateString()); // Converts the date portion of a Date object into a readable string
console.log(dob.toUTCString()); // Converts a Date object to a string, according to universal time
console.log(dob.toISOString()); // Returns the date as a string, using the ISO standard

