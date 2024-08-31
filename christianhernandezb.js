//Ejemplo utilizando todos los tipos de operadores de javascript

//Operadorores aritmeticos
//Suma
const var1 = 2;
const var2 = 2;
const suma = var1 + var2;
console.log(`suma: ${suma}`);

//Resta
const resta = var1 - var2;
console.log(`resta: ${resta}`);

//Multiplicacion
const multiplicacion = var1 * var2;
console.log(`multiplicacion: ${multiplicacion}`);

//Division
const division = var1 / var2;
console.log(`division: ${division}`);

//Modulo
const modulo = var1 % var2;
console.log(`modulo: ${modulo}`);

//Operadores de asignacion
//Asignacion
let varAsig = 2;
console.log(`Asignacion: ${varAsig}`);

//Suma y asigna
varAsig += 2;
console.log(`Suma y asigna: ${varAsig}`);

//Resta y asigna
varAsig -= 2;
console.log(`Resta y asigna: ${varAsig}`);

//Multiplica y asigna
varAsig *= 2;
console.log(`Multiplica y asigna: ${varAsig}`);

//Divide y asigna
varAsig /= 2;
console.log(`Divide y asigna: ${varAsig}`);

//Modulo y asigna
varAsig %= 2;
console.log(`Modulo y asigna: ${varAsig}`);

//Operadores de comparacion
//Igualdad debil
if (1 == 1) {
  console.log('Igualdad debil');
}

//Igualdad estricta
if (1 === 1) {
  console.log('Igualdad estricta');
}

//desigualdad debil
if (2 != 1) {
  console.log('Desigualdad debil');
}

//desigualdad estricta
if (2 !== 1) {
  console.log('Desigualdad estricta');
}

//Mayor que
if (2 > 1) {
  console.log('Mayor que');
}

//Menor que
if (1 < 2) {
  console.log('Menor que');
}

//Mayor o igual que
if (2 >= 2) {
  console.log('Mayor o igual que');
}

//Menor o igual que
if (2 <= 2) {
  console.log('Menor o igual que');
}

//Operadores Logicos
//OR
if (1 + 1 === 2 || 2 + 2 === 4) {
  console.log('Operador logico OR');
}

//AND
if (1 + 1 === 2 && 2 + 2 === 4) {
  console.log('Operador logico AND');
}

//NOT
const adulto = false;

if (!adulto) {
  console.log('Eres menor de edad');
}

//Operadores de tipo
//typeof
const tipoDeVariable = 1;
console.log(typeof tipoDeVariable);

//Operadores bit a bit
//AND Bit a Bit
const a = 5;
const b = 3;
const resultadoAB = a&b;
console.log(`Bit a bit: ${resultadoAB}`);

//Estructuras de control
//Condicional if
const edad = 18;

if (edad >= 18) {
  console.log('Eres mayor de edad');
}else {
  console.log('Eres menor de edad');
}

//Bucle for
for (let i = 0; i <= 5; i++) {
  console.log(`Bucle for: ${i}`);
}

//Bucle while
let contador = 0;
while (contador <= 5) {
  console.log(`Bucle while: ${contador}`);
  contador++;
}

//Bucle do while
let contador1 = 0
do {
  console.log(`Bucle do while: ${contador1}`);
  contador1++;
} while (contador1 <= 5);

//Dificultad Extra
console.log('Ejercicio de con dificultad extra:');
for (let i = 10; i <= 55; i++) {
  if (i === 55) {
    console.log(i);
  }

  if (i%2 === 0 && i !== 16 && i%3 !== 0) {
    console.log(i);
  }
}

