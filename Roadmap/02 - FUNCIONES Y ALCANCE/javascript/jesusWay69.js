console.clear()
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
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

// VARIABLES GLOBALES
var acc = 0
var operation = ''
var globalVariable = "Soy una variable global"
var string1 = "Hola"
var string2 = "Javascript"

//FUNCIÓN SUMA SIMPLE SIN RETORNO
function sumPrint(a, b) {
    console.log(`${a} + ${b} = ${a + b} \n`)
}
sumPrint(10, 9)

// FUNCIÓN SUMA SIMPLE CON RETORNO
function sumReturn(a, b) {
    return `${a} + ${b} = ` + (a + b)
}
console.log(sumReturn(9, 8), '\n')

// FUNCIÓN ANÓNIMA DE SUMA SIMPLE  
let sumAnonymousFuntcion = function (a, b) {
    let operation = `${a} + ${b} = `
    return operation + (a + b)
}
console.log(sumAnonymousFuntcion(10, 20), '\n')

//FUNCIÓN FLECHA DE SUMA SIMPLE
let sumArrowFuntcion = (a, b) => `${a} + ${b} = ` + (a + b)
console.log(sumArrowFuntcion(50, 50), '\n')

// FUNCIÓN SUMA CON OPERANDOS VARIABLES POR PROPAGACIÓN CON RETORNO
function sumSpreadingReturn(...numbers) {
    acc = 0
    operation = ''
    for (const [index, number] of numbers.entries()) {
        acc += number
        if (index < numbers.length - 1) operation += number + ' + '
        else operation += number + ' = '
    }
    return operation + acc
}
console.log(sumSpreadingReturn(7, 8, 3, 14, 25), '\n')
console.log(sumSpreadingReturn(8, 9, 11, 50, 14, 8, 71, 63, 2, 32), '\n')

// FUNCIÓN SUMA CON OPERANDOS VARIABLES POR PROPAGACIÓN SIN RETORNO
function sumSpreadingPrint(...numbers) {
    acc = 0
    operation = ''
    for (let i = 0; i < numbers.length; i++) {
        acc += numbers[i]
        if (i < numbers.length - 1) operation += numbers[i] + ' + '
        else operation += numbers[i] + ' ='
    }
    console.log(operation, acc, '\n')
}
sumSpreadingPrint(8, 7, 1, 16, 52, 9, 13, 4)
sumSpreadingPrint(5, 1, 7, 0.3, 10, 4)
sumSpreadingPrint(5, 8, 100, 50)

// FUNCIÓN ANÓNIMA SUMA CON OPERANDOS VARIABLES POR PROPAGACIÓN CON RETORNO
const anonymousFunction = function (...numbers) {
    acc = 0
    operation = ''
    for (const [index, number] of numbers.entries()) {
        acc += number
        if (index < numbers.length - 1) {
            operation += number + ' + '
        } else {
            operation += number + ' = '
        }

    }
    return operation + acc
}
console.log(anonymousFunction(4, 48, 7, 9, -10, 2, 1, 20), '\n')
console.log(anonymousFunction(3.56, 4.88, 9.48, 1.22, 5.71, 3.24, 6.91), '\n')

// FUNCIÓN FLECHA SUMA CON OPERANDOS VARIABLES POR PROPAGACIÓN CON RETORNO
const anonymousArrowFunction = (...numbers) => {
    acc = 0
    operation = ''
    for (const [index, number] of numbers.entries()) {
        acc += number
        if (index < numbers.length - 1) {
            operation += number + ' + '
        } else {
            operation += number + ' = '
        }

    }
    return operation + acc
}
console.log(anonymousArrowFunction(1, 7, 8), '\n')
console.log(anonymousArrowFunction(47, 72, 98), '\n')

// FUNCIÓN QUE IMPRIME UNA VARIABLE LOCAL DECLARADA DENTRO Y OTRA GLOBAL DECLARADA FUERA
let printVariables = function () {
    let localVariable = "Soy una variable local"
    console.log(localVariable)
    console.log(globalVariable)
}
printVariables()

// FUNCIÓN ANÓNIMA QUE SE LE PASA COMO ARGUMENTO A UNA FUNCIÓN DE ORDEN SUPERIOR SOBRE UN LISTADO
// Y DEVUELVE OTRO LISTADO CON LOS NÚMEROS TRANSFORMADOS EN BASE 2 USANDO LOS ORIGINALES COMO EXPONENTES
const simpleNumbers = [0, 1, 2, 3, 4, 5, 6, 7]
const base2Value = simpleNumbers.map(function (num) {
    return 2 ** num
})
console.log('\n', base2Value, '\n')

// FUNCIÓN FLECHA QUE RECIBE UN NÚMERO Y UTILIZA INTERNAMENTE LA FUNCIÓN ANTERIOR PARA
// DEVOLVER EL NÚMERO BINARIO DEL NÚMERO RECIBIDO
let decToBin = (num) => {
    bin = ''
    for (let i = base2Value.length - 1; i >= 0; i--) {
        if (num < base2Value[i]) {
            bin += 0 + ' '
        } else {
            bin += 1 + ' '
            num -= base2Value[i]
        }
    }
    return bin
}
console.log(decToBin(100), '\n')

/*
* DIFICULTAD EXTRA (opcional):
* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
* - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
*   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
*   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
*   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
*   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/

function numbers(str1, str2) {
    let counter = 0
    for (let i = 1; i <= 100; i++) {
        if (i % 3 == 0 && i % 5 == 0) console.log(str1, str2);
        else if (i % 3 == 0) console.log(str1);
        else if (i % 5 == 0) console.log(str2);
        else {
            console.log(i)
            counter++
        }
    }
    console.log(`\nLos números se han impreso ${counter} veces \n`)
}
numbers(string1, string2)