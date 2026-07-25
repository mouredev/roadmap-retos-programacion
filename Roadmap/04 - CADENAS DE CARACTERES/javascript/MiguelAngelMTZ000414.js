console.warn("----------(◉◉∖____/◉◉)---------- Cadena de Caracteres ----------(OO∖____/OO)----------")

let v1_string = "Lamborghini" // Cadena de caracteres "String", comillas dobles
let v2_string = 'Gallardo LP' // Cadena de caracteres "String", comillas simples
let v3_string = `560-4` // Cadena de caracteres "String", comillas invertidas
console.log(typeof v1_string) // Tipo de dato "String"
console.log(typeof v2_string) // Tipo de dato "String"
console.log(typeof v3_string) // Tipo de dato "String"
console.log(v1_string.length) // Longitud String
console.log(v2_string.length) // Longitud String
console.log(v3_string.length) // Longitud String
console.log(v1_string) // Imprimiendo por consola 
console.log(v2_string) // Imprimiendo por consola 
console.log(v3_string) // Imprimiendo por consola

console.warn("------------------------------- Concatenación -------------------------------")
console.log(v1_string + v2_string + v3_string)
console.log(v1_string, v2_string, v3_string)
let concatenacion = v1_string.concat(" ", v2_string, " ", v3_string) // Usando la funtion concat()
console.log(concatenacion)
console.log(typeof concatenacion)
console.log(concatenacion.length)

console.warn("------------------------------- Interpolación -------------------------------")
console.log(`Interpolación de cadenas: ${v1_string} ${v2_string} ${v3_string}}`)

console.warn("------------------------------- Mayusculas toLocaleUpperCase() -------------------------------")
console.log(`${v1_string.toLocaleUpperCase()} ${v2_string.toLocaleUpperCase()} ${v3_string.toLocaleLowerCase()}`) // Funcion toLocaleLowerCase() 

let convertir_1_letraMayuscalas = "miguel"
console.log(convertir_1_letraMayuscalas)
let obtenerEl_1_Valor = convertir_1_letraMayuscalas.charAt(0).toUpperCase()
console.log(obtenerEl_1_Valor + convertir_1_letraMayuscalas.slice(1))

console.warn("------------------------------- Minusculas toLocaleLowerCase() -------------------------------")
console.log(`${v1_string.toLocaleLowerCase()} ${v2_string.toLocaleLowerCase()} ${v3_string.toLocaleLowerCase()}`) // Funcion toLocaleLowerCase() 

console.warn("------------------------------- Acceso a caracteres específicos chartAt() -------------------------------")
console.log(v1_string)
console.log(v1_string.charAt(0)) // Funtion charAt()
console.log(v1_string.charAt(1)) // Funtion charAt()
console.log(v1_string.charAt(2)) // Funtion charAt()
console.log(v1_string.charAt(3)) // Funtion charAt()
console.log(v1_string.charAt(4)) // Funtion charAt()
console.log(v1_string.charAt(5)) // Funtion charAt()
console.log(v1_string.charAt(6)) // Funtion charAt()
console.log(v1_string.charAt(7)) // Funtion charAt()
console.log(v1_string.charAt(8)) // Funtion charAt()
console.log(v1_string.charAt(9)) // Funtion charAt()
console.log(v1_string.charAt(10)) // Funtion charAt()

console.warn("------------------------------- verificar primer caracter startsWith() -------------------------------")
let v17_string = "BMW 3.0 CSL HOMMAGE"
console.log(v17_string)
console.log(`"B" empieza al principio: ${v17_string.startsWith("B")}`)
console.log(`"b" empieza al principio: ${v17_string.startsWith("b")}`)
console.log(`"bmw" empieza al principio: ${v17_string.startsWith("bmw")}`)
console.log(`"BMW" empieza al principio: ${v17_string.startsWith("BMW")}`)
console.log(`"3.0" empieza al principio: ${v17_string.startsWith("3.0")}`)

console.warn("------------------------------- verificar ultimo caracter endsWith() -------------------------------")
let v4_string = "Porsche 918 Spyder"
console.log(v4_string)
console.log(`"Spyder" se encuentra al final de la cadena: ${v4_string.endsWith("Spyder")}`) // Ultimo caracter true
console.log(`"918" se encuentra al final de la cadena: ${v4_string.endsWith("918")}`) //false
console.log(`"r" se encuentra al final de la cadena: ${v4_string.endsWith("r")}`) //false

console.warn("------------------------------- verificar si existen caracteres en la cadena includes() -------------------------------")
let v5_string = "When Love Takes Over"
console.log(v5_string)
console.log(`"Love" se encuentra en la cadena: ${v5_string.includes("Love")}`)
console.log(`"Loves" se encuentra en la cadena: ${v5_string.includes("Loves")}`)
console.log(`"Two" se encuentra en la cadena: ${v5_string.includes("Two")}`)

console.warn("------------------------------- Busca cadena y devuelve el indice indexOf() -------------------------------")
console.log(v5_string)
// Devuelve la posición de la primera aparición de una subcadena.
// indexOf(searchString: string, position?: number)
// parametro = (searchString): la subcadena que se buscará en la cadena
// parametro (position): el índice en el que se comenzará a buscar el objeto String. Si se omite, la búsqueda comienza al principio de la cadena.
console.log(`Su posición de "L" es: ${v5_string.indexOf("L")}`) // Funtion indexOf(),  
console.log(`Su posición de "o" es: ${v5_string.indexOf("o", 7)}`) // Funtion indexOf(),  
console.log(`Su posición de "v" es: ${v5_string.indexOf("v")}`) // Funtion indexOf(),  
console.log(`Su posición de "e" es: ${v5_string.indexOf("e", 7)}`) // Funtion indexOf(),  
console.log(`Su posición de "Over" es: ${v5_string.indexOf("Over")}`) // Funtion indexOf(),
console.log(`Su posición de "z" es: ${v5_string.indexOf("z")}`) // Funtion indexOf(),

console.warn("------------------------------- Extrae caracteres si coincide en la cadena match() -------------------------------")
// Busca una cadena o un objeto que admita la búsqueda y devuelve una matriz que contiene los resultados de esa búsqueda o null si no se encuentran coincidencias.
let v6_string = "Ive Been Thinking About You"
const regex1 = /[A-Z]/g // Expresión Regular
const regex2 = /[a-z]/g // Expresión Regular
const regex3 = /[A-E]/gi // Expresión Regular
console.log(v6_string)
console.log(v6_string.match(regex1))
console.log(v6_string.match(regex2))
console.log(v6_string.match(regex3))

console.warn("------------------------------- Rellenando una cadena al final y al principio padStart() y padEnd() -------------------------------")
let v7_string = "123"
let v8_string = "CFMOTO 450MT"
console.log(v7_string)
console.log(v7_string.length)
console.log(v7_string.padEnd(6, "."))
console.log(v7_string.padStart(6, "."))

console.log(`${v8_string}, longitud de la cadena: ${v8_string.length}`) // Interpolacion ``
console.log(v8_string.padEnd(17, "⭐"))
console.log(v8_string.padStart(17, "⭐"))

let v9_string = '2034399002125581'
console.log(v9_string)
let Splitt = v9_string.slice(-4)
console.log(Splitt.padStart(v9_string.length, "*"))

console.warn("------------------------------- Repetir una cadena repeat() -------------------------------")
let v10_string = "GO! "
console.log(v10_string)
console.log(v10_string.repeat(3))

console.warn("------------------------------- Remplazando caracteres de una cadena replace() y replaceAll() -------------------------------")
let v11_string = "Asphalt Legends 9"
console.log(v11_string)
console.log(v11_string.replace("9", "Unite"))

let v12_string = "H_O_L_A_H_O_L_A"
console.log(v12_string)
console.log(v12_string.replaceAll("_", "-"))

console.warn("------------------------------- Extraer una sección de una cadena slice() -------------------------------")
let v13_string = "King of the Rodeo"
console.log(v13_string)
console.log(v13_string.slice(0,4))
console.log(v13_string.slice(8))
console.log(v13_string.slice(-5))

console.warn("------------------------------- Eliminiar los espacios de ambos extremos de un cadena trim() -------------------------------")
let v14_string = " Esto es una cadena con espacios "
console.log(v14_string)
console.log(v14_string.trim())

console.warn("------------------------------- Convertir a cadenas de caracteres (String) toString() -------------------------------")
let v15_string = 12345678910
console.log(`${v15_string}, es de tipo ${typeof v15_string}`)
const conversion = v15_string.toString()
console.log(`${conversion}, es de tipo ${typeof conversion}`)
// Convertimos a un Array (matriz/lista) usando la funsion split()
const conversionArray = conversion.split("")
console.log(conversionArray)

let v16_string = ["Uno", "Dos", "Tres"]
console.log(typeof v16_string)
console.log(v16_string)
const Array_String = v16_string.toString()
console.log(typeof Array_String)
console.log(Array_String)

console.warn("------------------------------- Ejercicio Extra -------------------------------")
// Palíndromos: palabras o frase que se lee igual de izquierda a derecha que de derecha a izquierda. Somos o no somos, Son robos o sobornos

// Anagramas: una palabra es anagrama de otra si las dos tienen las mismas letras, con el mismo numero de apariciones, pero en un orden diferente. Raza-Zara, Amor-Roma, Frase-Fresa

// Isogramas: palabra o frase en la que cada letra aparece el mismo número de veces

let ejemplo = "El Tiempo Que Tenemos"
// console.log(ejemplo.split("", 10))
let ejemplo2 = ejemplo.trim().replace(/ /g, "")
// let ejemplo3 = ejemplo2.replace(/ /g, "")
console.log(ejemplo2)

let string = "ElTiempoQueTenemos"
let string2 = string.split("")
console.log(string2)
let string3 = string2.reverse()
console.log(string3)
let string4 = string3.join("")
console.log(string4)

console.log(`${ejemplo2} y ${string4}`)
console.log(ejemplo2 == string4)
console.log(`${string2} y ${string3}`)
console.log(string2 === string3)

console.warn("------------------------------- Palabras Palíndromos -------------------------------")
function Palindromos(palabra1, palabra2) {
    // Convertimos las cadenas de caracteres a minisculas usando la funcion toLocaleLowerCase()
    // Para eliminar los espacios usaremos la función replace(), la parte "/" significa que es una exprecion regultar que busca espacios, y la "/g" significa que es global, es decir busca todos los espacios en la variable. 
    let palabraPalindromo1 = palabra1.toLocaleLowerCase().replace(/ /g, "")
    let palabraPalindromo2 = palabra2.toLocaleLowerCase().replace(/ /g, "")

    // Con la función split("") convertiremos la cadena a una arreglo "Array" de subcadenas
    // Con la funcion reverse() invertiremos el orden de los elementos del Array
    // Con la funcion join("") concarenaremos todos los elementos de Array, devolviendo una nueva cadena
    reverse_cadena = palabraPalindromo2.split("").reverse().join("")
    if (palabraPalindromo1 === reverse_cadena) {
        console.log(`La palabra = ${palabra1} es Palindromo`)
        console.log(`La palabra = ${palabra2} es Palindromo`)
    } else {
        console.log("Las palabras no son Palindromos")
    }
}
Palindromos("Adan y Raza", "Azar y Nada")

console.warn("------------------------------- Palabras Anagramas -------------------------------")
function Anagramas(anagrama1, anagrama2) {
    // Convertimos la cadena en minuscúlas con la función toLocaleLowerCase() y en arreglo de caracteres con la función split("")
    let cambio1 = anagrama1.toLocaleLowerCase().split("")
    let cambio2 = anagrama2.toLocaleLowerCase().split("")
    console.log(cambio1)
    console.log(cambio2)
    // (a, b) => a.localeCompare(b, undefined, { sensitivity: 'accent' }) (Checar el funcionamiento) ?
    // Ordenar el arreglo con la función sort()
    // Convertimos de nuevo el arreglo a una cadena de caracteres con la función join("")
    let ordenar1 = cambio1.sort().join("")
    let ordenar2 = cambio2.sort().join("")
    console.log(ordenar1)
    console.log(ordenar2)
    // Usamos la condición IF para comparar si las cadenas de caracteres son exactamente iguales 
    if (ordenar1 === ordenar2) {
        console.log(`La palabra "${anagrama1}" y la palabra "${anagrama2}" son palabras Anagramas`)
    } else {
        console.log("Estas palabras no son Anagramas")
    }
}
// Anagramas("Amor", "Roma")
Anagramas("Lastre", "Letras")

