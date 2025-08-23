// Tipos de Operadores 

// Aritmeticos

let a = 5
let b = 2

let suma = a + b
let resta = a - b
let multiplicacion = a * b
let division = a / b
let modulo = a % b
let incremento = a++
let decremento = a--

console.log(suma)
console.log(resta)
console.log(multiplicacion)
console.log(division)
console.log(modulo)
console.log(incremento)
console.log(decremento)

// Asignacion
let name = 'Josue'
let age = 20
let city = 'CDMX'

name += 'VH07'
age -= 5
city *= 2

console.log(name)
console.log(age)
console.log(city)

// Comparacion

let num1 = 5
let num2 = 5

let resultado = num1 == num2
let resultado2 = num1 === num2
let resultado3 = num1 != num2
let resultado4 = num1 !== num2
let resultado5 = num1 < num2
let resultado6 = num1 > num2
let resultado7 = num1 <= num2
let resultado8 = num1 >= num2

console.log(resultado)
console.log(resultado2)
console.log(resultado3)
console.log(resultado4)
console.log(resultado5)
console.log(resultado6)

// Logicos

let valor1 = true
let valor2 = false

let resultado9 = valor1 && valor2
let resultado10 = valor1 || valor2
let resultado11 = !valor1

console.log(resultado9)
console.log(resultado10)
console.log(resultado11)

// Bitwise

let num3 = 5
let num4 = 2

let resultado12 = num3 & num4
let resultado13 = num3 | num4
let resultado14 = num3 ^ num4
let resultado15 = ~num3
let resultado16 = num3 << num4
let resultado17 = num3 >> num4
let resultado18 = num3 >>> num4

console.log(`AND: 5 & 2 = ${resultado12}`)
console.log(`OR: 5 | 2 = ${resultado13}`)
console.log(`XOR: 5 ^ 2 = ${resultado14}`)
console.log(`NOT: ~5 = ${resultado15}`)
console.log(`Desplazamiento a la izquierda: 5 << 2 = ${resultado16}`)
console.log(`Desplazamiento a la derecha: 5 >> 2 = ${resultado17}`)
console.log(`Desplazamiento sin signo: 5 >>> 2 = ${resultado18}`)


// Operador ternario

let valor3 = true
let valor4 = false

let resultado19 = valor3 ? 'Verdadero' : 'Falso'
let resultado20 = valor4 ? 'Verdadero' : 'Falso'

console.log(resultado19)
console.log(resultado20)

// Concatenacion

let string1 = 'Hola'
let string2 = 'Mundo'

let resultado21 = string1 + ' ' + string2

console.log(resultado21)

// Typeof

let variable = 'JosueVH07'
let variable2 = 7
let variable3 = 7.7
let variable4 = true
let variable5 = null
let variable6 = undefined

console.log(typeof variable)
console.log(typeof variable2)
console.log(typeof variable3)
console.log(typeof variable4)
console.log(typeof variable5)


// Operadores de instancia

const person = {
    name: 'Josue',
    age: 20,
    city: 'CDMX',
    country: 'Mexico'
}

let resultado22 = 'name' in person
console.log(resultado22)



// Dificukltad extra 

for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i)
    }
}