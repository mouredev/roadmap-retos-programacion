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

// - Sitio oficial del lenguaje Javascript: https://developer.mozilla.org/es/docs/Web/JavaScript

/* - Comentarios */

// Comentario de una sola línea

/*
  Un comentario
  que se extiende
  en varias
  líneas
*/

// - Variable y constantes

let variable = 1;
const constante = 2;

// - Datos primitivos

let miUndefined; // undefined: Un valor primitivo automáticamente asignado a las variables que solo han sido declarados o a los argumentos formales para los cuales no existe argumentos reales.

let miBoolean = false // Boolean: En ciencias de informática, un boolean es un dato lógico que solo puede tener los valores true o false.

let miNumber = 7 //Number: es un tipo de datos numérico

let miString = "Hola Mundo" // String: En cualquier lenguaje de programación, un string es una secuencia de caracteres usado para representar el texto.

let miBigInt = 777n //BigInt: En JavaScript, BigInt es un tipo de dato numerico que puede representar números enteros en el formato de precision arbitrario. En otros lenguajes de programación pueden existir diferentes tipos numéricos, por ejemplo: enteros, flotantes, dobles o bignums (numeros grandes).

let miSimbol = Symbol("key") // Symbol: es un tipo de datos cuyos valores son únicos e immutables. Dichos valores pueden ser utilizados como identificadores (claves) de las propiedades de los objetos.

// - Imprimir por pantalla

console.log("¡Hola, javascript!")
