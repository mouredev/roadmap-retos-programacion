//#1

let x = 10
let y = 5

//Operaciones aritméticas
let suma = x + y //15
let resta = x - y // 5
let multiplicacion = x * y //50
let division = x / y // 2
let modulo = x % y // 0

//Operaciones de comparacion
let esMayor = x > y // True
let esMenor = x < y // False

//Operadores lógicos
let ambosVerdaderos = esMayor && esMenor // False
let algunoVerdadero = esMayor || esMenor // True

//operador ternario
let mensaje = x > y ? 'x es mayor que y' : 'y es mayor o igual que x'

//#2

//if - else if - else
let edad = 18

if (edad > 18) {
    console.log('Puedes pasar')
} else if (edad == 17) {
    console.log('Podemos hacer una exepción')
} else {
    console.log('No puedes pasar')
}

//switch
let dia = 'viernes'

switch (dia) {
    case 'lunes':
    case 'martes':
    case 'miercoles':
    case 'jueves':
    case 'viernes':
        console.log('Dia laborable');
        break;
    case 'sabado':
    case 'domingo':
        console.log('Fin de semana');
        break;
}

//Bucle while
let i = 0

while(i < 10){
    console.log(i)
    i++
}

//Bucle do while
let I = 0

do{
    console.log(I)
    i++
}while(I < 5)

//Bucle for
for(let i = 0; i < 7; i++){
    console.log(i)
}

//Ejercicio EXTRA
for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i)
    }
}
