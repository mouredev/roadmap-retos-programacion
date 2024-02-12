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

const cadena = "anita lava la tina"

    //at
let index = 5 //at toma un valor numérico y hace la bsuqueda
console.log(`el index número: ${index} regresara el carácter: "${cadena.at(index)}" de la cadena de texto`) //buscara en la cadena el carácter que este en la posición que especificamos
let negativeíndex = -3
console.log(`el index número: ${negativeíndex} regresara el carácter: "${cadena.at(negativeíndex)}" de la cadena de texto`) //si usamos un index negativo, la búsqueda del carácter comenzara desde el final de la cadena

    // charAt
let charnum = 6
console.log(`el index número: ${charnum} regresara el carácter: "${cadena.charAt(charnum)}" de la cadena de texto`) //buscara en la cadena el carácter que este en la posición que especificamos
let charnegative = -3
console.log(`el index número: ${charnegative} regresara el carácter: "${cadena.charAt(charnegative)}" de la cadena de texto`) //charAt no funciona con indices negativos

    // concat
const cadena2 = "no lavo nada anita"
console.log(cadena.concat(cadena2)) //concatenara ambas cadenas
console.log(cadena.concat(", ",cadena2)) //nos permite agregar una cadena intermedia para agregar espacios o comas

    // endsWith
console.log(cadena.endsWith('tina')) //regresa true o false si la cadena termina con los caracteres que hemos dado como parámetros
console.log(cadena.endsWith('tina', 20)) //no entiendo esta parte todavía

    // indexOf
const searchTerm = "lava"
console.log(`el index de la palabra "${searchTerm}" es: "${cadena.indexOf(searchTerm)}"`) //regresa el index del primer carácter que componga el parámetro especificado

    // repeat
const palabra = "Feliz "
console.log(`hoy me encuentro muy ${palabra.repeat(3)}!`)

    //include
console.log(`la la palabra tina se encuentra en la cadena ? ${cadena.includes('tina') ? 'verdadero': 'falso'}`) //regresa true o false si el parámetro especificado se encuentra en la cadena


    // replace
const mascota= "A mi me gustan mas los perros que los gatos porque son mas juguetones los perros que los gatos"
console.log(mascota.replace("mi me", 'mi amiga le')) //remplaza un pedazo de la cena con el parámetro especificado

    //replaceAll
const mascotas= "A mi me gustan mas los perros que los gatos porque son mas juguetones los perros que los gatos"
console.log(mascotas.replaceAll('perros', 'mapaches'))

    //slice
console.log(cadena.slice(6,12))

    // split
console.log(cadena.split('a'))
console.log(cadena.split('a')[2])
console.log(cadena.split(' '))
console.log(cadena.split('n'))

    // startsWith
console.log(cadena.startsWith('ani'))

    //substring
console.log(cadena.substring(3, 14))

    // toLocaleLowerCase
const minus = "miNUScuLas"
console.log(minus.toLocaleLowerCase('en-US'))
                                                        // estas funcionan similar a toLowerCase o toUpperCase pero agregando como parámetro un locale-specific case mapping
    //toLocalUpperCase
const mayus = "MayuscuLas"
console.log(mayus.toLocaleUpperCase('en-US'))

    // trim
const saludo = "      Hola   mundo!           "
console.log(saludo.trim())
console.log(saludo.trimEnd())
console.log(saludo.trimStart())
