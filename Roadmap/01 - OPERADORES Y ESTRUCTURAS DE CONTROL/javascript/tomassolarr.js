let a = 10;
let b = 3;

console.log("Suma:", a + b);
console.log("Resta:", a - b);
console.log("Multiplicación:", a * b);
console.log("División:", a / b);
console.log("Módulo:", a % b);
console.log("Potencia:", a ** b);

// Comparación
console.log("Mayor que:", a > b);
console.log("Menor que:", a < b);
console.log("Igual:", a == "10");   // true (coerción)
console.log("Estrictamente igual:", a === "10"); // false
console.log("Distinto:", a != b);
console.log("Estrictamente distinto:", a !== "10");

// Lógicos
let x = true;
let y = false;

console.log("AND:", x && y);
console.log("OR:", x || y);
console.log("NOT:", !x);

// Asignación
let c = 5;
c += 2; // 7
c -= 1; // 6
c *= 2; // 12
c /= 3; // 4
console.log("Asignación compuesta:", c);

// Identidad (referencias)
let obj1 = { nombre: "Tomás" };
let obj2 = obj1;
let obj3 = { nombre: "Tomás" };

console.log("Misma referencia:", obj1 === obj2); // true
console.log("Distinta referencia:", obj1 === obj3); // false

// Pertenencia
let array = [1, 2, 3];
console.log("Incluye 2:", array.includes(2));

// Bits
let num1 = 5; // 101
let num2 = 1; // 001

console.log("AND bit a bit:", num1 & num2);
console.log("OR bit a bit:", num1 | num2);
console.log("XOR:", num1 ^ num2);
console.log("Desplazamiento izquierda:", num1 << 1);
console.log("Desplazamiento derecha:", num1 >> 1);

// Condicional
let edad = 18;

if (edad >= 18) {
  console.log("Mayor de edad");
} else {
  console.log("Menor de edad");
}

// Switch
let dia = 2;

switch (dia) {
  case 1:
    console.log("Lunes");
    break;
  case 2:
    console.log("Martes");
    break;
  default:
    console.log("Otro día");
}

// Bucle for
for (let i = 0; i < 3; i++) {
  console.log("For:", i);
}

// While
let i = 0;
while (i < 3) {
  console.log("While:", i);
  i++;
}

// Do while
let j = 0;
do {
  console.log("Do While:", j);
  j++;
} while (j < 3);

// Manejo de excepciones
try {
  let resultado = 10 / 0;
  if (!isFinite(resultado)) {
    throw new Error("División inválida");
  }
} catch (error) {
  console.log("Error capturado:", error.message);
} finally {
  console.log("Bloque finally ejecutado");
}

 /* Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */
for(let i=10; i<=55;i++){
    if(i%2===0 && i!==16 && i%3!==0)
    console.log(i)
}