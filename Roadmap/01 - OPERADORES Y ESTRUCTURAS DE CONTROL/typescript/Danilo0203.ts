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

/*DIFICULTAD EXTRA (opcional):
 Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. */

let count: number = 10;
do {
  if (count % 2 === 0 && count !== 16 && count % 3 !== 0) {
    console.log(count);
  }
  count++;
} while (count <= 55);
