let n1 = 3
let n2 = 6

// Operadores de comparación
console.log(3 == n1); // Igual
console.log(n1 != 4); // No es igual
console.log('3' === n1); // Estrictamente igual
console.log(n1 !== '3'); // Desigualdad estricta
console.log(n1 > n2); // Mayor que
console.log(n1 >= n1); // Mayor o igual que
console.log(n1 > n2); // Menor que
console.log(n1 <= n2); // Menor o igual que

// Operadores aritméticos
console.log(n1 + n2); // Suma
console.log(n1 - n2); // Resta
console.log(n1 * n2); // Multiplicación
console.log(n1 / n2); // División
console.log(n1 % n2); // Residuo
console.log(n1++); // Incremento
console.log(n1--); // Decremento

// Operadores bit a bit
let a = 6;  // 0110 en binario
let b = 3;  // 0011 en binario

console.log(a & b);  // AND bit a bit: 0010 (salida: 2)
console.log(a | b);  // OR bit a bit: 0111 (salida: 7)
console.log(a ^ b);  // XOR bit a bit: 0101 (salida: 5)
console.log(~a);     // NOT bit a bit: 1001 (en complemento a dos, salida: -7)
console.log(a << 1); // Desplazamiento a la izquierda: 1100 (salida: 12)
console.log(a >> 1); // Desplazamiento a la derecha con signo: 0011 (salida: 3)
console.log(a >>> 1); // Desplazamiento a la derecha sin signo: 0011 (salida: 3)

// Operadores lógicos
let p = 8;
let q = 3;

let resultado1 = (p > q) && (q > 0);  // true && true => true
console.log(resultado1);  // Salida: true

let resultado2 = (p < q) || (q > 0);  // false || true => true
console.log(resultado2);  // Salida: true

let resultado3 = !(p < q);  // !false => true
console.log(resultado3);  // Salida: true

let m = false;
let n = true;
let o = false;

let resultado4 = m || n && o;  // false || true && false => false || false => false
console.log(resultado4);  // Salida: false

let resultado5 = !(m || (n && o));  // !(false || (true && false)) => !(false || false) => !false => true
console.log(resultado5);  // Salida: true

// Operadores de cadena
let r = 'JavaScript'
console.log("Hola mundo desde " + r); // Operador de concatenación

let s = 'Java'
s += 'Script' // Operador de concatenación abreviada
console.log(s);

// Operador condicional (Ternario)
let edad = 18
let resultado = edad >= 18 ? 'Es mayor de edad.' : 'Es menor de edad.'
console.log(resultado);

/*
  Utilizando las operaciones con operadores que tú quieras, crea ejemplos
  que representen todos los tipos de estructuras de control que existan
  en tu lenguaje:
  Condicionales, iterativas, excepciones...
*/

// Condicional
if (edad >= 18) {
  console.log('Eres mayor de edad.');
} else {
  console.log('Eres menor de edad.');
}

// Bucle for
let mult = 5;
for (let n = 1; n <= 12; n++) {
  console.log(`${mult} x ${n} = ${mult * n}`);
}

// Bucle forEach
let frutas = ['manzana', 'banana', 'cereza', 'durazno', 'fresa', 'kiwi', 'mango', 'naranja', 'pera', 'piña'];
console.log('########## forEach ##########');
frutas.forEach(fruta => {
  console.log(fruta);
})

// Bucle for...in
console.log('########## for...in ##########');
for (let fruta in frutas) {
  console.log(frutas[fruta]);
}

// Bucle for...of
console.log('########## for...of ##########');
for (let fruta of frutas) {
  console.log(fruta);
}

// Bucle while
let num = 1
while (num <= 10) {
  if (num % 2 === 0) {
    console.log(`${num} es par.`);
  }
  num++
}

// Bucle Do While
num = 1
do {
  if (num % 2 === 0) {
    console.log(`${num} es par.`);
  }
  num++
} while (num <= 10);

// Switch
let mes = new Date().getMonth() + 1

switch (mes) {
  case 1:
    console.log('Enero');
    break;
  case 2:
    console.log('Febrero');
    break;
  case 3:
    console.log('Marzo');
    break;
  case 4:
    console.log('Abril');
    break;
  case 5:
    console.log('Mayo');
    break;
  case 6:
    console.log('Junio');
    break;
  case 7:
    console.log('Julio');
    break;
  case 8:
    console.log('Agosto');
    break;
  case 9:
    console.log('Septiembre');
    break;
  case 10:
    console.log('Octubre');
    break;
  case 11:
    console.log('Noviembre');
    break;
  case 12:
    console.log('Diciembre');
    break;
  default:
    nombreDelMes = 'Número de mes no válido';
}

/*
  Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

for (let n = 10; n <= 55; n++) {
  if (n % 2 === 0 && n !== 16 && n % 3 !== 0) {
    console.log(n);
  }
}













