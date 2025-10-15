/*
_____________________________________
https://github.com/EliTeDev-44
2025 - JavaScript
_______________________________________
02 FUNCIONES Y ALCANCE
---------------------------------------
* - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 * 
 *  *
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

// ________________________
// Funciones
// https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Functions

// Sintaxis de una función
function nombre (parametro, parametro2) {
    // Código a ejecutar
}


// Función Básica (Sin parámetros)
function miFuncionBasica() {
    console.log("✅ Función Básica sin parámetros")
}
miFuncionBasica(); // Llamar a la función


// Función con 1 parámetro
function func1Parametro(texto) {
    console.log(texto)
}
func1Parametro("✅ Soy un parámetro")


// ________________________
// Función con retorno
// https://developer.mozilla.org/es/docs/Learn/JavaScript/Building_blocks/Return_values

function metrosCuadrados (ancho, largo) {
    return ancho * largo
}
console.log("✅ La superficie tiene", metrosCuadrados(4, 10), "m2"); // Llamada a la función pasando los 2 parámetros


// Retorno de múltiples datos
function calcularDatos(ancho, largo) {
    return {
      area: ancho * largo,
      perimetro: 2 * (ancho + largo)
    }
}

const rectangulo = calcularDatos(4, 12)
console.log(`✅ Área del rectángulo: ${rectangulo.area}`)   // Área: 48
console.log(`🔁 Perímetro del rectángulo: ${rectangulo.perimetro}`) // Perímetro: 32


// ________________________
// Variable Global
let variableGlobal = "Soy una Variable Global"

// Variable Local
function mostrarVariables () {
    let variableLocal = "Soy una variable Local"
    console.log(variableGlobal, "\n", variableLocal)
}
mostrarVariables()


// Función dentro de una Función:
function funcionExterna() {
    function funcionInterna(a, b) {
        return a - b
    }
    return funcionInterna(10, 4)
}
console.log("🧠 Devuelvo una función anidada:", funcionExterna())

const numeroMayor = Math.max(4, 44, 16, 22)
console.log("🧠 El número mayor es el", numeroMayor, "\n") // 44


/*  * DIFICULTAD EXTRA (opcional):
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
console.log("==========================")
console.log("🧠 Ejercicio Extra:\n")

function multiplos(multiplo3, multiplo5) {
    let contador = 0

    for (let num = 1; num <= 100; num++) {
        if (num % 3 === 0 && num % 5 === 0) {
            console.log(num, multiplo3 + ", y " + multiplo5)
        } else if (num % 3 === 0) {
            console.log(num, multiplo3)
        } else if (num % 5 === 0) {
            console.log(num, multiplo5)
        } else {
            contador += 1
            console.log(num)
        }
    }
    return contador
}

multiplos("Soy múltiplo de 3", "Soy múltiplo de 5")

console.log("\nFin del ejercicio Extra")
console.log("==========================")