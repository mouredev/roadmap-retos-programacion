// Operadores aritméticos
let suma = 5 + 3;
let resta = 5 - 3;
let multiplicacion = 5 * 3;
let division = 5 / 3;
let modulo = 5 % 3;
let potencia = 5 ** 3;
console.log('Aritméticos:', suma, resta, multiplicacion, division, modulo, potencia);

// Operadores lógicos
let and = true && false;
let or = true || false;
let not = !true;
console.log('Lógicos:', and, or, not);

// Operadores de comparación
let igual = 5 == '5';
let estrictamenteIgual = 5 === '5';
let diferente = 5 != '5';
let mayorQue = 5 > 3;
let menorQue = 5 < 3;
console.log('Comparación:', igual, estrictamenteIgual, diferente, mayorQue, menorQue);

// Operadores de asignación
let x = 5;
x += 3; // 8
x -= 2; // 6
x *= 2; // 12
x /= 2; // 6
x %= 2; // 0
console.log('Asignación:', x);

// Operadores de identidad
let identidad = 5 === 5;
console.log('Identidad:', identidad);

// Operadores de pertenencia
let array = [1, 2, 3, 4, 5];
let pertenece = array.includes(3);
console.log('Pertenencia:', pertenece); // true
console.log('Pertenencia:', array.includes(6)); // false

// Operadores de bits
let bitAnd = 5 & 3;
let bitOr = 5 | 3;
let bitXor = 5 ^ 3;
let bitNot = ~5;
let bitShiftLeft = 5 << 1;
let bitShiftRight = 5 >> 1;
console.log('Bits:', bitAnd, bitOr, bitXor, bitNot, bitShiftLeft, bitShiftRight);

// Estructuras de control condicionales
if (suma > 5) {
    console.log('Condicional if: La suma es mayor que 5');
} else {
    console.log('Condicional if: La suma no es mayor que 5');
}

// Estructuras de control iterativas
for (let i = 0; i < 5; i++) {
    console.log('Iterativa for:', i);
}

let j = 0;
while (j < 5) {
    console.log('Iterativa while:', j);
    j++;
}

// Estructuras de control excepciones
try {
    throw new Error('Esto es un error');
} catch (error) {
    console.log('Excepción:', error.message);
}

// Switch case
let mayor = 18;
switch (mayor) {    
  case 18:
      console.log('Eres mayor de edad');
      break;
  case 21:
      console.log('Ya puedes beber');
      break;
  default:
      console.log('No eres mayor de edad');
      break;
}

// For in
let persona = {
    nombre: 'Juan',
    edad: 25
};

for (let key in persona) {
    console.log('For in:', key, persona[key]);
}

// For of
let colores = ['rojo', 'verde', 'azul'];

for (let color of colores) { 
    console.log('For of:', color);
}

// DIFICULTAD EXTRA
for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log('Número:', i);
    }
}
