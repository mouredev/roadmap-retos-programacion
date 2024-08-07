// DATOS POR VALOR Y REFERENCIA
var a = 10;
var b = a;
a = 20;

console.log(b); // 10
console.log(a); // 20

var c = [10, 20];
var d = c;
d.push(30);

console.log(d);
console.log(c);

// FUNCIONES CON DATOS POR VALOR

var h = 10;

function my_valor(my_va) {
  my_va = 20;
  console.log(my_va);
}

my_valor(h); // 20
console.log(h); // 10

// FUNCIONES CON DATOS POR REFERENCIA

// var j = [10, 20];

// function my_referencia(my_re) {
//   my_re.push(30);
//   console.log(my_re);
// }

// my_referencia(j);
// console.log(j);

// EJERCICIO DE VALOR
function intercambioPorValor(a, b) {
  let temp = a;
  a = b;
  b = temp;
  return [a, b];
}

// Definimos variables originales
let valor1 = 10;
let valor2 = 20;

// Llamamos a la función para intercambiar los valores
let nuevosValores = intercambioPorValor(valor1, valor2);

// Imprimimos los valores originales y los nuevos
console.log(valor1, valor2);
console.log(nuevosValores[0], nuevosValores[1]);

// EJERCICIO DE REFERENCIA
function interPorRef(c, d) {
  let temp = c;
  c = d;
  d = temp;
  d.push(50);

  return [c, d];
}

var valor3 = [10, 20];
var valor4 = [30, 40];

let nuevoValor2 = interPorRef(valor3, valor4);
console.log(valor3, valor4);
console.log(nuevoValor2[0], nuevoValor2[1]);
