/*
 * EJERCICIO:

 * 1 Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
        Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
        (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * 2 Utilizando las operaciones con operadores que tú quieras, crea ejemplos
        que representen todos los tipos de estructuras de control que existan
        en tu lenguaje: Condicionales, iterativas, excepciones...
 * 3 Debes hacer print por consola del resultado de todos los ejemplos.
 
 * DIFICULTAD EXTRA (opcional):

 1.1 Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

  // 1
    // Operadores Aritmeticos
let suma = 6 + 7;
let resta = 6 - 7;
let multiplicacion = 6 * 7;
let division = 6 / 7;
let sobrante = 6 % 7;

console.log(suma);
console.log(resta);
console.log(multiplicacion);
console.log(division);
console.log(sobrante);

    // Operador de Incremento y Decremento
let numero = 6
numero++ // 7
numero-- // 6

console.log('Numero despues del incremento y el decremento', numero)

    // Operadores de Asignación 
let a = 6;

a += 7; // a = 13
console.log('a += 7:', a);

a -= 7; // a = 6
console.log('a -= 7:', a);

a *= 7; // a = 42
console.log('a *= 7:', a);

a /= 7; // a = 6
console.log('a /= 7:', a);

    // Operadores de Comparacion
let numero1 = 2
let numero2 = 4

console.log('numero1 === numero2:', numero1 === numero2); // Comprueba si ambos valores son iguales
console.log('numero1 !== numero2:', numero1 !== numero2); // Comprueba si ambos valores no son iguales
console.log('numero1 < numero2:', numero1 < numero2); // Comprueba si el valor izquierdo es menor que el derecho
console.log('numero1 > numero2:', numero1 > numero2); // Comprueba si el valor izquierdo es mayor que el derecho
console.log('numero1 <= numero2:', numero1 <= numero2); // Comprueba si el valor izquierdo es menor o igual que el derecho
console.log('numero1 >= numero2:', numero1 >= numero2); // Comprueba si el valor izquierdo es mayor o igual que el derecho

    // Operadores Logicos
let logica1 = 2
let logica2 = 3

const resultado1 = (logica1 === logica2)
const resultado2 = (logica1 !== logica2)
const resultado3 = (logica1 > logica2)
const resultado4 = (logica1 < logica2)

// && => Ambos valores deben ser verdaderos

console.log('resultado2 && resultado4:', resultado2 && resultado4); // true
console.log('resultado1 && resultado4:', resultado1 && resultado4); // false
console.log('resultado3 && resultado4:', resultado3 && resultado4); // false
console.log('resultado1 && resultado3:', resultado1 && resultado3); // false

// || => Uno de los 2 valores debe ser verdadero

console.log('resultado2 || resultado4:', resultado2 || resultado4); // true
console.log('resultado1 || resultado4:', resultado1 || resultado4); // true
console.log('resultado3 || resultado4:', resultado3 || resultado4); // true
console.log('resultado1 || resultado3:', resultado1 || resultado3); // false

    // Operadores de Cadena 

let nombre = "Joaquin"
let apellido = "Lopez"
let nombreCompleto = "Joaquin" + " " + "Lopez"

console.log('Nombre Completo:', nombreCompleto);

// 2

    // if, else
let valor = 5
 if ( valor === 5) {
  console.log(valor)
 } else {
  console.log("el valor no es compatible")
 }

  // while
let valor2 = 1
  while( valor2 < 10) {
    console.log(valor2)
    valor2++
 }

console.log(valor2)



// 1.1 Dificultad Extra

function printNumbers() {
    for ( let i = 10; i <= 55; i++) {
      if ( i % 2 === 0 && i !== 16 && i % 3 !== 0) {
            console.log(i)
        }
    }
}

printNumbers()
