/*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
*/

// Fecha actual
const fechaActual = new Date()

// Fecha de nacimiento: 2 de Noviembre de 1978 a las 03:15:00
// Recordar que en JS los meses van de 0 Enero a 11 Diciembre.
const fechaNacimiento = new Date(1978, 10, 2, 3, 15, 0 )

// Calculo de la edad
let edad = fechaActual.getFullYear() - fechaNacimiento.getFullYear()


console.log("Fecha actual: ", fechaActual)
console.log("Fecha de nacimiento: ", fechaNacimiento)
console.log("Antes de comprobar si todavía no ha llegado el cumpleaños.")
console.log(`Han transcurrido:  ${edad} años.`)

const mesActual = fechaActual.getMonth()
const diaActual = fechaActual.getDate() // Se calcula el día del mes, para calcular el día de la semana es getDay.

console.log(mesActual)
console.log(diaActual)

const mesNacimiento = fechaNacimiento.getMonth()
const diaNacimiento = fechaNacimiento.getDate()
console.log(mesNacimiento)
console.log(diaNacimiento)

// Comprobación de si todavía no ha llegado el cumpleaños.
if(
    mesActual < mesNacimiento ||
    (mesActual === mesNacimiento && diaActual < diaNacimiento)
) {
    edad--;
}

console.log("Fecha actual: ", fechaActual)
console.log("Fecha de nacimiento: ", fechaNacimiento)
console.log("Después de comprobar si todavía no ha llegado el cumpleaños.")
console.log(`Han trancurrido:  ${edad} años.`)

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

// 1. Fecha completa
console.log("1.", fechaNacimiento.toLocaleDateString("es-ES"))

// 2. Hora
console.log("2.", fechaNacimiento.toLocaleTimeString("es-ES"))

// 3. Fecha y hora
console.log("3.", fechaNacimiento.toLocaleString("es-ES"))

// 4. Día del mes
// console.log("4.", fechaNacimiento.toLocaleDateString) PORQUÉ NO ES ASÍ COMO LAS ANTERIORES!!!
console.log("4.", fechaNacimiento.getDate())

// 5. Mes (número)
console.log("5.", fechaNacimiento.getMonth() +1) // Al mostrarlo por consola tenemos que añadirle +1 porque los meses empiezan en 0.

// 6. Año
console.log("6.", fechaNacimiento.getFullYear())

// 7. Día de la semana (número)
console.log("7.", fechaNacimiento.getDay())

// 8. Nombre del día
console.log("8.", fechaNacimiento.toLocaleDateString("es-ES", {
    weekday: "long",
})
)

// 9. Nombre del mes
console.log(
    "9.",
    fechaNacimiento.toLocaleDateString("es-ES", {
        month: "long"
    })
)

// 10. Día del año

// Creamos una fecha que representa el 31 de diciembre del año anterior.
const inicioAnio = new Date(fechaNacimiento.getFullYear(), 0, 0)
const diferencia = fechaNacimiento - inicioAnio // Al restar dos objetos Date, JavaScript devuelve automáticamente
                                                // la diferencia entre ambas fechas en milisegundos.
console.log(diferencia)
console.log("/")
const unDia = 1000 * 60 * 60 * 24; // Por eso aquí calculamos los milisegundos que tiene un día
console.log(unDia)
const diaDelAnio = Math.floor(diferencia / unDia) // Y así podemos dividir los dos resultados que están en milisegundos,
                                                  // Convertimos los milisegundos en días dividiendo entre los
                                                  // milisegundos que tiene un día y con Math.floor() redondeamos y elimina la parte decimal.

console.log("=",diaDelAnio)

