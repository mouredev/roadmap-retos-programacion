// https://www.typescriptlang.org/

// Operadores aritméticos
let a: number = 10;
let b: number = 3;
console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);
console.log(a % b);
console.log(a ** b);

// Operadores de asignación
let c: number = 5;
c += 3;
c -= 1;
c *= 2;
c /= 2;
console.log(c);

// Operadores de comparación
console.log(a == b);
console.log(a === b);
console.log(a != b);
console.log(a !== b);
console.log(a > b);
console.log(a < b);
console.log(a >= b);
console.log(a <= b);

// Operadores lógicos
console.log(true && false);
console.log(true || false);
console.log(!true);

// Operadores bitwise
console.log(a & b);
console.log(a | b);
console.log(a ^ b);
console.log(~a);
console.log(a << 1);
console.log(a >> 1);

// Condicional if / else if / else
if (a > b) {
  console.log("a es mayor");
} else if (a < b) {
  console.log("b es mayor");
} else {
  console.log("son iguales");
}

// switch
switch (a) {
  case 10:
    console.log("es diez");
    break;
  default:
    console.log("otro valor");
}

// Ternario
const result: string = a > b ? "mayor" : "menor";
console.log(result);

// for
for (let i: number = 0; i < 3; i++) {
  console.log(i);
}

// while
let j: number = 0;
while (j < 3) {
  console.log(j);
  j++;
}

// do while
let k: number = 0;
do {
  console.log(k);
  k++;
} while (k < 3);

// for...of
const items: number[] = [1, 2, 3];
for (const item of items) {
  console.log(item);
}

// Excepciones
try {
  throw new Error("error forzado");
} catch (e) {
  console.log(e);
} finally {
  console.log("bloque finally");
}

// Dificultad extra: pares entre 10 y 55, sin 16, sin múltiplos de 3
for (let n: number = 10; n <= 55; n++) {
  if (n % 2 === 0 && n !== 16 && n % 3 !== 0) {
    console.log(n);
  }
}
