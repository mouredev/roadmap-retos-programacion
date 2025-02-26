/*

OPERADORES EN JAVASCRIPT


*/

// OPERADORES ARITMETICOS
let a = 5;
let b = 2;

console.log(a + b); // 7
console.log(a - b); // 3
console.log(a * b); // 10
console.log(a / b); // 2.5
console.log(a % b); // 1

// OPERADORES DE ASIGNACION
let c = 10;
let d = 5;

c += d; // c = c + d
console.log(c); // 15

c -= d; // c = c - d

c *= d; // c = c * d

c /= d; // c = c / d

c %= d; // c = c % d

// OPERADORES DE COMPARACION

let e = 5;

console.log(e == 5); // true
console.log(e == "5"); // true
console.log(e === "5"); // false
console.log(e != "5"); // false
console.log(e !== "5"); // true
console.log(e > 5); // false
console.log(e >= 5); // true
console.log(e < 5); // false

// OPERADORES LOGICOS

let f = 5;
let g = 10;

console.log(f == 5 && g == 10); // true
console.log(f == 5 && g == 5); // false
console.log(f == 5 || g == 5); // true
console.log(f == 5 || g == 10); // true
console.log(f == 10 || g == 5); // false
console.log(f == 10 || g == 10); // false
console.log(!true); // false
console.log(!false); // true

// OPERADORES DE CONCATENACION

let h = "Hola";
let i = "Mundo";

console.log(h + " " + i); // Hola Mundo

// OPERADORES DE INCREMENTO Y DECREMENTO

let j = 5;

console.log(j++); // 5

console.log(j); // 6

console.log(++j); // 7

console.log(j); // 7

console.log(j--); // 7

console.log(j); // 6

console.log(--j); // 5


// ESTRUCTURAS DE CONTROL

// IF 

let k = 5;

if (k == 5) {

  console.log("k es igual a 5");

}

// IF ELSE

let l = 10;

if (l == 5) {

  console.log("l es igual a 5");

}

else {

  console.log("l no es igual a 5");

}

// IF ELSE IF

let m = 10;

if (m == 5) {

  console.log("m es igual a 5");

}


else if (m == 10) {

  console.log("m es igual a 10");

}

else {

  console.log("m no es igual a 5 ni a 10");

}

// SWITCH


let n = 5;

switch (n) {

  case 5:

    console.log("n es igual a 5");
    break;

  case 10:

    console.log("n es igual a 10");
    break;

  default:

    console.log("n no es igual a 5 ni a 10");
    break;

}

// FOR

for (let o = 0; o < 5; o++) {

  console.log(o);

}

// WHILE

let p = 0;

while (p < 5) {

  console.log(p);
  p++;

}

// DO WHILE

let q = 0;

do {

  console.log(q);
  q++;

} while (q < 5);

// BREAK


for (let r = 0; r < 5; r++) {

  if (r == 3) {

    break;

  }

  console.log(r);

}

// CONTINUE

for (let s = 0; s < 5; s++) {

  if (s == 3) {

    continue;

  }

  console.log(s);

}

// FUNCIONES

function suma(t, u) {

  return t + u;

}

console.log(suma(5, 10)); // 15 

// FUNCIONES ANONIMAS

let suma2 = function (t, u) {

  return t + u;

}

console.log(suma2(5, 10)); // 15

// FUNCIONES FLECHA

let suma3 = (t, u) => t + u;

console.log(suma3(5, 10)); // 15


// FUNCIONES CON PARAMETROS POR DEFECTO

function suma4(t = 0, u = 0) {

  return t + u;

}

console.log(suma4(5)); // 5  

// FUNCIONES CON PARAMETROS REST

function suma5(t, u, ...v) {

  let w = t + u;

  v.forEach(x => w += x);

  return w;

}

console.log(suma5(5, 10, 15, 20)); // 50

// FUNCIONES CON PARAMETROS SPREAD

function suma6(t, u, v, w) {

  return t + u + v + w;

}

let x = [5, 10, 15, 20];


console.log(suma6(...x)); // 50


// FUNCIONES CON OBJETOS COMO PARAMETROS

function suma7(t) {

  return t.a + t.b;

}

let y = { a: 5, b: 10 };

console.log(suma7(y)); // 15

// FUNCIONES CON OBJETOS COMO PARAMETROS Y DESTRUCTURACION


function suma8({ a, b }) {

  return a + b;

}

let z = { a: 5, b: 10 };

console.log(suma8(z)); // 15

// FUNCIONES CON OBJETOS COMO PARAMETROS Y DESTRUCTURACION Y PARAMETROS REST

function suma9({ a, b, ...c }) {

  let d = a + b;

  Object.values(c).forEach(e => d += e);

  return d;

}

let obj1 = { a: 5, b: 10, c: 15, d: 20 };

console.log(suma9(obj1)); // 50


console.log("Numeros pares del 10 al 55");


/* 
 DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

*/
for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i);
  }
}



