// Ejemplos de operaciones con cadenas de caracteres en JavaScript

let cadena = "Hola Mundo";

// Acceso a caracteres específicos
console.log(cadena[0]); // H
console.log(cadena.charAt(1)); // o

// Subcadenas
console.log(cadena.substring(0, 4)); // Hola
console.log(cadena.slice(5)); // Mundo

// Longitud
console.log(cadena.length); // 10

// Concatenación
let cadena2 = " ¡Bienvenidos!";
console.log(cadena + cadena2); // Hola Mundo ¡Bienvenidos!

// Repetición
console.log(cadena.repeat(2)); // Hola MundoHola Mundo

// Recorrido
for (let char of cadena) {
    console.log(char);
}

// Conversión a mayúsculas y minúsculas
console.log(cadena.toUpperCase()); // HOLA MUNDO
console.log(cadena.toLowerCase()); // hola mundo

// Reemplazo
console.log(cadena.replace("Mundo", "JavaScript")); // Hola JavaScript

// División
let palabras = cadena.split(" ");
console.log(palabras); // ["Hola", "Mundo"]

// Unión
console.log(palabras.join(", ")); // Hola, Mundo

// Interpolación
let nombre = "Juan";
console.log(`Hola, ${nombre}`); // Hola, Juan

// Verificación
console.log(cadena.includes("Mundo")); // true
console.log(cadena.startsWith("Hola")); // true
console.log(cadena.endsWith("Mundo")); // true

// Dificultad extra: Programa para analizar dos palabras

function esPalindromo(palabra) {
    let invertida = palabra.split('').reverse().join('');
    return palabra === invertida;
}

function sonAnagramas(palabra1, palabra2) {
    let sorted1 = palabra1.split('').sort().join('');
    let sorted2 = palabra2.split('').sort().join('');
    return sorted1 === sorted2;
}

function esIsograma(palabra) {
    let letras = new Set(palabra);
    return letras.size === palabra.length;
}

let palabra1 = "amor";
let palabra2 = "roma";

console.log(`¿"${palabra1}" es un palíndromo? ${esPalindromo(palabra1)}`);
console.log(`¿"${palabra2}" es un palíndromo? ${esPalindromo(palabra2)}`);
console.log(`¿"${palabra1}" y "${palabra2}" son anagramas? ${sonAnagramas(palabra1, palabra2)}`);
console.log(`¿"${palabra1}" es un isograma? ${esIsograma(palabra1)}`);
console.log(`¿"${palabra2}" es un isograma? ${esIsograma(palabra2)}`);