/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */







/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
*/

// Función sin parametros

function saludo() {
    console.log(`Buenos días,`)
}
saludo()

// Función con uno o varios parámetros


function saludoLogin(login, nombreUsuario) {
    if(typeof login === "boolean" && login === true  ) {
        console.log(`¡Bienvenido! ${nombreUsuario}`)
    }else {
        console.log(`¡Datos incorrectos! Vuelva a intertarlo`)
    }
}
saludoLogin(true, "Adolfo" )


// Función con retorno

function sumar(a, b) {
    return a + b
}

const resultado = sumar (3,5)

console.log(resultado)

const precio = 50;

function calcularIva(precio) {
    return precio * 0.21
}

function calcularTotal(precio) {
    return precio + calcularIva(precio) // Reutilizar funciones
}
const mensajeIva2 = `El iva de ${precio} € es de = ${calcularIva(precio)} €;
El precio total de ${precio} € más el iva es de = ${calcularTotal(precio)}€`;

console.log(mensajeIva2)





// Comprueba si puedes crear funciones dentro de funciones.

function mensaje(nombre) {
    function saludo() {
        return `Hola, ¿que tal estás ${nombre}? `
    }
    return saludo()
}
console.log(mensaje("Pablo"))

// Si una función quiere exponer varias funciones devolveremos estas funciones en el return
// mediante un objeto

function mensajes(nombre) {
    function saludo() {
        return `¡Bienvenido a la aplicación ${nombre}!`
    }
    function despedida() {
        return `¡Hasta pronto!`
    }
    return {
        saludo,
        despedida
    }
}
const luis = mensajes("Luis")
const pablo = mensajes("Pablo")

console.log(luis.despedida())
console.log(pablo.saludo())
console.log(mensajes("Luis").saludo())// Podemos encadenar varias funciones mediante el (.)


// Otra manera con if en lugar de usar un objeto en el return

function calculadora(operacion, a, b) {
    function sumar() {
    return a + b;
    }
    function restar() {
        return a - b
    }
    if(operacion === "sumar") {
        return sumar()
    }
    if(operacion === "restar") {
        return restar()
    }
   return `Operación no válida`
}

function mensajeCalculo (operacion){
    return `El resultado es: ${operacion}`
}
console.log(mensajeCalculo(calculadora("sumar", 3, 2)))


// Funciones sin especificar la cantidad de parámetros que reciben y devuelven con REST y SPREAD.

// REST
function cantidadParamtrosX(...names) {
    for (const name of names)
        console.log(`Hola,${name}!`)
}
cantidadParamtrosX("python, javascript, java, kotlin")


// SPREAD
let nombres = ["juan", "paco", "jose"]

cantidadParamtrosX(...nombres)
function persona(nombre, ...resto) {
    console.log(nombre)
    console.log(resto)
}

persona("Juan", 30, "Oviedo")

console.log("--------------------------------")


//Utiliza algún ejemplo de funciones ya creadas en el lenguaje.

console.log()
console.log("hola".length) // Devuelve la cantidad de letras de la palabra
console.log("hola".toUpperCase())// convertir todo en mayusculas
console.log("HOLA".toLowerCase())// convertir todo en minusculas
console.log("Hola, mundo".includes("mundo")) // La frase: Hola mundo ¿incluye la palabra mundo?
console.log("Hola, mundo".slice(4)) // Devuelve desde el indice 4, que en este caso es la coma.
console.log("Hola, mundo".slice(0, 4))// Devuelve desde el indice 0 hasta antes del indice 4.
console.log("Hola, mundo".split(",")) // Convierte un string en un array de palabras, cuando encuentre una coma
console.log("Hola, mundo".split("")) // Convierte un string en un array de letras
console.log("  Hola, mundo  ".trim())//Elimina los espacios vacios al inicio y al final.

// Pon a prueba el concepto de variable LOCAL y GLOBAL.

let e = 3
let f = 2

function numG() {
    let g = 6
    return g
}

console.log(numG())
console.log(e + f)
//console.log(g + e) ReferenceError: g is not defined

/*
DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/

function imprimirMultiplos(cadenaTxt1, cadenaTxt2) {
    let contador = 0
    for(let i = 1; i <= 100; i++ ) {
        if(i % 3 === 0 && i % 5 === 0) {
            console.log(cadenaTxt1 + cadenaTxt2)
        }else if(i % 3 === 0) {
            console.log(cadenaTxt1)
        }else if (i % 5 === 0) {
            console.log(cadenaTxt2)
        }else {
            console.log(i)
            contador++
        }
    }
    return contador
}
console.log(imprimirMultiplos("cadenaTxt1", "cadenaTxt2"))

