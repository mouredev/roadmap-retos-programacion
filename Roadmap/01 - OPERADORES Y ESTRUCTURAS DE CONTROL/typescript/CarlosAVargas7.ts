/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes) */

// a) Operadores Aritmeticos
let a:number = 10;
let b:number = 5;

// Suma
console.log(a + b);

// Resta
console.log(a - b);

// Multiplicación
console.log(a * b);

// División
console.log(a / b);

// Modulo
console.log(a % b);

// Potencia
console.log(a ** b);

// Incremento
console.log(a++);

// Decremento
console.log(b--);

// b) Operadores de Comparación
let c:number = 10;
let d:number = 5;

// Igualdad
console.log(a == b);

// Desigualdad
console.log(a != b);

// Igualdad estricta
console.log(a === b);

// Desigualdad estricta
console.log(a !== b);

// Mayor que
console.log(a > b);

// Menor que
console.log(a < b);

// Mayor o igual que
console.log(a >= b);

// Menor o igual que
console.log(a <= b);

// c) Operadores Lógicos
let e:boolean = true;
let f:boolean = false;

// AND
console.log(e && f);

// OR
console.log(e || f);

// NOT
console.log(!e);

// d) Operadores de Asignación
let g:number = 10;
let h:number = 5;

// Asignación
console.log(g = h); // 5

// Suma y asignación
console.log(g += h); // 15

// Resta y asignación
console.log(g -= h); // 5

// Multiplicación y asignación
console.log(g *= h); // 50

// División y asignación
console.log(g /= h); // 2

// Modulo y asignación
console.log(g %= h); // 0

// Potencia y asignación
console.log(g **= h); // 100000

// Incremento y asignación
console.log(g++); // 11

// Decremento y asignación
console.log(g--); // 9

// e Operadores Bit a Bit
let i:number = 5;
let j:number = 3;

// AND
console.log(i & j); // 1

// OR
console.log(i | j); // 7

// XOR
console.log(i ^ j); // 6

// NOT
console.log(~i); // -6

// Desplazamiento a la izquierda
console.log(i << j); // 20

// Desplazamiento a la derecha
console.log(i >> j); // 1

// Desplazamiento a la derecha sin signo
console.log(i >>> j); // 1

// f) Operadores de Tipo (especificos de Typescript)
let k:any = "10";
let l:any = 10;

// as
console.log((k as string).length); // 2

// is
console.log(k is string); // true

// !
console.log(!k); // false

// typeof
console.log(typeof k); // string

// instanceof
console.log(k instanceof String); // false

// g) Operadores Ternarios
let m:number = 10;
let n:number = 5;

console.log(m > n ? "m es mayor que n" : "m no es mayor que n");

// h) Operadores Opcionales (Optional Chaining y Nulish Coalescing)
let o:any = {name: "Carlos"};
console.log(o?.name); // Carlos 
console.log(o?.age); // undefined
console.log(o?.age ?? 0); // 0

/* - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 */

// i) Estructuras de Control

// 1. Condicionales
let age:number = 18;

if (age >= 18) {
    console.log("Eres mayor de edad");
} else if (age >= 13) {
    console.log("Eres adolescente");
} else {
    console.log("Eres menor de edad");
}
switch (age) {
    case 18:
        console.log("Eres mayor de edad");
        break;
    case 13:
        console.log("Eres adolescente");
        break;
    default:
        console.log("Eres menor de edad");
        break;
}

// 2. Estructuras de Bucles
for (let i:number = 0; i < 10; i++) {
    console.log(i);
}

// for of
let array:number[] = [1, 2, 3, 4, 5];
for (let i of array) {
    console.log(i);
}

// for in
let object:any = {name: "Carlos", age: 18};
for (let i in object) {
    console.log(i);
}

while (age < 18) {
    console.log("Eres menor de edad");
    age++;
}

// do while
let i:number = 0;
do {
    console.log(i);
    i++;
} while (i < 10);

// 3. Control de Flujo

for (let i:number = 0; i < 10; i++) {
    if (i === 5) {
        break;
    }
    console.log(i);
}

// 4. Excepciones
try {
    let x:number = 10;
    console.log(x);
} catch (error) {
    console.log(error);
}

/* 
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */