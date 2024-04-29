/*
    * #14 FECHAS
*/

let fechaActual = new Date();
let fechaNacimiento = new Date("2005-04-15T12:00:00");

let diferenciaMilisegundos = fechaActual - fechaNacimiento;
let añosTranscurridos = Math.floor(diferenciaMilisegundos / (1000 * 60 * 60 * 24 * 365.25));
console.log("Han transcurrido " + añosTranscurridos + " años desde mi nacimiento.");

/*
    * DIFICULTAD EXTRA
*/

console.log("1. Día, mes y año: " + fechaNacimiento.getDate() + "/" + (fechaNacimiento.getMonth() + 1) + "/" + fechaNacimiento.getFullYear())

console.log("2. Hora, minuto y segundo: " + fechaNacimiento.getHours() + ":" + fechaNacimiento.getMinutes() + ":" + fechaNacimiento.getSeconds())

console.log("3. Día de año: " + (Math.floor((fechaNacimiento - new Date(fechaNacimiento.getFullYear(), 0, 0)) / 86400000)))

console.log("4. Día de la semana: " + fechaNacimiento.toLocaleString('es', { weekday: 'long' }))

console.log("5. Nombre del mes: " + fechaNacimiento.toLocaleString('es', { month: 'long' }))

console.log("6. Mes abreviado y año: " + fechaNacimiento.toLocaleString('es', { month: 'short' }) + " " + fechaNacimiento.getFullYear())

console.log("7. Hora en formato de 12 horas: " + ((fechaNacimiento.getHours() % 12) || 12) + ":" + fechaNacimiento.getMinutes() + ":" + fechaNacimiento.getSeconds() + " " + (fechaNacimiento.getHours() >= 12 ? 'PM' : 'AM'))

console.log("8. Edad en días: " + Math.floor((fechaActual - fechaNacimiento) / (1000 * 60 * 60 * 24)))

console.log("9. Edad en meses: " + Math.floor((fechaActual - fechaNacimiento) / (1000 * 60 * 60 * 24 * 30.44)))

console.log("10. Día de la semana abreviado, día de mes y año: " + fechaNacimiento.toLocaleString('es', { weekday: 'short' }) + ", " + fechaNacimiento.getDate() + " de " + fechaNacimiento.toLocaleString('es', { month: 'long' }) + " de " + fechaNacimiento.getFullYear())
