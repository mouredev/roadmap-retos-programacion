/* -------------------------- ASIGNACIÓN POR VALOR -------------------------- */
/* 
 * Esto aplica a todos los tipos de datos primitivos (números, cadenas, 
 * booleanos, null, undefined, symbol y bigInt)
 */
let number1: number = 5;
let number2: number = number1;  // Se copia el valor de 'number1' en 'number2'

console.log(number1); // 5
console.log(number2); // 5

// Ahora cambiamos el valor de 'number1'
number1 = 10;

console.log(number1); // 10
console.log(number2); // 5


/* ----------------------- ASIGNACIÓN POR REFERENCIA ------------------------ */
/* 
 * Esto aplica a los tipos de datos: objetos, arrays, funciones, clases, 
 * instancias de clases, etc.
 */
let object1 = { nombre: 'Juan' };
let object2 = object1;  // Se asigna la referencia de 'object1' a 'object2'

console.log(object1); // { nombre: 'Juan' }
console.log(object2); // { nombre: 'Juan' }

// Ahora cambiamos el valor de 'nombre' en 'object1'
object1.nombre = 'Pedro';

console.log(object1); // { nombre: 'Pedro' }
console.log(object2); // { nombre: 'Pedro' }


/* ------------------------- COPIAR OBJETOS Y ARRAYS ------------------------ */
// Spread para copiar objetos
let originalObject = { nombre: 'Ana' };
let copiedObject = { ...originalObject };
copiedObject.nombre = 'Maria';

console.log(originalObject); // { nombre: 'Ana' }
console.log(copiedObject); // { nombre: 'Maria' }

// Object.assign() para copiar objetos
let originalObject2 = { nombre: 'Carlos' };
let copiedObject2 = Object.assign({}, originalObject2);
copiedObject2.nombre = 'Roberto';

console.log(originalObject2); // { nombre: 'Carlos' }
console.log(copiedObject2); // { nombre: 'Roberto' }


// Array.slice() o Array.from() para copiar arrays
let originalArray = [1, 2, 3];
let copiedArray = originalArray.slice();
copiedArray.push(4);

console.log(originalArray); // [1, 2, 3]
console.log(copiedArray); // [1, 2, 3, 4]


/*
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como 
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, 
 *   por referencia. Estos parámetros los intercambia entre ellos en su 
 *   interior, los retorna, y su retorno se asigna a dos variables diferentes a 
 *   las originales. A continuación, imprime el valor de las variables 
 *   originales y las nuevas, comprobando que se ha invertido su valor en las 
 *   segundas. Comprueba también que se ha conservado el valor original en las 
 *   primeras.
 */

// Por valor
const number2_1: number = 5;
const number2_2: number = 10;

function swapPorReferencia(param1: number, param2: number): [number, number] {
  let temp = param1;
  param1 = param2;
  param2 = temp;
  return [param1, param2];
}

let [newNumber1, newNumber2]: [number, number] = swapPorReferencia(
  number2_1, 
  number2_2
);
console.log("Valor inicial 1", number2_1); // 5
console.log("Valor inicial 2", number2_2); // 10
console.log("Valor final 1", newNumber1); // 10
console.log("Valor final 2", newNumber2); // 5


// Por referencia
type Persona = { nombre: string };
let object2_1: Persona = { nombre: "Juan" };
let object2_2: Persona = { nombre: "Pedro" };

// Antes de llamar a la función pintamos los valores iniciales
console.log("Valor inicial objeto 1", object2_1); // { nombre: "Pedro" }
console.log("Valor inicial objeto 2", object2_2); // { nombre: "Juan" }

function swapPorReferencia2(a: Persona, b: Persona): void {
  let tempNombre = a.nombre;
  a.nombre = b.nombre;
  b.nombre = tempNombre;
}

swapPorReferencia2(object2_1, object2_2);

// Después de llamar a la función pintamos los valores finales
console.log("Valor final objecto 1", object2_1); // { nombre: "Pedro" }
console.log("Valor final objeto 2", object2_2); // { nombre: "Juan" }
