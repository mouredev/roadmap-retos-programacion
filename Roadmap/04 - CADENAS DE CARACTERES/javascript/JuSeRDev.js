let saludo = "Hola!"
let lenguaje = "JavaScript"

let saludar = saludo + " "+ lenguaje
console.log(saludar);

console.log(saludar.length)

console.log(saludar[0])
console.log(saludar[1])
console.log(saludar[2])
console.log(saludar[3])
console.log(saludar[4])
console.log(saludar[5])
console.log(saludar[6])
console.log(saludar[7])
console.log(saludar[8])
console.log(saludar[9])
console.log(saludar[10])
console.log(saludar[11])
console.log(saludar[12])
console.log(saludar[13])
console.log(saludar[14])
console.log(saludar[15])


let extraccion = saludar.substring(0,10)
console.log(extraccion)

let extraccion2 = saludar.slice(-16,-5)
console.log(extraccion2);





// const confirmacion = (palabra, palabra2)=>{
//     let invertido = ""
//     let invertido2 = ""
//     for (let i =  palabra.length -1; i >= 0 ; i--) {
//         invertido += palabra[i]
//     }
//     for (let i =  palabra2.length -1; i >= 0 ; i--) {
//         invertido2 += palabra2[i]
//     }
//     if (invertido === palabra) {
//         console.log(`la palabra: ${palabra} es un Palindromo`)
//     } else {
//         console.log(`la palabra: ${palabra} no es un Palindromo`)
//     }
//     if (invertido2 === palabra2) {
//         console.log(`la palabra: ${palabra2} es un Palindromo`)
//     } else {
//         console.log(`la palabra: ${palabra2} no es un Palindromo`)
//     }
// }

// confirmacion("casa", "lateleletal")

// const confirmacion = (palabra1, palabra2)=>{
//      //seprala la palabra en caracteres convirtiendolo en un array, luego lo pone alrevez y luego lo vuelve a unir en una cadena de texto
//     let invertido1 = palabra1.split("").reverse().join("")
//     let invertido2 = palabra2.split("").reverse().join("")
//     if (palabra1 === invertido1) {
//         console.log(`la plabra ${palabra1} es un Palindromo`)
//     } else {
//         console.log(`La palabra ${palabra1} no es un Palindromo`)
//     }
//     if (palabra2 === invertido2) {
//         console.log(`la plabra ${palabra2} es un Palindromo`)
//     } else {
//         console.log(`La palabra ${palabra2} no es un Palindromo`)
//     }
    
// }
// confirmacion("casa", "oso")



const invertirPalabra = (palabra)=> palabra.split("").reverse().join("")
const esPalindromo = (palabra) =>{
    const invertida = invertirPalabra(palabra)
    if (invertida === palabra) {
        return `la palabra: "${palabra}" es un palindromo`
    } else{
        return `la palabra "${palabra}" no es un palindromo`
    }
}

const esAnagrama = (opcion1, opcion2)=>{
    let separacion1 = opcion1.split("").sort()
    let separacion2 = opcion2.split("").sort()
    console.log(separacion1)
    console.log(separacion2)
    if (separacion1.length === separacion2.length && separacion1.join("") === separacion2.join("")) {
        return `la palabras 1: ${opcion1} y 2: ${opcion2} son un anagrama`
    } else{
        return `la palabras 1: "${opcion1}" y 2: "${opcion2}" no son un anagrama`
    }
}

const esIsograma = (palabra1, palabra2)=>{
    let isograma = new Set();
    (palabra1 + palabra2).split("").forEach(letra => isograma.add(letra))
    if (isograma.size === (palabra1.length + palabra2.length)) {
        console.log("si");
        return `Las palabras "${palabra1}" y "${palabra2}" son isogramas`
    } else {
        console.log("no");
        
        return `Las palabras "${palabra1}" y "${palabra2}" no son isogramas`
    }
}

const confirmacion = (palabra1, palabra2)=>{
    let resultado = []
    
    resultado.push(esPalindromo(palabra1))
    resultado.push(esPalindromo(palabra2))
    resultado.push(esAnagrama(palabra1, palabra2))
    resultado.push(esIsograma(palabra1, palabra2))
    
    console.log(esPalindromo(palabra1));
    console.log(esPalindromo(palabra2));
    console.log(esAnagrama(palabra1, palabra2))
    console.log(esIsograma(palabra1, palabra2))
//<<<<<<< main
    
=======

//>>>>>>> main
    return resultado.join("\n")
    
}

console.log(confirmacion("casa", "oso"))

//<<<<<<< main
//=======
console.log(confirmacion("perro", "lateleletal"))
//>>>>>>> main
