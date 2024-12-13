// * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
//  * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
//  * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
//  * Calcula cuántos años han transcurrido entre ambas fechas.

const fechaNow = new Date()
console.log(fechaNow)
const añoNow = fechaNow.getFullYear()
console.log(añoNow)

const fechaBD = new Date("1987-04-29:10:15:00z")
console.log(fechaBD)
const añoBD = fechaBD.getFullYear()
console.log(añoBD)

function calculadoraDeAños( añoN, añoB ){
    return añoN - añoB
}

console.log(calculadoraDeAños(añoNow, añoBD) + ' trascurridos desde que naciste')



// Extra 
// Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
//  * 10 maneras diferentes. Por ejemplo:
//  * - Día, mes y año.
//  * - Hora, minuto y segundo.
//  * - Día de año.
//  * - Día de la semana.
//  * - Nombre del mes.
//  * (lo que se te ocurra...)

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date


console.log( 'fecha normal' +fechaNow.getFullYear() ,fechaNow.getMonth(), fechaNow.getDay())
console.log(fechaNow.toDateString() +'datostring')
console.log( 'hora ' +fechaNow.getHours() ,fechaNow.getMinutes(), fechaNow.getSeconds())
console.log(fechaNow.toTimeString())
console.log(fechaNow[Symbol.toPrimitive]('string'))
console.log(fechaNow.toISOString()+ 'iso')
console.log(fechaNow.toTimeString())
const [mes, dia, año] = [
    fechaBD.getMonth(),
    fechaBD.getDay(),
    fechaBD.getFullYear()
]
console.log(mes, dia, año)

const [hour, minutes, seconds] = [
    fechaBD.getHours(),
    fechaBD.getMinutes(),
    fechaBD.getSeconds(),
  ];
  console.log(hour, minutes, seconds)