// Documentación de JavaScript (no oficial): https://es.javascript.info

/*
    En JavaScript y en otros lenguajes de programación usamos los comentarios para poder explicar cómo funciona nuestro código.

    No tienen ninguna función más que la de explicar el código a otras personas o a nosotros mismos.

    Hay dos tipos de comentarios en JavaScript:
    - Comentarios de una sola línea: Se crean con // y todo lo que escribamos después de las dos barras será un comentario.
    - Comentarios de varias líneas: Se crean con /* y se cierran con * / (sin el espacio entre el asterisco y la barra) y todo lo que escribamos entre ellos será un comentario.
\*/

// Variables: Es un nombre simbólico que se le da a un espacio de memoria que almacena un valor. Normalmente el espacio para almacenar el valor ocurre en la memoria RAM.
/*
    El proceso para reservar el espacio en memoria inicia con la declaración de la variable, luego la asignación y por último el acceso a ese valor asignado.
*/

/*
    En JavaScript se pueden declarar variables de tres formas:
    - var: Es la forma antigua de declarar variables. No se recomienda su uso (Hay excepciones).
    - let: Es la forma moderna de declarar variables. Se recomienda su uso.
    - const: Es la forma de declarar constantes. No se puede cambiar su valor una vez asignado.
*/

/*
La diferencia entre var y let y const es el alcance de la variables. var tiene un alcance de función, let y const tienen un alcance de bloque.
*/
var antigua = 'Soy una variable antigua';
let moderna = 'Soy una variable moderna';
const CONSTANTE = 'Soy una constante';

// Tipos de datos:
let n = 123;
let n2 = 12.345;
let n3 = 1 / 0; // Infinity (Infinito) también el -Infinity y el NaN (Not a Number)

// BigInt: Es un tipo de dato numérico que puede representar números enteros de longitud arbitraria.
const bigInt = 1234567890123456789012345678901234567890n; // Se declara con la letra n al final del número.

let str = 'Hola'; // Las cadenas de texto se declaran con comillas simples, dobles o con comillas invertidas.

let boolean = true; // Los valores booleanos son true (verdadero) y false (falso).

let nullValue = null; // null es un valor especial que no pertenece a ningún tipo de dato.

let undefinedValue = undefined; // undefined es un valor especial que significa que la variable no está asignada.

let simbolo = Symbol('Simbolo'); // Symbol es un tipo de dato que se utiliza para crear identificadores únicos.

let obj = {
  nombre: 'Andres',
  edad: 21,
}; // Los objetos son colecciones de datos y/o funcionalidades.

let array = [1, 2, 3, 4, 5]; // Los arrays son colecciones de datos.

// ps: En JavaScript todo lo que no sea un tipo de dato primitivo es un objeto.

console.log('¡Hola, JavaScript!');
