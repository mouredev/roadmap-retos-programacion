/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

// Creamos una cadena de texto
let mi_cadena = "Soy una cadena de texto"
console.log(mi_cadena)

//Acceso a caracteres específicos
let caracterY =console.log(mi_cadena[2])

//Longitud de una cadena de texto
let longitud = console.log(mi_cadena.length)

// Contatenación de cadenas de texto
let cadenaNueva= "y estoy creada por alexdevrep"
let cadenaConcatenada = console.log(mi_cadena+" "+cadenaNueva)

//Repetición de una cadena de texto
let cadenaRepetida = console.log(mi_cadena.repeat(3))

//Recorrido de una cadena de texto
for (i=0;i<mi_cadena.length;i++){
    console.log(mi_cadena[i])

}

//Conversión a minúsculas
let cadena_minus = console.log(mi_cadena.toLowerCase())

//Conversión a mayúsculas
let cadena_mayus = console.log(mi_cadena.toUpperCase())

//Reemplazo de caracteres
mi_cadena = mi_cadena.replace ("Soy","I´m")
console.log(mi_cadena)

//División de una cadena de texto
mi_cadena = mi_cadena.slice(8)
console.log(mi_cadena)

//Unión de cadenas de texto
let cadenasDivididas = ["a","b","c"]
let cadenaUnida = console.log(cadenasDivididas.join("-"))

//Interpolación de cadenas de texto
suma = 1+2
console.log(`El resultado de la suma es ${suma}`)

//Verificación de las cadenas de texto
let contiene = console.log(mi_cadena.includes("texto"))


//Dificultad extra

/*
* DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isograma

*/


function palabra3invertida(palabra3){
    palabra3reverse = palabra3.split("").reverse().join("")
    return palabra3reverse
}


function palabra4invertida(palabra4){
    palabra4reverse = palabra4.split("").reverse().join("")
    return palabra4reverse
}



function palindromo(inversion3,inversion4){
   
    if (inversion3 === palabra3){
        console.log("Esta palabra es un palíndromo")
    }
    else{
        console.log ("Esta palabra no es un palíndromo")
    }
    if (inversion4 === palabra4){
        console.log("Esta palabra es un palíndromo")
    }
    else{
        console.log ("Esta palabra no es un palíndromo")
    }
}

function Anagrama (palabra3, palabra4){
    let array3 = palabra3.split("").sort().join("")
    let array4 = palabra4.split("").sort().join("")
    
    if (array3 === array4){
        console.log("Estas palabras son anagramas")
    }
    else{
        console.log("Estas palabras no son un anagrama")
    }

}

function Isograma(palabra3,palabra4){
    let palabra3set = palabra3.split("")
    let palabra4set = palabra4.split("")
    let set3 = [...new Set (palabra3)]
    let set4 = [...new Set (palabra4)]
    console.log(set3)
    console.log(palabra3set)
    console.log(set4)
    console.log(palabra4set)
    
    if (set3.length == palabra3set.length){
        console.log("Esta palabra es un isograma")
    }
    else{
        console.log("Esta palabra no es un isograma")
    }
    if (set4.length == palabra4set.length){
        console.log("Esta palabra es un isograma")
    }
    else{
        console.log("Esta palabra no es un isograma")
    }
        

}


const prompt = require('prompt-sync')()
let palabra3 = prompt("Introduce la primera palabra al sistema: ")
let palabra4 = prompt("Introduce la segunda palabra al sistema: ")
inversion3 = palabra3invertida(palabra3)
inversion4 = palabra4invertida(palabra4)
palindromo(inversion3,inversion4,palabra3,palabra4)
Anagrama(palabra3,palabra4)
Isograma(palabra3,palabra4)













