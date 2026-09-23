// Crear strings (tres formas)
const simple = 'Hola';
const doble = "Mundo";
const template = `Hola Mundo`;  // Backticks (los más poderosos)

// Acceso a caracteres específicos (índice empieza en 0)
const texto = "JavaScript";
console.log(texto[0]);      // "J"
console.log(texto[4]);      // "S"
console.log(texto.charAt(2)); // "v" (método alternativo)

// Longitud
console.log(texto.length);  // 10

//Subcadenas

const frase = "El sol brilla hoy";

// slice(inicio, fin) - NO incluye el índice final
console.log(frase.slice(3, 6));    // "sol"

// substring(inicio, fin) - similar a slice
console.log(frase.substring(3, 6)); // "sol"

// substr(inicio, cantidad) - ⚠️ Obsoleto, mejor usar slice
console.log(frase.slice(3, 9));    // "sol br" (desde índice 3 hasta 9)

// Desde el final con índices negativos
console.log(frase.slice(-3));    // "hoy" (últimos 3 caracteres)

// Concatenacion y repeticion

// Concatenación con + (forma antigua)
const saludo = "Hola" + " " + "Mundo";
console.log(saludo);  // "Hola Mundo"

// Concatenación con método concat()
const nombre = "Ana";
console.log("Hola ".concat(nombre, "!"));  // "Hola Ana!"

// Repetición
const risa = "ja";
console.log(risa.repeat(3));  // "jajaja"

// Repetir con espacios
console.log("-".repeat(20));  // "--------------------"

// Conversion a mayusculas y minusculas

const mixto = "JaVaScRiPt";

console.log(mixto.toUpperCase());  // "JAVASCRIPT"
console.log(mixto.toLowerCase());  // "javascript"

// Primera letra mayúscula (combinación)
const palabra = "hola";
const capitalizada = palabra.charAt(0).toUpperCase() + palabra.slice(1);
console.log(capitalizada);  // "Hola"

//Reemplazo

const oracion = "El gato es negro y el gato es grande";

// replace - Solo reemplaza la PRIMERA coincidencia
console.log(oracion.replace("gato", "perro"));
// "El perro es negro y el gato es grande"

// replace con regex y flag /g (global) reemplaza TODAS
console.log(oracion.replace(/gato/g, "perro"));
// "El perro es negro y el perro es grande"

// replaceAll - Reemplaza todas (más moderno)
console.log(oracion.replaceAll("gato", "perro"));
// "El perro es negro y el perro es grande"

// Division y union

// split - Divide un string en array
const lista = "manzana,pera,uva,mango";
const frutasArray = lista.split(",");
console.log(frutasArray);  // ["manzana", "pera", "uva", "mango"]

// Split con espacio
const oracion2 = "Hola mundo JavaScript";
const palabras = oracion2.split(" ");
console.log(palabras);  // ["Hola", "mundo", "JavaScript"]

// join - Une un array en string
console.log(frutasArray.join(" - "));  // "manzana - pera - uva - mango"
console.log(palabras.join(" "));        // "Hola mundo JavaScript"

// Verificacion y busqueda

const frase3 = "La programación es divertida";

// includes - ¿Contiene esta subcadena?
console.log(frase3.includes("programación"));  // true
console.log(frase3.includes("aburrido"));      // false

// startsWith / endsWith
console.log(frase3.startsWith("La"));     // true
console.log(frase3.endsWith("divertida")); // true

// indexOf - Posición de la primera ocurrencia (devuelve -1 si no existe)
console.log(frase3.indexOf("es"));     // 16
console.log(frase3.indexOf("xyz"));    // -1

// lastIndexOf - Posición de la última ocurrencia
console.log(frase3.lastIndexOf("a"));  // 24 (última 'a')

//Interpolacion

// Con backticks ` ` puedes insertar variables directamente
const nombre2 = "Carlos";
const edad = 30;
const ciudad = "Medellín";

// Forma antigua (concatenación)
const mensajeAntiguo = "Me llamo " + nombre2 + ", tengo " + edad + " años y vivo en " + ciudad;

// Forma moderna (interpolación) - MUCHO MEJOR
const mensajeModerno = `Me llamo ${nombre2}, tengo ${edad} años y vivo en ${ciudad}`;

console.log(mensajeModerno);

// También puedes hacer operaciones dentro
console.log(`En 5 años tendré ${edad + 5} años`);

// Y multilínea
const poema = `
    Las rosas son rojas,
    las violetas son azules,
    JavaScript es genial.
`;
console.log(poema);

// Recorrido de caracteres

const palabra3 = "Hola";

// Con for clásico (por índice)
for (let i = 0; i < palabra3.length; i++) {
    console.log(`Índice ${i}: ${palabra3[i]}`);
}

// Con for...of (directamente el carácter)
for (const letra of palabra3) {
    console.log(letra);
}

// Con forEach (convirtiendo a array)
[...palabra3].forEach((letra, indice) => {
    console.log(`${indice}: ${letra}`);
});

//Verificacion de tipo y limpieza

// typeof - Verificar si es string
console.log(typeof "hola");  // "string"
console.log(typeof 123);     // "number"

// trim - Elimina espacios al inicio y final
const sucio = "   hola mundo   ";
console.log(sucio.trim());       // "hola mundo"
console.log(sucio.trimStart());  // "hola mundo   "
console.log(sucio.trimEnd());    // "   hola mundo"

// padStart / padEnd - Rellenar con caracteres
const numero3 = "7";
console.log(numero3.padStart(3, "0"));  // "007"
console.log(numero3.padEnd(3, "!"));    // "7!!"

// charCodeAt - Obtener código ASCII
console.log("A".charCodeAt(0));  // 65

// fromCharCode - Obtener letra desde código ASCII
console.log(String.fromCharCode(65));  // "A"

// Dificultad extra

console.log("-".repeat(20));

console.log(`Bienvenido al programa que verifica si dos palabras son:
    palindromo,
    anagrama o 
    isograma`);

console.log("-".repeat(20));

const palabra1 = prompt("Escriba la primer palabra analizar: ");
const palabra2 = prompt("Escriba la segunda palabra analizar: ");

function esPalindromo(palabra) {
    if(palabra.toLowerCase() === palabra.toLowerCase().split("").reverse().join("")){
        return "Es palindroma"
    }
    else {
        return "No es palindroma"
    }
}

function esAnagrama(palabra1,palabra2) {
    // Ordenar ambas palabras alfabéticamente y comparar
    const ordenada1 = palabra1.toLowerCase().split("").sort().join("");
    const ordenada2 = palabra2.toLowerCase().split("").sort().join("");
    return ordenada1 === ordenada2;
}

function esIsograma(palabra) {
    const letrasUnicas = new Set(palabra);
    return letrasUnicas.size === palabra.length;
}

// Mostrar resultados claramente
console.log("\n--- RESULTADOS ---");

// Palíndromos (cada palabra por separado)
console.log(`¿"${palabra1}" es palíndromo?: ${esPalindromo(palabra1)}`);
console.log(`¿"${palabra2}" es palíndromo?: ${esPalindromo(palabra2)}`);

// Anagramas (comparando ambas)
console.log(`¿"${palabra1}" y "${palabra2}" son anagramas?: ${esAnagrama(palabra1, palabra2)}`);

// Isogramas (cada palabra por separado)
console.log(`¿"${palabra1}" es isograma?: ${esIsograma(palabra1)}`);
console.log(`¿"${palabra2}" es isograma?: ${esIsograma(palabra2)}`);