/* Paso de variables por valor y por referencia */

// Paso por valor (tipos primitivos)
let num1 = 5;
let num2 = 10;

function sumarPorValor(a, b) {
  a += 5; // Modifica la copia local de 'a'
  b += 5; // Modifica la copia local de 'b'
  console.log(a, b);
}

sumarPorValor(num1, num2);
console.log(num1, num2);

// Paso por referencia (objetos)
let obj1 = { x: 1, y: 2 };
let obj2 = { z: 3 };

function modificarPorReferencia(objeto) {
  objeto.x = 10; // Modifica la propiedad 'x' del objeto original
}

modificarPorReferencia(obj1);
console.log(obj1); // { x: 10, y: 2 } (el objeto original se modificó)

/* Funciones con paso por valor y por referencia */

function sumarPorValor(a, b) {
  return a + b; // Retorna la suma de los valores (copias)
}

function modificarArrayPorReferencia(arr) {
  arr.push(5); // Modifica el array original
}

let numeros = [1, 2, 3];
modificarArrayPorReferencia(numeros);
console.log(numeros);

/* Desafio */

// Intercambio por valor
function intercambiarPorValor(a, b) {
  let temp = a;
  a = b;
  b = temp;
  return [a, b];
}

let x = 5;
let y = 10;
[x, y] = intercambiarPorValor(x, y);
console.log(x, y);

// Intercambio por referencia
function intercambiarPorReferencia(obj) {
  let temp = obj.a;
  obj.a = obj.b;
  obj.b = temp;
}

let obj = { a: 5, b: 10 };
intercambiarPorReferencia(obj);
console.log(obj);
