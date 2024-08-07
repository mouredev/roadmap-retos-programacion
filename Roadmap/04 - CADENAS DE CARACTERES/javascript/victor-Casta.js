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

//acceder a un caracter 
console.log("Hola".charAt(1)); //Imprime "o"
console.log("JavaScript"[1]); //Imprime "a"

//Subcadenas
//Método substring(startIndex, endIndex)
let originalString = "Hola JavaScript";
let subcadena = originalString.substring(5, 15);
console.log(subcadena);

//Propiedad slice(startIndex, endIndex)
let sliceSubcadena = originalString.slice(0, 4)
console.log(sliceSubcadena);

//Método substring(index)
let substringString = originalString.substring(5);
console.log(substringString);


//Longitud
let myString = 'JavaScript';
console.log(myString.length);

//Concatenación
let stringOne = 'hola';
let stringTwo = 'mundo';
console.log(stringOne + ' ' + stringTwo);
console.log(`${stringOne} ${stringTwo}`);

//repeticion
let repeatTimes = 3;
let repeatedString = `${stringOne.repeat(repeatTimes)}`
console.log(repeatedString);

//recorrido
let myString2 = () => {
  for (let i=0 ; i < myString.length ; i++) {
    console.log(myString[i]);
  }
}

myString2();

//conversión a mayúsculas y minúsculas
console.log("alphabet".toUpperCase());
console.log("alphabet".toLowerCase());

//reemplazo
let replacedString = "Hello World".replace("World", "JavaScript");
console.log(replacedString);

//interpolación
const a = 'Hello';
const b = 'JavaScript'

console.log(`${a} ${b} welcome to roadmap!`);

//verificación
let string  = "Hello World";
console.log(typeof(string));


//Programa

let myProgram = (word1, word2) => {
  const formatWord1 = word1.replace(/\s/g, '').toLowerCase();
  const formatWord2 = word2.replace(/\s/g, '').toLowerCase();

  const palindromo1 = formatWord1.split('').reverse().join('');
  const palindromo2 = formatWord2.split('').reverse().join('');

  const anagrama1 = formatWord1.split('').sort().join('');
  const anagrama2 = formatWord2.split('').sort().join('');

  const isIsogram = (word) => {
    const charCount = {};
    for (let char of word) {
      if (charCount[char]) {
        return false;
      }
      charCount[char] = 1;
    }
    return true;
  };

  if (word1 === palindromo1 && word2 === palindromo2) {
    console.log(`La palabra ${word1} y ${word2} son palíndromos.`);
  } else if (anagrama1 === anagrama2) {
    console.log(`La palabra ${word1} y ${word2} son anagramas.`);
  } else if (isIsogram(formatWord1) && isIsogram(formatWord2)) {
    console.log(`La palabra ${word1} y ${word2} son isogramas.`);
  } else {
    console.log('No son ni palíndromos ni anagramas ni isogramas.');
  }
};

myProgram('roma', 'amor');


