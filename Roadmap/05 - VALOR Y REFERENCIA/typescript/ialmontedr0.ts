/**
 * Asignacion de variables por valor
 */

let cadenaPorValor: string = "Cadena original";
cadenaPorValor = "Cadena modificada";

let numeroPorValor: number = 10;
numeroPorValor = 20;

let arregloPorValor: number[] = [1, 2, 3];
arregloPorValor[0] = 4;

let objetoPorValor: { nombre: string; edad: number } = {
  nombre: "Anthony",
  edad: 26,
};
objetoPorValor.nombre = "Hector";

let undefinedPorValor: undefined | null = undefined;
undefinedPorValor = null;

let symbolPorValor: symbol = Symbol("Simbolo");
symbolPorValor = Symbol("Simbolo modificado");

let tuplaPorValor: [string, number, boolean] = ["Cadena", 10, true];
tuplaPorValor[0] = "Cadena modificada";

console.log(`
    Variables por valor:
    - Cadena: ${cadenaPorValor}
    - Número: ${numeroPorValor}
    - Arreglo: ${arregloPorValor.join(", ")}
    - Objeto: ${JSON.stringify(objetoPorValor)}
    - Undefined: ${undefinedPorValor}
    - Simbolo: ${symbolPorValor}
    - Tupla: ${JSON.stringify(tuplaPorValor)}
`);

/**
 * Asignacion de variables por referencia
 */

let objetoPorReferencia: { nombre: string; edad: number } = {
  nombre: "Anthony",
  edad: 26,
};
let objetoPorReferencia2: { nombre: string; edad: number } =
  objetoPorReferencia;

objetoPorReferencia2.edad = 27;

console.log(`
    Variables por referencia:
    - Objeto original: ${JSON.stringify(objetoPorReferencia)}
    - Objeto modificado: ${JSON.stringify(objetoPorReferencia2)}
    `);

/**
 * Funciones con variables por valor
 */

// Funcion que recibe dos parametros y devuelve una suma
function sumaPorValor(valorA: number, valorB: number): number {
  valorA += valorB; // Esta linea modifica el valor de valorA en la función
  return valorA; // Retorna el valor modificado de valorA
}

sumaPorValor(5, 10); // Llama a la función con valores por valor

/**
 * Funciones con variables por referencia
 */

// Funcion que recibe dos parametros y los modifica en ellos
function sumaPorReferencia(valorA: number, valorB: number): void {
  valorA += valorB; // Esta linea modifica el valor de valorA en la función
  valorB = 0; // Esta linea modifica el valor de valorB en la función
  console.log(`
        Variables modificadas en la función:
        - Valor A: ${valorA}
        - Valor B: ${valorB}
    `);
}

sumaPorReferencia(5, 10); // Llama a la función con valores por referencia

/**
 * Ejercicio extra (intercambio de variables)
 */

function ejercicioUnoExtra(valor1: number, valor2: number): void {
  let temp: number = valor1; // Asigna el valor de valor1 a una variable temporal
  valor1 = valor2; // Asigna el valor de valor2 a valor1
  valor2 = temp; // Asigna el valor de la variable temporal a valor2
  console.log(`
        Variables intercambiadas en el ejercicio extra:
        - Valor 1: ${valor1}
        - Valor 2: ${valor2}
    `);
  // Comprueba que se ha intercambiado el valor de los parámetros
  console.log(`
        Variables originales en el ejercicio extra:
        - Valor 1: ${valor1}
        - Valor 2: ${valor2}
    `);
}

function ejercicioDosExtra(valor1: number, valor2: number): void {
  let temp: number = valor1; // Asigna el valor de valor1 a una variable temporal
  valor1 = valor2; // Asigna el valor de valor2 a valor1
  valor2 = temp; // Asigna el valor de la variable temporal a valor2
  console.log(`
        Variables intercambiadas en el ejercicio extra:
        - Valor 1: ${valor1}
        - Valor 2: ${valor2}
    `);
  // Comprueba que se ha conservado el valor original de los parámetros
  console.log(`
        Variables originales en el ejercicio extra:
        - Valor 1: ${valor1}
        - Valor 2: ${valor2}
    `);
}

ejercicioUnoExtra(10, 20); // Llama al ejercicio con variables por valor
ejercicioDosExtra(10, 20); // Llama a los ejercicios con variables por referencia
