/**
 * Operaciones con cadenas de caracteres en TypeScript
 */

// Creacion de cadena de caracteres
let cadena: string = "Nueva cadena de caracteres";
console.log(cadena);

// Templates literales
let numero: number = 12;
let cadenaConVariables: string = `El numero es: ${numero}`;
console.log(cadenaConVariables);

// Concatenacion
let stringConcatenado: string = "Hola " + "Mundo!";
console.log(stringConcatenado);

// Acceso a caracter especifico
//Indice => Los indices en TypeScript comienzan desde 0
let accesoACaracter: string = stringConcatenado[1];
console.log(accesoACaracter);

// Propiedades y metodos de cadena
// length => Devuelve la longitud de la cadena
let cadenaLongitud: number = cadena.length;
console.log(cadenaLongitud);

// toUppercase() => Convierte la cadena a mayúsculas
let cadenaAMayusculas: string = cadena.toUpperCase();
console.log(cadenaAMayusculas);

// toLowerCase() => Convierte la cadena a minúsculas
let cadenAMinusculas: string = cadena.toLowerCase();
console.log(cadenAMinusculas);

// indexOf() => Devuelve el índice de la primera aparición de una subcadena en la cadena
let indice: number = cadena.indexOf("cadena");
console.log(indice); // devuelve -1 si no lo encuentra, si lo enc

// lastIndexOf() => Devuelve el índice de la última aparición de una subcadena en la cadena
let ultimoIndice: number = cadena.lastIndexOf("cadena"); // devuelve -1 si no lo encuentra, si lo encuentra devuelve el último índice
console.log(ultimoIndice);

// slice() => Devuelve una subcadena de la cadena
let subcadena: string = cadena.slice(0, 5); // devuelve "Nueva"
console.log(subcadena);

// charAt() => Devuelve el carácter en la posición especificada
let caracterEnPosicion: string = cadena.charAt(5); // devuelve "c"
console.log(caracterEnPosicion);

/**
 * Programa con dificultad extra: Analisis de palabras
 */

let palindroma: string = "radar";
let anagrama: string = "adram";
let isograma: string = "estrla";

// Verificando si una palabra es palindroma
function esPalindroma(palabra: string): boolean {
    let sinEspacios: string = palabra.replace(/\s/g, "").toLowerCase(); // Convertimos a minusculas y quitamos los espacios
    return sinEspacios === sinEspacios.split("").reverse().join(""); // Comparamos con la versión invertida, si son iguales devuelve true
}

function esAnagrama(palabra: string, otraPalabra: string): boolean {
    let sinEspacios: string = palabra.replace(/\s/g, "").toLowerCase(); // Convertimos a minusculas y quitamos los espacios
    let otraSinEspacios: string = otraPalabra.replace(/\s/g, "").toLowerCase(); // Convertimos a minusculas y quitamos los espacios
    return sinEspacios.split("").sort().join("") === otraSinEspacios.split("").sort().join(""); // Comparamos los arrays ordenados, si son iguales devuelve true
}

function esIsograma(palabra: string): boolean {
    let sinEspacios: string = palabra.replace(/\s/g, "").toLowerCase(); // Convertimos a minusculas y quitamos los espacios
    return new Set(sinEspacios).size === sinEspacios.length; // Comparamos el tamaño del Set con la longitud de la cadena, si son iguales devuelve true
}

console.log(`Palindroma: ${esPalindroma(palindroma)}`); // true
console.log(`Anagrama: ${esAnagrama(anagrama, palindroma)}`); // false
console.log(`Isograma: ${esIsograma(isograma)}`); // true (porque no contiene caracteres repetidos)