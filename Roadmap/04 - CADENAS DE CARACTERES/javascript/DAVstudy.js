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

let myString = "Hola! JavaScript";

// Acceso
console.log(myString[0]);
console.log(myString[1]);
console.log(myString[2]);

// at() retorna el caracter del indice indicado
console.log(myString.at(-1));

// Subcadenas
console.log(myString.substring(0, 8));

// Longitud
console.log(myString.length);

// Concatenacion

let name = "Diego";
let lastname = "Arenas";
let fullname = name.concat(" ", lastname);

console.log(fullname);

// Repeticion
console.log(name.repeat(10));

// Recorrer un string
for (let i = 0; i < myString.length; i++) {
  console.log(myString[i]);
}

// Conversion mayus y minus
console.log(myString.toUpperCase());
console.log(myString.toLowerCase());

// Reemplazar
console.log(myString.replace("javascript", "JavaScript")); // Reemplaza la primera palabra que coincida con lo indicado pero solo esa
console.log(myString.replaceAll("a", "!")); // Reemplaza todos los caracteres que coinciden

// Split
const words = myString.split(" "); // devolvera un array, separarando elementos dado el string que se indicque
console.log(words);

// Splice
let newString = myString.slice(3, -3); // El método slice() extrae una sección de una cadena y devuelve una cadena nueva.
console.log(newString);

// template literal
console.log(`Mi nombre es ${name}`);

// Verificacion

// Busqueda

// search
console.log(myString.search(/[aeiouáéíóú]/)); // sirve para buscar expresiones regulares si encuentra una coincidencia retorna el indice, si no -1

// includes
console.log(myString.includes("la")); // Retorna true si incluye y false en caso contrario

// indexOf
console.log(myString.indexOf("Java")); // Retorna el indice de una subcadena literal

// lastIndexOf
console.log(myString.lastIndexOf("Java")); // Retorna el indice de una subcadena literal buscando desde el final hacia el inicio

// match
const regex = /[A-Z]/g;
const found = myString.match(regex); // devolvera un arrai con todas las expreciones regulares indicadas, en este caso todas las mayusculas
console.log(found);

// matchAll
// El método matchAll() retorna un iterador de todos los resultados de ocurrencia en una cadena de texto contra una expresión regular, incluyendo grupos de captura.
const regexp = /t(e)(st(\d?))/g;
const str = "test1test2";

const array = [...str.matchAll(regexp)];

console.log(array[0]);
// Expected output: Array ["test1", "e", "st1", "1"]

console.log(array[1]);
// Expected output: Array ["test2", "e", "st2", "2"]

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */


const AnalizeWords = {
  reverseString: (str) => str.split("").reverse().join(""),
  sortString: (str) => str.split("").sort().join(""),
  isIsogram: function (str) {
    const listChars = str.split("").sort();
    const Counts = {};
    let result = true;
    for (const element of listChars) {
      if (Object.hasOwn(Counts, element)) {
        Counts[element] += 1;
        result = false;
      } else {
        Counts[element] = 1;
      }
    }
    return result ? `${str} es un Isograma` : `${str} no es un Isograma`;
  },
  isAnagram: function (word1, word2) {
    return this.sortString(word1) === this.sortString(word2)
      ? `${word1} y ${word2} son un anagrama`
      : `${word1} y ${word2} no son un anagrama`;
  },
  isPalindrome: function (word) {
    return word === this.reverseString(word)
      ? `${word} es un palindromo`
      : `${word} no es un palindromo`;
  },
  verify : function (word1, word2) {
    console.log(AnalizeWords.isPalindrome(word1));
    console.log(AnalizeWords.isPalindrome(word2));

    console.log(AnalizeWords.isAnagram(word1, word2));

    console.log(AnalizeWords.isIsogram(word1));
    console.log(AnalizeWords.isIsogram(word1));
  }
};

console.log(AnalizeWords.verify("arroz", "zorra"));

