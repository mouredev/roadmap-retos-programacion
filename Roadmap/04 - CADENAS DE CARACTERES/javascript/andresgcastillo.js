// Crear una cadena de caracteres
let cadena = "Hola Mundo";

// Acceso a caracteres específicos
let primerCaracter = cadena[0]; // "H"

// Subcadenas
let subcadena = cadena.substring(0, 4); // "Hola"

// Longitud
let longitud = cadena.length; // 10

// Concatenación
let cadenaConcatenada = cadena + ", ¿Cómo estás?"; // "Hola Mundo, ¿Cómo estás?"

// Repetición
let cadenaRepetida = cadena.repeat(2); // "Hola MundoHola Mundo"

// Recorrido
for (let i = 0; i < cadena.length; i++) {
  console.log(cadena[i]);
}

// Conversión a mayúsculas
let mayusculas = cadena.toUpperCase(); // "HOLA MUNDO"

// Conversión a minúsculas
let minusculas = cadena.toLowerCase(); // "hola mundo"

// Reemplazo
let cadenaReemplazada = cadena.replace("Mundo", "Andres"); // "Hola Andres"

// División
let cadenaDividida = cadena.split(" "); // ["Hola", "Mundo"]

// Unión
let cadenaUnida = cadenaDividida.join("-"); // "Hola-Mundo"

// Interpolación
let nombre = "Andres";
let cadenaInterpolada = `Hola ${nombre}`; // "Hola Andres"

// Verificación
let contiene = cadena.includes("Mundo"); // true

//Dificultad Extra

function esPalindromo(palabra) {
  let palabraReversa = palabra.split("").reverse().join("");
  return palabra === palabraReversa;
}

function esAnagrama(palabra1, palabra2) {
  let ordenarPalabra = (palabra) => palabra.toLowerCase().split("").sort().join("");
  return ordenarPalabra(palabra1) === ordenarPalabra(palabra2);
}

function esIsograma(palabra) {
  let letras = palabra.toLowerCase().split("");
  let unicas = [...new Set(letras)];
  return letras.length === unicas.length;
}

let palabra1 = "anagram";
let palabra2 = "nagaram";

console.log(`Las palabras son ${palabra1} y ${palabra2}`);

console.log(`¿Son palíndromos?`);
console.log(`Palabra 1: ${esPalindromo(palabra1)}`);
console.log(`Palabra 2: ${esPalindromo(palabra2)}`);

console.log(`¿Son anagramas? ${esAnagrama(palabra1, palabra2)}`);

console.log(`¿Son isogramas?`);
console.log(`Palabra 1: ${esIsograma(palabra1)}`);
console.log(`Palabra 2: ${esIsograma(palabra2)}`);
