// Tipos de Operadores en TypeScript

// 📌 OPERADORES ARITMETICOS (+, -, *, /)

// Operador de Adicion (+)
let sum: number = 10 + 20;
console.log(sum); // 30

// Operador de Substracion (-)
let rest: number = 20 - 10;
console.log(rest); // 10

// Operador de Multiplicación
let mult: number = 10 * 20;
console.log(mult); // 200

// Operador de Division
let division: number = 20 / 10;
console.log(division); // 2

/* ********************************* */

// 📌 OPERADOR RESTO (%)
let modulo: number = 10 % 2;
console.log(modulo); // El resto de la division de 10 entre 2 es => 0

/* ********************************* */

// 📌 OPERADORES DE ASIGNACION

// Operador de asignacion
let x: number = 10;
let y: number = x;
console.log(y); // El valor de "x" se asigno a "y"

let sumAsign: number = (x += y); // Asigna el resultado de "x" mas "y" a "x"
let restAsign: number = (x -= y); // Asigna el resultado de "x" menos "y" a "x"
let multAsign: number = (x *= y); // Asigna el resultado de "x" multiplicado por "y" a "x"
let divAsign: number = (x /= y); // Asigna el resultado de "x" dividido por "y" a "x"
let modAsign: number = (x %= y); // Asigna el resultado de "x" modulo "y" a "x"

/* ********************************* */

// 📌 OPERADORES UNARIOS

// Operador Unario Plus (+x)
let unarioPlus: string = "23";
console.log(+unarioPlus, typeof +unarioPlus); // 23 number

// Operador Unario Menos (-x)
let unarioMenos: string = "10";
console.log(-unarioMenos, typeof -unarioMenos); // 10 number

// Operador de Incremento Prefix (++x)
let contador: number = 10;
console.log(++contador); // 11

// Operador de Decremento Prefix
console.log(--contador); // 10

// Operador de Incremento Postfix
console.log(contador++); // 10

// Operador de Decremento Postfix
console.log(contador--); // 11
console.log(contador); // 10

/* ********************************* */

// 📌 OPERADORES DE COMPARACIÓN

// Operador Menor que (<)
let menorQue: boolean = 10 < 20;
console.log(menorQue); // true

// Operador Mayor que (>)
let mayorQue: boolean = 10 > 20;
console.log(mayorQue); // false

// Operador Menor o igual que (<=)
let menorIgualQue: boolean = 10 <= 20;
console.log(menorIgualQue); // true

// Operador Mayor o igual que (>=)
let mayorIgualQue: boolean = 10 >= 20;
console.log(mayorIgualQue); // false

// Operador de Igual a (==)
let igual: boolean = 10 == 10;
console.log(igual); // true

// Operador de No Igual (!=)
let noIgual: Boolean = 10 != 10;
console.log(noIgual); // false

// Operador de Estricto Igual
let estrictoIgual: boolean = 10 === 10;
console.log(estrictoIgual); // true

// Operador de No Estricto Igual
let noEstrictoIgual: boolean = 10 !== 10;
console.log(noEstrictoIgual);

/* ********************************* */

// 📌 OPERADORES LOGICOS (!, ||, &&)

// Operador NOT (!)
let negacion: boolean = true;
console.log(!negacion); // false

let dobleNegacion: boolean = true;
console.log(!!dobleNegacion);

// Operador AND (&&)
console.log(true && true); // true
console.log(true && false); // false
console.log(false && true); // false
console.log(false && false); // false

// Operador OR (||)
console.log(true || true); // true
console.log(true || false); // true
console.log(false || true); // true
console.log(false || false); // false

/* ********************************* */

// 📌 EJEMPLOS ESTRUCTURAS DE CONTROL (IF - ELSE, SWITCH, FOR, WHILE, DO WHILE, BREAK, CONTINUE)

// IF ELSE
let edad: number = 23;
if (edad < 18) {
  console.log(`Tienes ${edad} años, eres menor de edad`);
} else if (edad >= 18) {
  console.log(`Tienes ${edad} años, eres mayor de edad`);
} else {
  console.log("Por favor ingrese una edad");
}

// Switch
let diasSemana: Date = new Date();
switch (diasSemana.getDay()) {
  case 0:
    console.log("Domingo");
    break;
  case 1:
    console.log("Lunes");
    break;
  case 2:
    console.log("Martes");
    break;
  case 3:
    console.log("Miercoles");
    break;
  case 4:
    console.log("Jueves");
    break;
  case 5:
    console.log("Viernes");
    break;
  case 6:
    console.log("Sabado");
    break;
}

// FOR
for (let i = 1; i <= 10; i++) {
  console.log(i);
}

// WHILE
let contar: number = 1;
while (contar <= 10) {
  console.log(contar);
  contar++;
}

// DO WHILE
let i: number = 1;
do {
  console.log(i);
  i++;
} while (i <= 10);

// Break (Solo se puede usar en FOR, WHILE y DO WHILE)
let productos: object[] = [
  { nombre: "Telefono", precio: 700 },
  { nombre: "Tablet", precio: 900 },
  { nombre: "Computadora", precio: 2500 },
];
for (let i = 0; i <= productos.length; i++) {
  if (productos[i]["precio"] === 900) break;
  console.log(productos[i]);
}

// Continue (Solo se puede usar en FOR, WHILE y DO WHILE)

for (let i = 0; i <= 10; i++) {
  if (i % 2 !== 0) continue;
  console.log(i);
}

/*
  DIFICULTAD EXTRA (opcional):
 Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. */

let count: number = 10;
do {
  if (count % 2 === 0 && count !== 16 && count % 3 !== 0) {
    console.log(count);
  }
  count++;
} while (count <= 55);
