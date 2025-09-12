/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */


/* Soluciones */


// Acceso a caracteres específicos

let palabra = "Hola";
console.log(palabra[0]);  // Imprime "H"
console.log(palabra.charAt(2));  // Imprime "l"


//Subcadenas

let frase = "JavaScript es poderoso";
let subcadena = frase.substring(0, 10);
let subcadena2 = frase.indexOf("poderoso");
console.log(subcadena);  // Imprime "JavaScript"
console.log(subcadena2); // Imprime la posicion de la primera letra de la subcadena mencionada "14"


// Longitud de una cadena

let texto = "Ejemplo";
console.log(texto.length);  // Imprime 7


// Concatenación

let cadena1 = "Hola";
let cadena2 = " Mundo";
let resultado = cadena1 + cadena2;
console.log(resultado);  // Imprime "Hola Mundo"

// Repetición

let palabra1 = " Hola";
let repetida = palabra1.repeat(3);
console.log(repetida);  // Imprime " Hola Hola Hola"


// Recorrido

let palabra2 = "JavaScript";
for (let i = 0; i < palabra2.length; i++) {
    console.log(palabra2[i]);
}
// Imprime cada letra de "JavaScript" en líneas separadas


// Conversión a mayúsculas y minúsculas

let minusculas = "javascript";
let mayusculas = minusculas.toUpperCase();
console.log(mayusculas);  // Imprime "JAVASCRIPT"


// Reemplazo

let frase2 = "JavaScript es divertido";
let nuevaFrase2 = frase2.replace("divertido", "poderoso");
console.log(nuevaFrase2);  // Imprime "JavaScript es poderoso"


// División

let lista = "manzana,banana,cereza";
let arrayFrutas = lista.split(",");
console.log(arrayFrutas);  // Imprime ["manzana", "banana", "cereza"]


// Unión

let arrayColores = ["rojo", "verde", "azul"];
let cadenaColores = arrayColores.join(", ");
console.log(cadenaColores);  // Imprime "rojo, verde, azul"


// Interpolación

let nombre = "Juan";
let edad = 25;
let mensaje = `Hola, me llamo ${nombre} y tengo ${edad} años.`;
console.log(mensaje);
// Imprime "Hola, me llamo Juan y tengo 25 años."


// Verificación

let correo = "usuario@dominio.com";
let esCorreoValido = correo.includes("@");
console.log(esCorreoValido);  // Imprime true


// Extra - Opcional


// Funcion para verificar si una palabra es palíndroma
function esPalindromo(palabra) {
    const palabraReversa = palabra.split('').reverse().join('');
    return palabraReversa === palabra;
}

// Funcion para verificar si una palabra es un anagrama
function esAnagrama(palabra) {
    const ordenada = palabra.split('').sort().join('');
    return ordenada === palabra;
}

// Funcion para verificar si una palabra es un isograma
function esIsograma(palabra) {
    const letras = {};
    for (let letra of palabra) {
        if (letras[letra]) {
            return false;
        }
        letras[letra] = true;
    }
    return true;
}


// Funcion que dependiendo el resultado de si una o mas palabras son palíndromos, anagramas o isogramas, devuelve un resultado
function palabras(palabra1, palabra2) {
    let resultado = "";

    if (esPalindromo(palabra1) && esPalindromo(palabra2)) {
        resultado += `"${palabra1}" y "${palabra2}" son Palíndromos.\n`;
    } else if (esPalindromo(palabra1)) {
        resultado += `"${palabra1}" es un Palíndromo y "${palabra2}" no lo es.\n`;
    } else if (esPalindromo(palabra2)) {
        resultado += `"${palabra2}" es un Palíndromo y "${palabra1}" no lo es.\n`;
    } else {
        resultado += `Ninguna es un Palíndromo.\n`;
    }

    if (esAnagrama(palabra1) && esAnagrama(palabra2)) {
        resultado += `"${palabra1}" y "${palabra2}" son Anagramas.\n`;
    } else if (esAnagrama(palabra1)) {
        resultado += `"${palabra1}" es un Anagrama y "${palabra2}" no lo es.\n`;
    } else if (esAnagrama(palabra2)) {
        resultado += `"${palabra2}" es un Anagrama y "${palabra1}" no lo es.\n`;
    } else {
        resultado += `Ninguna es un Anagrama.\n`;
    }

    if (esIsograma(palabra1) && esIsograma(palabra2)) {
        resultado += `"${palabra1}" y "${palabra2}" son Isogramas.\n`;
    } else if (esIsograma(palabra1)) {
        resultado += `"${palabra1}" es un Isograma y "${palabra2}" no lo es.\n`;
    } else if (esIsograma(palabra2)) {
        resultado += `"${palabra2}" es un Isograma y "${palabra1}" no lo es.\n`;
    } else {
        resultado += `Ninguna es un Isograma.\n`;
    }

    return resultado.trim(); // Elimina posibles espacios en blanco al final
}

// Ejemplo de uso
console.log(palabras("Uruguay", "Amor"));
