//https://www.typescriptlang.org/


// Declaración de variables con tipos de datos

/** comentar un documento 
 * multilinea de comentarios en TypeScrpt
 * puedo seguir escribiendo
 */
//comentar una sola linea

/*
comentar varias lineas
en TypeScript	
*/
//number

let edad: number = 25;
//declarar una constante
const edad3: number = 30;

// Cadena de texto
const nombre: string = "Juan";

// Booleano
const esEstudiante: boolean = true;
// Arreglo de números

// Tupla
let persona: [string, number] = ["Juan", 25];

// Enumeración
enum Color {
    Rojo,
    Verde,
    Azul
}
let colorFavorito: Color = Color.Verde;

// Any (puede ser cualquier tipo de dato)
let variableIndefinida: any = "Hola";
variableIndefinida = 10;

// Void (usualmente para funciones que no retornan valor)
function saludar(): void {
    console.log("Hola, mundo!");
}

// Null y Undefined
let variableNula: null = null;
let variableIndefinida2: undefined = undefined;

// Object
let personaObj: { nombre: string, edad: number } = { nombre: "Juan", edad: 25 };

console.log('Hola TypeScript!');


