/* 🔥 EJERCICIO:
Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
- Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
- Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
Calcula cuántos años han transcurrido entre ambas fechas.
*/
const fechaActual = new Date()
// Fecha de nacimiento : 1 de agosto de 2004, a las 01:30:00.
const fechaNacimiento = new Date(2004, 7, 1, 1, 30, 0)

function calcularEdad(fechaNac) {
    const diffMs = fechaActual - fechaNac
    const diffYears = diffMs / (1000 * 60 * 60 * 24 * 365.25)
    return Math.floor(diffYears)
}
console.log(`Han transcurrido ${calcularEdad(fechaNacimiento)} años desde tu fecha de nacimiento.`)
/* Dictionary 📗 = {
    Math.floor : "Redondea un número hacia abajo al entero más cercano"
    Date : "Meses en JavaScript son base 0 (7 = agosto) y este maneja milisegundos"
    "(1000 * 60 * 60 * 24 * 365.25)" : "Convierte milisegundos en años, considerando años bisiestos"
}
*/

/*----------------------------------------------------------------------------------------------------------------------
🔥 DIFICULTAD EXTRA (opcional):
Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
10 maneras diferentes. Por ejemplo:
- Día, mes y año.
- Hora, minuto y segundo.
- Día de año.
- Día de la semana.
- Nombre del mes.
(lo que se te ocurra...)
*/
// ! 10 maneras diferentes
function formatearFecha(fecha) {
    const opciones = {
        weekday: 'long', // Nombre del día de la semana
        year: 'numeric', // Año completo
        month: 'long',   // Nombre del mes
        day: 'numeric',  // Día del mes
        hour: '2-digit', // Hora en formato de 2 dígitos
        minute: '2-digit', // Minutos en formato de 2 dígitos
        second: '2-digit'  // Segundos en formato de 2 dígitos
    };

    console.log("1. Día, mes y año:", fecha.toLocaleDateString())
    console.log("2. Hora, minuto y segundo:", fecha.toLocaleTimeString())
    console.log("3. Día del año:", obtenerDiaDelAño(fecha))
    console.log("4. Día de la semana:", fecha.toLocaleDateString('es-ES', { weekday: 'long' }))
    console.log("5. Nombre del mes:", fecha.toLocaleDateString('es-ES', { month: 'long' }))
    console.log("6. Fecha completa:", fecha.toLocaleString('es-ES', opciones))
    console.log("7. Año:", fecha.getFullYear())
    console.log("8. Mes (número):", fecha.getMonth() + 1)
    console.log("9. Fecha en formato ISO:", fecha.toISOString())
    console.log("10. Tiempo en milisegundos desde 1970:", fecha.getTime())
}
// ! For 3. Día del año:
function obtenerDiaDelAño(fecha) {
    const inicioAño = new Date(fecha.getFullYear(), 0, 1)
    const diffMs = fecha - inicioAño
    return Math.floor(diffMs / (1000 * 60 * 60 * 24)) + 1
}

formatearFecha(fechaNacimiento);