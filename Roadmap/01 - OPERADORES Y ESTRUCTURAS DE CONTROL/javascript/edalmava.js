console.log('Operadores')
console.log('')

// Operadores matemáticos

const x = 5, y = 10
console.log('Operadores Matemáticos')
console.log(`Dado los valores x = ${x}, y = ${y}`)
console.log(`La suma de ${x} + ${y} = ${x + y}`)
console.log(`La resta de ${x} - ${y} = ${x - y}`)
console.log(`La multiplicación de ${x} * ${y} = ${x * y}`)
console.log(`La división de ${x} / ${y} = ${x / y}`)
console.log(`El resto de la división entera entre ${x} % ${y} = ${x % y}`)
console.log(`La exponenciación: ${y} ** ${x} = ${y ** x}`)

console.log('Operador de Incremento y Decremento')
let z = 5, w = 6
console.log(`Dado los  valores z = ${z} y w = ${w}`)
z++, w--
console.log(`z++ = ${z}`)
console.log(`w-- = ${w}`)

console.log('Operadores a nivel de bit')
const a = 5, b = 3
console.log(`Dado los valores a = ${a} y b = ${b}`)
console.log(`AND bit a bit: ${a} & ${b} = ${a & b}`)
console.log(`OR bit a bit: ${a} | ${b} = ${a | b}`)
console.log(`XOR bit a bit: ${a} ^ ${b} = ${a ^ b}`)
console.log(`NOT bit a bit: ~${a} y ~-${b} = ${~a} y ${~-b}`)  // -(x + 1)
console.log(`Left Shift: ${a} << ${b} = ${a << b}`)
console.log(`Right Shift: ${a} >> ${2} = ${a >> 2}`)
console.log(`Unsigned Right Shift: ${a} >>> ${2} = ${a >>> 2}`)

console.log('Operador coma')
/*
  El operador coma nos permite evaluar varias expresiones, 
  separándolas con una coma ,. Cada expresión se evalúa, 
  pero sólo se devuelve el resultado de la última.
*/
let c = (1 + 2, 3 + 4);
console.log(c)   // 7 (el resultado de 3 + 4)

console.log('Operadores de Comparación')
const d = 10, e = 15
console.log(`Dado los valores d = ${d} y e = ${e}`)
console.log(`Mayor que: ${d} > ${e} = ${d > e}`)
console.log(`Menor que: ${d} < ${e} = ${d < e}`)
console.log(`Igual que: ${d} == ${e} = ${d == e}`)
console.log(`Distinto que: ${d} != ${e} = ${d != e}`)
console.log(`Igualdad: 0 === false = ${0 == false}`)
console.log(`Igualdad estricta: 0 === false = ${0 === false}`)

console.log('Operador Ternario')
const age = 20
console.log((age > 18) ? true : false)

console.log('Operadores Lógicos')
console.log(`OR: true || false = ${true || false}`)
console.log(`OR: false || false = ${false || false}`)
console.log(`AND: true && false = ${true && false}`)
console.log(`AND: true && true = ${true && true}`)
console.log(`NOT: !true = ${!true}`)
console.log(`NOT: !false = ${!false}`)

console.log("Operador Nullish Coalescing '??'")
/*
  Una expresión es “definida” cuando no es null ni undefined.

  El resultado de a ?? b:
      si a está “definida”, será a,
      si a no está “definida”, será b.
*/
let user
console.log(user ?? "Anonymous")

console.log('')
console.log('Bucles o ciclos')
console.log('')

console.log('Bucle while')
let i = 0
while (i < 3) {
    console.log(i)
    i++
}

console.log('Bucle do..while')
/*
  Esta sintaxis solo debe ser usada cuando quieres que el 
  cuerpo del bucle sea ejecutado al menos una vez sin importar 
  que la condición sea verdadera. 
*/
i = 0
do {
    console.log(i)
    i++
} while (i < 3)

console.log('Bucle for')
for (let i = 0; i < 3; i++) {
    console.log(i)
}

console.log('Bucle for..in')
/*
  Para recorrer todas las claves de un objeto 
*/
user = {
  name: "John",
  age: 30,
  isAdmin: true
}

for (let key in user) {
  // claves
  console.log( key ) // name, age, isAdmin
  // valores de las claves
  console.log( user[key] ) // John, 30, true
}
// Recorrer todas las letras de una cadena
let cadena = "Hola, JavaScript"
for (let l in cadena) {
    console.log(cadena[l])
}

console.log('Bucle for..of')
/*
  Para iterar sobre los elementos de un array
*/
let fruits = ["Apple", "Orange", "Plum"]

// itera sobre los elementos del array
for (let fruit of fruits) {
  console.log( fruit )
}
// Recorrer todas las letras de una cadena
cadena = "Hola, JavaScript"
for (let l of cadena) {
    console.log(l)
}

console.log('')
console.log('Sentencia switch')
let res = 2 + 2;

switch (res) {
  case 3:
    console.log( 'Muy pequeño' );
    break;
  case 4:
    console.log( '¡Exacto!' );
    break;
  case 5:
    console.log( 'Muy grande' );
    break;
  default:
    console.log( "Desconozco estos valores" );
}

console.log('')
console.log('RETO EXTRA')
console.log('')

Array.from({ length: 55 - 10 + 1 }
           , (_, i) => 10 + i)
    .filter(n => n % 2 === 0 && n !== 16 && n % 3 !== 0)
