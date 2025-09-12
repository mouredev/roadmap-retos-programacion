// Realizado con https://www.typescriptlang.org/

// Comentarios
// Comentario de línea
/*
Comentario de bloque
*/

// Variables
// var, let, const
var variable_var = "Una variable";
let variable_let = "Una variable";
const CONSTANTE = "Una constante";

// Tipos de datos
// number, string, boolean, any, void, null, undefined, never, object
const numero: number = 1;
const cadena: string = "TypeScript";
const booleano: boolean = true;
const cualquier_cosa: any = "Cualquier cosa";
const nada: void = undefined;
const nulo: null = null;
const indefinido: undefined = undefined;
const objeto: object = {};

// Arrays
const arreglo: number[] = [1, 2, 3];
const otro_arreglo: Array<number> = [1, 2, 3];

// Tuplas
const tupla: [number, string] = [1, "Hola"];

// Enumeración
enum Color {
  Rojo,
  Verde,
  Azul,
}

const color: Color = Color.Rojo;

console.log(`¡Hola, ${cadena}`);
document.write(`¡Hola, ${cadena}`);
