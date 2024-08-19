
let birth_day = new Date(1991,8,11,15,0,0,0);
let now = new Date();
console.log(birth_day);
console.log(now);

let dif = now.getFullYear() - birth_day.getFullYear();
console.log(`Diference in year is ${dif}`);

/*Extra*/

//Day of the week
const formatter_day = new Intl.DateTimeFormat('en', { weekday: 'long' });
day_name = formatter_day.format(birth_day);
console.log(`Day of the week for birth date was: ${day_name}`);

//Name of the month
const formatter = new Intl.DateTimeFormat('en', { month: 'long' });
month_name = formatter.format(birth_day);
console.log(`Month for birth date was ${month_name}`);

//Format date Spanish format
console.log('Formatting date in Spanish version: ',new Intl.DateTimeFormat('es').format(birth_day));

//Format date USA format
console.log('Formatting date in USA version: ',new Intl.DateTimeFormat('en-US').format(birth_day));

// Format date HH:MM:SS
console.log(`Formating HH:MM:SS: ${birth_day.getHours()}:${birth_day.getMinutes()}:${birth_day.getSeconds()}`)
