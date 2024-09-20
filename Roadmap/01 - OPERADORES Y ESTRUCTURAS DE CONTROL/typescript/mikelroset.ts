// ------------------------- OPERADORES ARITMÉTICOS ------------------------- //

// Suma	
let sum: number = 5 + 2 // 7

// Resta
let rest: number = 5 - 2 // 3

// Multiplicación
let mult: number = 5 * 2 // 10

// División
let div: number = 5 / 2 // 2.5

// Módulo (resto)
let mod: number = 5 % 2 // 1

// Exponenciación
let exp: number = 5 ** 2 // 25

// Incremento
let x: number = 5; 
x++ // x es 6

// Decremento
let y: number = 5;
y-- // y es 4


// ------------------------ OPERADORES DE ASIGNACIÓN ------------------------ //

// Asignación
let z: number = 5;

// Asignación de suma
z += 5 // z = z + 5

// Asignación de resta
z -= 5 // z = z - 5

// Asignación de multiplicación
z *= 5 // z = z * 5

// Asignación de división
z /= 5 // z = z / 5

// Asignación de módulo
z %= 5 // z = z % 5

// Asignación de exponenciación
z **= 5 // z = z ** 5


// ------------------------- OPERADORES DE COMPARACIÓN ---------------------- //

// ==	Igual a
let val1: number = 5;
let val2: string = '5';
val1 == val2 // true

// ===	Estrictamente igual a
val1 === val2 // false

// !=	No igual a
val1 != val2 // false

// !==	Estrictamente no igual a
val1 !== val2 // true

// >	Mayor que
5 > 2 // true

// <	Menor que
5 < 2 // false

// >=	Mayor o igual que
5 >= 5 // true

// <=	Menor o igual que
5 <= 5 // true


// -------------------------- OPERADORES LÓGICOS ---------------------------- //

// AND
let a: boolean = true;
let b: boolean = false;
let c: boolean = a && b; // false

// OR
let d: boolean = true;
let e: boolean = false;
let f: boolean = d || e; // true

// NOT
let g: boolean = true;
let h: boolean = !g; // false


// -------------------------- OPERADORES DE BITS ---------------------------- //

// AND
let i: number = 5; // 0101
let j: number = 3; // 0011
let k: number = i & j; // 0001

// OR
let l: number = 5; // 0101
let m: number = 3; // 0011
let n: number = l | m; // 0111

// XOR
let o: number = 5; // 0101
let p: number = 3; // 0011
let q: number = o ^ p; // 0110

// Complemento
let r: number = 5; // 0101
let s: number = ~r; // 1010

// Desplazamiento a la izquierda
let t: number = 5; // 0101
let u: number = t << 1; // 1010

// Desplazamiento a la derecha
let v: number = 5; // 0101
let w: number = v >> 1; // 0010

// Desplazamiento a la derecha sin signo
let x2: number = 5; // 0101
let y2: number = x2 >>> 1; // 0100


// ------------------------- OPERADORES DE CADENAS -------------------------- //

// Concatenación de cadenas
let a3: string = "Hello";
let b3: string = "World";
let c3: string = a3 + b3; // HelloWorld

// Concatenación y asignación
let d3: string = a3;
d3 += b3; // HelloWorld


// -------------------------- OPERADORES TERNARIOS -------------------------- //

// Condicional
let z2: boolean = true;
let a2: number = z2 ? 5 : 10; // 5

// Condicional con ternario
let b2: number = z2 ? 5 : 10; // 5


// -------------------- OPERADORES DE DESESTRUCTURACIÓN --------------------- //

// ... Spread o Rest
let [a4, b4]: [number, number] = [1, 2];
let otherObj: object = { name: "John", age: 25 };
let obj: object = { ...otherObj };


// ------------------------ OPERADORES DE TIPO TYPEOF ----------------------- //

// typeof
typeof 5 // number


// ------------------------ OPERADORES DE ELIMINACIÓN ----------------------- //

// delete
type Person = {
  name?: string;
  age: number;
};
let obj2: Person = { name: "John", age: 25 };
delete obj2.name; // Elimina el nombre de la variable 'obj'


// ----------------------- OPERADORES DE INSTANCIA -------------------------- //

// instanceof
class Person2 {
  name: string;
  age: number;
}
obj2 instanceof Person2 // true


// ----------------------- OPERADORES DE INCLUSIÓN -------------------------- //

// in
let a5: object = { message: "Hello World" };
"message" in a5; // true


// --------------- OPERADORES DE ENCADENAMIENTO OPCIONAL -------------------- //

// ?.
type Person3 = {
  personalInfo?: {
    name: string;
    age: number;
  };
};
let obj3: Person3 = { personalInfo: { name: "John", age: 25 } };
obj3?.personalInfo?.name // undefined si obj3 o personalInfo no existen


// ------------------ OPERADORES DE COALESCENCIA NULA ----------------------- //

// ?? (Devuelve el valor de la derecha si el valor izquierdo es null)
null ?? "John" // John


// ------------------------ OPERADORES SATISFIES ---------------------------- //

// satisfies
type Config = {
  url: string;
  port: number;
};
// config sigue teniendo la prop. "protocol", aunque satisface el tipo "Config"
const config = {
  url: "https://example.com",
  port: 8080,
  protocol: "https",
} satisfies Config;


// ------------------ OPERADORES DE ASIGNACIÓN LÓGICA ----------------------- //

// &&=
let a6: boolean = true;
let b6: boolean = false;
a6 &&= b6; // false

// ||=
let c6: boolean = true;
let d6:  = false;
c6 ||= d6; // true

// ??=
let e6: string | null = null;
let f6 = "John";
e6 ??= f6; // "John"


// ----------------------------- OPERADOR VOID ------------------------------ //

// void
function someFunction(): void {
  console.log("Hello World");
}
void someFunction(); // Ejecuta la función pero ignora su valor de retorno


// --------------------- OPERADOR DE MÓDULOS DINÁMICOS ---------------------- //

/*
 * import
 * Se utiliza para importar módulos de forma dinámica. Aunque no es un operador
 * estándar, actúa como tal para cargar módulos bajo demanda
*/
import { add } from "./math";
add(5, 5); // 10


// ----------------------------- OPERADOR NEW ------------------------------- //

// new
let date = new Date(); // Crea una nueva instancia del objeto Date


// ---------------------------- OPERADOR SUPER ----------------------------- -//

// super
class Animal {
  constructor(public name: string) {}
}

class Dog extends Animal {
  constructor(name: string) {
    super(name); // Llama al constructor de la clase padre
  }
}


// --------------------------- OPERADOR THIS -------------------------------- //

// this
class MyClass {
  constructor(public name: string) {}

  sayHello() {
    console.log(`Hello, ${this.name}`);
  }
}

let obj5 = new MyClass('TypeScript');
obj5.sayHello(); // "Hello, TypeScript"


// ---------------------- ESTRUCTURAS CONDICIONALES ------------------------- //

// if, else if, else
const age: number = 25;

if (age < 18) {
  console.log("You are a child");
} else if (age >= 18 && age < 65) {
  console.log("You are an adult");
} else {
  console.log("You are a senior citizen");
}

// switch
const fruit: string = "banana";

switch (fruit) {
  case "apple":
    console.log("Es una manzana");
    break;
  case "banana":
    console.log("Es un plátano");
    break;
  default:
    console.log("Fruta desconocida");
}


// ---------------------- ESTRUCTURAS ITERACIONES --------------------------- //

// for
for (let i: number = 0; i < 5; i++) {
  console.log(i);
}

// for...of
for (const fruit of ["apple", "banana", "orange"]) {
  console.log(fruit);
}

// for...in
let obj6: object = { name: "John", age: 25 };
for (const key in obj6) {
  console.log(`${key}: ${obj6[key]}`);
}

// while
let j: number = 0;
while (j < 5) {
  console.log(j);
  j++;
}

// do...while
let k: number = 0;
do {
  console.log(k);
  k++;
} while (k < 5);


// ----------------- ESTRUCTURAS DE CONTROL DE ITERACIÓN -------------------- //

// break
for (let i: number = 0; i < 5; i++) {
  if (i === 3) {
    break;
  }
  console.log(i);
}

// continue
for (let i: number = 0; i < 5; i++) {
  if (i === 2) {
    continue;
  }
  console.log(i);
}

// return
function add(a: number, b: number): number {
  return a + b;
}

add(5, 5); // 10


// ------------------ ESTRUCTURAS DE CONTROL DE EXCEPCIONES ---------------- //

// try...catch...finally
try {
  throw new Error("Something went wrong");
} catch (error) {
  console.log(error.message);
} finally {
  console.log("Finally block");
}

// throw
function throwError(): never {
  throw new Error("Something went wrong");
}


// ---------------------- ESTRUCTURAS DE CONTROL DE ASYNC ------------------- //

// async await
async function fetchData() {
  try {
    const response = await fetch("https://api.example.com/data");
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("Error al obtener los datos:", error);
  }
}

fetchData();

// Promise.then().catch().finally()
fetch("https://api.example.com/data")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error))
  .finally(() => console.log("Proceso terminado"));


// -------------------------- BONUS EJERCICIO ------------------------------- //

/*
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3
*/
const conf = {
  MULTIPLE_OF_X: 3,
  EXCLUDED_NUMBER: 16,
  MIN: 10,
  MAX: 55
};

/**
 * Verifica si un número es par
 * @param num - Número a verificar
 * @returns true si el número es par
 */
function isEven(num: number): boolean {
  return num % 2 === 0;
}

/**
 * Verifica si un número no es el número excluido (conf.EXCLUDED_NUMBER)
 * @param num - Número a verificar
 * @returns true si el número no es conf.EXCLUDED_NUMBER
 */
function isNotExcludedNumber(num: number): boolean {
  return num !== conf.EXCLUDED_NUMBER;
}

/**
 * Verifica si un número no es múltiplo de un valor dado
 * @param num - Número a verificar
 * @param divisor - Valor divisor
 * @returns true si el número no es múltiplo del divisor
 */
function isNotMultipleOf(num: number, divisor: number): boolean {
  return num % divisor !== 0;
}

/**
 * Verifica si un número es par, no es conf.EXCLUDED_NUMBER y no es múltiplo de
 * conf.MULTIPLE_OF_X
 * @param num - Número a verificar
 * @returns true si el número cumple todas las condiciones
 */
function isEvenAndValid(num: number): boolean {
  return isEven(num) 
    && isNotExcludedNumber(num) 
    && isNotMultipleOf(num, conf.MULTIPLE_OF_X);
}

// Recorremos el rango y mostramos solo los números que cumplen las condiciones
for (let i = conf.MIN; i <= conf.MAX; i++) {
  if (isEvenAndValid(i)) {
    console.log(i);
  }
}
