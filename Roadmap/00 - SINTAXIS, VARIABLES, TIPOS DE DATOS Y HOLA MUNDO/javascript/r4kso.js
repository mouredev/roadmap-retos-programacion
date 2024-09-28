// 00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO

/*
  EJERCICIO:
  - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
  - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
  - Crea una variable (y una constante si el lenguaje lo soporta).
  - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
  - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
*/

/* --------------------------------*/

// - Sitio oficial del lenguaje JavaScript: https://developer.mozilla.org/en-US/docs/Web/javascript

/* COMENTARIOS:
    -> // Comentario de una sola línea
    -> /*
        Comentario
        de
        múltiples
        líneas
       */

// VARIABLES Y CONSTANTES
let variable = 69
const constant = 13

// DATOS PRIMITIVOS
// 1. Undefined: Es una manera de representar la ausencia de un valor
let undefinedAux;

// 2. Null: Quiere decir que tenemos un valor nulo y es otra manera de representar la ausencia de un valor
const nullAux = null

// 3. Number: Todos los valores que representan un número, tanto enteros como racionales
const numberAux = 3

// 4. String: Datos en formato texto (Cadena de caracteres)
const stringAux = "Esto es un string"

// 5. Boolean: Aquellos valores que se representan como verdadero/falso (1/0)
const booleanAux = true

// 6. BigInt: Permite representar números muy grandes
const bigIntAux = 1234783n

// 7. Symbol: Incluye un constructor que devuelve un symbol primitivo cuyo valor está garantizado que es único. Se suelen usar para añadir claves únicas a objetos
const symbolAux = Symbol("key")

// IMPRIMIR POR PANTALLA
console.log("¡Hola, JavaScript!")