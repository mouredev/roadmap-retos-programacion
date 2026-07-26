/*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 */

const currentDay = new Date(Date.now())
console.log(currentDay.toString())

const bornDay = new Date(1996, 0, 30, 21, 9, 10, 1000)
console.log(bornDay.toString())

function calculateAge(actual, birth) {
    let years = actual.getFullYear() - birth.getFullYear()

    let actualMonth = actual.getMonth()
    let birthMonth = birth.getMonth()
    let actualDayNum  = actual.getDate()
    let birthDayNum = birth.getDate()

    if (actualMonth < birthMonth || actualMonth === birthMonth && actualDayNum  < birthDayNum) {
        years--
    }
    return years
}

console.log(calculateAge(currentDay,bornDay))

/* DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
 */

const monthNames = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
const dayNames = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

function showFormats(birth) {
    const startAnio = new Date(birth.getFullYear(), 0, 0)
    const difference = birth - startAnio

    const milisecondsDay = 1000 * 60 * 60 * 24
    const dayYear = Math.floor(difference / milisecondsDay)

    console.log(birth.toDateString())
    console.log(birth.toTimeString())
    console.log(`${birth.getDate()}/${birth.getMonth()+1}/${birth.getFullYear()}`)
    console.log(`${birth.getHours()}:${birth.getMinutes()}:${birth.getSeconds()}`)
    console.log(`Día número ${dayYear} del año`)
    console.log(`Nací un día: ${dayNames[birth.getDay()]}`)
    console.log(`Nací en el mes: ${monthNames[birth.getMonth()]}`)
    console.log(`La fecha en formato ISO es: ${birth.getFullYear()}/${String(birth.getMonth()+1).padStart(2, "0")}/${birth.getDate()}`)
    console.log(birth.toLocaleDateString(`es-PE`))
    console.log(birth.toLocaleString())
}

showFormats(bornDay)