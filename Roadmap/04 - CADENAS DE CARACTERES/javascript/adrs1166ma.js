/*
EJERCICIO:
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
  conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
*
DIFICULTAD EXTRA (opcional):
Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas
*/

// 🔥 Acceso a caracteres específicos
const texto = "JavaScript";
console.log("Primer carácter:", texto[0]); // J
console.log("Último carácter:", texto[texto.length - 1]); // t

// 🔥 Subcadenas
console.log("Subcadena (índice 0 a 4):", texto.slice(0, 4)); // Java
console.log("Subcadena desde índice 4:", texto.substring(4)); // Script

// 🔥 Longitud
console.log("Longitud de la cadena:", texto.length); // 10

// 🔥 Concatenación
const saludo = "Hola";
const lenguaje = "Mundo";
console.log("Concatenación:", saludo + " " + lenguaje); // Hola Mundo
console.log("Concatenación con template string:", `${saludo} ${lenguaje}`); // Hola Mundo  - con Backtick 

// 🔥 Repetición
console.log("Repetición:", "JS ".repeat(3)); // JS JS JS 

// 🔥 Recorrido
for (let char of texto) {
    console.log(char); // Imprime cada carácter de "JavaScript"
}

// 🔥 Conversión a mayúsculas y minúsculas
console.log("Mayúsculas:", texto.toUpperCase()); // JAVASCRIPT
console.log("Minúsculas:", texto.toLowerCase()); // javascript

// 🔥 Reemplazo
console.log("Reemplazo:", texto.replace("Script", "Code")); // JavaCode

// 🔥 División
console.log("División:", texto.split("a")); // ["J", "v", "Script"]

// 🔥 Unión
const palabras = ["Hola", "Mundo"];
console.log("Unión:", palabras.join(" ")); // Hola Mundo

// 🔥 Interpolación
const nombre = "Alice";
console.log(`Hola, me llamo ${nombre}`); // Hola, me llamo Alice

// 🔥 Verificación
console.log("Incluye 'Java':", texto.includes("Java")); // true
console.log("Empieza con 'Java':", texto.startsWith("Java")); // true
console.log("Termina con 'Script':", texto.endsWith("Script")); // true

// 🔥 Eliminación de espacios en blanco
const frase = "   Espacios alrededor   ";
console.log("Trim:", frase.trim()); // "Espacios alrededor"

// 🔥 Búsqueda de posición
console.log("Índice de 'S':", texto.indexOf("S")); // 4
console.log("Última aparición de 'a':", texto.lastIndexOf("a")); // 3

// 🔥 Extra 
function analizarPalabras(palabra1, palabra2) {
    /*
    Palíndromos : Una palabra es igual cuando se lee de izquierda a derecha y viceversa.
    Anagramas : Dos palabras contienen exactamente las mismas letras, pero en diferente orden.
    Isogramas : Una palabra no tiene letras repetidas.
    */

    const normalizar = (str) => str.replace(/\s+/g, "").toLowerCase();

    // Si una palabra es palíndromo
    const esPalindromo = (palabra) => {
        const normalizada = normalizar(palabra);
        return normalizada === normalizada.split("").reverse().join("");
    };

    // Si dos palabras son anagramas
    const sonAnagramas = (palabra1, palabra2) => {
        const normalizada1 = normalizar(palabra1).split("").sort().join("");
        const normalizada2 = normalizar(palabra2).split("").sort().join("");
        return normalizada1 === normalizada2;
    };

    // Si una palabra es isograma
    const esIsograma = (palabra) => {
        const letras = normalizar(palabra).split("");
        return new Set(letras).size === letras.length;
    };

    console.log(`${palabra1} es palíndromo:`, esPalindromo(palabra1));
    console.log(`${palabra2} es palíndromo:`, esPalindromo(palabra2));
    console.log(`${palabra1} y ${palabra2} son anagramas:`, sonAnagramas(palabra1, palabra2));
    console.log(`${palabra1} es isograma:`, esIsograma(palabra1));
    console.log(`${palabra2} es isograma:`, esIsograma(palabra2));
}

analizarPalabras("radar", "anagram");