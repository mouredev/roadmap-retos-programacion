// ** EJERCICIO

let fechaActual = new Date
let fechaNacimiento = new Date(2001, 9, 16, 20, 22, 22)

new Date()

let restaAños = fechaActual.getFullYear() - fechaNacimiento.getFullYear() + ' años'
restaAños // '23 años'


// ** DIFICULTAD EXTRA ** -----------------------------------------------------------------------------------------------------------------------------------------------

let diaMesAño = fechaNacimiento.getDate() + ' - ' + fechaNacimiento.getMonth() + ' - ' + fechaNacimiento.getFullYear()
diaMesAño // '1 - 1 - 2000'


let horaMinutoSegundo = fechaNacimiento.getHours() + ':' + fechaNacimiento.getMinutes() + ':' + fechaNacimiento.getSeconds()
horaMinutoSegundo // '20:22:22'


function diaDeAño(date) {
    let fechaInicioAño = new Date(Date.UTC(date.getFullYear(), 0, 1))
    console.log(Math.floor((fechaNacimiento.getTime() - fechaInicioAño.getTime())/1000/60/60/24) + ' días')
}

diaDeAño(fechaNacimiento)


let semanas = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
let nombreDeLaSemana = semanas[fechaNacimiento.getDay()-1]
nombreDeLaSemana


let meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
let nombreDelMes = meses[fechaNacimiento.getMonth()-1]
nombreDelMes