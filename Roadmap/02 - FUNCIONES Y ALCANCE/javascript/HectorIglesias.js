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


function funcion(){
    console.log("Función sin parámetros ni retorno")
}
funcion()

function funcion2(){
    let variable = "Función sin parámetros con retorno"

    return variable
}
console.log(funcion2())

function funcion3(param1){
    console.log(param1)
}
funcion3("Función con un parámetro y sin retorno")

function funcion4(param1, param2){
    return param1 +" y "+ param2
}
console.log(funcion4("Función con varios parámetros", "con retorno"))

//Función dentro de función
function mother(){
    let aux = 5
    function child(sum){
        return sum + 1
    }
    return child(aux)
}
console.log(mother())

//Función ya creada en el lenguaje
let num_random= Math.random()
console.log(num_random)

//Variable LOCAL Y GLOBAL
let global = "Variable global"

function funcion4(){
    let local = "Variable local"

    console.log("Dentro de la función puedo usar la " +global+ " y la " +local)
}
funcion4()
console.log("Fuera de la función puedo seguir usando la " +global+ " pero si intentará usar la variable local me daría error")

//DIFICULTAD EXTRA
function extra(param1, param2){
    let cont = 0
    for (let i=1; i<=100; i++){
        if(i % 3== 0 && i % 5 == 0){
            console.log(param1+param2)
        }
        else if (i % 3 == 0){
           console.log(param1)
        }
        else if (i % 5 == 0){
            console.log(param2)
        }
        else{
            cont++
            console.log(i)
        }
    }

    return cont
}

console.log(extra("fizz", "buzz"))
