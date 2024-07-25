/*
 * EJERCICIO:
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

//Fecha actual
let fecha = new Date()
console.log(fecha)

//Fecha de nacimiento
let nacimiento = new Date()
nacimiento.setUTCFullYear(1999)
nacimiento.getUTCFullYear()
nacimiento.setMonth(6) //Los meses en JavaScript van de 0 (enero) a 11 (diciembre)
nacimiento.getMonth()
nacimiento.setDate(22)
nacimiento.getDate()
console.log(nacimiento)

//Calculamos el tiempo transcurrido entre ambas fechas
let edad = fecha -nacimiento //Edad en milisegundos
console.log(edad)




