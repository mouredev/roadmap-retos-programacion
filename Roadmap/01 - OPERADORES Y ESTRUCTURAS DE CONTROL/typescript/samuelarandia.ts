
/*
 * EJERCICIO:
 * [x] Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * [x] Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 *[x] Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * [x] Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
// ----- Operadores aritméticos

let a:number = 5;
let b:number = 3;

//Suma (+)
console.log("suma", a + b); // 8
//Resta (-)
console.log("resta", a - b); // 2
//Multiplicación (*)
console.log("multiplicación", a * b); // 15
//División (/)
console.log("división", a / b); // 1.6666666666666667
//Módulo (%)
console.log("módulo", a % b); // 2
//Incremento (++)
console.log("incremento", a++); // 5
//Decremento (--)
console.log("decremento", b--); // 3
//exponenciación (**)
console.log("exponenciación", 5 ** 3); // 125


//---- Operadores lógicos

let c:boolean = true;
let d:boolean = false;

// AND
console.log("AND", c && d); // false
// OR
console.log("OR", c || d); // true
// NOT
console.log("NOT", !c); // false


//---- Operadores de comparación

let e:number = 20;
let f:number = 10;

// Igual (==)
console.log("Igual", e == f); // false
// Distinto (!=)
console.log("Distinto", e != f); // true
// Mayor que (>)
console.log("Mayor que", e > f); // true
// Menor que (<)
console.log("Menor que", e < f); // false
// Mayor o igual que (>=)
console.log("Mayor o igual que", e >= f); // true
// Menor o igual que (<=)
console.log("Menor o igual que", e <= f); // false


//---- Operadores de asignación

let g:number = 5;
let h:number = 3;

// Asignación (=)
console.log("Asignación", g = h); // 3
// Asignación de adición (+=)
console.log("Asignación de adición", g += h); // 6
// Asignación de sustracción (-=)
console.log("Asignación de sustracción", g -= h); // 3
// Asignación de multiplicación (*=)
console.log("Asignación de multiplicación", g *= h); // 9
// Asignación de división (/=)
console.log("Asignación de división", g /= h); // 3
// Asignación de módulo (%=)
console.log("Asignación de módulo", g %= h); // 0



//---- Operadores de identidad

let i:number = 5;
let j:number = 5;

// Estrictamente igual (===)
console.log("Estrictamente igual", i === j); // true
// Estrictamente no igual (!==)
console.log("Estrictamente no igual", i !== j); // false


// ---- Estrucutras de control

let k:number = 5;
let l:number = 3;

// If
if (k > l) {
    console.log("k es mayor que l");
}

// If else
if (k < l) {
    console.log("k es menor que l");
} else {
    console.log("k no es menor que l");
}

// If else if else

if (k < l) {
    console.log("k es menor que l");
} else if (k > l) {
    console.log("k es mayor que l");
}

// Switch

let m:number = 2;
let n:string; 

switch (m) {
    case 1:
        n = "uno";
        console.log(n);
        break;
    case 2:
        n = "dos";
        console.log(n);
        break;
    case 3:
        n = "tres";
        console.log(n);
        break;
    default:
        n = "no es ni uno, ni dos, ni tres";
        break;
}


// For

for (let o = 0; o < 5; o++) {
    console.log(o);
}

// While

let p:number = 0;

while (p < 5) {
    console.log(p);
    p++;
}

// Do while

let q:number = 0;

do {
    console.log(q);
    q++;
} 
while (q < 5);


// Try catch

let r:number = 5;

try {
    console.log(r);
} catch (error) {
    console.log(error);
}


// Números entre 10 y 55 (pares, no múltiplos de 3 ni 16)

for ( let s:number = 10; s <= 55 ; s ++) { 
    if ((s % 2 == 0) && (s != 16) && (s % 3 != 0)) {
        console.log(s);
    }
}


