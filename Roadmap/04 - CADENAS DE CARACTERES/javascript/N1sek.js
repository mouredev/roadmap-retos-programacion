/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 */

const palabra = "Javascript"

//Acceder a un caracter.
console.log(palabra.charAt(0))
console.log(palabra[0]) //Opcion mas moderna, pero no soportada en IE7
console.log("---------------------------")


//Comparar caracteres
let a = "a"
let b = "b"

if(a < b){
    console.log(a + " es menor que " + b) //Se imprime esto porque el valor ASCII de la letra a es menor que la letra b
} else if(a > b){
    console.log(a + " es mayor que " + b)
} else{
    console.log("Son iguales")
}
console.log("---------------------------")

//Substring
console.log(palabra.substring(1,3)) //Primera letra se incluye y la utlima NO se incluye
console.log(palabra.substring(2)) //Se imprime a partir de la letra seleccionada hasta el final
console.log("---------------------------")

//Longitud
const emoji = "😄" 
console.log(palabra.length)
console.log(palabra.length - 1) //Tambien se le puede restar a la longitud

console.log(emoji.length) //Devuelve 2 debido a que Javascript usar utf-16 para representar caracteres
console.log([...emoji].length) //De esta manera devuelve el numero de caracteres

console.log("---------------------------")

//Concatenacion
let nombre = "Denis"
let frase = "Hola, me llamo"

console.log("Hola, me llamo " + nombre) //Usando el operador +
console.log(`Hola, me llamo ${nombre}`) //Usando plantillas literales. No soportado en IE7
console.log(frase.concat(" ", nombre)) //Usando concat()

console.log("---------------------------")

//Repeticion
console.log(palabra.repeat(3))

console.log("---------------------------")

// Recorrido
for (let i = 0; i < palabra.length; i++) {
    console.log(palabra[i]);
}

console.log("---------------------------")

//Conversion Mayusculas <-> Minusculas
console.log(palabra.toLowerCase())
console.log(palabra.toUpperCase())

console.log("---------------------------")

//Reemplazo
let frase2 = "Hola Hola mundo"
console.log(frase.replace("Hola", "Adios")) //Solo reemplaza la primera coincidencia
console.log(frase.replaceAll("Hola", "Adios")) //Reemplaza todas las coincidencias

console.log("---------------------------")

//Division
let frase3 = "Hola mundo estoy aprendiendo Javascript"
let split = frase3.split(" ")
console.log(split)
console.log("---------------------------")

//Union
let joined = split.join(" ") 
console.log(joined)
console.log("---------------------------")

//Interpolacion (mismo ejemplo que en el apartado concatenacion)
console.log(`Hola, me llamo ${nombre}`)
console.log("---------------------------")

//Verificacion
console.log(frase3.includes("mundo")) // True
console.log(frase3.includes("Mundo")) //False
console.log("---------------------------")

//Trim
let frase4 = "    Hola mundo    "
console.log(frase4)
console.log(frase4.trim()) //Quita los espacios en blanco al principio y al final del string.
console.log(frase4.trimEnd()) //Quita los espacios en blanco al final del string.
console.log(frase4.trimStart()) //Quita los espacios en blanco al principio del string.
console.log("---------------------------")

//Reverse
console.log(split.reverse().join(" "))
console.log("---------------------------")



/*
* DIFICULTAD EXTRA (opcional):
* Crea un programa que analice dos palabras diferentes y realice comprobaciones
* para descubrir si son:
* - Palíndromos
* - Anagramas
* - Isogramas
*/

//Palindromo
function esPalindromo(palabra1){
    return palabra1 === palabra1.split("").reverse().join("")

}
console.log(esPalindromo("somos"))

//Anagrama
function esAnagrama(palabra1, palabra2){
    return palabra1.split("").reverse().join("") === palabra2
}
console.log(esAnagrama("roma", "amor"))

//Isograma
function esIsograma(palabra1){
    let letras = palabra1.split("")
    for (let i = 0; i < letras.length; i++) {
        for (let j = i+1; j < letras.length; j++) {
            if(letras[i] === letras[j]){
                return false
            }
        }
    }
    return true
}
console.log(esIsograma("murcielago"))