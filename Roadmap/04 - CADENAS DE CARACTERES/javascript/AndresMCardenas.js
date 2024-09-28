/*
  * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
  * en tu lenguaje.Algunas de esas operaciones podrían ser(busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 * conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA(opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
  * para descubrir si son:
 * - Palíndromos
  * - Anagramas
  * - Isogramas
*/

// Acceso a caracteres específicos
let cadena = "Hola Mundo";
console.log(cadena[0]); // Himprime H por que es el primer caracter de la cadena

// Subcadenas
console.log(cadena.substring(0, 4)); // Imprime Hola por que es la subcadena que va desde el caracter 0 hasta el 4

// Longitud
console.log(cadena.length); // Imprime 10 por que es la longitud de la cadena

// Concatenación
let cadena2 = " desde JavaScript";  
console.log(cadena + cadena2); // Imprime Hola Mundo desde JavaScript

// Repetición
console.log(cadena.repeat(3)); // Imprime Hola MundoHola MundoHola Mundo

// Recorrido
for (let i = 0; i < cadena.length; i++) {
  console.log(cadena[i]); // Imprime cada caracter de la cadena en una linea
}

// Conversión a mayúsculas y minúsculas
console.log(cadena.toUpperCase()); // Imprime HOLA MUNDO  
console.log(cadena.toLowerCase()); // Imprime hola mundo

// Reemplazo
console.log(cadena.replace("Hola", "Adios")); // Imprime Adios Mundo

// División
console.log(cadena.split(" ")); // Imprime ["Hola", "Mundo"]

// Unión
console.log(cadena.split(" ").join("")); // Imprime HolaMundo

// Interpolación
console.log(`${cadena} desde JavaScript`); // Imprime Hola Mundo desde JavaScript

// Verificación
console.log(cadena.includes("Hola")); // Imprime true

// Palíndromos
let palabra = "oso";
let palabraInvertida = palabra.split("").reverse().join("");

if (palabra === palabraInvertida) {
  console.log("Es palíndromo");
} else {
  console.log("No es palíndromo");
}

// Anagramas
let palabra1 = "roma";
let palabra2 = "amor";

if (palabra1.split("").sort().join("") === palabra2.split("").sort().join("")) {
  console.log("Es anagrama");
} else {
  console.log("No es anagrama");
}

// Isogramas
let palabra3 = "murcielago";
let isograma = true;

for (let i = 0; i < palabra3.length; i++) {
  for (let j = i + 1; j < palabra3.length; j++) {
    if (palabra3[i] === palabra3[j]) {
      isograma = false;
      console.log("No es isograma");
      break;
    }
  }  
}

if (isograma) {
  console.log("Es isograma");
}


