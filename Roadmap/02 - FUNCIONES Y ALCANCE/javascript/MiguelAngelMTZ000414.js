console.log(`----------(◉◉∖____/◉◉)---------- Functions ----------(OO∖____/OO)----------

    Ejemplos de funciones básicas que representa JavaScript:
    -- Sin parámetros ni retorno, 
    -- Con uno o varios parámetros, 
    -- Y con retorno...
    `
)

// Declaramos la funcion sin parametros
function ejemplo_1(){
    // Imprimiendo por consola
    console.log("-. Este es un ejemplo de una función sin paremetros, ni return, imprimiendo por consola.")
} 
ejemplo_1() // Llamando a la función

// Declaramos la función con un solo paremetro/argumento
function ejemplo_2(paremetro_String){
    // Imprimiendo por consola al parametro "paremetro_String"
    console.log(paremetro_String)
}
ejemplo_2("-. Este es un ejemplo de una funcion con un solo parametro de tipo 'String', imprimiendo por consola.") // Llamando a la función

// Declaramos la función con dos paremetro/argumento
function ejemplo_3(parametro_String, parametro_Number){
    // Imprimiendo por consola los dos parametro "paremetro_String" y "parametro_Numbre"
    console.log("-. Este es un ejemplo de una funcion con dos parametro de tipo 'String' y 'Number', imprimiendo por consola.", parametro_String + " " + parametro_Number)
}
ejemplo_3("McLaren W1", 2024) // Llamando a la función

// Declaramos la función con tres parametros/argumento
function ejemplo_4(parametro_String, parametro_Number, parametroString) {
    // Usamos return para devolver el valor
    return `-. Este es un ejemplo de una funcion con tres parametro de tipo 'String', 'Number' y 'String', usando 'return' palabra reservada. ${parametro_String}, ${parametro_Number}, ${parametroString}`
}
console.log(ejemplo_4("Porsche", 918, "Spyder")) // Mandamos a llamar por consola la función

// Declaramos la función con dos paremetro/argumento
function ejemplo_5(parametro_String, parametro_Number){
    // Imprimiendo por consola los dos parametro "paremetro_String" y "parametro_Numbre"
    console.log("-. Este es un ejemplo de una funcion con dos parametro de tipo 'String' y 'Number', imprimiendo por consola.", parametro_String + " " + parametro_Number)
}
ejemplo_3(2024, "McLaren W1") // Llamando a la función

// Declaramos la función con tres parametros/argumento
function ejemplo_6(parametro_Number, parametroNumber) {
    // Usamos return para devolver el valor
    return `-. Este es un ejemplo de una funcion con dos parametros de tipo 'Number', usando 'return' palabra reservada. Sumando ${parametro_Number} + ${parametroNumber} = ${parametro_Number + parametroNumber}`
}
console.log(ejemplo_6(918, 82)) // Mandamos a llamar a la función por consola 

// Declaramos la función con dos parametros/argumentos predeterminados
function ejemplo_7(parametro_Number = 100, parametroNumber = 76) {
    // Usamos return para devolver el valor
    return `-. Este es un ejemplo de una funcion con dos parametros predeterminados de tipo 'Number', usando 'return' palabra reservada. Sumando ${parametro_Number} - ${parametroNumber} = ${parametro_Number - parametroNumber}`
}
console.log(ejemplo_7()) // Mandamos a llamar a la función por consola 

let parametroNumber_1 = 24
let parametroNumber_2 = 10
// Declaramos la función con dos parametros/argumentos predeterminados
function ejemplo_8(parametro_Number_1, parametro_Number_2) {
    // Usamos return para devolver el valor
    return `-. Este es un ejemplo de una funcion con dos parametros predeterminados de tipo 'Number', usando 'return' palabra reservada. Sumando ${parametro_Number_1} x ${parametro_Number_2} = ${parametro_Number_1 * parametro_Number_2}`
}
console.log(ejemplo_8(parametroNumber_1, parametroNumber_2)) // Mandamos a llamar a la función por consola 

console.log(`----------(◉◉∖____/◉◉)---------- Functions ----------(OO∖____/OO)----------

    - Comprobar si se puede crear funciones dentro de funciones.
    function name(params) {
        function name(params) {
        
        }
    }
    `
)
// Declaramos la función "funcionInterno()", con un argumento
function funcionInterno(a) { // Funcion Principal/Padre
    
    function functionExterno(b) { // Funcion anidada/Hijo
        /* La funcion "functionExterno()" toma el argumento que se le pasa a la función "functionInterno(5)".
           Para posteriormente SUMAR el argumento(5) x  2 */
        return b * 2 // Retorna: 10
    }
    /* Retornamos la función "functionExterno(), la cual hara la suma 10 + 3 = 13 " */
    return functionExterno(a) + 3
}
console.log("El resultado de la funcion es: " + funcionInterno(5)) // Salida: 13

console.log(`----------(◉◉∖____/◉◉)---------- Predefined Functions ----------(OO∖____/OO)----------

    - Utilizando algúnos ejemplos de funciones ya creadas en el lenguaje.

    - ⭐substring  - codePointAt    - normalize     - toString
    - ⭐indexOf    - concat         - padEnd        - toUpperCase
    - ⭐lenght     - endsWith       - padStart      - trim
    - ⭐split      - includes       - repeat        - trimEnd
    - ⭐replace    - lastIndexOf    - repeatAll     - trimStart
    - at           - localeCompare   - slice         - valueOf
    - chartAt      - match           - startsWith    
    - charCodeAt   - matchAll        - toLowerCase   
    `
)
console.log("-------------------------------- substring() --------------------------------")
let funcion_1 = "Miguel Angel"
console.log(funcion_1)
console.log(funcion_1.substring(1, 8))

console.log("-------------------------------- indexOf() --------------------------------")
let funcion_2 = "McLaren Ferrari Lamborghini Porsche"
console.log(funcion_2)
console.log(funcion_2.indexOf("Ferrari"))

console.log("-------------------------------- lenght() --------------------------------")
let funcion_3 = "McLaren Ferrari Lamborghini Porsche"
console.log(funcion_3)
console.log(funcion_3.length)

console.log("-------------------------------- split() --------------------------------")
let funcion_4 = "1,2,3,4,5,6,7,8,9,10"
console.log(`Cadenas de texto "1,2,3,4,5,6,7,8,9,10" ${typeof funcion_4}`)
funcion_4_1 = funcion_4.split(",")
console.log(funcion_4_1)
console.log(typeof funcion_4_1)

console.log("-------------------------------- replace() --------------------------------")
let funcion_5 = "ASPHATL LEGENDS 9"
console.log(funcion_5)
console.log(funcion_5.replace("9", "Unite"))

console.log("-------------------------------- at() --------------------------------")
let funcion_6 = "When Love Takes Over"
console.log(funcion_6)
console.log(funcion_6.at(0))
console.log(funcion_6.at(1))
console.log(funcion_6.at(2))
console.log(funcion_6.at(3))

console.log("-------------------------------- chartAt() --------------------------------")
let funcion_7 = "Ooh Ahh (My Life Be Like)"
console.log(funcion_7)
console.log(funcion_7.charAt(0))
console.log(funcion_7.charAt(1))
console.log(funcion_7.charAt(2))

console.log("-------------------------------- charCodeAt() --------------------------------")
let funcion_8 = "Entro dos tierras"
console.log(funcion_8)
console.log(funcion_8.charCodeAt())

let funcion_8_1 = funcion_8.charCodeAt(funcion_8.length-1)
console.log(funcion_8_1)

console.log("-------------------------------- codePointAt() --------------------------------")
let funcion_9 = "Entro dos tierras"
console.log(funcion_9)
console.log(funcion_9.codePointAt(1))
let funcion_9_1 = "Hola"
console.log(funcion_9_1)
console.log(funcion_9_1.codePointAt(1))

console.log("-------------------------------- concat() --------------------------------")
let funcion_10_1 = "Hola"
let funcion_10_2 = "Developer"
console.log(funcion_10_1)
console.log(funcion_10_2)
console.log(funcion_10_1.concat(", ", funcion_10_2))

console.log("-------------------------------- endsWith() --------------------------------")
let funcion_11_1 = "¿Cual es tu coche deportivo favorito?"
let funcion_11_2 = "Hola JavaScript!"
console.log(funcion_11_1)
console.log(funcion_11_1.endsWith("favorito?"))
console.log(funcion_11_1.endsWith("favorito"))
console.log(funcion_11_1.endsWith("favorito", 12))
console.log(funcion_11_2)
console.log(funcion_11_2.endsWith("JavaScript!"))
console.log(funcion_11_2.endsWith("JavaScript"))
console.log(funcion_11_2.endsWith("JavaScript", 13))

console.log("-------------------------------- includes() --------------------------------")
let funcion_12 = "The Beloved - Sweet Harmony"
console.log(funcion_12)
console.log(funcion_12.includes("The"))
console.log(funcion_12.includes("Beloved"))
console.log(funcion_12.includes("-"))
console.log(funcion_12.includes("Sweet"))
console.log(funcion_12.includes("Harmony"))
console.log(funcion_12.includes("Ford"))

console.log("-------------------------------- lastIndexOf() --------------------------------")
let funcion_13 = "Hard to Say Im Sorry"
console.log(funcion_13)
console.log(funcion_13.lastIndexOf("H", 0))
console.log(funcion_13.lastIndexOf("a", 1))
console.log(funcion_13.lastIndexOf("r", 2))
console.log(funcion_13.lastIndexOf("d", 3))
console.log(funcion_13.lastIndexOf("Sorry"))

console.log("-------------------------------- localeCompare() --------------------------------")
let funcion_14_1 = "Vivo V2050"
let funcion_14_2 = "Vivo X200 Pro"
console.log(`${funcion_14_1}, ${funcion_14_2}`)
console.log(funcion_14_2.localeCompare(funcion_14_1)) // 1
console.log(funcion_14_1.localeCompare(funcion_14_2)) // -1
console.log(funcion_14_1.localeCompare(funcion_14_1)) // 0

console.log("-------------------------------- match() --------------------------------")
let funcion_15 = "A Horse With No Name"
let funcion_15_1 = /[A-Z]/g // La gbandera es para búsqueda global, lo que significa que esta bandera indica que probamos la expresión regular contra todas las coincidencias en la cadena.
console.log(funcion_15)
console.log(funcion_15.match(funcion_15_1))


console.log("-------------------------------- matchAll() --------------------------------")
let abecedario = "abcdefghijklm"
let regexp = /[a-m]/g // Expresión regular
let iterador = abecedario.matchAll(regexp)
resultado = Array.from(iterador)
console.log(resultado)

console.log("-------------------------------- normalize() --------------------------------")
let name1 = '\u0041\u006d\u00e9\u006c\u0069\u0065';
let name2 = '\u0041\u006d\u0065\u0301\u006c\u0069\u0065';
console.log(`${name1}, ${name2}`) // Expected output: "Amélie, Amélie"
console.log(name1 === name2); // false
console.log(name1.length === name2.length); // false

let name1NFC = name1.normalize('NFC');
let name2NFC = name2.normalize('NFC');
console.log(`${name1NFC}, ${name2NFC}`); // "Amélie, Amélie"
console.log(name1NFC === name2NFC); // true
console.log(name1NFC.length === name2NFC.length) // true

console.log("-------------------------------- padEnd() --------------------------------")
let funcion_16 = "Time Wont Let Me Go"
console.log(funcion_16)
console.log(funcion_16.length)
console.log(funcion_16.padEnd(24, "."))
console.log(funcion_16.padEnd(24, ".").length)

console.log("-------------------------------- padStart() --------------------------------")
let funcion_17 = "10"
console.log(funcion_17)
console.log(funcion_17.length)
console.log(funcion_17.padStart(10, "0"))
console.log(funcion_17.padStart(10, "0").length)

console.log("-------------------------------- repeat() --------------------------------")
let funcion_18 = "Dinero "
console.log(funcion_18)
console.log(funcion_18.repeat(5))

console.log("-------------------------------- replaceAll() --------------------------------")
let funcion_19 = "01, 02, 03, 04, 05, 06, 07, 08, 09"
console.log(funcion_19)
console.log(funcion_19.replaceAll("0", "1"))
console.log(funcion_19.replaceAll("0", "2"))
console.log(funcion_19.replaceAll("0", "3"))

console.log("-------------------------------- slice() --------------------------------")
let funcion_20 = "Goodbye Angels"
console.log(funcion_20)
console.log(funcion_20.length)
console.log(funcion_20.slice(0, 4))
console.log(funcion_20.slice(4, 7))
console.log(funcion_20.slice(8))

console.log("-------------------------------- startsWith() --------------------------------")
let funcion_21 = "Apuesta por el rock 'n' roll"
console.log(funcion_21)
console.log(funcion_21.startsWith("Apuesta"))
console.log(funcion_21.startsWith("Apuesta", 24))
console.log(funcion_21.startsWith("Apuesta por"))
console.log(funcion_21.startsWith("por"))

console.log("-------------------------------- toLowerCase() --------------------------------")
let funcion_22 = "ASPHATL LEGENDS UNITE"
console.log(funcion_22)
console.log(funcion_22.toLowerCase())

console.log("-------------------------------- toString() --------------------------------")
let funcion_23 = ["Uno", "Dos", "Tres", "Cuatro", "Cinco"] // Array
console.log(funcion_23)
console.log(funcion_23.toString())

console.log("-------------------------------- toUpperCase() --------------------------------")
let funcion_24 = "habia una vez en el espacio"
console.log(funcion_24)
console.log(funcion_24.toUpperCase())

console.log("-------------------------------- trim() --------------------------------")
let funcion_25 = " Miguel Angel Martinez "
console.log(`" ${funcion_25} " con espacios al principio y al final.`)
console.log(`,${funcion_25.trim()}, con trim() quitamos los espacios en blanco del principio y final`)

console.log("-------------------------------- trimEnd() --------------------------------")
let funcion_26 = " Stupid Love Story "
console.log(`" ${funcion_26} "`)
console.log(`,${funcion_26.trimEnd()},`)

console.log("-------------------------------- trimStart() --------------------------------")
let funcion_27 = " Niño del recreo feat El M Beats "
console.log(`" ${funcion_27} "`)
console.log(`,${funcion_27.trimStart()},`)

console.log(`----------(◉◉∖____/◉◉)---------- Variables LOCAL y GLOBAL ----------(OO∖____/OO)----------
    `
)
let variableGlobal = "hola"
function Ejemplo() {
    let variableLocal = "Hola"
    return variableLocal
}
console.log(variableGlobal)
// console.log(variableLocal)  Esto es una variable Local, significa que no se puede imprimir

console.log(`----------(◉◉∖____/◉◉)---------- Ejercicio Extra ----------(OO∖____/OO)----------
    Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
        - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
        - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
        - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
        - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
        - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
    `
)
// Tambien llamado Fizz Buzz
// Definimos la función con dos parametros.
function Rango_1_100(Uno, Cien) {
    // La variable "contador" se inicializara en 0, permitiendo que podamos imprimir el numero total de las veces que se han imprimido los numeros, pero no con los textos 
    let contador = 0
    for (let i = 0; i <= 100; i++) {
        // Condición (Si): comprobamos si los número del 1 al 100 son multiplos de 3 y 5 
        if (i % 3 == 0 && i % 5 == 0) {
            console.log(Uno + " y " + Cien) // Imprimimos por consola el resultado de la condición if
        }else if (i % 3 == 0) { // Condición (Si/No): comprobamos si los números del 1 al 100 son multiplos de 3
            console.log(Uno) // Imprimimos por consola el resultado de la condución else if
        }else if (i % 5 == 0) { // Condición (Si/No): comprobamos si los números del 1 al 100 son multiplos de 5
            console.log(Cien) // Imprimimos el resultado de la condución else if
        }else { // Condición (No): De no cumplirse algunas de las condiciones anteriores, imprimiremos los números del 1 al 100
            console.log (i) // Imprimimos por consola los números del 1 al 100
            contador ++ // Cada vez que se valla imprimiendo los numeros "console.log(i)", con "contador" incrementamos 1 para que lo cuente
        }
    }
    // Al acabar el bucle for retornamos "contador"
    return contador
}
// Imprimimos por consola el valor de "contador", además del resultado de la función
console.log("Se han imprimido:", Rango_1_100("Es multiplo de 3", "Es multiplo de 5"))
