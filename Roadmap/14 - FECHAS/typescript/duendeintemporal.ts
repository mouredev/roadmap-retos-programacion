/*
 * EJERCICIO #14 { retosparaprogramadortes } FECHAS:
 * Crea dos variables utilizando los objetos fecha (Date) de TypeScript:
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

// Short for console.log()
const log = console.log;

// Conditional check for browser environment
if (typeof window !== 'undefined') {
    window.addEventListener('load', () => {
        const body: HTMLBodyElement | null = document.querySelector('body');
        const title = document.createElement('h1');

        body?.style.setProperty('background', '#000');
        body?.style.setProperty('text-align', 'center');

        title.textContent = 'Retosparaprogramadores #14.';
        title.style.setProperty('font-size', '3.5vmax');
        title.style.setProperty('color', '#fff');
        title.style.setProperty('line-height', '100vh');

        body?.appendChild(title);

        setTimeout(() => {
            alert('Retosparaprogramadores #14. Please open the Browser Developer Tools.');
        }, 2000);
        log('Retosparaprogramadores #14');
    });
} else {
    log('This code is designed to run in a browser environment. Skipping window-related code.');
    log('Retosparaprogramadores #14');
}

// Get the current date and time
const today: Date = new Date();
log(today); // Current date and time  output example: 2025-02-25T00:41:23.422Z
log(today.toDateString()); // Current date in a readable format  output example: Mon Feb 24 2025

// Define a birthday date (example: August 8, 1983, 08:30:00)
const myBirthday: Date = new Date(Date.parse("1983-08-08T08:30:00"));
log(myBirthday); // Birthday date and time  1983-08-08T12:30:00.000Z
log(myBirthday.toDateString()); // Birthday date in a readable format   8/8/1983
log(myBirthday.toLocaleDateString()); // Birthday date in a localized format   8/8/1983
log(myBirthday.toLocaleString()); // Birthday date and time in a localized format   8/8/1983, 8:30:00 

/**
 * Calculates the number of years between two dates.
 * @param date1 - The first date.
 * @param date2 - The second date.
 * @returns The number of years between the two dates.
 */
const calcYearsBetween = (date1: Date, date2: Date): number => {
    if (date1 < date2) {
        [date1, date2] = [date2, date1]; // Swap if date1 is earlier
    }

    const differenceInMilliseconds: number = date1.getTime() - date2.getTime();
    const years: number = differenceInMilliseconds / (1000 * 60 * 60 * 24 * 365.25);

    let fullYears: number = Math.floor(years);

    // Check if the anniversary has not yet occurred this year
    if (
        date1.getMonth() < date2.getMonth() ||
        (date1.getMonth() === date2.getMonth() && date1.getDate() < date2.getDate())
    ) {
        fullYears--;
    }
    return years;
};

const yearsBetween: number = calcYearsBetween(today, myBirthday);
log(`Years between: ${yearsBetween.toFixed(2)}`); // Output: Years between: 41.55

/**
 * Alternative method to calculate the number of years between two dates.
 * @param date1 - The first date.
 * @param date2 - The second date.
 * @returns The number of years between the two dates.
 */
const calcYearsBetween2 = (date1: Date, date2: Date): number => {
    if (date1 < date2) {
        [date1, date2] = [date2, date1]; // Swap if date1 is earlier
    }
    let years: number = date1.getFullYear() - date2.getFullYear();

    if (
        date1.getMonth() < date2.getMonth() ||
        (date1.getMonth() === date2.getMonth() && date1.getDate() < date2.getDate())
    ) {
        years--;
    }

    return years;
};

log(calcYearsBetween2(today, myBirthday)); // Output: 41

/**
 * Calculates the difference between two dates in years, months, weeks, days, hours, minutes, and seconds.
 * @param date1 - The first date.
 * @param date2 - The second date.
 * @returns An object containing the difference in years, months, weeks, days, hours, minutes, and seconds.
 */
const calcDateDifference = (date1: Date, date2: Date) => {
    if (date1 < date2) {
        [date1, date2] = [date2, date1]; // Swap if date1 is earlier
    }

    const differenceInMilliseconds: number = date1.getTime() - date2.getTime();
    const totalSeconds: number = Math.floor(differenceInMilliseconds / 1000);
    const totalMinutes: number = Math.floor(totalSeconds / 60);
    const totalHours: number = Math.floor(totalMinutes / 60);
    const totalDays: number = Math.floor(totalHours / 24);

    const years: number = date1.getFullYear() - date2.getFullYear();
    const months: number = date1.getMonth() - date2.getMonth() + (years * 12);
    const weeks: number = Math.floor(totalDays / 7);
    const days: number = totalDays % 7;

    const remainingHours: number = totalHours % 24;
    const remainingMinutes: number = totalMinutes % 60;
    const remainingSeconds: number = totalSeconds % 60;

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

/* Output:
Difference:         
42 years,
498 months,
2168 weeks,
0 days,
12 hours,
11 minutes,
23 seconds */

/**
 * Formats a birthday date in 10 different ways.
 * @param birthday - The birthday date.
 */
const formatBirthday = (birthday: Date): void => {
    const date: Date = new Date(birthday);

    const dayMonthYear: string = date.toLocaleDateString('en-US', { day: 'numeric', month: 'long', year: 'numeric' });
    const time: string = date.toLocaleTimeString('es-ES', { hour: 'numeric', minute: 'numeric', second: 'numeric' });
    const dayOfYear: number = Math.floor((date.getTime() - new Date(date.getFullYear(), 0, 0).getTime()) / 1000 / 60 / 60 / 24);
    const dayOfWeek: string = date.toLocaleDateString('en-US', { weekday: 'long' });
    const monthName: string = date.toLocaleDateString('en-US', { month: 'long' });
    const isoFormat: string = date.toISOString();
    const shortFormat: string = date.toLocaleDateString('en-US');
    const longFormat: string = date.toLocaleDateString('en-US', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });
    const time12Hour: string = date.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', second: 'numeric', hour12: true });
    const timeWithTimezone: string = date.toLocaleString('es-ES', { timeZoneName: 'short' });

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

/* Output:
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