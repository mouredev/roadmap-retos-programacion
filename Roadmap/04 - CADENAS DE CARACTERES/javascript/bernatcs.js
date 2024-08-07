// ** EJERCICIO

// Acceso a caracteres específicos
let str = "Hola"
str.charAt(1) // "o"
str[1] // "o"

// Longitud
str.length // 4

// Subcadenas
str.substring(1, 3) // "ol"
str.slice(1, 3) // "ol"

// Concatenación
let str2 = " Mundo"
str + str2 // "Hola Mundo"
str.concat(str2); // "Hola Mundo"
`Hola,${str2}` // "Hola, Mundo"

// Repetición
str.repeat(2) // "HolaHola"

// Recorrido
for (let char of str) {
  (char); // 'H', 'o', 'l', 'a'
}

// Conversión a mayúsculas y minúsculas
str.toUpperCase() // "HOLA"
str.toLowerCase() // "hola"

// Reemplazo
str.replace("a", "o") // "Holo"
"banana".replace("a", "o") // "bonana"
"banana".replaceAll("a", "o") // "bonono"

// Separación
str.split("") // ["H", "o", "l", "a"]
str.split("", 2) // ["H", "o"]

// Unión
let arr = ["H", "o", "l", "a"];
arr.join("") // "Hola"

// Verificación
str.includes("ol") // true
str.startsWith("Ho") // true
str.endsWith("la") // true

// Búsqueda
str.indexOf("o") // 1
str.lastIndexOf("o") // 1
str.search(/o/) // 1

// Eliminación de espacios
let strWithSpaces = "  Hola  ";
strWithSpaces.trim() // "Hola"
strWithSpaces.trimStart() // "Hola  "
strWithSpaces.trimEnd() // "  Hola"

// Conversión
let num = 123;
String(num) // "123"
num.toString() // "123"

// Comparación
"a".localeCompare("a") // 0
"a".localeCompare("b") // -1
"a".localeCompare("1") // 1

// Extracción de códigos Unicode
str.charCodeAt(1) // 111

// Otros
str.padStart(6, "0") // "00Hola"
str.padEnd(6, "0") // "Hola00"
String.fromCharCode(72, 111, 108, 97) // "Hola"

// ** EXTRA ** ----------------------------------------------------------------------------------------------------------------------------------------------------------

function palindromo(palabra1, palabra2) {

    palabra1 = palabra1.toLowerCase().trim()
    palabra2 = palabra2.toLowerCase().trim()

    if (palabra1.split("").reverse().join("") == palabra2) {
        console.log(`Las palabra ${palabra1} y ${palabra2} son palíndromo`)
    } else {
        console.log(`La palabra ${palabra1} y ${palabra2} NO son palíndromo`)
    }
}

function analgamas(palabra1, palabra2) {

    palabra1 = palabra1.toLowerCase().trim()
    palabra2 = palabra2.toLowerCase().trim()

    if (palabra1.split("").sort().join("") == palabra2.split("").sort().join("")) {
        console.log(`Las palabras ${palabra1} y ${palabra2} son anagramas`)
    } else {
        console.log(`Las palabras ${palabra1} y ${palabra2} NO son anagramas`)
    }
}

function isograma(palabra) {
    palabra = palabra.toLowerCase().trim()
    let set = new Set(palabra.split(""))
    if (palabra.split("").length == set.size) {
        console.log(`La palabra ${palabra} es un isograma, no contiene letras repetidas`)
    } else {
        console.log(`La palabra ${palabra} NO es un isograma, contiene letras repetidas`)
    }
}

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

function comprobacionPalabras(){
    readline.question('Este programa va a comparar dos palabras. Introduce la primera palabra: ', (palabra1) => {
        readline.question('Introduce la segunda palabra: ', (palabra2) => {
            readline.question('¿Cómo las quieres comparar?\n[Palíndromos] - [Anagramas] - [Isogramas] ', (respuesta) => {
                switch (respuesta.toLowerCase()) {
                    case 'palíndromos':
                        palindromo(palabra1, palabra2)
                        comprobacionPalabras();
                        break;
                    case 'anagramas':
                        analgamas(palabra1, palabra2)
                        comprobacionPalabras();
                        break;
                    case 'isogramas':
                        isograma(palabra1)
                        isograma(palabra2)
                        comprobacionPalabras();
                        break;
                    default:
                        console.error(`No reconocí "${respuesta}".`);
                        comprobacionPalabras();
                }
            });
        });
    });
}

comprobacionPalabras()


