/* Operadores Aritmeticos */

let a = 5;
let b = 7;

let suma = a + b; // Suma
let resta = a - b; // Resta
let multiplicación = a * b; // Multiplicación
let división = a / b; // División
let modulo = a % b; // Módulo
let potencia = a ** b; // Potencia

// incremento
console.log(++a);
console.log(a++);
// decrementar
console.log(--a);
console.log(a--);

/* Operadores de Asignación */

let x = 5;
x += 5; // Suma
x -= 5; // Resta
x *= 5; // Multiplicación
x /= 5; // División
x %= 5; // Módulo
x **= 5; // Potencia

/* Operadores de Comparación */

//Relacionales
let n1 = 10;
let n2 = 5;
let comp1 = n1 > n2;
let comp2 = n1 >= n2;
let comp3 = n1 < n2;
let comp4 = n1 <= n2;

//Igualdad
let comp5 = n1 === n2;
let comp6 = n1 !== n2;

/* Operadores Lógicos */

// AND
let and = true && true; // true
let and2 = false && true; // false

// OR
let or = true || false // true
let or2 = false || false; // false

// NOT
let verdadero = true;
let falso = false;
let not = !verdadero; // false
let not2 = !falso; // true

/* Operadores de Bitwise */

// Operador Bitwise de AND
let bitwise = 1 | 3; // 00000011 = 3
let bitwise2 = 1 | 4; // 00000101 = 5
let bitwise3 = 3 | 5; // 00000111 = 7

//Operador Bitwise de OR
let bitwise4 = 1 & 3; // 000000001 = 1
let bitwise5 = 1 & 4; // 000000000 = 0
let bitwise6 = 3 & 5; // 000000001 = 1


/* if - else - else if */
let edad = 15;

if (edad > 17) {
  console.log('Usuario mayor de edad');
} else if (edad >= 13) {
  console.log('Usuario necesita estar acompañado');
} else {
  console.log('Usuario menor de edad');
}

/* switch */
let accion = 'listar';

switch (accion) {
  case 'listar':
    console.log('Acción de listar');
    break;
  case 'guardar':
    console.log('Acción de guardar');
    break
  default:
    console.log('Accion no reconocida');
}

/* while */
// cuales son los numeros pares
let i = 0;
while (i < 10) {
  if (i % 2 == 0) {
    console.log('Número par', i);
  }
  i++;
}

/* do while */
do {
  if (i % 2 == 0) {
    console.log('Número par', i);
  }
  i++;
} while (i < 10)

/* for */
for (let i = 2; i < 8; i++) {
  if (i % 2 == 0) {
    console.log('Número par', i);
  }
}

/* for of */
let animales = ['dragon', 't-rex', 'cobra'];

for (let animal of animales) {
  console.log(animal);
}

/* for in */
let user = {
  id: 1,
  name: 'diego',
  age: 22,
};

for (let prop in user) {
  console.log(prop, user.prop);
}

/* DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. */

for (let x = 10; x <= 55; x ++) {
  if (x % 2 === 0 && x !== 16 && x % 3 !== 0) {
    console.log(x);
  }
}











