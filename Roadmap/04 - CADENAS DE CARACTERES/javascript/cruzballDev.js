/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 */

let texto1 = "¡Hola Mundo! "
let texto2 = "Me llamo Antonio"
let texto3 = "¡HOLA JAVASCRIPT!"

// Acceso a caracteres específicos
console.log(texto1[1])
console.log(texto1[4])// Accedemos a dichos caracteres mediante el indice.

// Subcadenas
console.log(texto1.slice(6)) // Resultado: Mundo!; Extrae a partir de la 6 posición sin tener en cuenta esta última.
console.log(texto1.slice(0,5))// Resultado: !Hola; Extrae a partir de la posición 0 hasta la 6 sin tener en cuenta esta última.

// Longitud
console.log(texto1.length) //Resultado:13; Da la longitud de la cadena de texto o String.

// Concatenación
console.log(texto1 + ", " + texto2 + " y así concatenamos de distintas formas.")

//Repetición
console.log(texto1.repeat(5)) // Repite el String 5 veces.

//Recorrido
console.log()
for(let i = 0; i < texto1.length; i++) { // Recorre el String caracter a caracter.
    console.log(texto1[i])
}

//Conversión a Mayusculas
console.log(`Covertir el String "¡Hola mundo!" en mayusculas: ` , texto1.toLocaleUpperCase())

//Conversión a Minusculas
console.log(texto3)
console.log(`Covertir el String "¡HOLA JAVASCRIPT!" en minusculas: ` , texto3.toLocaleLowerCase())

// Reemplazo
texto1 = "¡Hola Mundo! "
console.log(texto1.replace("Mundo", "gente")) // "Mundo" es el texto que se busca y "gente" por el que se sustituye.

console.log(texto1.replaceAll("¡Hola Mundo!","¡Buenas People!")) // Con replaceAll remplazamos  todas las palabras del String.

// División de un String en palabras
let texto4 = "Hola, ¿qué tal estás?"
console.log(texto4.split(",")) // Convierte un String en un Array y si hay una coma entremedias del string, los separa en distintos grupos (antes de la coma y después de la coma).
console.log(texto4.split(" ")) // Convierte un String en un Array de palabras. (Cuidado con los espacios al final, porque los cuenta como en string en vacio,
                              // ya que cuenta las palabras guiandose por los espacios en blanco).
console.log(texto4.split("")) // Así se convierte un String en un Array de Caracteres o letras.

// Unión
let frutas = ["pera", "manzana", "tomate"]
console.log(frutas.join(" ")) // Unir varias palabras de un Array en un único String de palabras.
console.log(frutas.join("")) // Unir varias palabras de un Array en un único String como si fuera una frase.

// Interpolación
console.log(`Esto es un saludo: ${texto1};`)

//Verificación
console.log(typeof(texto1)) // Con typeof comprobamos el tipo de dato y verificamos que es un String.

// Eliminación de espacios al principio y al final
let texto5 = "   Eliminar espacios al principio y al final   "
console.log(texto5.trim())

// Convertir Números a String
let numero = 1234
console.log(numero.toString()) // Devuelve un string pero no modifica el valor de la variable.
console.log(typeof numero)

console.log(numero = String(numero)) // Modifica el valor de la variable y devuelve el nuevo valor
console.log(typeof numero)

// Convertir String a Números
console.log(numero = Number(numero)) // para cambiar realmente el valor, tenemos que igualar el valor de la variable al nuevo valor.
console.log(typeof numero)

// Convertir a Float
let aFloat = "15.4"
console.log(aFloat)
console.log(parseFloat(aFloat)) // Convierte una cadena de texto en float.

// Convertir a Entero
console.log(parseInt(aFloat)) // Convierte una cadena de texto en entero.

// Busqueda
console.log(texto1.includes(["a"])) // Buscamos si está la letra o caracter a en el texto1 = "¡Hola Mundo! ".
console.log(texto1.includes(["p"]))

console.log(   )

 /* DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
