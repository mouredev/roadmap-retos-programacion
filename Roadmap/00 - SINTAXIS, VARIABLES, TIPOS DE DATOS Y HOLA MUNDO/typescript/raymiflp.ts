// Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado. 

// https://www.typescriptlang.org/

// Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...). 

// comentario una linea

/*
comentario de varias lineas
*/

// Crea una variable (y una constante si el lenguaje lo soporta).

let variable:string = "esto es una variable"

const constante:string ="esto es una constante"

// Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).

const tipo1:string = "hola" //tipo de dato string
const tipo2:number = 123 //tipo de dato number
const tipo3:boolean = true //tipo de dato booleano
const tipo4:bigint = 312345678901234567890n //tipo de dato bigint
const tipo5:symbol = Symbol("id") //tipo de dato symbol
const tipo6:undefined = undefined //tipo de dato undefined
const tipo7:null = null //tipo de dato null


// Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
const lenguaje:string = "TypeScript"

console.log(`¡Hola, ${lenguaje}!`);