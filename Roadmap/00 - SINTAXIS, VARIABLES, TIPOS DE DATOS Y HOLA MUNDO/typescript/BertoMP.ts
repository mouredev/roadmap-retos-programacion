// WEB OFICIAL
// Para encontrar información sobre TypeScript, se puede utilizar la web:
// https://www.typescriptlang.org/

// COMENTARIOS
// En TypeScript existen tres tipos de comentarios:
// - Comentarios de una única línea (// Comentario):
// Esto es un comentario de una línea y puede servir, por ejemplo, para explicar una variable.

// - Comentarios de varias líneas (/* Comentario */):
/* Esto es un comentario
 * de varias líneas y puede
 * servir para explicar una parte
 * más extensa del código. */

// - Comentarios de documentación (/** Comentario */):
/**
 * Este tipo de comentarios nos van a servir para documentar
 * nuestro código y van a permitir la generación de documentación
 * automática llamada TSDoc que facilita la comprensión
 * y el mantenimiento del código.
 * Al igual que pasa con otros lenguajes, pueden ir acompañados
 * de etiquetas como @param o @return que identifican valores
 * como los parámetros de entrada de la función o el valor de
 * retorno que produce la función. */

// VARIABLES Y CONSTANTES
/* - Variables: En TypeScript, se puede declarar una variable utilizando 'let' o 'var' seguido del nombre de la
                variable, dos puntos (:), el tipo de dato y el valor asignado.
                La declaración con 'var' se considera obsoleta y su uso no se recomienda ampliamente. */
var miVariableVar: number = 12;
let miVariableLet: number = 33;

/* - Constantes: Para declarar constantes en TypeScript, utilizamos la palabra clave 'const'. Similar a las variables,
                 las constantes deben tiparse al momento de la declaración. Se fomenta la inmutabilidad en el
                 código TypeScript mediante el uso de constantes. */
const miConstante: string = 'Alberto';

// DATOS PRIMITIVOS
//En TypeScript, los tipos de datos primitivos son los siguientes:
const miString: string = "Esto es un string"; // string: Sirve para almacenar cadenas de texto.
const miNumberEntero: number = 40; // number: Sirve para almacenar datos de tipo numérico, ya sean enteros o decimales.
const miNumberDecimal: number = 23.4;
const miBigInt: bigint = 123456789012345678901234567890n; /* bigint: Es otro tipo de dato numérico que permite
                                                                     representar enteros más grandes que el tipo
                                                                     'number'. Se define agregando la letra "n" al
                                                                     final del número seguido de "n". */
const miBoolean: boolean = true; // boolean: Representa un valor lógico, verdadero o falso.
let miUndefined: undefined; // undefined: Indica que una variable ha sido declarada pero no tiene un valor asignado.
const miSymbol: symbol = Symbol('mi Symbol'); // symbol: Tipo de dato cuyas instancias son únicas e inmutables.
// También existe el null que aunque puede tomarse como primitivo, en realidad es propio de cada Object.

// IMPRESIÓN POR CONSOLA
console.log('¡Hola, TypeScript!');