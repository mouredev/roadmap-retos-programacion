const currentDate: Date = new Date();
const birthdate: Date = new Date('2001-10-21T08:30:00');

function calculateAge(currentDate: Date, birthdate: Date): number {
    let age: number = currentDate.getFullYear() - birthdate.getFullYear();
    const month: number = currentDate.getMonth() - birthdate.getMonth();

    if (month < 0 || (month === 0 && currentDate.getDate() < birthdate.getDate())) {
        age--;
    }

    return age;
}

const age: number = calculateAge(currentDate, birthdate);
console.log(`${age} years have passed since the date of birth`);

// ** Extra Exercise ** //
const dayMonthYear: string = birthdate.toLocaleDateString('es-ES');

const hourMinuteSecond: string = birthdate.toLocaleTimeString('es-ES');

const startYear: Date = new Date(birthdate.getFullYear(), 0, 0);
const difference: number = birthdate.getTime() - startYear.getTime();
const oneDay: number = 1000 * 60 * 60 * 24;
const dayOfTheYear: number = Math.floor(difference / oneDay);

const dayOfTheWeek: string = birthdate.toLocaleDateString('es-ES', { weekday: 'long' });

const nameMonth: string = birthdate.toLocaleDateString('es-ES', { month: 'long' });

const longDate: string = birthdate.toLocaleDateString('es-ES', { year: 'numeric', month: 'long', day: 'numeric' });

const formatISO: string = birthdate.toISOString();

const formatUTC: string = birthdate.toUTCString();

const timeUnix: number = birthdate.getTime();

const abbreviatedDate: string = birthdate.toLocaleDateString('es-ES', { weekday: 'short', month: 'short', day: 'numeric' });

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
