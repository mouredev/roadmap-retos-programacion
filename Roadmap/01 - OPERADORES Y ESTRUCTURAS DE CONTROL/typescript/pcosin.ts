// OPERADORES ARITMÉTICOS

let num1: number = 10;
let num2: number = 50;
let resultado: number;

// Adición:

resultado = num1 + num2;

console.log(resultado);

// Sustracción:

resultado = num1 - num2;

console.log(resultado);

// Multiplicación:

resultado = num1 * num2;

console.log(resultado);

// División:

resultado = num1 / num2;

console.log(resultado);

// Módulo:

resultado = num1 % num2;

console.log(resultado);

// OPERADORES DE ASIGNACIÓN

// Aignación:

const str: string = "Se le asigna una cadena de caractéres";

// Asignación compuesta:

resultado += num1;
console.log(resultado);

resultado -= num1;
console.log(resultado);

resultado *= num1;
console.log(resultado);

resultado /= num1;
console.log(resultado);

// OPERADORES DE COMPARACIÓN

// igualdad

console.log(num1 == num1);

// igualdad estricta

console.log(num1 === 10);

// desigualdad

console.log(num1 != num2);

// desigualdad estricta

console.log(num1 !== num2);

// mayor, menor, mayor o igual, menor o igual

console.log(num1 < num2);
console.log(num1 <= num2);

//OPERADORES LÓGICOS

const varTrue: boolean = true;
const varFalse: boolean = false;

let resultBool: boolean;

// and

resultBool = varTrue && varFalse;
console.log(resultBool);

// or

resultBool = varTrue || varFalse;
console.log(resultBool);

// not

resultBool = !varFalse;
console.log(resultBool);

// OPERADORES DE INCREMENTO/DECREMENTO

console.log(num1++);
console.log(num1--);

// OPERADORE AND A NIVEL DE BITS

let varbits: number = 5 & 3;
console.log(varbits);

// Operador OR a nivel de Bits

varbits = 5 | 3;

console.log(varbits);

// Operador XOR a nivel de Bits

varbits = 5 ^ 3;

console.log(varbits);

//  Desplazamiento a la izquierda

varbits = 5 << 1;

console.log(varbits);

// Desplazamiento a la derecha

varbits = 5 >> 1;

console.log(varbits);

//  Desplazamiento a la derecha sin signo

varbits = -5 >>> 1;

console.log(varbits);

// OPERADORES DE TIPOS

console.log(typeof varbits);

// CONDICIONAL

const user: string = "1234";

if (!user) {
  console.log("No existe el usuario");
} else {
  console.log("Usuario encontrado");
}

// ternario:

console.log(user ? "Usuario encontrado" : "No existe el usuario");

// BUCLES

//for loop

for (let i: number = 0; i < 10; i++) {
  console.log(i);
}

// while

let islarger: boolean = true;
let num3: number = 0;
while (islarger) {
  if (num3 >= 5) {
    islarger = false;
  }
  console.log(num3);
  num3++;
}

// do while

let i: number = 0;

do {
  console.log(i);
  i++;
} while (i < 10);

// Switch

const day: string = "Martes";

switch (day) {
  case "Lunes": {
    console.log("Hoy es lunes");
    break;
  }
  case "Martes": {
    console.log("Hoy es martes");
    break;
  }
  case "Miercoles": {
    console.log("Hoy es miercoles");
    break;
  }
  case "Jueves": {
    console.log("Hoy es jueves");
    break;
  }
  case "Viernes": {
    console.log("Hoy es viernes");
    break;
  }
}

// EXCEPTIONS

// try-catch

let password: string = "1235";

try {
  if (password === "1234") {
    console.log("contraseña correcta");
  } else {
    throw new Error("Contraseña incorrecta");
  }
} catch (error: any) {
    console.error(error.message);
    
}

// EXTRA

for (let i: number = 10; i <= 55; i++) {
  if (i === 16 || i % 3 === 0) continue;
  else if (i % 2 === 0) console.log(i);
}
