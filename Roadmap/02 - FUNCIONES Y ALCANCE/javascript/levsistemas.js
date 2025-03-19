/*# #02 FUNCIONES Y ALCANCE
> #### Dificultad: Fácil | Publicación: 08/01/24 | Corrección: 15/01/24

## Ejercicio

```

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

//FUNCIONES

function helloWorld () {
    console.log("Hello World")
}

function helloWorld1 (name) {
    console.log("Hello World, " + name)
}
function helloWorld2 (name, age) {
    return "Hello World, " + name + ' ' + age
}

function helloWorld3 (name) {
    return "Hello World, " + name
}

function helloWorld4 () {
    function hellowWorldChildren() {
        console.log("Llamando a la función anidada")
    }
    hellowWorldChildren()
}

helloWorld()
helloWorld1('SlipKnot')
helloWorld2('SlipKnot', 38)
console.log(helloWorld3('Return of SlipKnot'))
helloWorld4()

//FUNCIONES YA CREADAS

console.log(Date().slice(0, Date().indexOf('GMT')) + "hs")
console.log(helloWorld2('Leandro'.toUpperCase(), 38))
console.log(helloWorld3('Return of SlipKnot').toLowerCase())

//VARIABLE GLOBAL Y LOCAL

let global = "Hola Mundo"

function hW(){
    let saludo = "Hola Mundo desde función"
    return saludo
}

console.log(global)
console.log(hW())

function option(string1, string2) {
    console.log("Bienvenida palabra: " + string1 + " y palabra: " + string2)
    let number = 0
    for (i=1; i<=100; i++) {

        if(i % 3 == 0) {
            console.log('string n° 1')
            number++
        }

        if (i % 5 == 0) {
            console.log('string n° 2')
            number++
        }

        if(i % 3 == 0 && i % 5 == 0) {
            console.log('string n° 1' + 'string n° 2')
        }
    }
    return number
}

console.log(option('palabra1', 'palabra2'))