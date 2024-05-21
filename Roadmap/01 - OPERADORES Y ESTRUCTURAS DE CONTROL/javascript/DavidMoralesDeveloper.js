/*
 * EJERCICIO:
 * 1- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
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


//1 Operadores 
const a = 1
 const b = 2
 const c = 3
//Aritméticos 
// suma+, resta-, multiplicasion*, division/, modulo(resto)%
// exponenciación **, incremento ++, decremento  --

 const suma = a + b
 const resta = a - b
 const multiplicasion = a * b
 const division = a / b
 const modulo = a % b
 const exponecia = a ** b 

//  lógicos
// || or si una es true , &&  si las dos son true !true diferente de 

console.log(a || b)
console.log(a && b)
console.log(!true);

//asignación
// = asignacion de un valor, +=sumar , -= para restar el operando derecho  *= , /=, %=
let x = 10;
x += 5; // x = 15
x -= 2; // x = 13
x *= 3; // x = 39
x /= 2; // x = 19.5
x %= 4; // x = 3.5


//De comparación:
console.log(2 === 2); // Igualdad estricta: true
console.log(2 == 2); // Igualdad no estricta: true
console.log(2 > 1); // Mayor que: true
console.log(2 >= 2); // Mayor o igual que: true
console.log(1 < 2); // Menor que: true
console.log(1 <= 2); // Menor o igual que: true

//Identidad:
const d = 10;
const e = 10;
console.log(d === e); // true (mismo valor y tipo)
const f = "10";
console.log(d === f); // false (mismo valor, diferente tipo) 


//Pertenencia:
const lista = ["a", "b", "c"];
console.log("a" in lista); // true
console.log("d" in lista); // false

//Bits
console.log(1 | 2); // OR a nivel de bits: 3
console.log(1 & 2); // AND a nivel de bits: 0
console.log(1 ^ 2); // XOR a nivel de bits: 3
console.log(~1); // NOT a nivel de bits: -2


//Estructuras de Control
//OPERADOR TERNARIO
//expresión ? "si es true" : "si es false";
let edad = 16;
let acceso = edad > 17 ? "Permitir acceso" : "Denegar acceso";
console.log(acceso);

//Condicional
const g = 19
if(g > 18 ) {
    console.log('Es mayor de edad') 
}else{console.log('es menor de edad') }

//Iterativas:
// Bucle for
for (let i = 0; i = 100; i++){
  console.log(i + 'bucle for')
}
  // Bucle while

  let i = 0;
let j = 0;
while (n < 3) {
  i++;
  j += i;
}

    // Bucle do-while
      // let j = 0; do{i+1; console.log(i)}; wile{i <5}
    let z = 3;

// do...while loop
do {
    console.log(z);
    z--;
} while (z > 0);

    //for of for in
    const arr = [3, 5, 7];
arr.foo = "hola";

for (let i in arr) {
  console.log(i); // logs "0", "1", "2", "foo"
}

for (let i of arr) {
  console.log(i); // logs 3, 5, 7
}


// * DIFICULTAD EXTRA (opcional):
// * Crea un programa que imprima por consola todos los números comprendidos
// * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for (let i = 10; i < 55; i++){
  if(i%2 === 0 && i !=16 && i % 3 != 0)
  console.log(i)
}

// 10, 14, 20, 22, 26, 28, 32, 34, 38, 40, 44, 46, 50, 52
//i%2 === 0 = 10 12 14 16 18 20
//i !=16 = 12 14 18 20
//modulo de tres es distinto a 0 4 / 3 = 0.12  (!=)
