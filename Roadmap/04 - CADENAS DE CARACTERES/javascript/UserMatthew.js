
/* #04 CADENAS DE CARACTERES
   ## Ejercicio
 */
// ---- Crear Cadenas ----
let nombre = "Andres"
let apellido = "Machuca"

// ---- Concatenar Cadenas ----
let nombreCompleto = nombre + " " + apellido
console.log(nombreCompleto)
let nombreCompleto2 = `${nombre} ${apellido}`
console.log(nombreCompleto2)

// ---- Longitud de cadena ----
console.log(nombreCompleto.length)

// ---- Acceder a un caracter especifico ----
console.log(nombreCompleto[0])
console.log(nombreCompleto.charAt(7))

// ---- Convertir en mayuscula o miniscula todo ----
console.log(nombreCompleto.toUpperCase())
console.log(nombreCompleto.toLowerCase())

// ---- Extraer parte de una cadena ----
console.log(nombreCompleto.slice(0, 6))
console.log(nombreCompleto.substring(7, 14))

// ---- Reemplazar parte de una cadena ----
console.log(nombreCompleto.replace("Machuca", "Machado"))

// ---- Buscar dentro de una cadena ----
console.log(nombreCompleto.indexOf("Machuca"))   // Devuelve el inicio de la posicion en la cadena
console.log(nombreCompleto.indexOf("Fernando"))  // Devuelve -1 si no se encuentra el valor
console.log(nombreCompleto.includes("Fernando")) //Devuelve un Booleano
console.log(nombreCompleto.endsWith("Machado"))  // Devuelve un Booleano

// ---- Buscar dentro de una cadena ----
console.log(nombreCompleto.repeat(3))

// ---- Dividir una cadena ----
let lista = "manzana,pera,banana";
console.log(lista.split(","))

// ---- Eliminar espacios en blanco ----
let saludo = "     Hola gente           "
console.log(saludo)
console.log(saludo.trim())

// ---- Convertir valores numericos a cadena ----
let numero = 123;
console.log(numero.toString());
// ---- Sustituir caracteres usando expresiones regulares ----
let textoRegExp = "Hola 1234";
console.log(textoRegExp.replace(/\d/g, "*"))

// ---- Invertir una cadena ----
console.log(nombreCompleto.split("").reverse().join(""))

// ---- Contar la cantidad de veces que se repite una letra ----
console.log(nombreCompleto.split("a").length - 1)



function analizarPalabras(Primera, segunda) {
   anagramas(Primera, segunda)
   sonPalindromos(Primera, segunda)
   Isogramas(Primera, segunda)
}

function anagramas(Primera, segunda) {
   let palabraInertida = Primera.toLowerCase().split("").reverse().join("");
   if (palabraInertida === segunda.toLowerCase()) {
      console.log(`Las palabras ${Primera} y ${segunda} son anagramas`);
   } else {
      console.log(`Las palabras ${Primera} y ${segunda} no son anagramas`);
   }
}

function palindromo(palabra) {
   let normal = palabra.toLowerCase();
   let invertida = normal.split("").reverse().join("");
   return invertida === normal
}

function sonPalindromos(palabra1, palabra2) {
   if (palindromo(palabra1) && palindromo(palabra2)) {
      console.log(`Las palabras ${palabra1} y ${palabra2} son palíndromos`);
   } else{
      console.log(`Las palabras ${palabra1} y ${palabra2} no son palíndromos`);
   }
}


function esIsograma(palabra){
   let letras = new Set();
    let normalizada = palabra.toLowerCase(); 
    
    for (let letra of normalizada) {
        if (letras.has(letra)) {
            return false; 
        }
        letras.add(letra);
    }
    return true;
}

function Isogramas(primera, segunda) {
   if (esIsograma(primera) && esIsograma(segunda)) {
      console.log(`Las palabras ${primera} y ${segunda} son Isogramas`);
   }
   else {
      console.log(`Las palabras ${primera} y ${segunda} no son Isogramas`);
   }
}
  
analizarPalabras("murcielago" , "hola")

