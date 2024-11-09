/* 1- Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.*/
//https://www.typescriptlang.org/

/* 2- Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).*/
//Inicio del TSDoc, TSDoc is a proposal to standardize the doc comments used in TypeScript code e.g.:
export class Statistics {
    /**
     * Returns the average of two numbers.
     *
     * @remarks
     * This method is part of the {@link core-library#Statistics | Statistics subsystem}.
     *
     * @param x - The first input number
     * @param y - The second input number
     * @returns The arithmetic mean of `x` and `y`
     *|
     * @beta
     */
    public static getAverage(x: number, y: number): number {
      return (x + y) / 2.0;
    }
  }
//Final del TSDoc

/*
Multilinea con este tipo de comentarios podemos agregar muchos saltos de linea

Sin preocuparnos de seguir especificando que la linea actual es un comentario
*/

/* 3- Crea una variable (y una constante si el lenguaje lo soporta).*/
var isDone: boolean = true;
const num:number = 10;

/* 4- Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...). */
//Numbers
let decimal: number = 6;
let hex: number = 0xf00d;
let binary: number = 0b1010;
let octal: number = 0o744;
let big: bigint = 900719925474n;

//Strings
let color: string = "blue";
color = 'red';
let lenguaje: string = "Typescript"

//Boolean
let isTrue: boolean = true;

/* 5- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!*/
console.log(`¡Hola, ${lenguaje}!`)