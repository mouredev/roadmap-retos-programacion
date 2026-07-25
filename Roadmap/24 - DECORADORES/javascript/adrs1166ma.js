/* 🔥 EJERCICIO:
Explora el concepto de "decorador" y muestra cómo crearlo
con un ejemplo genérico.
*/

function decoradorEjemplo(funcionOriginal) {
    return function(...args) {
        console.log(`Antes de ejecutar la función: ${funcionOriginal.name}`)
        const resultado = funcionOriginal(...args)
        console.log(`Después de ejecutar la función: ${funcionOriginal.name}`)
        return resultado
    }
}

// Función a decorar
function saludar(nombre) {
    console.log(`¡Hola, ${nombre}!`)
}

// Crear una versión decorada de la función
const saludarDecorado = decoradorEjemplo(saludar)

// Uso de la función decorada
saludarDecorado("Anderson")
// Antes de ejecutar la función: saludar
// ¡Hola, Anderson!
// Después de ejecutar la función: saludar



/* 🔥 DIFICULTAD EXTRA (opcional): --------------------------------------------------------------------------
Crea un decorador que sea capaz de contabilizar cuántas veces
se ha llamado a una función y aplícalo a una función de tu elección.
 */

function contadorDeLlamadas(funcionOriginal) {
    let contador = 0
    return function(...args) {
        contador++
        console.log(`Llamada ${contador} a la función: ${funcionOriginal.name}`)
        return funcionOriginal(...args)
    }
}

function sumar(a, b) {
    return a + b
}

// Crear una versión decorada de la función
const sumarContada = contadorDeLlamadas(sumar)

console.log(sumarContada(2, 3))
console.log(sumarContada(5, 5))
console.log(sumarContada(10, 10))
// Llamada 1 a la función: sumar
// 5
// Llamada 2 a la función: sumar
// 10
// Llamada 3 a la función: sumar
// 20