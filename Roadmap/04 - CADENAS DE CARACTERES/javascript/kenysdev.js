/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#04 CADENAS DE CARACTERES
---------------------------------------
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
*/

// ________________________________________________________
// Declaraciones de cadenas
const str1 = "Esto es una cadena"; // Comillas dobles
const str2 = 'Esto es una cadena'; // Comillas simples
console.log(typeof str2); // "string"

// Salto de línea: \n
const str4 = "Primer linea\nSegunda linea";
console.log(str4);

// ASCII y Unicode
console.log("\u00F1"); // Unicode para 'ñ'

// Texto multilínea
console.log(`Primer linea
Segunda linea
Tercer linea`);

// Longitud de la cadena
const s = "abcdef";
console.log(s.length); // 6

// Acceso a caracteres individuales
console.log(s[1]); // "b"

// Obtener porciones específicas de una cadena
console.log(s.slice(1, 4)); // "bcd"
console.log(s.slice(3)); // "def"

// Revertir una cadena
console.log("abcd".split('').reverse().join(''));

// ________________________________________________________
// Formateo de cadenas:

// Concatenación
const s1 = "hola";
const s2 = "javascript";
console.log(`${s1}, ${s2}`);

// Interpolación
const a = 5, b = 10;
console.log(`Los números son ${a} y ${b}`);

// Replicación o repetición de cadenas
const greeting = "Hola ";
console.log(greeting.repeat(3));

// Valor numérico que representa un carácter y viceversa
console.log(String.fromCharCode(241)); // "ñ"
console.log("ñ".charCodeAt(0)); // 241

// Ordenar caracteres de una cadena
console.log("cdba".split('').sort().join(''));

// ________________________________________________________
// Métodos:

const txt = "Hello, javascript!";
console.log(txt.includes("javascript")); // true
console.log(txt.indexOf("javascript")); // 7
console.log(txt.replace("javascript", "world"));
console.log("mi cadena".charAt(0).toUpperCase() + "mi cadena".slice(1));
console.log("MI CADENA".toLowerCase());
console.log("mI cAdEnA".split('').map(c => c === c.toUpperCase() ? c.toLowerCase() : c.toUpperCase()).join(''));
console.log("mi cadena".toUpperCase());
console.log("mi cadena".split(' ').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' '));

const txt2 = "Cantando y llorando.";
console.log((txt2.match(/ando/g) || []).length); // 2
console.log("aeiou1234".match(/^[a-z0-9]+$/i) !== null); // true
console.log("abcdefg".match(/^[a-z]+$/i) !== null); // true
console.log("12345".match(/^[0-9]+$/) !== null); // true
console.log("abc".toLowerCase() === "abc"); // true
console.log("ABC".toUpperCase() === "ABC"); // true
console.log(/^\s+$/.test("   ")); // true
console.log("  abc  ".trim()); // "abc"
console.log("123".padStart(5, '0')); // "00123"
console.log(["1", "2", "3"].join(" y ")); // "1 y 2 y 3"
console.log("a,b,c".split(",")); // ["a", "b", "c"]

// ________________________________________________________
// DIFICULTAD EXTRA

function analyze(str1, str2) {
    const esPalindromo = str => str === str.split('').reverse().join('');
    const esAnagrama = (str1, str2) => str1.split('').sort().join('') === str2.split('').sort().join('');
    const esIsograma = str => new Set(str).size === str.length;

    console.log(`\n    "${str1}" es un palíndromo?: ${esPalindromo(str1)}
    "${str2}" es un palíndromo?: ${esPalindromo(str2)}

    "${str1}" es un anagrama de "${str2}"?: ${esAnagrama(str1, str2)}

    "${str1}" es un isograma?: ${esIsograma(str1)}
    "${str2}" es un isograma?: ${esIsograma(str2)}\n`);
}

analyze("reconocer", "vida");
analyze("notas", "santo");
analyze("héroe", "radar");
