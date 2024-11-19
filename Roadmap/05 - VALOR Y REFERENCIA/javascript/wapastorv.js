/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

// Por valor
var a = 1;
var b = a;
b = 2;
console.log(a); // 1
console.log(b); // 2

// Por referencia
var obj1 = { name: 'John' };
var obj2 = obj1;
obj2.name = 'Jane';
console.log(obj1.name); // Jane
console.log(obj2.name); // Jane

// Por valor
function addOne(num) {
  num++;
}
var num = 1;
addOne(num); // num es pasado por valor
console.log(num); // 1

// Por referencia
function changeName(obj) {
  obj.name = 'Jane';
}
var obj = { name: 'John' };
changeName(obj); // obj es pasado por referencia
console.log(obj.name); // Jane

// DIFICULTAD EXTRA
function swapByValue(a, b) {
  var temp = a;
  a = b;
  b = temp;
  return [a, b];
}

function swapByReference(obj1, obj2) {
  var temp = obj1.name;
  obj1.name = obj2.name;
  obj2.name = temp;
  return [obj1, obj2];
}

var a = 1;
var b = 2;
var obj1 = { name: 'John' };
var obj2 = { name: 'Jane' };

var swappedValues = swapByValue(a, b);
var swappedReferences = swapByReference(obj1, obj2);

console.log(a); // 1
console.log(b); // 2
console.log(swappedValues[0]); // 2
console.log(swappedValues[1]); // 1

console.log(obj1.name); // Jane
console.log(obj2.name); // John
console.log(swappedReferences[0].name); // John
console.log(swappedReferences[1].name); // Jane

