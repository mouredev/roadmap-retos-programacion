// Operadores aritméticos
console.log('Operadores Aritméticos')

const suma = 10 + 3
console.log( 'Suma: 10 + 3 = ', suma )

const resta = 10 - 3
console.log( 'Resta: 10 - 3 = ', resta )

const multiplicacion = 10 * 3
console.log( 'Multiplicación: 10 * 3 = ', multiplicacion )

const division = 10 / 3
console.log( 'División: 10 / 3 = ', division )

const modulo = 10 % 3
console.log( 'Módulo: 10 % 3 = ', modulo ) // El resto que nos queda al dividir

const exponente = 10 ** 3
console.log( 'Exponente: 10 ** 3 = ', exponente ) // Calcula la base a la potencia


console.log('******************************')


// Operaciones de comparación => nos retorna true o false
console.log('Operadores de Comparación')

const igualdad = 3 == '3'
console.log( '3 es igual que "3" => ', igualdad)

const igualdadEstricta = 3 === '3'
console.log( '3 es igual que "3" => ', igualdadEstricta)

const desigualdad = 3 != '3'
console.log( '3 es desigual que "3" => ', desigualdad)

const desigualdadEstricta = 3 !== '3'
console.log( '3 es desigual que "3" => ', desigualdadEstricta)

const mayorQue = 3 > 5
console.log( '3 es mayor que 5 => ', mayorQue)

const mayorIgual = 3 >= 3
console.log( '3 es mayor o igual que 3 => ', mayorIgual)

const menorQue = 3 < 5
console.log( '3 es menor que 5 => ', menorQue)
const menorIgual = 3 <= 5
console.log( '3 es menor o igual que 5 => ', menorIgual)


console.log('******************************')


// Operadores lógicos
console.log( 'Operadores Lógicos')

const and = 10 + 3 == 13 && 5 - 1 == 4
console.log(` AND &&: 10 + 3 == 13 and 5 - 1 == 4 => ${ and } `)

const or = 10 + 3 == 14 || 5 - 1 == 4
console.log(` OR ||: 10 + 3 == 14 or 5 - 1 == 4 => ${ or } `)

const not = !(10 + 3 == 14)
console.log(` NOT !: not 10 + 3 == 14 => ${ not } `)


console.log('******************************')


// Operadores de asignación
console.log('Operadores de Asignación')

let myNumber = 11
console.log( 'Mi número: ', myNumber ) // Asignación

myNumber += 1
console.log( 'Suma 1 y asignación: ', myNumber) // Suma y asignación

myNumber -= 1
console.log( 'Resta 1 y asignación: ', myNumber) // Resta y asignación

myNumber *= 2
console.log( 'Multiplicación por 2 y asignación: ', myNumber) // Multiplicación y asignación

myNumber /= 2
console.log( 'División por 2 y asignación: ', myNumber) // División y asignación

myNumber %= 2
console.log( 'Módulo de 2 y asignación: ', myNumber) // Módulo y asignación

myNumber **= 1
console.log( 'Exponente de 1 y asignación: ', myNumber) // Exponente y asignación


console.log('******************************')


// Operadores de pertenencia
console.log('Operadores de Pertenencia')

const name = 'socramdev'
console.log( 'Mi nombre es ', name)

const result = name.includes('d')
console.log( 'Mi nombre incluye la letra d: ', result )


console.log('******************************')


// Operadores de bit
console.log('Operadores de bit')

let n1 = 10 // 1010
console.log( n1, 'en binario es 1010' )

let n2 = 3 // 0011
console.log( n2, 'en binario es 0011' )

// Operador bit AND. Convierte los números a bits, y los compara, donde 0+0=0, 1+0=0, 0+1=0, 1+1=1, en este caso el resultado es 0010, que convertido a numero entero es el 2
let resultado = n1 & n2
console.log( 'Si los bits son iguales da 1: ', resultado, 'que en binario es 0010')

// Si al menos hay un 1, el resultado es 1, por lo que seria 1011
let resultado2 = n1 | n2
console.log( 'Si al menos un bit es 1 da 1: ', resultado2, 'que en binario es 1011')

// Si los bit son iguales, el resultado es 0, por lo que es 1001
let resultado3 = n1 ^ n2
console.log( 'Si los bits son iguales da 0: ', resultado3, 'que en binario es 1001')


console.log('******************************')


/*
    Estructuras de Control
*/

// Condicionales
console.log('Condicional IF')
const edad = 46
if(edad < 46) {
    console.log('Tengo más edad')
} else if(edad == 46) {
    console.log('Es mi edad')
} else {
    console.log('Tengo menos edad')
}


console.log('******************************')

// Iterativas
console.log('Iterativa FOR')
const limite = 10
for (let index = 0; index < 11; index++) {
    console.log( index )
}


console.log('******************************')


console.log('Iterativa WHILE')
let contador = 0
while (contador < 11) {
    contador++
    console.log(contador)
}


console.log('******************************')


console.log('Manejo de Excepciones')
try {
    console.log( 'Dividimos 10/1: ', 10 / 1 )
} catch (error) {
    console.log( 'El error es: ', error )
} finally {
    console.log('Ha finalizado el manejo de excepciones')
}


console.log('******************************')


console.log('EXTRA')
for (let i = 10; i < 56; i++) {
    if( i % 2 === 0 && i !== 16 && i % 3 !== 0 ) {
        console.log(i)
    }
}