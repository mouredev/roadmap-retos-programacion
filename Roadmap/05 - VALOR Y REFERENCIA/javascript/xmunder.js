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

// Ejemplo de asignación por valor para tipos primitivos
let a = 10;
let b = a; // Asignación por valor
b = 20; // Modificar 'b' no afecta 'a'
console.log(a); // Resultado: 10

// Ejemplo de asignación por referencia para objetos
let array1 = [1, 2, 3];
let array2 = array1; // Ambas variables apuntan al mismo objeto en la memoria

array2.push(4); // Modificar 'array2' afecta a 'array1'
console.log(array1); // Resultado: [1, 2, 3, 4]

// Ejemplo de función que recibe parámetros por valor
function modificarNumero(num) {
  num = 100; // Modificar el parámetro 'num' no afecta el valor original
}

let x = 5;
modificarNumero(x);
console.log(x); // Resultado: 5

// Ejemplo de función que recibe parámetros por referencia (objeto)
function modificarArray(arr) {
  arr.push(4); // Modificar el parámetro 'arr' afecta al array original
}

let miArray = [1, 2, 3];
modificarArray(miArray);
console.log(miArray); // Resultado: [1, 2, 3, 4]

function intercambiarPorValor(a, b) {
  let temp = a;
  a = b;
  b = temp;
  return [a, b];
}

//DIFICULTAD EXTRA
// Definir variables
let valor1 = 10;
let valor2 = 20;

// Llamar a la función y asignar los resultados a nuevas variables
let nuevosValores = intercambiarPorValor(valor1, valor2);
let nuevoValor1 = nuevosValores[0];
let nuevoValor2 = nuevosValores[1];

// Imprimir resultados
console.log("Original (por valor):", valor1, valor2); // Original (por valor): 10 20
console.log("Nuevos (por valor):", nuevoValor1, nuevoValor2); // Nuevos (por valor): 20 10
console.log("Comprobación:", valor1, valor2); // Comprobación: 10 20

function intercambiarPorReferencia(obj) {
  let temp = obj.prop1;
  obj.prop1 = obj.prop2;
  obj.prop2 = temp;
  return obj;
}

// Definir objeto
let objeto = { prop1: "hola", prop2: "mundo" };

// Llamar a la función y asignar los resultados a un nuevo objeto
let nuevoObjeto = intercambiarPorReferencia(objeto);

// Imprimir resultados
console.log("Original (por referencia):", objeto.prop1, objeto.prop2); // Original (por referencia): hola mundo
console.log("Nuevo (por referencia):", nuevoObjeto.prop1, nuevoObjeto.prop2); // Nuevo (por referencia): mundo hola
console.log("Comprobación:", objeto.prop1, objeto.prop2); // Comprobación: mundo hola
