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

//  Funcion sin parametros

function saludar(){
    console.log('Hola, buenos dias.')
}
saludar()

// Funcion con un parametro

function saludarNombre(name){
    console.log(`Hola, te saluda ${name}.`)
}
saludarNombre("Mickey")

// Funcion con parametros 

function suma(a,b){
    let res = a + b
    console.log(`La suma de los numeros es: ${res}`)
}
suma(2,2)

// Fucion con return

function resta(a,b){
    let res = a - b
    return res
}

console.log(resta(9,4))

// Funcion dentro de una funcione

function funcUno(){
    function funcDos(){
        console.log('Esta es la funcion Dos')
    }
    funcDos()
    console.log('Esta es la funcion Uno')
}

funcUno()

// Funciones ya creadas por el lenguaje

let str = "2"
console.log(str)
console.log(parseFloat(str))

// variable Local vs variable Global 

let Global = "Soy una variable Global"

function func(){
    let Local = "Soy una variable Local"
    console.log(`LLamo a la varible global: ${Global}`)
    console.log(`LLamo a la varible local: ${Local}`)
}

func()
console.log(Global)
// console.log(Local) No funciona porque es local - Error Message :Local is not defined

// Ejercicio Extra 

function funcTres (paramI,paramII){
    let i   
    for(let i = 1; i <= 100; i++){
        if (i % 3 == 0 && i % 5 == 0) {
            console.log(paramI + paramII);
        } else if (i % 3 == 0) {
            console.log(paramI);
        } else if (i % 5 == 0) {
            console.log(paramII);
        } else {
            console.log(i);
        }
    }
    return i;
}

funcTres("perro","Gato")