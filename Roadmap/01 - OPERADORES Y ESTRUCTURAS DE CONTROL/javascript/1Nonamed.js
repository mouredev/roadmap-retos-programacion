// OPERADORES

console.log(`------------------ Asignación ------------------`);
let num = 10;
console.log(`num: ${num}\n`);

// Asignación suma
console.log(`num: ${num} || num += 2 => ${(num += 2)}`);
// Asignación resta
console.log(`num: ${num} || num -= 1 => ${(num -= 1)}`);
// Asignación multiplicación
console.log(`num: ${num} || num *= 2 => ${(num *= 2)}`);
// Asignación exponencial
console.log(`num: ${num} || num **= 2 => ${(num **= 2)}`);
// Asignación división
console.log(`num: ${num} || num /= 2 => ${(num /= 2)}`);
// Asignación residuo
console.log(`num: ${num} || num %= 2 => ${(num %= 2)}\n`);

console.log(`------------------ Comparación ------------------`);
let num1 = 20;
let num2 = 27;
console.log(`num1: ${num1}    num2: ${num2}\n`);

// Igual
console.log(`num1 == num2? => ${num1 == num2}`);
console.log(
  `'27' == num2? => ${"27" == num2} | Convierte tipos, comparación débil`
);
// No igual
console.log(`num1 != num2? => ${num1 != num2}`);
console.log(
  `'27' != num2? => ${"27" != num2} | Convierte tipos, comparación débil`
);
// Estricta
console.log(`num1 === num2? => ${num1 === num2}`);
console.log(
  `'27' === num2? => ${"27" === num2} | No convierte tipos, comparación fuerte`
);
// No igual estricto
console.log(`num1 !== num2? => ${num1 !== num2}`);
console.log(
  `'27' !== num2? => ${"27" !== num2} | No convierte tipos, comparación fuerte`
);
// Mayor que
console.log(`num1 > num2? => ${num1 > num2}`);
// Mayor o igual que
console.log(`num1 >= num2? => ${num1 >= num2}`);
// Menor que
console.log(`num1 < num2? => ${num1 < num2}`);
// Menor o igual que
console.log(`num1 <= num2? => ${num1 <= num2}`);

console.log(`------------------ Aritméticos ------------------`);
// Adicional a las operaciones +, -, *, **, / y %, JavaScript también tiene las siguientes operaciones:
let x = 2;
let y;
console.log(`x: ${x}    y: ${y}\n`);

// Incrementar
console.log(`++x => x = ${x}; y = ${++x}`);
// Decrementar
console.log(`--x => x = ${x}; y = ${--x}`);
// Unary negation => Regresa la negación del operando
console.log(`x => -x || x = ${x} => -x = ${-x}`);
// Unary plus => Intenta convertir el operando en número
console.log(`+x => x || x = ${-x} => +x = ${+x}`);
console.log(`+'x' => x || x = '27' => +x = ${+"27"}\n`);

console.log(`------------------ Lógicos ------------------`);
const a = 10;
const b = 15;
console.log(`a: ${a}    b: ${b}\n`);

// Y (and -- &&)
console.log(`a < b && b >= 15 => ${a < b && b >= 15}`);
// O (Or -- ||)
console.log(`a < b || b > 15 => ${a < b || b > 15}`);
// No (Not -- !)
console.log(`!(a < b && b >= 15) => ${!(a < b && b >= 15)}`);
console.log(`!!(a < b && b >= 15) => ${!!(a < b && b >= 15)}`); // Negación doble
// Nullish coalescing operator (??) => Devuelve el valor de la derecha sí el de la izquierda es null o undefined
console.log(`null ?? a => ${null && a}`);
console.log(`10 ?? a => ${10 && a}`);
console.log(`10 ?? undefined => ${10 && undefined}`);

console.log(`------------------ Strings ------------------`);
let msj = "Hello,";
msj += " World!";

console.log(msj);

console.log(`\n------------------ Ternary ------------------`);
let age = 28;
console.log(`age: ${age}\n`);

console.log(`${age > 20 ? "Allowed to enter" : "Not allowed to enter"}`);

// ESTRUCTURAS DE CONTROL

console.log(`\n------------------ Condicionales: If Else ------------------`);
let grade = 3;
let color = "red";
console.log(`grade: ${grade}   color: ${color}\n`);

if (grade >= 3) console.log("Aprobaste");

if (color === "yellow") {
  console.log("El color es el mismo");
} else {
  console.log("El color no es el mismo");
}

console.log(`\n------------------ Condicionales: Switch ------------------`);
let grade2 = 2;
console.log(`grade: ${grade2}\n`);

switch (grade2) {
  case 5:
    finalGrade = "Excelente";
    break;
  case 4:
    finalGrade = "Sobresaliente";
    break;
  case 3:
    finalGrade = "Suficiente";
    break;
  case 2:
  case 1:
  case 0:
    finalGrade = "Insuficiente";
    break;

  default:
    finalGrade = "Nota erronea";
    break;
}
console.log(`Mi nota final es ${finalGrade}\n`);

console.log(`------------------ Bucles: While ------------------`);
let i = 0;

while (i <= 3) {
  console.log(`While => i: ${i}`);
  i = i + 1;
}

console.log("\ndo While from here:");
// do while se ejecuta al menos UNA vez
do {
  console.log(`do While => i: ${i}`);
  i = i + 1;
} while (i < 8);

console.log(`------------------ Bucles: For ------------------`);
for (let j = 0; j < 3; j++) {
  console.log(`Log #${j} from loop for (Incremental)\n`);
}

for (let k = 5; k > 2; k--) {
  console.log(`Log #${k} from loop for (Decremental)`);
}

console.log(`\n------------------ Extra ------------------`);
// Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

const arr = [];
const arrMultiplesOf3 = [];

for (let i = 10; i <= 55; i++) {
  if (i % 3 === 0) {
    arrMultiplesOf3.push(i);
  }
}
console.log("Multiples of 3:");
console.log(arrMultiplesOf3);

for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    arr.push(i);
  }
}


console.log('\nFinal Array:')
console.log(arr);
