/*
# #02 FUNCIONES Y ALCANCE
> #### Dificultad: Fácil | Publicación: 08/01/24 | Corrección: 15/01/24

## Ejercicio

```
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
 
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.*/

// Funciones sin retorno y sin parámetros
const helloWorld = () => console.log(`>>> hello world`)
helloWorld()

// Funciones sin retorno y con parámetros
const helloWorldTwo = (alias) => console.log(`>>> hello world ${alias}`)
helloWorldTwo("Spiderman")

// Funciones con retorno y parámetros
const ciaoWorld = () => `>>> ciao world`
let resultCiao = ciaoWorld()
console.log(resultCiao)

// Funciones con retorno y parámetros
const ciaoWorldTwo = (alias) => `>>> ciao world ${alias}`
let resultCiaoTwo = ciaoWorldTwo("Iron Man")
console.log(resultCiaoTwo)

// Funciones dentro de funciones
function checkPositive(num) {
  function validate(num) {
    let check = num > 0 ? true : false
    return check
  }

  let resultValidate = validate(num)
    ? `>> Número positivo`
    : `>> Número negativo o 0`
  return resultValidate
}

console.log(checkPositive(-5))

// Uso de una función del lenguaje ya existente
let texto = "JavaScript"
console.log(">>> Texto en mayúsculas:", texto.toUpperCase())

// Ámbito variables globales- locales
let global = ">> Soy una variable GLOBAL"

function checkAccesVar() {
  console.log("==================")
  console.log("Invocación desde función")
  let local = `>> Soy una variable LOCAL`
  console.log(local)
  console.log(global)
  console.log("==================")
}

checkAccesVar()

try {
  console.log(local)
} catch (e) {
  console.log(
    "!!! Error variable local inaccesible fuera de la función\n",
    e.message
  )
}


/*
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
 * */

function checkMultiple(string1, string2) {
    let counter=0
      for (let i = 1; i <= 100; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
          console.log(`${string1} y ${string2}`)
        } else if (i % 3 == 0) {
          console.log(string1)
        } else if (i % 5 == 0) {
          console.log(`${string2}`)
        } else {
          console.log(i)
          counter++
        }
      }
    console.log(`Números impresos: ${counter}`)
    }
    
    let stringOne = `Soy múltiple de 3`
    let stringTwo = `Soy múltiple de 5`
    
    checkMultiple(stringOne, stringTwo)