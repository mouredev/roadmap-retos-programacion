//Variables globales
var variableGlobal1 = 100
var variableGlobal2 = 20

//Función básica / sin retorno ni parámetros
function bienvenida() {
    console.log("Les damos la bienvenida a nuestra casa")
}

bienvenida()

//Función con parámetro
function clima(estado) {
    console.log("Hoy el clima está " + estado)
}

clima("soleado")

//Función con varios parámetros
function mesa(p1, p2) {
    console.log("Esta mesa está reservada para " + p1 + " y " + p2)
}

mesa("José Hernandez", "María Valdez")

//Función con retorno
function sumar(a, b) {
    return a + b
}

function multiplicacion(a, b) {
    return a * b
}

resultadoSuma = sumar(variableGlobal1, variableGlobal2)
resultadoMultiplicacion = multiplicacion(variableGlobal1, variableGlobal2)
console.log("Resultado de la suma: " + resultadoSuma + ". Resultado de la multiplicación: " + resultadoMultiplicacion)

//Variables locales
function local() {
    let funcionLocal1 = 200
    let funcionLocal2 = 50

    console.log(funcionLocal1 + funcionLocal2)
}

local()

//Funciones dentro de funciones
function dobleFuncion(c, d) {
    const r1 = sumar(c, d)
    const r2 = multiplicacion(c, d)
    const res = (r2 / r1)
    console.log("División de los resultados de las operaciones: " + res)
}

dobleFuncion(15, 10)
 
/* DIFICULTAD EXTRA
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos. 
 */

function extra(p1, p2) {
    for(i=1; i <=100; i++) {
        if ((i % 3 === 0) && (i % 5 === 0)) {
            console.log(`${p1}${p2}`)
        } else if (i % 3 === 0) {
            console.log(p1)
        } else if (i % 5 === 0) {
            console.log(p2)
        } else {
            console.log(i)
        }
    }
}

extra("Fizz", "Buzz")