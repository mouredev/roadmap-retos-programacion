const string1 = "El cielo está soleado"
const string2 = "puede que hoy llueva"

//Concatenación
console.log(string1 + " pero " + string2)
console.log(`${string1} pero ${string2}`)

//Index de un caracter en específico
console.log(string1[5]) //e

//Subcadena
console.log(string1.slice(9,21)) //está soleado

//Longitud
console.log(string1.length); //21

//División
const listaColores = "rojo, amarillo, azul, morado"
let separar = string1.split(",");
console.log(separar); //(4) ["rojo", "amarillo", "azul", "morado"]

//Conversión mayúsculas
console.log(string2.toUpperCase()); //PUEDE QUE HOY LLUEVA

//Conversión minúsculas
console.log(string1.toLowerCase()); //el cielo está soleado

//Reemplazo
console.log(string1.replace("soleado", "nublado")) //"El cielo está nublado"

//Verificación
console.log(string1.includes("llueva")); //true

// Repetir
console.log(string2.repeat(3)); //

//Busqueda de posición
console.log(string1.search("elo")); //5

   /* DIFICULTAD EXTRA (opcional):
    * Crea un programa que analice dos palabras diferentes y realice comprobaciones
    * para descubrir si son:
    * - Palíndromos
    * - Anagramas
    * - Isogramas
    */ 

//Palíndromo
function palindromo(palabra) {
palabraInvertida = "";
    for (i = palabra.length - 1; i >= 0; i--) {
        palabraInvertida += palabra[i];
    }
    if (palabra===palabraInvertida) {
        console.log("Es palíndromo");
    } else {
        console.log("No es palíndromo");
    }
}

//Anagrama
function anagrama(palabra1, palabra2) {
    const arr1 = palabra1.toLowerCase().split('').sort().join('');
    const arr2 = palabra2.toLowerCase().split('').sort().join('');
    if (arr1 === arr2) {
        console.log("Es un anagrama");
    } else {
        console.log("No es un anagrama");
    }
}

//Isograma
function isograma(palabra) {
    const array = palabra.toLowerCase().split('');
    const set = new Set(array);
    if (array.length === set.size) {
        console.log("Es un isograma");
    } else {
        console.log("No es un isograma");
    }
}

const palabra1 = "reconocer";
const palabra2 = "ballena";
const palabra3 = "llenaba";
const palabra4 = "cuervo";


palindromo(palabra1); //True
palindromo(palabra4); //False

anagrama(palabra2, palabra3); //True
anagrama(palabra3, palabra4); //False

isograma(palabra4); //True
isograma(palabra1); //False