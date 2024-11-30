let a = 5;
let b = 4;
let resultadoA;
// Operadores aritméticos
resultado = a + b;
console.log(resultado);

resultado = a - b;
console.log(resultado);

resultado = a * b;
console.log(resultado);

resultado = a / b;
console.log(resultado);

resultado = a % b; // Módulo
console.log(resultado);

resultado = a ** b; // Exponente
console.log(resultado);

b++; // Incremento
console.log(b);

b--; // Decremento
console.log(b);

// Operadores lógicos
let t = true,
  f = false;
let resultadoL;
resultadoL = t && f; // false
console.log(resultadoL);

resultadoL = t || f; // true
console.log(resultadoL);

resultadoL = !t; // false
console.log(resultadoL);

// Operadores de comparación
let n1,
  n2 = 0;
n1 = n2; // 0
console.log(n1);

n1 += n2; // 0
console.log(n1);

n1 -= n2; // 0
console.log(n1);

n1 /= n2; // 0
console.log(n1);

n1 %= n2; // 0
console.log(n1);

n1 **= n2; // 1
console.log(n1);

// Operadores de identidad
let x = 5,
  y = 6;
let resultadoI;
resultadoI = a === b; // identidad estricta
console.log(resultadoI);

resultadoI = a !== b; // no identidad estricta
console.log(resultadoI);

// Operadores de pertenencia
let z = 4,
  w = [1, 2, 6, 3, 5, 4, 10];
let resultadoP;
resultadoP = z in w; // Verifica si una propiedad existe en un objeto
console.log(resultadoP);

function persona(nombre, edad) {
  this.nombre = nombre;
  this.edad = edad;
}
let niño = new persona("Juan", 10);
console.log(niño instanceof persona); // Verifica si un objeto es instancia de otro

// Operadores de bit a bit
let b1 = 5,
  b2 = 3; // 5 (00000101) ; 3 (00000011)
let resultadoB;
resultadoB = b1 & b2; // 1 (00000001)
console.log(resultadoB);

resultadoB = b1 | b2; // 7 (00000111)
console.log(resultadoB);

resultadoB = b1 ^ b2; // 6 (00000110)
console.log(resultadoB);

resultadoB = ~b1; // -6 (11111010)
console.log(resultadoB);

resultadoB = b1 << 2; // 20 (00010100)
console.log(resultadoB);

resultadoB = 20 >> 2; // 5 (00000101)
console.log(resultadoB);

resultadoB = -20 >>> 2; // 1073741823 (01111111 11111111 11111111 11111011)
console.log(resultadoB);

// Condicionales
let edad = 19;
if (edad >= 18) {
  console.log("Usted es mayor de edad");
} else {
  console.log("Usted no es mayor de edad");
}

let dia = "viernes";
switch (dia) {
  case "lunes":
    console.log("Hoy es lunes");
  case "martes":
    console.log("Hoy es martes");
  default:
    console.log("Hoy no es lunes ni martes");
}

// Iterativas
let i = 0;
while (i <= 3) {
  console.log(i);
  i++;
}

i = 1;
do {
  console.log(i);
  i += 2;
} while (i <= 7);

for (let i = 2; i <= 8; i += 2) {
  console.log(i);
}

let objeto = { a: 12, b: 14, c: 16 };
for (let propiedad in objeto) {
  // for-in
  console.log(objeto[propiedad]);
}

let arreglo = [11, 12, 13, 14, 15];
for (let elemento of arreglo) {
  // for-of
  console.log(elemento);
}

try {
  // Código que puede generar un error
  let nro = null;
  nro.length();
} catch (error) {
  // Código que se ejecuta si se produce un error
  console.log("Error");
} finally {
  // Código que se ejecuta siempre
  console.log("Ejecución finalizada");
}

// Ejercicio Extra
for (let i = 10; i <= 55; i += 2) {
  if (i % 16 !== 0 && i % 3 !== 0) {
    console.log(i);
  }
}
