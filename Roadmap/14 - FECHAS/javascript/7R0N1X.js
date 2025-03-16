const currentDate = new Date();
console.log(currentDate);

const dateOfBirth = new Date(1999, 7, 30, 5, 51, 30)
console.log(dateOfBirth);

function calculateElapsedYears(date1, date2) {
  return date1.getFullYear() - date2.getFullYear();
}

console.log(`De ${dateOfBirth.getFullYear()} a ${currentDate.getFullYear()} han transcurrido ${calculateElapsedYears(currentDate, dateOfBirth)} años.`);

const days = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"];
const months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];

function formatDate(date) {
  const dayMonthYear = `${days[date.getDay()]} ${date.getDate()} de ${months[date.getMonth()]} de ${date.getFullYear()}`
  const hourMinuteSecond = `Hora: ${date.getHours()} Minuto: ${date.getMinutes()} Segundo: ${date.getSeconds()}`
  const dayOfYear = `Día del año: ${date.getDate()}`
  const dayOfWeek = `Día de la semana: ${days[date.getDay()]}`
  const nameOfMonth = `Mes: ${months[date.getMonth()]}`

  return {
    dayMonthYear,
    hourMinuteSecond,
    dayOfYear,
    dayOfWeek,
    nameOfMonth
  }
}

const data = formatDate(dateOfBirth);

for(const value in data){
  console.log(data[value]);
}