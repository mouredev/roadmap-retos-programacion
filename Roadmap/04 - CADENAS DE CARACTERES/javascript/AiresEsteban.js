let cadena = "Hola Javascript"

//- Acceso a caracteres específicos
console.log(cadena[0])

//- Subcadenas
console.log(cadena.substring(0,4))
console.log(cadena.slice(5))

//- Longitud
console.log(cadena.length)

//- Concatenación
let cadena2 = "Comencemos!"
console.log(cadena + cadena2)

//- Repetición
console.log(cadena.repeat(2))

//- Recorrido
for (let char of cadena){
    console.log(char)
}

//- Conversión a mayúsculas y minúsculas
console.log(cadena.toUpperCase())
console.log(cadena.toLowerCase())

//- Reemplazo
console.log(cadena.replace("Javascript", "Python"))

//- División
let palabras = cadena.split(" ")
console.log(palabras)

//- Unión
console.log(palabras.join(", "))

//- Interpolación
let profesion = "Desarrollador"
console.log(`Hola, ${profesion}`)

//- Verificación
console.log(cadena.includes("Javascript"))
console.log(cadena.startsWith("Hola"))
console.log(cadena.endsWith("Javascript"))

//- Trim

let mySpacedString = "     Hola    "
console.log(mySpacedString.trim())
console.log(mySpacedString.trimEnd())
console.log(mySpacedString.trimStart())


// Dificulta extra

function esPalindromo(palabra){
    let invertida = palabra.split("").reverse().join("")
    return palabra === invertida
}

function esAnagrama(palabra2,palabra3){
    let sorted1 = palabra2.split("").sort().join("")
    let sorted2 = palabra3.split("").sort().join("")
    return sorted1 === sorted2
}

function esIsograma(palabra){
    let letras = new Set(palabra)
    return letras.size === palabra.length
}

let palabra1 = "anana"
let palabra2 = "roma"
let palabra3 = "amor"

console.log(`"${palabra1}" es un palíndromo? ${esPalindromo(palabra1)}`)
console.log(`¿"${palabra2}" es un palíndromo? ${esPalindromo(palabra2)}`)
console.log(`"${palabra2}" y "${palabra3}" son anagramas?${esAnagrama(palabra2,palabra3)}`)
console.log(`¿"${palabra1}" es un isograma? ${esIsograma(palabra1)}`);
console.log(`¿"${palabra2}" es un isograma? ${esIsograma(palabra2)}`);