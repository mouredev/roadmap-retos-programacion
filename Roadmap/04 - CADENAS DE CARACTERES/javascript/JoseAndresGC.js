// cadenas de texto
// metodos de cadenas de texto

let str = "Banana";
let my_name = "Andrés";
console.log(my_name);

// Acceso a caracteres específicos

console.log(my_name.charAt(0)); // "A"
console.log(my_name.charAt(100)); // "" si está fuera de rango devuelve una cadena vacía

console.log(my_name.at(0), my_name.at(1), my_name.at(2));  // ["A", "n", "d"]
console.log(my_name.at(200)); // undefined ... si está fuera de rango devuelve undefined
console.log(my_name.at(-1)); // s ... acepta valores negativos. En indices negativos se representa -1 como la ultima letra o posicion de la cadena

// subcadenas

console.log(my_name.substring()) // Andrés .substring(inicio, fin) Si no se especifica el fin devuelve toda la cadena
console.log(my_name.substring(1, 4)) // "ndr"

console.log(my_name.slice(-5, -1)); // "ndré" .slice(inicio, fin) Funciona parecido a substring, pero acepta valores negativos.
console.log(my_name.slice(500)); // ""
console.log(my_name.slice(0)); // "Andrés"

// longitud

console.log(my_name.length); // 6

// búsqueda

console.log(str.match(/a/g)); // busca de manera global por la cadena y separa en un array todas las coindidencias ["a","a","a"]
console.log(str.match(/[an]/g)); // para buscar más de una letra usar [] ["a", "n", "a", "n", "a"]

console.log(my_name.search("A")); // 0 devuelve la posición de la primera coincidencia
console.log(my_name.search("z")); // -1 si no encuentra la letra devuelve -1

console.log(my_name.indexOf("A")); // 0 devuelve la posición de la primera coincidencia
console.log(my_name.indexOf("z")); // -1 si no encuentra la letra devuelve -1

// concatenación

console.log(my_name + ' ' + str); // "Andrés Banana" con operador +

console.log(my_name.concat(' ', str)); // "Andrés Banana" .concat(str1, str2,  ...)

console.log(`José ${my_name} ${str} con backticks`); // "José Andrés Banana" con el metodo de los backstick. Se pueden concatenar variables y variables directamente en la cadena de texto

// repetición

console.log(my_name.repeat(3)); // "AndrésAndrésAndrés" .repeat(n) repite la cadena n veces

// recorrido

console.log(my_name.endsWith("s")); // true ...verifica si la cadena termina con el caracter especificado
console.log(my_name.startsWith("A")); // true ...verifica si la cadena comienza con el caracter especificado 
console.log(my_name.includes("n")); // true ...verifica si la cadena contiene el caracter especificado 

// conversion a mayusculas y minusculas

console.log(my_name.toUpperCase()); // "ANDRÉS" convierte la cadena de texto a mayúsculas
console.log(my_name.toLowerCase()); // "andrés" convierte la cadena de texto en minúsculas

// reemplazo

console.log(my_name.replace("A", "a")); // "andrés" reemplaza la primera coincidencia
console.log(my_name.replace(/A/g, "a")); // "andrés" reemplaza todas las coincidencias

let str2 = "Hola, Hola mundo, Hola a todos";
console.log(str2.replaceAll("Hola", "Chao")); // 

// división

console.log(my_name.split("")); // ["A", "n", "d", "r", "é", "s"] Divide la cadena de texto en un array de caracteres equivalente a la cadena original

// interpolación

console.log(`
    Hola! Mi nombre es ${my_name}
    Y esto es un ejemplo de interpolación de cadenas de texto`);

// DIFICULTAD EXTRA:

let word1 = "Zorra";
let word2 = "Arroz";
let word3 = "Background";
let word4 = "Mary";
let word5 = "Army";

function isPalindrom() { // palabras que se leen igual de izquierda a derecha que de derecha a izquierda
    let _word1 = word1.toLowerCase().split("").reverse().join("");
    let _word2 = word2.toLowerCase();
    
    return _word1 === _word2 ? true : false;
    
}

function isAnagram() { // palabras que tienen las mismas letras pero en diferente orden
    let _word4 = word4.toLowerCase().split("").sort().join("");
    return _word4 === word5.toLowerCase().split("").sort().join("") ? true : false;
}

function isIsogram() { // palabras que o frases que no tienen letras repetidas

    let _word3 = word3.toLowerCase().split("").sort().join("");
    let _word3Set = new Set(_word3);

    return _word3.length === _word3Set.size ? true : false;
}

console.log(`Las palabras ${word1} y ${word2} son Palíndromos? : ${isPalindrom()}`);

console.log(`Las palabras ${word4} y ${word5} son Anagramas? : ${isAnagram()}`);

console.log(`La palabra ${word3} es un Isograma? : ${isIsogram()}`);