// #04 CADENAS DE CARACTERES

// Ejercicio 

// Acceso a caracteres específicos

let cadena = "Hola, mundo!";

console.log("Primer caracter:", cadena[0]);
console.log("Primer caracter:", cadena.charAt(0));

// Subcadena

let subcadena = cadena.substring(6, 11);
console.log("Subcadena:", subcadena);

// Longitud de cadena

console.log("Longitud de la cadena:", cadena.length);

// Concatenación de cadenas

let cadena1 = "Hola";
let cadena2 = "mundo!";

let cadenaConcatenada = cadena1 + " " + cadena2;
console.log("Cadena concatenada:", cadenaConcatenada);

let cadenaConcatenada2 = cadena1.concat(" ", cadena2);
console.log("Cadena concatenada:", cadenaConcatenada2);

// Repetición

let cadenaRepetida = cadena.repeat(3);
console.log("Cadena repetida:", cadenaRepetida);

// Recorrido 

for (let i = 0; i < cadena.length; i++) {
    console.log("Carácter en posición", i, ":", cadena[i]);
}

// Conversión a mayúsculas y minúsculas
console.log("Mayúsculas:", cadena.toUpperCase());
console.log("Minúsculas:", cadena.toLowerCase());

// Reemplazo
let cadenaReemplazada = cadena.replace("mundo", "javascript");
console.log("Reemplazo:", cadenaReemplazada);

// División
let palabras = cadena.split(" ");
console.log("División por espacio:", palabras);

// Unión
let nuevaCadenaUnida = palabras.join(":) ");
console.log("Unión con guiones:", nuevaCadenaUnida);

// Interpolación

let lenguaje = "JavaScript";
console.log(`El lenguaje es ${lenguaje}`);

// Verificación

let contieneHola = cadena.includes("Hola");
console.log("Contiene 'Hola':", contieneHola);

// Dificultad extra

function programa(cadena1, cadena2) {
    function esPalindromo(cadena1, cadena2) {
        return cadena1.toLowerCase() === cadena2.split("").reverse().join("").toLowerCase();
    }
    console.log("Es palíndromo:", esPalindromo(cadena1, cadena2));

    function esAnagrama(cadena1, cadena2) {
        return cadena1.toLowerCase().split("").sort().join("") === cadena2.toLowerCase().split("").sort().join("")
    }
    console.log("Es anagrama:", esAnagrama(cadena1, cadena2));

    function esIsograma(cadena1, cadena2) {
        let caracteres = {};

        for (let i = 0; i < cadena1.length; i++) {
            if (caracteres[cadena1[i].toLowerCase()]) {
                return false;
            }
            caracteres[cadena1[i]] = true;
        }

        for (let i = 0; i < cadena2.length; i++) {
            if (caracteres[cadena2[i].toLowerCase()]) {
                return false;
            }
            caracteres[cadena2[i]] = true;
        }

        return true;
    }
    console.log("Es isograma:", esIsograma(cadena1, cadena2));
}


programa("Hola", "aloh");
programa("Dart", "Go");