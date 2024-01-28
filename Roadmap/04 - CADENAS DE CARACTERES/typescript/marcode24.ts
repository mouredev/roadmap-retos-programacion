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

// Operaciones comunes con cadenas de caracteres

// Acceso a caracteres específicos
const cadena: string = "Hola, mundo!";
console.log("Carácter en la posición 0:", cadena[0]);

// Subcadenas
const subcadena: string = cadena.substring(2, 6);
console.log("Subcadena:", subcadena);

// Longitud de la cadena
console.log("Longitud de la cadena:", cadena.length);

// Concatenación
const otraCadena: string = " Qué tal?";
const cadenaConcatenada: string = cadena + otraCadena;
console.log("Cadena concatenada:", cadenaConcatenada);

// Repetición
const cadenaRepetida: string = cadena.repeat(3);
console.log("Cadena repetida 3 veces:", cadenaRepetida);

// Recorrido
for (let i: number = 0; i < cadena.length; i++) {
  console.log("Carácter en posición", i, ":", cadena[i]);
}

// Conversión a mayúsculas y minúsculas
const mayusculas: string = cadena.toUpperCase();
const minusculas: string = cadena.toLowerCase();
console.log("Mayúsculas:", mayusculas);
console.log("Minúsculas:", minusculas);

// Reemplazo
const nuevaCadena: string = cadena.replace("mundo", "amigo");
console.log("Cadena con reemplazo:", nuevaCadena);

// División
const palabras: string[] = cadena.split(" ");
console.log("Palabras divididas:", palabras);

// Unión
const union: string = palabras.join("-");
console.log("Palabras unidas con guiones:", union);

// Interpolación
const nombre: string = "Juan";
const edad: number = 30;
const mensaje: string = `Hola, me llamo ${nombre} y tengo ${edad} años.`;
console.log("Mensaje interpolado:", mensaje);

// Verificación
const contieneHola: boolean = cadena.includes("Hola");
console.log("¿La cadena contiene 'Hola'?", contieneHola);

// Programa que verifica palíndromos, anagramas e isogramas

function esPalindromo(palabra: string): boolean {
  const palabraInvertida: string = palabra.split("").reverse().join("");
  return palabra === palabraInvertida;
}

function esAnagrama(palabra1: string, palabra2: string): boolean {
  const ordenPalabra1: string = palabra1.split("").sort().join("");
  const ordenPalabra2: string = palabra2.split("").sort().join("");
  return ordenPalabra1 === ordenPalabra2;
}

function esIsograma(palabra: string): boolean {
  const caracteresUnicos: Set<string> = new Set(palabra);
  return palabra.length === caracteresUnicos.size;
}

// Ejemplos
const palabra1: string = "oso";
const palabra2: string = "soso";
console.log(`"${palabra1}" es palíndromo:`, esPalindromo(palabra1));
console.log(`"${palabra1}" es anagrama de "${palabra2}":`, esAnagrama(palabra1, palabra2));
console.log(`"${palabra1}" es isograma:`, esIsograma(palabra1));

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
