let str = "zzz";

// INSTRUCCIONES EN EL OUTPUT
console.log("Acceso al carácter específico\n" + str[0]);
console.log(str.charAt(1));
console.log("\nSubcadena: " + str.substring(0, 2));
console.log("\nLongitud: " + str.length);
console.log("\nConcatenación: " + str.concat(" sadasd"));
console.log("\nRepetición: " + str.repeat(4));
console.log("\nRecorrido: ");
for (let char of str){console.log(char);}
console.log("\nConversión a mayúsculas: " + str.toUpperCase());
console.log("\nConversión a minúsculas: " + str.toLowerCase());
console.log("\nReemplazo\n" + str.replace("zz", "xd"));
console.log(str.replaceAll("xd", "zzz"));
console.log("\nDivisión: " + str.split(""));
console.log("\nUnión: " + str.split("").join("-"));
console.log(`\nInterpolación:\nEl string ${str} tiene ${str.length} carácteres`);
console.log("\nVerificación con\nincludes: " + str.includes("z"));
console.log("startsWith: " + str.startsWith("xd"));
console.log("endsWith: " + str.endsWith("z"));
console.log("\nElimina los espacios en blanco...\n" + str.trim());
console.log("al comienzo del string: " + str.trimStart());
console.log("al final del string: " + str.trimEnd());
console.log("\nExtrae parte del string y lo retorna como nuevo string: " + str.slice(1, 3));
console.log("\nBusca una coincidencia entre una expresión regular y el string: " + str.search("xd"));
console.log("\nRetorna índice donde se indica un carácter\nprimer índice: " + str.indexOf("z"));
console.log("último índice: " + str.lastIndexOf("z") + "\n");



// DIFICULTAD EXTRA

/* PALÍNDROMOS */

function Palindromo(str){
    // Convertir a string (en lo demás es sensible)
    str = String(str);
    return str === str.split('').reverse().join('');
}

console.log(Palindromo("zzz")); // true

/* Anagrama */

function Anagrama(str1, str2) {
    // Eliminar espacios y convertir a minúsculas
    str1 = str1.replace(/\s+/g, '').toLowerCase();
    str2 = str2.replace(/\s+/g, '').toLowerCase();

    // Convertir a arrays, ordenar y convertir de nuevo a cadenas
    let arr1 = str1.split('').sort().join('');
    let arr2 = str2.split('').sort().join('');

    return arr1 === arr2;
}

console.log(Anagrama("listen", "silent")); // true

/* Isograma */

function Isograma(str) {
    // Eliminar espacios y convertir a minúsculas
    str = str.replace(/\s+/g, '').toLowerCase();

    let letras = new Set();

    for (let char of str) {
        if (letras.has(char)) {
            return false; // Si la letra ya está en el conjunto, no es un isograma
        }
        letras.add(char);
    }
    return true; // Si no se repite ninguna letra, es un isograma
}

console.log(Isograma("lumberjacks")); // true
