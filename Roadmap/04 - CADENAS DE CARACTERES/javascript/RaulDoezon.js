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

var cadena = "Parangaricutirimícuaro";
var arreglo = ["See", "you", "next", "mission"];

console.log("El rey de " + cadena + ", es la concatenación de dos cadenas de texto.");
console.log("La longitud de " + cadena + " es: " + cadena.length);
console.log("El tercer caracter de " + cadena + " es: " + cadena[2]);
console.log("El último caracter de " + cadena + " es: " + cadena[cadena.length - 1]);
console.log("Una subcadena de " + cadena + ": " + cadena.substring(9, 15));
console.log(cadena.toUpperCase() + " en MAYÚSCULAS.");
console.log(cadena.toLowerCase() + " en minúsculas.");
console.log("Parte de la cadena se reemplaza: " + cadena.replace("cutirimícuaro", "fláutica"));
console.log("La cadena se repite tres veces: " + cadena.repeat(3));
console.log("La cadena se divide: " + cadena.split(""));
console.log("El arreglo [" + arreglo + "] se une para formar una cadena: " + arreglo.join(" "));
console.log(`Estoy interpolando a ${cadena} en esta cadena de texto.`);
console.log(`¿La cadena ${cadena} incluye el texto Paranga? ${cadena.includes("Paranga") === true ? "Así es." : "No lo contiene."}`);
console.log("Esta es la iteración de la cadena:");

for (caracter of cadena) {
  console.log(caracter);
}

// +++++++++ DIFICULTAD EXTRA +++++++++
var firstWord = "Samus".toUpperCase();
var secondWord = "Sumas".toUpperCase();

function isPalindrome() {
  var secondPalindrome = secondWord.toUpperCase().split("").reverse().join("");

  if (firstWord === secondPalindrome) {
    return "son palíndromos.";
  } else {
    return "no son palíndromos."
  }
}

function isAnagram() {
  var firstAnagram = firstWord.split("").sort().join("");
  var secondAnagram = secondWord.split("").sort().join("");

  if (firstAnagram === secondAnagram) {
    return "son Anagramas.";
  } else {
    return "no son Anagramas.";
  }
}

function isIsogram(theString) {
  for (var index = 0; index < theString.length; index++) {

    if (theString.indexOf(theString[index]) !== index) {
      return `${theString} no es Isograma.`;
    }
  }

  return `${theString} es Isograma.`;
}

console.log("------------------------------");
console.log(`${firstWord} y ${secondWord} ${isPalindrome()}`);
console.log(" ");
console.log(`${firstWord} y ${secondWord} ${isAnagram()}`);
console.log(" ");
console.log(isIsogram(firstWord));
console.log(isIsogram(secondWord));
