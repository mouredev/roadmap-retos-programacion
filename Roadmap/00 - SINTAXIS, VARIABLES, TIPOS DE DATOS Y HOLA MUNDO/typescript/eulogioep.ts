// URL del sitio web oficial de TypeScript
// https://www.typescriptlang.org/

// Diferentes formas de crear comentarios en TypeScript:

// 1. Comentario de una línea

/*
   2. Comentario 
   de varias 
   líneas
*/

/**
 * 3. Comentario de documentación
 * Usado frecuentemente para describir funciones, clases e interfaces
 */

// Creación de una variable con tipo inferido
let miVariable = "Soy una variable";

// Creación de una constante con tipo explícito
const MI_CONSTANTE: string = "Soy una constante";

// Variables representando tipos de datos en TypeScript

// String (cadena de texto)
let cadena: string = "Hola, mundo";

// Number (número)
let entero: number = 42;
let decimal: number = 3.14;

// Boolean (booleano)
let verdadero: boolean = true;
let falso: boolean = false;

// Undefined (indefinido)
let indefinido: undefined = undefined;

// Null (nulo)
let nulo: null = null;

// Symbol (símbolo)
let simbolo: symbol = Symbol("descripción");

// BigInt (entero grande)
let enteroGrande: bigint = BigInt(9007199254740991);

// Any (cualquier tipo)
let cualquiera: any = "Puedo ser cualquier cosa";

// Unknown (desconocido)
let desconocido: unknown = 4;

// Void (vacío, típicamente para funciones sin retorno)
function sinRetorno(): void {
    console.log("Esta función no retorna nada");
}

// Never (nunca, para funciones que nunca retornan)
function error(mensaje: string): never {
    throw new Error(mensaje);
}

// Tuple (tupla)
let tupla: [string, number] = ["hola", 42];

// Enum (enumeración)
enum Color {
    Rojo,
    Verde,
    Azul
}

// Imprimir por terminal
console.log("¡Hola, TypeScript!");