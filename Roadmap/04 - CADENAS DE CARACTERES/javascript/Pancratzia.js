/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */


/***********OPERACIONES CON CADENAS - PARTE 1*************/

/******* IMPORTANTE
 * 
 * Todos los metodos retornan una nueva cadena, no modifican la cadena original a menos que se indique lo contrario
 * 
********/

const stringExample = 'Hello, Javascript!';

//LARGO DE LA CADENA

console.log(`La cadena "${stringExample}" tiene ${stringExample.length} caracteres.`);

//EXTRACCIÓN DE CARACTERES DE UN STRING

console.log(`at(n) - ${stringExample}.at(1) es la letra "${stringExample.at(1)}".`);
console.log(`charAt(n) - ${stringExample}.charAt(1) es la letra "${stringExample.charAt(1)}".`);

//La diferencia entre at() y charAt() es que at() permite usar indexes negativos

console.log(`charCodeAt(n) - ${stringExample}.charCodeAt(1) es la letra "${stringExample.charCodeAt(1)}".`); //Devuelve el valor ASCII del caracter

console.log(`También se puede acceder a un caracter como si fuese un array`)
console.log(`string[n] - ${stringExample}[1] es la letra "${stringExample[1]}".`);

//EXTRAYENDO PARTES DE UN STRING

console.log(`slice(n,m) - ${stringExample}.slice(0,5) es la cadena "${stringExample.slice(0,5)}".`); //Si no se coloca el segundo argumento, toma hasta el final de la cadena
console.log(`substring() - ${stringExample}.substring(0,5) es la cadena "${stringExample.substring(0,5)}".`); //Si no se coloca el segundo argumento, toma hasta el final de la cadena

//La diferencia entre slice() y substring() es que slice() puede tomar negativos

console.log(`substr(n,m) - ${stringExample}.substr(0,5) es la cadena "${stringExample.substr(0,5)}".`); //Si no se coloca el segundo argumento, toma hasta el final de la cadena

//Está deprecado. Se recomienda usar substring() o substr(). El segundo argumento indica la longitud de la subcadena.

//CONVERSION A MAYÚSCULAS Y MINÚSCULAS

console.log(`toUpperCase() - ${stringExample}.toUpperCase() es la cadena "${stringExample.toUpperCase()}".`);
console.log(`toLowerCase() - ${stringExample}.toLowerCase() es la cadena "${stringExample.toLowerCase()}".`);

//CONCATENACION

const string1 = 'Fizz';
const string2 = 'Buzz';

console.log(`concat() - ${string1}.concat(${string2}) es la cadena "${string1.concat(string2)}".`);
console.log(`+ - ${string1}+${string2} es la cadena "${string1+string2}".`);

//TRIM - Elimina espacios al principio y al final de una cadena

const trimStringExample = "          Hello, Javascript!          ";

console.log(`trim() - ${trimStringExample}.trim() es la cadena "${trimStringExample.trim()}".`);
console.log(`trimStart() - ${trimStringExample}.trimStart() es la cadena "${trimStringExample.trimStart()}".`);
console.log(`trimEnd() - ${trimStringExample}.trimEnd() es la cadena "${trimStringExample.trimEnd()}".`);

//PADDING - Rellena una cadena con un caracter

let text = "5";
let padded = text.padStart(3,"x");

console.log(`padStart() - ${text}.padStart(4,"x") es la cadena "${padded}".`);
console.log(`padEnd() - ${text}.padEnd(4,"x") es la cadena "${text.padEnd(4,"x")}".`);

//REPETICION

console.log(`repeat() - ${stringExample}.repeat(3) es la cadena "${stringExample.repeat(3)}".`);

//REEMPLAZO

console.log(`replace() - ${stringExample}.replace("Javascript","JS") es la cadena "${stringExample.replace("Javascript","JS")}".`);
console.log(`replaceAll() - ${stringExample}.replaceAll("Javascript","JS") es la cadena "${stringExample.replaceAll("Javascript","JS")}".`);

//La diferencia entre replace() y replaceAll() es que replace() reemplaza la primera coincidencia, mientras que replaceAll() reemplaza todas las coincidencias.

//CONVERSION A ARRAY

const textToSplit = new String("Hello|,|Javascript!");

console.log(`split() - ${textToSplit}.split("|") es el array "${textToSplit.split("|")}".`);

//El split() separa la cadena en un array de caracteres dado un separador

/***********OPERACIONES CON CADENAS - EXTRA***************/