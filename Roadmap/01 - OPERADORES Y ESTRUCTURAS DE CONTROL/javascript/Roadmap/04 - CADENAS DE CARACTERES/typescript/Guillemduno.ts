/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 */

console.log("Dentro consola!");

const miFrase: string = "Hay una casa verde.";

/**
 *  charAt() - Devuelve la letra de la posicion indicada.
 */
const posicionA = miFrase.charAt(1);
console.log(`charAt: ${posicionA}`); // a

/**
 * charCodeAt() - Devuelve el valor en format Unicode.
 *
 * Unicode provides a unique number for every character,
 * no matter what the platform,
 * no matter what the program,
 * no matter what the language.
 */
const posicionB = miFrase.charCodeAt(1);
console.log(`charCodeAt: ${posicionB}`); // 97

/**
 * codePointAt() -
 */

const posicionC = miFrase.codePointAt(1);
console.log(`codePointAt: ${posicionC}`); // 97

/**
 * concat() - concatena dos cadenas.
 */

const posicionD = miFrase.concat(miFrase, " El sol se pone.");
console.log(`concat: ${posicionD}`);

/**
 * endsWith() - Devuelve true si la cadena termina con la misma cadena que se le
 * passa en el argumento, sino coincide devuelve false.
 */

const posicionE = miFrase.endsWith("verde.");
console.log(`endsWith: ${posicionE}`); // true

const posicionF = miFrase.endsWith("verdes.");
console.log(`endsWith: ${posicionF}`); // false

/**
 * include () - Devuelve true o false si se encuentra la cadena que se passa como
 * argumento.
 */

const posicionG = miFrase.includes("casa");
console.log(`include: ${posicionG}`); // true

const posicionH = miFrase.includes("casita");
console.log(`include: ${posicionH}`); // false

/**
 * indexOf() - Devuelve la posicion de la primera letra de la cadena que se le
 * passa como argumento.
 */

const posicionI = miFrase.indexOf("casa");
console.log(`indexOf: ${posicionI}`); // 8

/**
 * lastIndexOf() - Devuelve la posicion de la última ocurrencia de la cadena que
 * se pasa como argumento.
 */

const posicionJ = miFrase.lastIndexOf("e");
console.log(`lastIndexOf: ${posicionJ}`); // 17

/**
 * length - Devuelve el total de caracteres que contiene la cadena.
 */

const posicionK = miFrase.length;
console.log(`length: ${posicionK}`); // 19

/**
 * localeCompare() - ?
 */

const posicionL = miFrase.localeCompare("La casa roja.");
console.log(`localeCompare: ${posicionL}`); // -1

const posicionM = miFrase.localeCompare("Hay una casa verde.");
console.log(`localeCompare: ${posicionM}`); // 0

/**
 * match() - Devuelve un objeto con los caracteres encontrados mediante la
 * expresión regular.
 */

const posicionN = miFrase.match(/[a-z]/g);
console.log(`match: ${posicionN}`); //  a,y,u,n,a,c,a,s,a,v,e,r,d,e

/**
 * normalize() - ?
 */

const posicionO = miFrase.normalize();
console.log(`normalize: ${posicionO}`);

/**
 * repeat() - Repite la cadena tantas veces como se indica numericamente en el
 * argumento.
 */

const posicionP = miFrase.repeat(4);
console.log(`repeat: ${posicionP}`);

/**
 * replace() - Sustituye un caracter por otro.
 */

const posicionQ = miFrase.replace("a", "A");
console.log(`replace: ${posicionQ}`);

/**
 * search() - Devuelve la posicion de la primera palabra encontrada.
 * si no encuentra nada devuelve -1.
 *
 * Se le puede passar como argumento una expresion regular /ver/i
 */

const posicionR = miFrase.search("verde");
console.log(`replace: ${posicionR}`); // 13
const posicionRR = miFrase.search("verdes");
console.log(`replace: ${posicionRR}`); // -1
const posicionRRR = miFrase.search(/ver/i);
console.log(`replace: ${posicionRRR}`); // 13

/**
 * slice() - Devuelve un trozo de la cadena.
 */

const posicionS = miFrase.slice(0, 3);
console.log(`slice: ${posicionS}`); // Hay

/**
 * split() - Devuelve un array con los trozos de la cadena separados.
 */

const posicionT = miFrase.split(" ");
console.log(`split: ${posicionT}`);
console.log(posicionT[2]); // casa

/**
 *  startsWith() - Devuelve true o false si la cadena empieza o no con la
 * misma cadena que se le pasa por argumento.
 */
const posicionSs = miFrase.startsWith("Hay");
console.log(`startsWith: ${posicionSs}`); // true
const posicionSss = miFrase.startsWith("Tay");
console.log(`startsWith: ${posicionSss}`); // false

/**
 * substring() - Devuelve una cadena con el trozo de string seleccionado.
 */
const posicionU = miFrase.substring(8, 12);
console.log(`substring: ${posicionU}`); // casa

/**
 * toLocateLowerCase() -
 */

const posicionUu = miFrase.toLocaleLowerCase();
console.log(`toLocateLowerCase: ${posicionUu}`);

/**
 * toLocaleUpperCase() -
 */

const posicionUuu = miFrase.toLocaleUpperCase();
console.log(`toLocaleUpperCase: ${posicionUuu}`);

/**
 * toLowerCase() -
 */

const posicionUuuu = miFrase.toLowerCase();
console.log(`toLowerCase: ${posicionUuuu}`);

/**
 * toString() - Devuelve una cadena.
 */

const posicionV1 = miFrase.toString();
console.log(`toString: ${posicionV1}`);

/**
 * toUpperCase() -
 */

const posicionV = miFrase.toUpperCase();
console.log(`toUpperCase: ${posicionV}`);

/**
 * trim() - Elimina los espacios en blanco de inici i fin.
 */

const posicionV2 = miFrase.trim();
console.log(`trim: ${posicionV2}`);

/**
 * valueOf() - Devuelve el valor primitivo del objeto especificado.
 */

const posicionV3 = miFrase.valueOf();
console.log(`valueOf: ${posicionV3}`);

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 *
 * - Palíndromos: es una palabra o frase que se lee igual en un sentido que en
 *                otro (por ejemplo; Ana, Anna, Otto). Si se trata de números en
 *                lugar de letras, se llama capicúa.
 *
 * - Anagramas: Un anagrama es una palabra que resulta de la transposición de
 *              todas las letras de otra palabra. Dicho de otra forma, una palabra
 *              es anagrama de otra si las dos tienen las mismas letras, con el
 *              mismo número de apariciones, pero en un orden diferente. Esto se
 *              aplica también a grupos de palabras o frases.
 *
 * - Isogramas: Un isograma (del griego isos, 'igual' y gramma, 'letra') es
 *              una palabra o frase en la que cada letra aparece el mismo número
 *              de veces.3​ Si cada letra aparece solo una vez será un heterograma,
 *              si aparece dos, un isogroma de segundo orden y así sucesivamente.
 */

function analizaPalabras(palabra1: string, palabra2: string): void {
  console.log("===========================================================================================");
  console.log(`================ ANALIZADOR DE LAS PALABRAS (${palabra1}) y (${palabra2}) =================`);
  console.log("===========================================================================================");
  // Comprueba si son iguales
  if (palabra1 === palabra2) {
    // validar si és palindromo
    esPalabraPalindromo(palabra2);
    esPalabraAnagrama(palabra1, palabra2);
    esPalabraIsograma(palabra2);

    // Comprueba si tienen la misma longitud
  } else if (palabra1.length === palabra2.length) {
    esPalabraPalindromo(palabra2);
    esPalabraAnagrama(palabra1, palabra2);
    esPalabraIsograma(palabra2);
  } else {
    console.log(`Las palabra '${palabra2}' no tiene la misma longitud que la palabra '${palabra1}'.`);
  }
}

// Comprueba si una palabra és palindromo o no.
function esPalabraPalindromo(palabra: string): boolean {
  for (let index = 0; index < palabra.length; index++) {
    let indexNegativo = palabra.length - 1 - index;
    let letraInicial = palabra[index];
    let letraFinal = palabra[indexNegativo];

    if (letraInicial !== letraFinal) {
      console.log(`${palabra} no és palindromo...`);
      return false;
    }
  }
  console.log(`${palabra} no és un super palindromo!`);
  return true;
}

// Comprueba si una palabra és anagrama.
function esPalabraAnagrama(palabra1: string, palabra2: string): boolean {
  if (palabra1 === palabra2) {
    console.log(`${palabra2} no és una anagrama!`);
    return false;
  }
  // Recorre la primera palabra para ver si la segunda palabra contiene las mismas letras.
  for (let index = 0; index < palabra1.length; index++) {
    let letra = palabra1[index];
    if (!palabra2.includes(letra)) {
      console.log(`${palabra2} no és una anagrama!`);
      return false;
    }
  }
  console.log(`${palabra2} és un super anagrama!`);
  return true;
}

function esPalabraIsograma(palabra: string): boolean {
  for (let index = 0; index < palabra.length; index++) {
    const letra = palabra[index];
    const palabraMenosletra = palabra.replace(letra, "");
    if (palabraMenosletra.includes(letra)) {
      console.log(`${palabra} NO és un isograma...`);
      return false;
    }
  }
  console.log(`${palabra} és un isograma!`);
  return true;
}

// Guarda las dos palabras que introduce el usuario.
const palabra1 = prompt("Escribe una palabra o frase");
const palabra2 = prompt("Escribe otra palabra o frase");

// Si los campos estan llenos ejecutamos el programa para analizar palabras.
if (palabra1 && palabra2) {
  analizaPalabras(palabra1, palabra2);
}
