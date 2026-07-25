// Operaciones con cadenas en TypeScript

// Declaración de una cadena
const texto: string = "Hola, mundo!";

console.log("Texto original:", texto);

// 1. Acceso a caracteres específicos
console.log("1. Primer carácter:", texto[0]);

// 2. Subcadenas
console.log("2. Subcadena:", texto.substring(0, 4));

// 3. Longitud
console.log("3. Longitud:", texto.length);

// 4. Concatenación
const otraCadena: string = " Bienvenidos";
console.log("4. Concatenación:", texto.concat(otraCadena));

// 5. Repetición
console.log("5. Repetición:", texto.repeat(3));

// 6. Recorrido
console.log("6. Recorrido:");
for (let char of texto) {
    console.log(char);
}

// 7. Conversión a mayúsculas y minúsculas
console.log("7. Mayúsculas:", texto.toUpperCase());
console.log("   Minúsculas:", texto.toLowerCase());

// 8. Reemplazo
console.log("8. Reemplazo:", texto.replace("mundo", "TypeScript"));

// 9. División
console.log("9. División:", texto.split(", "));

// 10. Unión
const arrayPalabras: string[] = ["TypeScript", "es", "genial"];
console.log("10. Unión:", arrayPalabras.join(" "));

// 11. Interpolación (template literals en TypeScript)
const nombre: string = "Alice";
const edad: number = 30;
console.log(`11. Interpolación: Me llamo ${nombre} y tengo ${edad} años.`);

// 12. Verificación
console.log("12. Empieza con 'Hola':", texto.startsWith("Hola"));
console.log("    Termina con '!':", texto.endsWith("!"));
console.log("    Contiene 'mundo':", texto.includes("mundo"));

// 13. Recorte de espacios
const textoConEspacios: string = "  Hola Mundo  ";
console.log("13. Recorte de espacios:", textoConEspacios.trim());

// 14. Extracción de subcadenas
console.log("14. Extracción (slice):", texto.slice(0, 4));

// 15. Búsqueda de índice
console.log("15. Índice de 'mundo':", texto.indexOf("mundo"));

// DIFICULTAD EXTRA
console.log("\nDIFICULTAD EXTRA:");

const palabra1: string = "amor";
const palabra2: string = "roma";

console.log("Palabra 1:", palabra1);
console.log("Palabra 2:", palabra2);

// Función para verificar si una palabra es un palíndromo
function esPalindromo(palabra: string): boolean {
    return palabra === palabra.split('').reverse().join('');
}

// Función para verificar si dos palabras son anagramas
function sonAnagramas(palabra1: string, palabra2: string): boolean {
    return palabra1.toLowerCase().split('').sort().join('') === 
           palabra2.toLowerCase().split('').sort().join('');
}

// Función para verificar si una palabra es un isograma
function esIsograma(palabra: string): boolean {
    return new Set(palabra.toLowerCase()).size === palabra.length;
}

console.log("¿Son palíndromos?", 
    esPalindromo(palabra1), esPalindromo(palabra2));
console.log("¿Son anagramas?", sonAnagramas(palabra1, palabra2));
console.log("¿Son isogramas?", esIsograma(palabra1), esIsograma(palabra2));