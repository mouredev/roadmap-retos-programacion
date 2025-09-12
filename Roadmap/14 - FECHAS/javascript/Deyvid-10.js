// Fechas

let fechaActual = new Date()
let fechaNacimiento = new Date(1999, 10, 10, 2, 0)

console.log(`La fecha actual es: ${fechaActual.getDate()}-${fechaActual.getMonth() + 1}-${fechaActual.getFullYear()}\nLa hora es: ${fechaActual.getHours()}:${fechaActual.getMinutes()}`);
console.log(`La fecha de nacimiento es: ${fechaNacimiento.getDate()}-${fechaNacimiento.getMonth() + 1}-${fechaNacimiento.getFullYear()}\nLa hora de nacimineto es: ${fechaNacimiento.getHours()}:${fechaNacimiento.getMinutes()}`);

let diferencia = fechaActual.getTime() - fechaNacimiento.getTime()

let difMin = diferencia / (1000 * 60)
let difHoras = difMin / 60
let difDias = difHoras / 24
let difMes = difDias / 30.4375
let difAnio = difMes / 12

console.log(`Han pasado ${Math.floor(difAnio)} anios`); // Diferencia de anios

// DIFICULTAD EXTRA

let arrayMeses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

let arrayDiaSemana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

let ampm = fechaNacimiento.toLocaleTimeString()
let fecha = fechaNacimiento.toLocaleDateString()
let segundos = fechaNacimiento.getSeconds()
let min = fechaNacimiento.getMinutes()
let hora = fechaNacimiento.getHours()
let diaSemana = fechaNacimiento.getDay()
let dia = fechaNacimiento.getDate()
let mes = fechaNacimiento.getMonth()
let anio = fechaNacimiento.getFullYear()

console.log(`La fecha completa: ${fechaNacimiento}`); // Fecha y hora completa
console.log(`Fecha: ${fecha}`); // Formato DD/MM/AAAA
console.log(`Hora: ${hora}:${min}:${segundos}`); // Formato HH:MM:SS
console.log(`El nombre del mes: ${arrayMeses[mes]}`); // Nombre del mes
console.log(`El dia de la semana es: ${arrayDiaSemana[diaSemana]}`); // Dia de la semana
console.log(`Dia ${dia} de ${arrayMeses[mes]} del ${anio}`); // Fecha con nombre del mes
console.log(`Hora: ${hora}:${min}`);// Formato HH:MM
console.log(`Hora: ${ampm}`); // Formato AM/PM
console.log(`Mi anio de nacimiento es: ${anio}`); // Solo el anio
console.log(`Naci a las ${hora} horas con ${min} minutos`); // Hora de nacimineto