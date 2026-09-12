//Tipos de operadores en javascript

//Operadores de asignacion

let asignacion1 = 2 //asignacion
asignacion1+=3 //asignacion de suma + 3
asignacion1-=2 //asignacion de resta -2 
asignacion1*=2 //asignacion de multiplicacion *2 
asignacion1/=2 //asignacion de division /2 
asignacion1%=2 //asignacion de residuo 
asignacion1**=2 //asignacion de exponente 
asignacion1<<=2 //asignacion de desplazamiento a izquierda cada posicion es como un exponente 2 si es 2 daria igual a *2 *2 
asignacion1>>=2 //asignacion de desplazamiento a derecha cada posicion es como una dividsion entre si es 2 daria iguala /2 /2
asignacion1>>>=2 //asignacion de desplazamiento a derecha sin signo cada posicion es como una dividsion entre si es 2 daria iguala /2 /2
asignacion1>>=2 //asignacion de desplazamiento a derecha cada posicion es como una dividsion entre si es 2 daria iguala /2 /2

console.log(asignacion1)

//Operadores aritmeticos

let a = 0
let b = 0

let suma = a + b
let resta = a - b
let multiplicacion = a * b
let division = a / b
let modulo = a % b
let exponente = a ** b
console.log(suma)
console.log(resta)
console.log(multiplicacion)
console.log(division)
console.log(modulo)
console.log(exponente)

++a //incremento de la variable antes de su uso
--a //decremento de la variable antes de su uso
a++ //incremento de la variable luego de su uso
a-- // decremento de la variable luego de su uso
console.log(a)


//Operadores de comparacion

let igual = a == b //comparar los valores de dos variables sean iguales
let noIgual = a != b //comparar que dos valores de dos variables no sean iguales
let estrictoIgual = a === b //comparar que dos valores sean exactamente igual el uno del otro
let noEstrictoIgual = a !== b //comparara que dos valores no sean exactamente igual el uno del otro
let mayorQue = a > b //comparar o verificar que un numero sea mayor que otro
let menorQue = a < b //comparar que un numero sea menor que otro
let mayorIgual = a >= b //comparar que un numero sea mayor o que sea exactamente igual al otro
let menorIgual = a <= b //comparar que un numero sea menor o sea igual al otro
console.log(igual)
console.log(noIgual)
console.log(estrictoIgual)
console.log(noEstrictoIgual)
console.log(mayorQue)
console.log(menorQue)
console.log(mayorIgual)
console.log(menorIgual)


// Operadores logicos 
c = Math.random()
let and =  (a > b && c < a)
let or =  (a > b || c < a)
let not =  (!(a > b) && c < a)
console.log(and)
console.log(or)
console.log(not)

//Estructuras de control

// if

let num1 = Math.random()
let num2 = Math.random()
if (num1 < num2){
    console.log(`${num2} is greater than ${num1}`)
} else if (num1 == num2){
    console.log(`${num1} is equal than ${num2}`)
} else {
    console.log(`${num1} is greater than ${num2}`)
}

// switch
let month = 9
let monthName

switch(month){
    case 9:
      monthName = 'September'
      break;
    case 10:
      monthName = 'October'
      break;
    case 11:
      monthName = 'November'
      break;
    case 12:
      monthName = 'December'
      break;
    default:
      monthName = "This mont can't be soon"
}
console.log(monthName)

//Operador Ternario

let hour = 12

const time = hour < 12 ? 'Is morning right now' : 'Is afternoon right now'
console.log(time)


//Extra
for (let i = 10; i<=55; i++){
    if(i % 3 == 0) {
        continue
    } else if (i == 16) {
        continue
    } else if(i % 2 == 0){
        console.log(i)
    }
}