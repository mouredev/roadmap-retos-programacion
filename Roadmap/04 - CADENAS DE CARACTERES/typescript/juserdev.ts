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

const texto: string = "hello typeScript"
console.log(texto[0]) //obtiene el caracter en la posicion indicada, en este caso en la posicion 0
console.log(texto.charAt(6)) //hace lo mismo que el anterior
console.log(texto.length) // obtiene la logitud del string

//concatenaciones

const saludar: string = "hola "
const lenguaje: string = "typescript"

console.log(saludar + lenguaje)
console.log(saludar.concat(lenguaje))

// repeticion

console.log(texto.repeat(2)) //repite la cadena de texto n numero de veces

// conversion a mayusculas y minusculas

console.log(texto.toUpperCase())
console.log(texto.toLowerCase())

console.log(texto.replace("hello" , "hi"))
console.log(texto.replace("t" , "T"))

// division
const palabras: string[] = texto.split(" ")
console.log(palabras)

//union

console.log(palabras.join(", "))

//interpolacion
console.log(`Hola ${lenguaje}`)

//verificacion

console.log(texto.startsWith("hello"))
console.log(texto.endsWith("typeScript"))
console.log(texto.includes("type"))

//recorrido

for (const char of texto) {
    console.log(char)
}

//Extra

interface returnFunction { //esto es el retorno de la funcion
    anagrama: string,
    isograma: string,
    palindromo: string
}

const comprobaciones = (a: string, b: string): returnFunction =>{
    let ar = a.split("").reverse().join("")
    let br = b.split("").reverse().join("")
    
    let aa = a.split("").sort().join("")
    let ba = b.split("").sort().join("")
    
    let ai = a.split("").sort().join("")
    let aiSet = [...new Set(ai)].join("")
    let bi = b.split("").sort().join("")
    let biSet = [...new Set(bi)].join("")

    let isograma: string
    
    if (ai === aiSet && bi === biSet) {
        isograma = `Tanto "${a}" como "${b}" son isogramas`
    } else if (ai === aiSet && bi !== biSet) {
        isograma = `"${a}" es un isograma y "${b}" no lo es`
    } else if (ai !== aiSet && bi === biSet) {
        isograma = `"${b}" es un isograma y "${a}" no lo es`
    } else {
        isograma = `Ni "${a}" es un isograma y "${b}" tampoco`
    }

    let anagrama: string 
    anagrama = aa === ba ? `Las palabras "${a}" y "${b}" son anagramas` : `Las palabras "${a}" y "${b}" no son anagramas`

    let palindromo: string

    if (a === ar && b === br) {
        palindromo = `Tanto "${a}" como "${b}" son palindromas`
    } else if (a === ar && b !== br) {
        palindromo = `"${a}" es palindroma y "${b}" no lo es`
    } else if (a!==ar && b === br) {
        palindromo =` "${a}" no es palindroma pero "${b}" si lo es`
    } else{
        palindromo = `Ninguna de las palabras es palindroma`
    }

    return {anagrama, palindromo, isograma}
}

console.log(comprobaciones("carne", "ana"))
console.log(comprobaciones("radar", "ana"))
console.log(comprobaciones("radar", "carlos"))
console.log(comprobaciones("carlos", "ana"))
console.log(comprobaciones("juan", "carlos"))