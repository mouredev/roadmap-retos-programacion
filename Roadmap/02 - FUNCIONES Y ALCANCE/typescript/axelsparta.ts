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

function firstFunction () {
  console.log('first function')
}

const firstFunctionResult = firstFunction() // ejecutamos la función con esta sintaxis, el resultado se guardará en la constante 'firstFunctionResult'
console.log(firstFunctionResult) // 'undefined', si no se indica un return por defecto las funciones devuelven 'undefined'

function functionWithParameters(firstParameter: number, secondParameter: number){
  return firstParameter ** secondParameter
}

const functionResult = functionWithParameters(10, 2)
console.log(functionResult)

const arrowFunction = (num1: number, num2: number) => {
  return num1 + num2
}

const arrowFunctionResult = arrowFunction(10, 30)
console.log(arrowFunctionResult)

let globalVariable = 'My global variable'

const myFunction = () => {
  // función creada dentro del bloque de la función 'myFunction', solo se puede llamar dentro de la misma
  const myLocalFunction = () => {
    return 'My local function result'
  }

  const myLocalFunctionResult = myLocalFunction()
  let localVariable = 'My local variable'
  console.log(localVariable, globalVariable, myLocalFunctionResult) // si se puede acceder a la variable global y a las variables declaradas dentro del bloque de la función
}

// console.log(localVariable) -> error no se puede acceder a la variable creada dentro de la función 'myFunction'  

// Ejercicio extra...
const exerciseFunction = (param1: string, param2: string): number => {
  let countResult = 0
  for(let i = 1; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      console.log(param1, param2)
    } else if(i % 3 == 0) {
      console.log(param1)
    } else if(i % 5 == 0) {
      console.log(param2)
    } else {
      console.log(i)
      countResult++
    }
  }
  return countResult
}

const exerciseFunctionResult = exerciseFunction('fizz', 'buzz')
console.log(exerciseFunctionResult)