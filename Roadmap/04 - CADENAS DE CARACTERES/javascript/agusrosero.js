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

let miCadena = "Hola Mundo!";

// Acceso a caracteres
let accederCadena = miCadena[1];
console.log(accederCadena);

// Longitud
let longitud = miCadena.length;
console.log(longitud);

// Concatenación
let concatenacion = miCadena + " Javascript";
console.log(concatenacion);

// Repetición
let repeticion = miCadena.repeat(5);
console.log(repeticion);

// Recorrido
for (let i = 0; i < miCadena.length; i++) {
  console.log(miCadena[i]);
}

// Mayúscula
let mayuscula = miCadena.toUpperCase();
console.log(mayuscula);

// Minúscula
let minuscula = miCadena.toLowerCase();
console.log(minuscula);

// Reemplazo
let reemplazo = miCadena.replace("Mundo", "Javascript");
console.log(reemplazo);

// División
let division = miCadena.split("");
console.log(division);

// Unión
let caracteres = ["a", "b", "c", "d"];
let union = caracteres.join("");
console.log(union);

// Interpolación
let nombre = "Hernan";
console.log(`Mi nombre es ${nombre}`);

// Verificación
let verificacion = miCadena.includes("Hola");
console.log(verificacion);

// DIFICULTAD EXTRA:
function esPalindromo(str1) {
  return str1 === str1.split("").reverse().join("");
}

console.log(esPalindromo("radar"));

function esAnagrama(str1, str2) {
  let cadena1 = str1.toLowerCase();
  let cadena2 = str2.toLowerCase();

  if (cadena1.length !== cadena2.length) {
    return false;
  }

  let ordenada1 = cadena1.split("").sort().join("");
  let ordenada2 = cadena2.split("").sort().join("");

  return ordenada1 === ordenada2;
}

console.log(esAnagrama("amor", "roma"));

function esIsograma(str1) {
  let letras = str1.toLowerCase().split("").sort();
  for (let i = 1; i < letras.length; i++) {
    if (letras[i] === letras[i - 1]) {
      return false;
    }
  }
  return true;
}

console.log(esIsograma("murcielago"));
