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
const num1 = 10;
let num2 = num1; // Asignación por valor
num2 = 20;

console.log(num1); // Salida: 10 (valor original no cambia)
console.log(num2); // Salida: 20

// Ejemplo de asignación por referencia para objetos
const obj1 = { nombre: 'Juan' };
const obj2 = obj1; // Asignación por referencia
obj2.nombre = 'Carlos';

console.log(obj1.nombre); // Salida: Carlos (el valor original cambia)
console.log(obj2.nombre); // Salida: Carlos

// Ejemplo de función que recibe parámetros por valor
function duplicar(numero) {
  numero *= 2;
  return numero;
}

const original = 5;
const resultado = duplicar(original);

console.log(original); // Salida: 5 (el valor original no cambia)
console.log(resultado); // Salida: 10

// Ejemplo de función que recibe parámetros por referencia (objeto)
function cambiarNombre(persona) {
  persona.nombre = 'Pedro';
}

const personaOriginal = { nombre: 'Juan' };
cambiarNombre(personaOriginal);

console.log(personaOriginal.nombre); // Salida: Pedro (el valor original cambia)

console.log(`${'\n'}${'*'.repeat(50)}${'\n'}`);

// Función que intercambia valores por valor
function intercambiarValoresPorValor(a, b) {
  const temp = a;
  a = b;
  b = temp;
  return [a, b];
}

// Función que intercambia valores por referencia
function intercambiarValoresPorReferencia(obj) {
  const copia = { ...obj }; // Crear una copia del objeto original
  const temp = copia.valor1;
  copia.valor1 = copia.valor2;
  copia.valor2 = temp;
  return copia; // Devolver la copia del objeto modificado
}

// Ejemplos
const valorA = 3;
const valorB = 7;

const [nuevoValorA, nuevoValorB] = intercambiarValoresPorValor(valorA, valorB);
console.log(valorA, valorB); // Salida: 3 7
console.log(nuevoValorA, nuevoValorB); // Salida: 7 3

const valores = { valor1: 10, valor2: 5 };

const nuevosValores = intercambiarValoresPorReferencia(valores);
console.log(valores.valor1, valores.valor2); // Salida: 10 5
console.log(nuevosValores.valor1, nuevosValores.valor2); // Salida: 5 10

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
