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

// Funcion básica

function saludar() {
  console.log("Hola Mundo!!")
}
saludar()

// Funcion con parámetros

function saludar2(texto) {
  console.log(`Bienvenido ${texto}`)
}
saludar2("Younes")

// Funcion con retorno

function saludar3(texto) {
  return `Hola ${texto}`
}
console.log(saludar3("Younes"))

// Funcion dentro de funcion

function saludar4() {
  function saludar5() {
    console.log("Hola")
  }
  saludar5()
}
saludar4()

// Funcion dentro de funcion con retorno

function saludar6() {
  function saludar7() {
    return "Hola"
  }
  return saludar7()
}
console.log(saludar6())

// Variable global

let variableGlobal = "Variable global"
function saludar8() {
  console.log(variableGlobal)
}
saludar8()
console.log(variableGlobal)

// Variable local

function saludar9() {
  let variableLocal = "Variable local"
  console.log(variableLocal)
}
saludar9()
// console.log(variableLocal) -> Error de ejecución

//DIFICULTAD EXTRA

function extra(texto1, texto) {
  let contador = 0
  for (let i = 1 ; i <= 100 ; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      console.log(texto1 + texto)
    } else if (i % 3 == 0) {
      console.log(texto1)
    } else if (i % 5 == 0) {
      console.log(texto)
    } else {
      console.log(i)
      contador++
    }
  }
  return `Los numeros impresos, que NO son texto, son: ${contador}`
}
