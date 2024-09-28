// Concatenación o interpolación por medio de los templates string: ` ${} `
let apellido = "Henao"
let nombreApellido = `Marisol ${apellido}` // Marisol Henao

// Extraer o cortar una cadena pasando índice de inicio y fin
//  H  A  R  R  Y     P  O  T  T   E   R
//  0  1  2  3  4  5  6  7  8  9  10  11
let pelicula = "Harry Potter"
let extraer = pelicula.slice(0, 7) // Harry P

// Buscar el dato que se pasa como argumento en una cadena
let incluir = pelicula.includes("Potter") // true

// Concatenar dos o más cadenas
let descripcion = " es mi saga favorita"
let guardianes = ' y guardianes de la galaxia'
let concatenarCadenas = pelicula.concat( descripcion, guardianes) // Harry Potter es mi saga favorita y guardianes de la galaxia
concatenarCadenas = pelicula.concat(" es").concat(" maravilloso") // Harry Potter es maravilloso

// eliminar espacios iniciales y finales de una cadena
let eliminarEspacios = descripcion.trim() // es mi saga favorita

// Fragmentar el texto cada que encuetre el dato que se pasa como agurmento 
let fragmentar = pelicula.split("") // [ 'H', 'a', 'r', 'r','y', ' ', 'P', 'o','t', 't', 'e', 'r' ]

// Reemplazar un caracter o cadena por otro
let reemplazar = pelicula.replace("r","p") // Hapry Potter

// Reemplazar un caracter más de una vez. g: global, capturar todo; i: ignorar mayúsculas y minúsculas
reemplazar = pelicula.replace(/r/gi,"p") // Happy Pottep

// Encontrar índice de un caracter (el primero) en una cadena, devuleve -1 si no lo encuentra 
let primerCaracter = pelicula.indexOf("t") // 8

// Encontrar indice de un caracter (el último) en una cadena desde el index 8 hacia atrás
let ultimoCaracter = pelicula.lastIndexOf("r", 8) // 3

// Encontrar la longitud de una cadena
let longitud = pelicula.length-1 // 11

// Convertir una cadena a mayúsculas
let mayusculas = pelicula.toUpperCase() // HARRY POTTER

// Convertir una cadena a minúsculas
let minusculas = pelicula.toLowerCase() // harry potter

// Acceder a un caracter pasanso su índice
let accederCaracter = pelicula.charAt(0) // H
accederCaracter = pelicula[0] // H

// Unir un los elementos de un arreglo en una sola cadena
let array = ["estoy", "aprendiendo a", "programar en js"]
let unir = array.join(" ") // estoy aprendiendo a programar en js

// Saber si una cadena inicia con una subcadena específica. Distingue entre mayúscaulas y minúsculas
let comienzaCon = unir.startsWith("estoy") // true

// Saber si una cadena termina con una subcadena específica. Distingue entre mayúscaulas y minúsculas
let terminaCon = unir.endsWith("en js") // true

// Operaciones combinadas
let operacionesCombinadas = pelicula.toUpperCase().slice(0, 5).split("") // [ 'H', 'A', 'R', 'R', 'Y' ]

// ----------> Ejercicio: palíndromos <----------

let palabra1 = "AniMal"
let palabra2 = "lamINa"
let longitudPal2 = palabra2.length-1

function palindromo (palabra1, palabra2) {
    palabra1 = palabra1.toLowerCase()
        
    let arr = []
    for(let j=longitudPal2; j>=0; j--) {
        arr.push(palabra2[j])
    }
    let unionPalabra2 = arr.join("").toLowerCase()
    
    if (palabra1 === unionPalabra2) {
        return `Es un palíndromo: ${palabra1} = ${unionPalabra2}`
    } 
}
let resultado = palindromo(palabra1, palabra2)
console.log(resultado)