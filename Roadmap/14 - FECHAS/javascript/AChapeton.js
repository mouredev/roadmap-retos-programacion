const currentDate = new Date();
console.log(currentDate);

const birthDate = new Date(1997, 5, 2, 13, 30, 0);
console.log(birthDate);

const getYearsBetweenDates = function (birthDate, currentDate) {
    if (currentDate === void 0) { currentDate = new Date(); }
    const birthTime = new Date(birthDate).getTime();
    const currentTime = new Date(currentDate).getTime();
    const age = (currentTime - birthTime) / (365 * 24 * 60 * 60 * 1000);
    return Math.floor(age);
};

console.log(getYearsBetweenDates(birthDate));


const days = ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado'];
const months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
const isLeapYear = function (y) { return y % 4 === 0 && y % 100 !== 0 || y % 400 === 0; };
const daysInAYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

// DIFICULTAD EXTRA
console.log('Dia, mes, y año: ', birthDate.getDay() + 1, '/', months[birthDate.getMonth()], '/', birthDate.getFullYear());
console.log('Hora, minuto y segundo: ', 'Hora: ', birthDate.getHours(), ' Minutos: ', birthDate.getMinutes(), ' Segundos: ', birthDate.getSeconds());
console.log('Dia de la semana: ', (birthDate.getDay() > 7) ? days[birthDate.getDay() - 7] : days[birthDate.getDay()]);
console.log('Nombre del mes: ', months[birthDate.getMonth()]);
console.log('Año: ', birthDate.getFullYear());
console.log('Version ingles: ', birthDate.toDateString());
function dayOfYear(date) {
    const d = new Date(date);
    const daysGiven = d.getDate();
    const month = d.getMonth();
    const year = d.getFullYear();
    if (isLeapYear(year) && month > 1) {
        return daysInAYear.slice(0, month).reduce(function (a, c) { return a + c; }, 0) + 1 + daysGiven;
    }
    else {
        return daysInAYear.slice(0, month).reduce(function (a, c) { return a + 1; }, 0) + daysGiven;
    }
}
console.log('Dia de año: ', dayOfYear("06/02/2020"));
console.log('Fecha completa: ', birthDate.getDay() + 1, ' de ', months[birthDate.getMonth()], ' de ', birthDate.getFullYear());
console.log('Mes/Dia/Año: ', birthDate.toLocaleDateString());
console.log('Formato Tiempo 12 horas: ', birthDate.toLocaleTimeString());
console.log('Formato Tiempo 24 horas: ', birthDate.toTimeString());
