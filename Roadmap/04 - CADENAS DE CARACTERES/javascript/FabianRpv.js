// Cadena de Caracteres

let cadena = "Hola Mundo ";
console.log(cadena);

// Acceso a caracteres especificos

console.log(cadena[0]); // H

// Subcadenas

console.log(cadena.substring(0, 5)); // Hola
console.log(cadena.slice(-5)); // Mundo

// Longitud

console.log(cadena.length); // 10

// Concatenación

let cadena2 = "desde JavaScript";
console.log(cadena + cadena2); // Hola Mundo desde JavaScript

// Repetición

console.log(cadena.repeat(3)); // Hola Mundo Hola Mundo Hola Mundo

// Recorrido

for (let i = 0; i < cadena.length; i++) {
  console.log(cadena[i]);
}

// Conversion a mayusculas y minusculas

console.log(cadena.toUpperCase()); // HOLA MUNDO
console.log(cadena.toLowerCase()); // hola mundo

// Reemplazo

console.log(cadena.replace("Mundo", "Fabian")); // Hola Fabian

// Division 

console.log(cadena.split(" ")); // ["Hola", "Mundo"]

// Union 

console.log(cadena.split(" ").join(" ")); // Hola Mundo

// Interpolación

console.log(`Hola ${cadena2}`); // Hola desde JavaScript

// Verificacion 

console.log(cadena.includes("Hola")); // true
console.log(cadena.startsWith("Hola")); // true
console.log(cadena.endsWith("Mundo ")); // true

// Eliminacion de espacios en blanco

console.log(cadena.trim()); // Hola Mundo

// Busqueda de indice

console.log(cadena.indexOf("Mundo")); // 5
console.log(cadena.lastIndexOf("o")); // 9

/*
Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas
*/

let palabra1 = "Amor";
let palabra2 = "Roma";

// Palindromo

const palindromo = palabra => {
    let palabraInvertida = palabra.toLowerCase().split("").reverse().join("");
    return palabra.toLowerCase() === palabraInvertida;
}

console.log(`Es palindromo: ${palindromo(palabra1)}`);
console.log(`Es palindromo: ${palindromo(palabra2)}`);

// Anagrama

const anagrama = (palabra1, palabra2) => {
    return palabra1.toLowerCase().split('').sort().join('') === palabra2.toLowerCase().split('').sort().join('');
}

console.log(`Es anagrama: ${anagrama(palabra1, palabra2)}`);

// Isograma

const isograma = palabra => {
    let palabraArray = palabra.toLowerCase().split("");
    let palabraSet = new Set(palabraArray);
    return palabraArray.length === palabraSet.size;
}

console.log(`Es isograma: ${isograma(palabra1)}`);
console.log(`Es isograma: ${isograma(palabra2)}`);