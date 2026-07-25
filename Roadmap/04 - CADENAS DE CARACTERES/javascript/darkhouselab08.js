/*
 * EJERCICIO #04: CADENAS DE CARACTERES
 * darkhouselab08 (Jorge Franco)
 */

// 1. Definición y longitud de cadenas de texto. 
let usuario = "darkhouselab08";
let nombreReal = "Jorge Franco";

console.log(`Usuario: ${usuario} - Longitud: ${usuario.length}`); 

// 2. Acceso a caracteres (lo que practicamos hoy)
console.log("Primera letra del usuario:", usuario[0]); 
console.log("Última letra del nombre:", nombreReal.at(-1));

// 3. Transformaciones (Limpieza y Mayúsculas)
let entradaSucia = "   jorge franco   ";
let nombreLimpio = entradaSucia.trim().toUpperCase();
console.log(`Nombre normalizado: "${nombreLimpio}"`);

// 4. Reemplazo e Interpolación
let saludo = "Hola, bienvenido al reto 03";
let saludoCorregido = saludo.replace("03", "04"); // Corregimos el número del reto
console.log(`${saludoCorregido}, ${nombreReal}!`);

// 5. División y Unión (El puente)
let habilidades = "JavaScript, Git, Terminal, Warp";
let arrayHabilidades = habilidades.split(", ");
console.log("Mis herramientas:", arrayHabilidades);
console.log("Lista unida con guiones:", arrayHabilidades.join(" - "));

/* * DIFICULTAD EXTRA: EL ANALIZADOR DE JORGE
 */

function analizadorDePalabras(palabra1, palabra2) {
    
    // Normalización: quitamos espacios y pasamos a minúsculas
    const limpiar = (str) => str.toLowerCase().trim();
    
    let p1 = limpiar(palabra1);
    let p2 = limpiar(palabra2);

    // --- 1. PALÍNDROMO ---
    const esPalindromo = (palabra) => {
        return palabra === palabra.split("").reverse().join("");
    };

    // --- 2. ANAGRAMA ---
    const esAnagrama = (str1, str2) => {
        if (str1 === str2) return false;
        return str1.split("").sort().join("") === str2.split("").sort().join("");
    };

    // --- 3. ISOGRAMA ---
    const esIsograma = (palabra) => {
        // Usamos Set para ver si hay letras repetidas
        return new Set(palabra).size === palabra.length;
    };

    console.log(`\n--- RESULTADOS PARA: "${palabra1}" y "${palabra2}" ---`);
    console.log(`¿"${palabra1}" es Palíndromo?: ${esPalindromo(p1)}`);
    console.log(`¿Son Anagramas?: ${esAnagrama(p1, p2)}`);
    console.log(`¿"${palabra1}" es Isograma?: ${esIsograma(p1)}`);
}

