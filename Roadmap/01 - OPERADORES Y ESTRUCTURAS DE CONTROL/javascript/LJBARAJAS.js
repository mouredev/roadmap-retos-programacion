// OPERADORES

// Aritméticos
let a = 10;
let b = 3;

console.log("Aritméticos:");
console.log(a + b); // suma
console.log(a - b); // resta
console.log(a * b); // multiplicación
console.log(a / b); // división
console.log(a % b); // módulo
console.log(a ** b); // potencia
console.log(a++); // post-incremento
console.log(++b); // pre-incremento
console.log(a--); // post-decremento
console.log(--b); // pre-decremento

// De comparación
console.log("Comparación:");
console.log(a > b);   // mayor que
console.log(a < b);   // menor que
console.log(a == b);  // igual
console.log(a != b);  // distinto
console.log(a === b); // estrictamente igual
console.log(a !== b); // estrictamente distinto


// Lógicos
let x = true;
let y = false;

console.log("Lógicos:");
console.log(x && y); // AND
console.log(x || y); // OR
console.log(!x);     // NOT

// De asignación
let num = 5;
console.log("Asignación:");
num += 3;  // num = num + 3
console.log(num);
num -= 2;  // num = num - 2
console.log(num);
num *= 4;  // num = num * 4
console.log(num);
num /= 2;  // num = num / 2
console.log(num);
num %= 3;  // num = num % 3
console.log(num);


// De identidad (comparación de referencia y tipo)
let obj1 = { nombre: "Luis" };
let obj2 = { nombre: "Luis" };
let obj3 = obj1;

console.log("Identidad:");
console.log(obj1 == obj2);  // false (no es el mismo objeto)
console.log(obj1 === obj3); // true (misma referencia)

// De pertenencia
console.log("Pertenencia:");
let frutas = ["manzana", "pera", "plátano"];
console.log("pera" in frutas);         // false (para arrays no sirve así)
console.log(frutas.includes("pera"));  // true (forma correcta)
let persona = { nombre: "Luis", edad: 22 };
console.log("edad" in persona);        // true

// De bits
console.log("Bits:");
console.log(5 & 1);  // AND bit a bit
console.log(5 | 1);  // OR bit a bit
console.log(5 ^ 1);  // XOR
console.log(~5);     // NOT bit a bit
console.log(5 << 1); // desplazamiento izquierda
console.log(5 >> 1); // desplazamiento derecha


// Condicionales
let edad = 20;

console.log("Condicionales:");
if (edad >= 18) {
  console.log("Eres mayor de edad");
} else {
  console.log("Eres menor de edad");
}

edad >= 18 ? console.log("Ternario: Mayor de edad") : console.log("Ternario: Menor");


// Switch
let dia = "martes";
switch (dia) {
  case "lunes":
    console.log("Inicio de semana");
    break;
  case "martes":
    console.log("Segundo día");
    break;
  default:
    console.log("Otro día");
}


// Bucle for
console.log("Bucle for:");
for (let i = 0; i < 3; i++) {
  console.log("i =", i);
}


// Bucle while
console.log("Bucle while:");
let n = 0;
while (n < 3) {
  console.log("n =", n);
  n++;
}


// Bucle do...while
console.log("Bucle do...while:");
let m = 0;
do {
  console.log("m =", m);
  m++;
} while (m < 3);


// try...catch
console.log("Excepciones:");
try {
  throw new Error("Algo salió mal");
} catch (error) {
  console.log("Error capturado:", error.message);
} finally {
  console.log("Bloque finally ejecutado");
}

// DIFICULTAD EXTRA

console.log("DIFICULTAD EXTRA:");
for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i);
  }
}
