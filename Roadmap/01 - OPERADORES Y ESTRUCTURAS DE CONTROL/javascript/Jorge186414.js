/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

//* Opearadores de Asignacion
var x
var y = x
// Asignacion de adicion
console.log(x += y)
// Asignacion de resta
console.log(x -= y)
// Asignacion de multiplicacion
console.log(x *= y)
// Asignacion de division
console.log(x /= y)
// Asignacion de residuo
console.log(x %= y)
// Asignacion de exponenciacion
console.log(x **= y)

//* Operadores de Comparacion
var numero1 = 10
var numero2 = 8
// Igual
console.log(numero1 == numero2)
// No es igual
console.log(numero1 != numero2)
// Estrictamente igual
console.log(numero1 === numero2)
// Desigualdad estricta
console.log(numero1 !== numero2)
// Mayor que
console.log(numero1 > numero2)
// Mayor o igual que
console.log(numero1 >= numero2)
// Menor que
console.log(numero1 < numero2)
// Menor o igual que
console.log(numero1 <= numero2)

//* Operadores Aritmeticos
// Residuo
console.log(numero1 % numero2)
// Suma
console.log(numero1 + numero2)
// Resta 
console.log(numero1 - numero2)
// Division
console.log(numero1 / numero2)
// Multitplicacion
console.log(numero1 * numero2)
// Decremento
console.log(numero1--)
// Incremento
console.log(numero2++)

//* Operadores bit a bit 
var var1 = 8
var var2 = 4
// AND
console.log(var1 & var2)
// OR
console.log(var1 | var2)
// XOR 
console.log(var1 ^ var2)
// NOT
console.log(~var1);
// Desplazamiento a la derecha
console.log(var1 >> 1)
// Desplazamiento a la izquierda
console.log(var1 << 1)
// Desplazamiento a la derecha sin signo
console.log(var1 >>> 1)

//* Operadores Logicos
var x = 19
var y = 87
let and = (x < y) && (y > 70)
let or = (x == y) || (x < y)
let not = !(x > y)
console.log(`AND: ${and}`)
console.log(`OR: ${or}`)
console.log(`NOT: ${not}`)

//* Operadores de cadena
// Concatenacion 
let nombre = 'Jorge'
console.log("Hola " + nombre);
// Concatenacion Abreviado
nombre += ' Miranda'
console.log(nombre);

// Operador condicional (Ternario)
let edad = 22
let resultado = edad >= 18 ? 'Es mayor de edad.' : 'Es menor de edad.'
console.log(resultado);

/*
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
*/

//! Condicionales
if ((edad > 10) && (edad < 15)) {
  console.log('Eres un ninio')
} else if ((edad > 15) && edad < 18) {
  console.log('Eres un adolescente')
} else {
  console.log('Eres un universitario')
}

//! Bucle for
for (let i = 0; i < 10; i++) {
  let siguiente = i + 1
  console.log(`${i} * ${siguiente} = ${siguiente * i}`)
}

//! Bucle for of
let mangas = ['Dragon Ball', 'One Piece', 'Hunter X Hunter', 'BTOOM']
for (manga of mangas) {
  console.log(manga)
}
//! Bucle for in
const datos_manga = {
  autor: 'Eichiro Oda',
  nombre: 'One Piece',
  tomos: 108,
  editorial: 'Panini Mexico'
}

for (dato in datos_manga) {
  console.log(dato)
}

for (dato in datos_manga) {
  console.log(`${dato}: ${datos_manga[dato]}`)
}

//! Bucle while
let contador = 0
while (contador < 10) {
  console.log(`contador desde while: ${contador}`)
  contador++
}

//! Bucle do while
let contador2 = 0
do {
  console.log(`contador desde do while: ${contador2}`)
  contador2++
} while (contador2 < 10)

//! Switch
var nombre1 = 'Julio'
switch (nombre1.length) {
  case 4:
    console.log('Tu nombre tiene 4 letras')
    break
  case 5:
    console.log('Tu nombre tiene 5 letras')
    break
  case 6:
    console.log('Tu nombre tiene 6 letras')
    break
}

/* 
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/
for (i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 === 0) {
    console.log(i)
  }
}