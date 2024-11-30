//  * EJERCICIO:
//  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
//  *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
//  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
//  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
//  *   que representen todos los tipos de estructuras de control que existan
//  *   en tu lenguaje:
//  *   Condicionales, iterativas, excepciones...
//  * - Debes hacer print por consola del resultado de todos los ejemplos.


// OPERADORES ARITMETICOS:
const operadores = ['suma: +', 'resta: -', 'division: /', 'multiplicacion: *', 'modulo: %']
const suma = 2 + 2
const resta = 3 - 2
const division = 4 / 2
const multiplicacion = 2 * 4
const modulo = 4 % 3
const exponente = 4 ** 2

console.log("los operadores aritmeticos son", operadores)
console.log("suma 2 + 2 =", suma)
console.log("resta 3 - 2 = ", resta)
console.log("division 4 / 2 =", division)
console.log("multiplicacion 2 * 4 =", multiplicacion)
console.log("modulo de 4 % 3 =", modulo)
console.log("potencia de 4 =", exponente)


// OPERADORES DE COMPARACION:
const comparacion = ['igual: ==', 'distinto: !=', 'mayor: >', 'menor: <', 'mayor o igual: >=', 'menor o igual: <=']
const igualdad = (10 == 3)
const distintos = (10 != 3)
const mayor = (10 > 3)
const menor = (10 < 3)
const mayorOigual = ('>=')
const menorOigual = ('<=')

console.log(comparacion)
console.log("son iguales? ", igualdad)
console.log("son distintos? ", distintos)
console.log("es 10 mayor que 3?", mayor)
console.log("es 10 menor que 3?", menor)
console.log("mayor o igual es:", mayorOigual, "menor o igual es:", menorOigual)

// OPERADORES LOGICOS
const logicos = ['and: &&', 'or: ||', 'not: !']
const and = (10 + 3 === 14 && 3 + 10 === 13)
const or = (10 + 3 === 14 || 3 + 10 === 13)
const not = (!(10 + 3 === 14))

console.log("los operadores logicos son:", logicos)
console.log("10 + 3 es 14 Y 3 + 10 es 13?", and)
console.log("10 + 3 es 14 O 3 + 10 es 13?", or)
console.log("10 + 3 NO es 14?", not)

// OPERADORES DE ASIGNACION <- combinamos los operadores con la asignacion =
const asignacion = ["asignale: =", "sumale y asignale: +=", "restale y asignale: -=", "multiplicale y asignale: *=", "dividilo y asignale: /=", "modulo asignale: %=", "exponente y asignale: **="]
console.log("los operadores de asignacion son:", asignacion)
let numero = 21
console.log("numero asignado:", numero)
numero += 2
console.log("sumale 2:", numero)
numero -= 4
console.log("restale 4:", numero)
numero *= 3
console.log("multiplicalo x 3:", numero)
numero /= 2
console.log("dividido x 2:", numero)
numero %= 2
console.log("modulo de 2:", numero)
numero = 1

// OPERADORES DE IDENTIDAD <- compara el valor de la pos. de memoria
const identidad = ['estrictamente igual: ===', 'estrictamente desigual: !==']
console.log("operadores de identidad:", identidad)
let miNumero = "1"
console.log("\"1\" es estrictamente igual que 1?", miNumero === numero)
console.log("\"1\" no es estrictamente igual que 1?", miNumero !== numero)

// PERTENENCIA
const pertenencia = ["in: se utiliza para verificar si una propiedad existe en un objeto o en el prototipo de un objeto", "includes(): se utiliza para verificar si un array contiene un valor específico", "indexOf(): se utiliza para encontrar la posición de un valor en un array. Devuelve el índice del primer elemento encontrado o -1 si no se encuentra"]
const objeto = { name: 'Pau', age: 30 }
console.log('name' in objeto)     // <- true si hay un campo 'name' en el objeto
console.log('address' in objeto)  // <- false porque no hay un campo 'address' en el objeto
const array = [1, 2, 3, 4]
console.log("el array incluye un 2?", array.includes(2))
console.log("el array incluye un 5?:", array.includes(5))
console.log("el index o indice donde esta el 3 es:", array.indexOf(3))      // el index donde esta el 3 es -> 2
console.log("si no hay un 5 en el array, devolvera:", array.indexOf(5))     // devuelve -1 porque no hay un 5 en el array


// OPERADORES DE BITS <- raramente los usaremos
// operador bitwise AND(&) - Este operador realiza una operación AND booleana en cada bit de sus argumentos enteros.        
// en binario:
// 4: 100
// 1: 001
console.log("bitwise &:", 4 & 1) //0

// operador Bitwise OR (|) - Este operador realiza una operación OR booleana en cada bit de sus argumentos enteros.
console.log("OR 4 | 1:", 4 | 1) //5
// operador Bitwise XOR (^) - Este operador realiza una operación OR exclusiva booleana en cada bit de sus argumentos enteros.
console.log("XOR 4 ^ 1:", 4 ^ 1) //5
// operador Bitwise NOT (~) - Este operador invierte todos los bits del operando.
console.log("NOT ~ 4:", ~4); // -5
// operador de desplazamiento a la izquierda (<<)
console.log("desplazamiento a la izq 4 << 1:", 4 << 1) //8
// operador de desplazamiento a la derecha (>>)
console.log("desplazamiento a la der 4 >> 1:", 4 >> 1) //2


// OPERADOR TERNARIO: El operador ternario es la abreviatura de la instrucción if-else. Asigna valor a una variable en base a una condición, la sintaxis de la misma es:

const estructura = "condition ? value1 : value2"

//Si la condición es verdadera, el operador devuelve el valor de value1. De lo contrario, devuelve el valor de value2.

let resultado = (200 > 100) ? "Si" : "No";
console.log("es 200 mayor que 100?", resultado)

// OPOERADOR TYPEOF
// Se utiliza para encontrar el tipo de datos de un valor o variable.
console.log(typeof (38))    //number
console.log(typeof ("38"))  //string

/*
 ESTRUCTURAS DE CONTROL
*/

// CONDICIONALES
const condicion = "soy un string"
if (typeof condicion == 'string') {
  console.log("esto se imprime porque la condicion es string")
} else {
  console.log("la condicion no se cumplio")
}

// ITERACION
// Ciclos, Bucles o Loops 

// FOR ->
const total = 10

for (let i = 0; i <= total; i++) {
  console.log("iteracion: ", i, "hasta llegar a:", total)
}

// FOR IN ->
var dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

for (i in dias) {
  console.log(dias[i])
}

// WHILE -> 
let contador = 0

while (contador < 3) {
  contador++
}
console.log("Contador es igual a :", contador)

// SWITCH ->
const fruta = "Naranjas"

switch (fruta) {
  case "Naranjas":
    console.log("Las Naranjas cuestan $5")
    break
  case "Manzanas":
    console.log("Las Manzanas cuestan $10")
    break
  case "Fresas":
    console.log("Las Fresas cuestan $15")
    break
  default:
    console.log("Disculpa, no tenemos ese tipo de fruta: ", fruta)
    break
}

// MANEJO DE EXCEPCIONES:
const random = Math.floor(Math.random() * 10) + 1

if (random <= 10)
  try {
    console.log("numero random generado correctamente")
  } catch {
    console.log("se ha producido un error")
  } finally {
    console.log("finally: esto se ejecuta igual")
  }

//  * DIFICULTAD EXTRA (opcional):
//  * Crea un programa que imprima por consola todos los números comprendidos
//  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

const programa = () => {
  for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) { 
      console.log(i) 
    }
  }
}

programa()