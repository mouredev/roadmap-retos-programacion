// Ejemplo por valor
let num1 = 10;
let num2 = num1;

console.log(num1);
console.log(num2);

num2 = 20;

console.log(num1);
console.log(num2);

// Ejemplo por referencia
let array1 = [1, 2, 3];
let array2 = array1;

console.log(array1);
console.log(array2);

array2.push(4);

console.log(array1);
console.log(array2);

// Ejemplo funciones por valor
function incrementar(numero) {
  numero++;
}

let a = 5;
incrementar(a);

console.log(a);

// Ejemplo funciones por referencia
function agregarElemento(array) {
  array.push(4);
}

let b = [1, 2, 3];
agregarElemento(b);

console.log(b);
