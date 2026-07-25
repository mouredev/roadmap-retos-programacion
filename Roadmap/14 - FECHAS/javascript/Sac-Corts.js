const currentDate = new Date();
const birthdate = new Date('2001-10-21T08:30:00');

function calculateAge(currentDate, birthdate) {
    let age = currentDate.getFullYear() - birthdate.getFullYear();
    const month = currentDate.getMonth() - birthdate.getMonth();

    if (month < 0 || (month === 0 && currentDate.getDate() < birthdate.getDate())) {
        age--;
    }

    return age;
}

const age = calculateAge(currentDate, birthdate);
console.log(`${age} years have passed since the date of birth`);

// Extra Exercise //
const dayMonthYear = birthdate.toLocaleDateString('es-ES');

const hourMinuteSecond = birthdate.toLocaleTimeString('es-ES');

const startYear = new Date(birthdate.getFullYear(), 0, 0);
const difference = birthdate - startYear;
const oneDay = 1000 * 60 * 60 * 24;
const dayOfTheYear = Math.floor(difference / oneDay);

const dayOfTheWeek = birthdate.toLocaleDateString('es-ES', { weekday: 'long' });

const nameMonth = birthdate.toLocaleDateString('es-ES', { month: 'long' });

const longDate = birthdate.toLocaleDateString('es-ES', { year: 'numeric', month: 'long', day: 'numeric' });

const formatISO = birthdate.toISOString();

const formatUTC = birthdate.toUTCString();

const timeUnix = birthdate.getTime();

const abbreviatedDate = birthdate.toLocaleDateString('es-ES', { weekday: 'short', month: 'short', day: 'numeric' });

console.log('Day, month and year:', dayMonthYear);
console.log('Hour, minute and second:', hourMinuteSecond);
console.log('Day of the year:', dayOfTheYear);
console.log('Day of the week:', dayOfTheWeek);
console.log('Name of the month:', nameMonth);
console.log('Long date:', longDate);
console.log('Format ISO:', formatISO);
console.log('Format UTC:', formatUTC);
console.log('Time in milliseconds since 1970:', timeUnix);
console.log('Abbreviated date:', abbreviatedDate);