// <-------------- Objeto Date() -------------->

const fechaActual = new Date()

const fechaDeNacimiento = new Date(1998, 0, 12, 3, 23, 8)

const diferenciaMilisegundos = fechaActual - fechaDeNacimiento
const diferenciaAnios = Math.floor(diferenciaMilisegundos / (1000 * 60 * 60 * 24 * 365))

console.log(`Entre ambas fechas han transcurrido ${diferenciaAnios} años.`)


// <-------------- Extra -------------->

const semana = ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']
const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

let anio = fechaDeNacimiento.getFullYear()
let mes = fechaDeNacimiento.getMonth()
let mes_formateado = ('0' + (mes + 1)).slice(-2)
let dia = fechaDeNacimiento.getDate()
let diaSemana = fechaDeNacimiento.getDay()
let horas = fechaDeNacimiento.getHours()
horas = ('0' + horas).slice(-2)
let minutos = fechaDeNacimiento.getMinutes()
minutos = ('0' + minutos).slice(-2)
let segundos = fechaDeNacimiento.getSeconds()
segundos = ('0' + segundos).slice(-2)

console.log(`${anio}-${mes_formateado}-${dia}`) // 1998-01-12
console.log(`${meses[mes]} ${dia} de ${anio}`) // Enero 12 de 1998
console.log(`${horas} horas / ${minutos} minutos / ${segundos} segundos`) // 03 horas / 23 minutos / 08 segundos
console.log(`${horas}:${minutos}:${segundos}`) // 03:23:08
console.log(`${semana[diaSemana]} de ${anio}`) // Lunes de 1998
console.log(`${meses[mes]}`) // Enero
console.log(`${semana[diaSemana]} ${dia} de ${meses[mes]} de ${anio}`) // Lunes 12 de Enero de 1998