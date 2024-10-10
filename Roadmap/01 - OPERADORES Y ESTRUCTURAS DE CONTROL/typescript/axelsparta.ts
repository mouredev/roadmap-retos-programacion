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

// #Operadores de asignación
let x, y

// ##Asignación
x = 10
y = 5

// ##Asignación de adición
x += y // lo mismo que x = x + y 

// ##Asignación de resta
x -= 5 // lo mismo que x = x - 5

// ##Asignación de multiplicación
y *= 3 // lo mismo que y = y * 3

// ##Asignación de división
x /= 2 // lo mismo que x = x / 2

// ##Asignación de residuo
x /= 2 // lo mismo que x = x / 2

// ##Asignación de exponenciación
y **= 3 // lo mismo que y = y**3

// #Operadores de comparación
let myVar = 3
// Igual ==: devuelve true si los operandos son iguales
console.log(3 == myVar)
// Diferente o no es igual != devuelve true si los operandos son distintos
console.log(3 != myVar)
// Estrictamente igual === devuelve true si los operandos son iguales y del mismo tipo de datos
console.log(3 === myVar)
// Desigualdad estricta !== devuelve true si los operandos son del mismo tipo pero no iguales, o son de diferente tipo
console.log(3 !== myVar)
// mayor que
console.log(3 > 5) // false
console.log(5 > 2) // true
// mayor o igual que
console.log(5 >= 5) // true
// menor que
console.log(3 < 5) // true
console.log(3 < 3) // false
// menor o igual que
console.log(3 <= 3) // true

// #Operadores aritméticos
console.log(`Residuo ${10 % 3}`) // devuelve el resto de la división 10 / 3
// incremento
++myVar // si se utiliza como operador prefijo devuelve el valor del operando después de haber sumado uno
myVar++  // si se utiliza como operador sufijo devuelve el valor del operando y luego se suma uno
// decremento
--myVar // similar al incremento
myVar--
// negación unaria: devuelve la negación de su operando
console.log(-myVar)
// positivo unario: intenta convertir el operando en un número aún si no lo es
console.log(+true) // 1
// operador de exponenciación
console.log(3 ** 2)

// #Operadores lógicos
// AND Lógico &&: expr1 && expr2 -> devuelve true sólo cuando las dos expresiones son true
let a1 = true && true // -> true
let a2 = false && true // -> false

// OR lógico ||: expr1 || expr2 -> devuelve true si la expr1 es true o la expr2 es true, y devuelve false cuando las dos expresiones son falsas
let o1 = true || true; // -> true
let o2 = false || true; // -> true
let o3 = true || false; // -> true
let o4 = false || false // -> false

// NOT lógico !expr: simplemente niega la expresión
let n1 = !true; // -> false
let n2 = !false; // -> true
let n3 = !"Cat"; // -> false

// #Operadores de cortocircuito
// ## Cortocircuito OR - cuando el valor de la izquierda de la expresión siempre pueda validar a true, es el valor que se cargará por defecto  (encuentra el primer valor verdadero), cargará el valor que sea truthy  
let myValue = '' || ''
console.log(myValue) // -> ''
let myValue2 = 'first value' || 'second value'
console.log(myValue2) // -> 'first value'
let myValue3 = '' || 'second value'
console.log(myValue3) // -> 'second value'
let myValue4 = 'first value' || ''
console.log(myValue4) // -> 'first value'

// ## Cortocircuito AND - cuando el valor de la izquierda en la expresión siempre pueda validar a false, es el valor que se cargará por defecto (encuentra el primer valor false)
myValue = '' && ''
console.log(myValue) // -> ''
myValue2 = 'first value' && 'second value'
console.log(myValue2) // -> 'second value'
myValue3 = '' && 'second value'
console.log(myValue3) // -> ''
myValue4 = 'first value' && ''
console.log(myValue4) // -> ''

// ##Operador Nullish Coalescing '??'
/* Es parecido al operador '||' a diferencia que solo valida si los datos son null o undefined */
let myVariable1 = 0
let myResult = myVariable1 || 30
console.log(myResult) // -> 30 como 0 es un valor falsy no toma ese valor
myResult = myVariable1 ?? 30
console.log(myResult) // -> 0 myVariable1 no es undefined ni null con lo cual toma ese valor

// #Operador ternario condicional
let age = 20
let statusAge = age >= 18 ? "adult" : "minor";


// #Estructuras de control básicas

// ##IF-ELSE
let myCondition = true
if (myCondition) {
  console.log('My condition is true')
} else {
  console.log('My condition is false')
}

// ##WHILE
let i = 0
while (i < 10) {
  console.log(`Se repite el while hasta que no se cumpla la condición ${i}`)
  i++
}
// ##DO-WHILE
i = 0
do {
  console.log(`Se repite el bucle al menos una vez, y se seguirá repitiendo hasta que no se cumpla la condición ${i}`)
  i++
} while(i < 10)

// ##FOR for([iniciacion de la variable]; [condición]; [incremento o decremento de la variable])
for(let j = 0; j <= 10; j++) {
  console.log(j)
}
// ##SWITCH
let fruit = 'Naranjas'
switch (fruit) {
  case "Naranjas":
    console.log("El kilogramo de naranjas cuesta $0.59.");
    break; // Al utilizar el break salimos de la estructura y no se sigue evaluando las siguientes expresiones
  case "Manzanas":
    console.log("El kilogramo de manzanas cuesta $0.32.");
    break;
  case "Platanos":
    console.log("El kilogramo de platanos cuesta $0.48.");
    break;
  case "Cerezas":
    console.log("El kilogramo de cerezas cuesta $3.00.");
    break;
  case "Mangos":
  case "Papayas":
    console.log("El kilogramo de mangos y papayas cuesta $2.79.");
    break;
  default:
    console.log("Lo lamentamos, por el momento no disponemos de " + fruit + ".");
}
/*
// #Ejercicio extra:  * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. */

for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i)
  }
}