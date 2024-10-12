/* - Sin parámetros ni retorno, con uno o varios parámetros, con retorno... - */
// Función anónima autoejecutable
(function () {
  console.log("Hola Mundo");
})(); // Hola Mundo

// Función anónima
const funcionAnonima = function() {
  console.log("Hola Mundo");
};
funcionAnonima(); // Hola Mundo

// Función declarativa sin retorno
function funcionSinRetorno(): void {
  console.log("Hola Mundo");
}
funcionSinRetorno(); // Hola Mundo

// Función declarativa con retorno
function funcionConParametro(name: string): void {
  console.log(`Hola ${name}`);
}
funcionConParametro("Miquel"); // Hola Miquel

// Función declarativa con varios parámetros
function funcionConVariosParametros(
  firstName: string, 
  lastName: string
): void {
  console.log(`Hola ${firstName} ${lastName}`);
}
funcionConVariosParametros("Miquel", "Roset"); // Hola Miquel Roset

// Función expresada con retorno
function funcionConRetorno(a: number, b: number): number {
  return a + b;
}
funcionConRetorno(5, 5); // 10

// Función con parámetros opcionales
function funcionConParametrosOpcionales(a: number, b?: number): number {
  return b ? a + b : a;
}
funcionConParametrosOpcionales(5); // 5
funcionConParametrosOpcionales(5, 5); // 10

// Función con parámetros de tipo rest
function funcionConParametrosRest(a: number, ...b: number[]): number {
  return a + b.reduce((total, current) => total + current, 0);
}
funcionConParametrosRest(5, 1, 2, 3, 4, 5); // 15

// Función con parámetros de tipo rest y parámetros opcionales
function funcionConParametrosRestOpcionales(
    a: number, c?: number, ...b: number[]
): number {
  return a + b.reduce((total, current) => total + current, 0) + (c || 0);
}
funcionConParametrosRestOpcionales(5, undefined, 1, 2, 3, 4, 5); // 20
funcionConParametrosRestOpcionales(5, 10, 1, 2, 3, 4, 5); // 25

// Función flecha
const funcionFlecha = (a: number, b: number): number => a + b;
funcionFlecha(5, 5); // 10

// Función con callbacks
function funcionConCallbacks(
  a: number, 
  b: number, 
  callback: (a: number, b: number) => number
): number {
  return callback(a, b);
}
funcionConCallbacks(5, 5, (a, b) => a + b); // 10


/* ----------- Funciones dentro de funciones (o de orden superior) ---------- */
function ordenSuperior(): void {
  function funcionDentro(): void {
    console.log("Hola Mundo");
  }
  funcionDentro();
}
ordenSuperior(); // Hola Mundo


/* ---------------- Funciones ya creadas por el lenguaje -------------------- */
function creadasPorLenguaje(): void {
  console.log("Hola Mundo");
  alert("Hola Mundo");
  prompt("Hola Mundo");
  confirm("Hola Mundo");
}
creadasPorLenguaje(); // Hola Mundo, Hola Mundo, Hola Mundo, Hola Mundo


/* -------------------- Variable local y variable global -------------------- */
let variableGlobal: string = "Hola Mundo Global";

function funcionConVariableLocal(): void {
  let variableLocal: string = "Hola Mundo Local";
  console.log(variableLocal); // Hola Mundo Local
  console.log(variableGlobal); // Hola Mundo Global
}
funcionConVariableLocal(); // Hola Mundo Local, Hola Mundo Global

console.log(variableLocal); // ReferenceError: variableLocal is not defined


// -------------------------- BONUS EJERCICIO ------------------------------- //

/*
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne 
 * un número.
 * 
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer 
 *     parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo 
 *     parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto 
 *     concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en 
 *     lugar de los textos.
 * 
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los 
 * casos. Cada lenguaje sigue una convenciones que debes de respetar para que el 
 * código se entienda.
 */

function bonus(a: string, b: string): number {
  let count: number = 0;
  for (let i: number = 1; i <= 100; i++) {
    if (i % 3 === 0) {
      console.log(a);
    } else if (i % 5 === 0) {
      console.log(b);
    } else if (i % 3 === 0 && i % 5 === 0) {
      console.log(a + b);
    } else {
      console.log(i);
      count++;
    }
  }
  return count;
}
bonus("Miquel", "Roset"); // 100
