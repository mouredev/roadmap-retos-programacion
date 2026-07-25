/*
OPERACIONES Y ESTRUCTURAS DE CONTROL
  EJERCICIO:
  - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
    (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
  - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...
  - Debes hacer print por consola del resultado de todos los ejemplos.
 
  DIFICULTAD EXTRA (opcional):
  Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 
* Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

// Operadores aritmeticos
let suma = 5 + 3;        // 8
let resta = 10 - 2;      // 8
let multiplicacion = 4 * 2; // 8
let division = 16 / 2;   // 8
let modulo = 17 % 9;     // 8 (resto de la división)
let exponente = 2 ** 3;  // 8 (2 elevado a 3)
let incremento = 7; incremento++; // 8
let decremento = 9; decremento--; // 8

//Operadores de comparacion
5 == "5"   // true (igualdad no estricta, compara valor)
5 === "5"  // false (igualdad estricta, compara valor y tipo)
5 != "5"   // false (desigualdad no estricta)
5 !== "5"  // true (desigualdad estricta)
7 > 5      // true (mayor que)
5 < 7      // true (menor que)
8 >= 8     // true (mayor o igual que)
8 <= 8     // true (menor o igual que)

//Operadores logicos
true && false  // false (AND lógico)
true || false  // true (OR lógico)
!true          // false (NOT lógico)

//Operadores de asignacion
let x = 5;     // Asignación básica
x += 3;        // x = x + 3 (x ahora es 8)
x -= 2;        // x = x - 2 (x ahora es 6)
x *= 2;        // x = x * 2 (x ahora es 12)
x /= 3;        // x = x / 3 (x ahora es 4)
x %= 3;        // x = x % 3 (x ahora es 1)

//ESTRUCTURAS DE CONTROL
//Condicionales
// if, else if, else
let edad = 18;

if (edad < 13) {
  console.log("Niño");
} else if (edad = 13 && edad< 18) {
  console.log("Adolescente");
} else {
  console.log("Adulto");  // Este se ejecutará
}

// Operador ternario (condición ? valor_si_verdadero : valor_si_falso)
let mensaje = edad >= 18 ? "Mayor de edad" : "Menor de edad";

// switch
let dia = 3;
switch (dia) {
  case 1:
    console.log("Lunes");
    break;
  case 2:
    console.log("Martes");
    break;
  case 3:
    console.log("Miércoles"); // Este se ejecutará
    break;
  default:
    console.log("Otro día");
}


//Irativas o bucles

// for
for (let i = 0; i < 5; i++) {
  console.log(i); // Imprime 0, 1, 2, 3, 4
}

// while
let contador = 0;
while (contador < 3) {
  console.log(contador); // Imprime 0, 1, 2
  contador++;
}

// do-while (se ejecuta al menos una vez)
let j = 0;
do {
  console.log(j); // Imprime 0
  j++;
} while (j < 1);

// for...of (para iterar elementos de arrays, strings, etc.)
let frutas = ["manzana", "banana", "cereza"];
for (let fruta of frutas) {
  console.log(fruta); // Imprime manzana, banana, cereza
}

// for...in (para iterar propiedades de objetos)
let usuario = { nombre: "Carlos", edad: 30 };
for (let propiedad in usuario) {
  console.log(propiedad + ": " + usuario[propiedad]);
  // Imprime "nombre: Carlos", "edad: 30"
}

/*
 DIFICULTAD EXTRA (opcional):
  Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

let array = [];
for (let i = 10; i < 56; i++) {
    if ( i % 2 == 0 && i != 16 && i % 3 != 0) {
        console.log(i)    
    }
}
// 
//
