/*
 * EJERCICIO #14 FECHAS:
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

// bibliography
//Professional JavaScript for web developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)
//GPT


// short for console.log()
let log = console.log;

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #14.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #14. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #14'); 
});


let today = new Date()
log(today); // Date Fri Oct 18 2024 10:24:48 GMT-0400 (Venezuela Time)
log(today.toDateString()); // Fri Oct 18 2024
let myBirthday = new Date(Date.parse("1983-08-08T08:30:00"));
log(myBirthday); // Date Mon Aug 08 1983 08:30:00 GMT-0400 (Venezuela Time)
log(myBirthday.toLocaleDateString()); // 8/8/1983
log(myBirthday.toLocaleString()); // 8/8/1983, 8:30:00 AM

const calcYearsBetween = (date1, date2) => {
    if (date1 < date2) {
        [date1, date2] = [date2, date1]; // Swap if date1 is earlier
    }

    const differenceInMilliseconds = date1.getTime() - date2.getTime();

    const years = differenceInMilliseconds / (1000 * 60 * 60 * 24 * 365.25);

    let fullYears = Math.floor(years);

    // Check if the anniversary has not yet occurred this year
    if (
        date1.getMonth() < date2.getMonth() ||
        (date1.getMonth() === date2.getMonth() && date1.getDate() < date2.getDate())
    ) {
        fullYears--;
    }    
    return years; 
};

// Note: By incorporating the anniversary check, the function provides a more accurate representation of the year difference.


// Note: Using 365.25 rather than 365 allows for greater precision because it accounts for leap years.

const yearsBetween = calcYearsBetween(today, myBirthday);
log(`Years between: ${yearsBetween.toFixed(2)}`); // 41.20


//or just
const calcYearsBetween2 = (date1, date2) => {
    if (date1 < date2) {
        [date1, date2] = [date2, date1]; // Swap if date1 is earlier
    }
    const years = date1.getFullYear() - date2.getFullYear();  
    
    if (
        date1.getMonth() < date2.getMonth() ||
        (date1.getMonth() === date2.getMonth() && date1.getDate() < date2.getDate())
    ) {
        years--; 
    }

    return years; 
 }; 

log(calcYearsBetween2(today, myBirthday)); // 41



const calcDateDifference = (date1, date2) => {
    // Ensure date1 is the later date
    if (date1 < date2) {
        [date1, date2] = [date2, date1]; // Swap if date1 is earlier
    }

    // Calculate the difference in milliseconds
    const differenceInMilliseconds = date1.getTime() - date2.getTime();

    // Calculate total seconds
    const totalSeconds = Math.floor(differenceInMilliseconds / 1000);
    
    // Calculate total minutes
    const totalMinutes = Math.floor(totalSeconds / 60);
    
    // Calculate total hours
    const totalHours = Math.floor(totalMinutes / 60);
    
    // Calculate total days
    const totalDays = Math.floor(totalHours / 24);
    
    // Calculate years, months, weeks, and remaining days
    const years = date1.getFullYear() - date2.getFullYear();
    const months = date1.getMonth() - date2.getMonth() + (years * 12);
    const weeks = Math.floor(totalDays / 7);
    const days = totalDays % 7;

    // Calculate remaining hours, minutes, and seconds
    const remainingHours = totalHours % 24;
    const remainingMinutes = totalMinutes % 60;
    const remainingSeconds = totalSeconds % 60;

    return {
        years,
        months,
        weeks,
        days,
        hours: remainingHours,
        minutes: remainingMinutes,
        seconds: remainingSeconds
    };
};


const difference = calcDateDifference(today, myBirthday);
log(`Difference: 
${difference.years} years, 
${difference.months} months, 
${difference.weeks} weeks, 
${difference.days} days, 
${difference.hours} hours, 
${difference.minutes} minutes, 
${difference.seconds} seconds`);

/* Difference: 
41 years, 
494 months, 
2149 weeks, 
4 days, 
6 hours, 
28 minutes, 
38 seconds */


// Extra dificulty Exercise

const formatBirthday = (birthday) => {
    const date = new Date(birthday);

    const dayMonthYear = date.toLocaleDateString('en-US', { day: 'numeric', month: 'long', year: 'numeric' });
    
    const time = date.toLocaleTimeString('es-ES', { hour: 'numeric', minute: 'numeric', second: 'numeric' });
    
    const dayOfYear = Math.floor((date - new Date(date.getFullYear(), 0, 0)) / 1000 / 60 / 60 / 24);
    
    const dayOfWeek = date.toLocaleDateString('en-US', { weekday: 'long' });
    
    const monthName = date.toLocaleDateString('en-US', { month: 'long' });
    
    const isoFormat = date.toISOString();
    
    const shortFormat = date.toLocaleDateString('en-US');
    
    const longFormat = date.toLocaleDateString('en-US', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });
    
    const time12Hour = date.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', second: 'numeric', hour12: true });
    
    const timeWithTimezone = date.toLocaleString('es-ES', { timeZoneName: 'short' });

   log("1. I was born on:", dayMonthYear);
   log("2. at:", time + ' AM');
   log("3. the day:", dayOfYear + ' of the year ' + date.getFullYear());
   log("4. on:", dayOfWeek);
   log("5. one special day of:", monthName);
   log("6. isoFormat:", isoFormat);
   log("7. shortFormat:", shortFormat);
   log("8. longFormat:", longFormat);
   log("9. time12hour:", time12Hour);
   log("10. timeWithTimezone:", timeWithTimezone);
};

formatBirthday(myBirthday);
/* 
1. I was born on: August 8, 1983 
2. at: 8:30:00 AM 
3. the day: 220 of the year 1983 
4. on: Monday 
5. one special day of: August 
6. isoFormat: 1983-08-08T12:30:00.000Z 
7. shortFormat: 8/8/1983 
8. longFormat: Monday, August 8, 1983 
9. time12hour: 8:30:00 AM 
10. timeWithTimezone: 8/8/1983, 8:30:00 GMT-4 */



//REFERENCE INFORMATION:


/* Date-Formatting Methods
There are several Date type methods used specifically to format the date as a string. They are
as follows:
➤➤ toDateString()—Displays the date’s day of the week, month, day of the month, and year in
an implementation-specific format.
➤➤ toTimeString()—Displays the date’s hours, minutes, seconds, and time zone in an imple-
mentation-specific format.
➤➤ toLocaleDateString()—Displays the date’s day of the week, month, day of the month, and
year in an implementation- and locale-specific format.
➤➤ toLocaleTimeString()—Displays the date’s hours, minutes, and seconds in an implementa-
tion-specific format.
➤➤ toUTCString()—Displays the complete UTC date in an implementation-specific format.
The output of these methods, as with toLocaleString() and toString(), varies widely from
browser to browser and therefore can’t be employed in a user interface for consistent display of a date.

NOTE There is also a method called toGMTString(), which is equivalent to toUTCString() and is provided for backwards compatibility. However, the specification recommends that new code use toUTCString() exclusively.

Date/Time Component Methods
The remaining methods of the Date type (listed in the following table) deal directly with getting and
setting specific parts of the date value. Note that references to a UTC date mean the date value when
interpreted without a time-zone offset (the date when converted to GMT).
METHOD DESCRIPTION
getTime() Returns the milliseconds representation of the date; same as
valueOf().
setTime(milliseconds) Sets the milliseconds representation of the date, thus changing the entire date.
getFullYear() Returns the four-digit year (2019 instead of just 19).
getUTCFullYear() Returns the four-digit year of the UTC date value.
setFullYear(year) Sets the year of the date. The year must be given with four digits (2019 instead of just 19).
setUTCFullYear(year) Sets the year of the UTC date. The year must be given with four digits (2019 instead of just 19).
getMonth() Returns the month of the date, where 0 represents January and 11 represents December.
getUTCMonth() Returns the month of the UTC date, where 0 represents January and 11 represents December.
setMonth(month) Sets the month of the date, which is any number 0 or greater. Numbers greater than 11 add years.
setUTCMonth(month) Sets the month of the UTC date, which is any number 0 or greater. Numbers greater than 11 add years.
getDate() Returns the day of the month (1 through 31) for the date.
getUTCDate() Returns the day of the month (1 through 31) for the UTC date.
setDate(date) Sets the day of the month for the date. If the date is greater
than the number of days in the month, the month value also
gets increased.
setUTCDate(date) Sets the day of the month for the UTC date. If the date is greater than the number of days in the month, the month value also gets increased.
getDay() Returns the date’s day of the week as a number (where 0 represents Sunday and 6 represents Saturday).
getUTCDay() Returns the UTC date’s day of the week as a number (where 0 represents Sunday and 6 represents Saturday).
getHours() Returns the date’s hours as a number between 0 and 23.
getUTCHours() Returns the UTC date’s hours as a number between 0 and 23.
setHours(hours) Sets the date’s hours. Setting the hours to a number greater than 23 also increments the day of the month.
setUTCHours(hours) Sets the UTC date’s hours. Setting the hours to a number greater than 23 also increments the day of the month.
getMinutes() Returns the date’s minutes as a number between 0 and 59.
getUTCMinutes() Returns the UTC date’s minutes as a number between 0 and 59.
setMinutes(minutes) Sets the date’s minutes. Setting the minutes to a number greater than 59 also increments the hour.
setUTCMinutes(minutes) Sets the UTC date’s minutes. Setting the minutes to a number greater than 59 also increments the hour.
getSeconds() Returns the date’s seconds as a number between 0 and 59.
getUTCSeconds() Returns the UTC date’s seconds as a number between 0 and 59.
setSeconds(seconds) Sets the date’s seconds. Setting the seconds to a number greater than 59 also increments the minutes.
setUTCSeconds(seconds) Sets the UTC date’s seconds. Setting the seconds to a number greater than 59 also increments the minutes.
getMilliseconds() Returns the date’s milliseconds.
getUTCMilliseconds() Returns the UTC date’s milliseconds.
setMilliseconds(milliseconds) Sets the date’s milliseconds.
setUTCMilliseconds(milliseconds) Sets the UTC date’s milliseconds.
getTimezoneOffset() Returns the number of minutes that the local time zone is offset from UTC. For example, Eastern Standard Time returns 300. This value changes when an area goes into Daylight Saving Time. */