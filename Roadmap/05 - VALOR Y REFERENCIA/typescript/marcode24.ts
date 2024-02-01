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
const num1: number = 10;
let num2: number = num1; // Asignación por valor
num2 = 20;

console.log(num1); // Salida: 10 (valor original no cambia)
console.log(num2); // Salida: 20

// Ejemplo de asignación por referencia para objetos
interface Persona {
  nombre: string;
}

const obj1: Persona = { nombre: 'Juan' };
const obj2: Persona = obj1; // Asignación por referencia
obj2.nombre = 'Carlos';

console.log(obj1.nombre); // Salida: Carlos (el valor original cambia)
console.log(obj2.nombre); // Salida: Carlos

// Ejemplo de función que recibe parámetros por valor
function duplicar(numero: number): number {
  numero *= 2;
  return numero;
}

const original: number = 5;
const resultado: number = duplicar(original);

console.log(original); // Salida: 5 (el valor original no cambia)
console.log(resultado); // Salida: 10

// Ejemplo de función que recibe parámetros por referencia (objeto)
function cambiarNombre(persona: Persona): void {
  persona.nombre = 'Pedro';
}

const personaOriginal: Persona = { nombre: 'Juan' };
cambiarNombre(personaOriginal);

console.log(personaOriginal.nombre); // Salida: Pedro (el valor original cambia)

console.log(`${'\n'}${'*'.repeat(50)}${'\n'}`);

// Función que intercambia valores por valor
function intercambiarValoresPorValor(a: any, b: any): [any, any] {
  const temp = a;
  a = b;
  b = temp;
  return [a, b];
}

// Función que intercambia valores por referencia
function intercambiarValoresPorReferencia(obj: { valor1: any; valor2: any }): { valor1: any; valor2: any } {
  const { valor1, valor2 } = obj;
  return { valor1: valor2, valor2: valor1 }; // Devolver un nuevo objeto con valores intercambiados
}

// Ejemplos
const valorA: number = 3;
const valorB: number = 7;

const [nuevoValorA, nuevoValorB]: [number, number] = intercambiarValoresPorValor(valorA, valorB);
console.log(valorA, valorB); // Salida: 3 7
console.log(nuevoValorA, nuevoValorB); // Salida: 7 3

const valores: { valor1: number; valor2: number } = { valor1: 10, valor2: 5 };

const nuevosValores: { valor1: number; valor2: number } = intercambiarValoresPorReferencia(valores);
console.log(valores.valor1, valores.valor2); // Salida: 10 5
console.log(nuevosValores.valor1, nuevosValores.valor2); // Salida: 5 10

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
