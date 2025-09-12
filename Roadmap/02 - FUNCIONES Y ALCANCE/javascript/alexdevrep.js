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

//Función sin parámetros ni retorno
function simpleFunction(){
    console.log("Hola Mundo!")
}
simpleFunction()

// Función con un parámetro
function oneArg(Arg1){
    console.log(`Hola ${Arg1}`) //${} sirve para inyectar variables en una cadena de texto

}
oneArg("JavaScript")

//Función con varios parámetros
function manyArgs(día,mes,año){
    console.log(`Hoy es ${día} del ${mes} del ${año}`)

}
manyArgs(9,1,2024)

//Función con retorno
function withReturn(a,b){
    return a + b //return nos permite guardar el resultado de la función en una variable
}
resultado= withReturn(2,3)
console.log(resultado)

//Funciones dentro de funciones
function funcionPadre(sum3){
    function funcionHijo(sum1,sum2){
        return sum1 + sum2
    }
resultadoHijo = funcionHijo(1,2)
console.log ("El resultado de la suma de las 2 funciones es:",resultadoHijo + sum3)

}
funcionPadre(3)

//Funciones ya creadas en el lenguaje

//Math.random
const number = Math.random()
console.log(number)

//Variable global (es una variable que está declarada fuera de la función y puede accederse a ella desde cualquier punto del código)
let variable1 = 8
function suma (){
    console.log("El resultado es:", variable1 + 3)
}
suma()

//Variable local (es una variable que está declarada dentro de una función y solo puede usarse dentro de ella)
function resta (){
    let variable2 = 2
    console.log("El resultado de la resta es",variable2 - 1)
}
resta()

//DIFICULTAD EXTRA
function extra (string1,string2){
    let numero = 0
    for(let i=1;i<=100;i++){
        
        if (i%3==0 && i%5==0){
            console.log(string1+" "+string2)
            continue
        }
        else if(i%3==0){
            console.log(string1)
            continue
        }
        else if (i%5==0){
            console.log(string2)
            continue
        }
        else {
            console.log(i)
        }
        
        numero ++
    }
    return numero
}
console.log("Numero de veces que se ha impreso el contador:",extra("Hola JavaScript","Hola alexdevrep"))

