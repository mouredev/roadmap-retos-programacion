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

function hola(){
    let name = "EonOzux"
    console.log("Mi nombre es " + name)
};
// funcion con variable
hola();

function parametro(lenguaje){
    console.log(`Codigo en ${lenguaje}`) //${} inyectar variables en una cadena de texto

};
parametro("JavaScript")

function expiracion(dia,mes){
    console.log(`El producto vence en ${dia}/ ${mes}`)
};
expiracion("30","Setiembre")

function retorno(y,x){
    return x + y
};
let resultado = retorno(5,8);
console.log(resultado);


//Variable global (es una variable que está declarada fuera de la función y puede accederse a ella desde cualquier punto del código)
let variable1 = 8
function sumar (){
    console.log("El resultado es:", variable1 + 3)
}
sumar()

//Variable local (es una variable que está declarada dentro de una función y solo puede usarse dentro de ella)
function restar (){
    let variable2 = 6
    console.log("El resultado de la resta es",variable2 - 1)
}
restar()

/* * DIFICULTAD EXTRA (opcional):
* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
* - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
*   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
*   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
*   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
*   - La función retorna el número de veces que se ha impreso el número en lugar de los textos. */


// Crear los prompts de tipo texto y se almacenen en una variable.



function tarea_Extra(){
    //Definimos Variables
    let primer_texto = "Primer texto";
    let segundo_texto = "Segundo texto";
    let numero = 0
    for(let x = 1;x < 100;x++){  //Creamos el contador hasta 100
        if (x % 3 == 0 && x % 5 == 0){  // Si el numero del contador es el residuo de 3 o .
            console.log(primer_texto + "" + segundo_texto)
            continue
        }
        else if(x % 3 == 0){   // Si el numero del contador es el residuo de 3
            console.log(primer_texto)
            continue
        }
        else if(x % 5 == 0){   // Si el numero del contador es el residuo de 5
            console.log(segundo_texto)
            continue
        }
        else {  // Si el numero del contador no es residuo de los 2 anteriores 
            console.log(x)  // Imprima en la consola el numero
        }
        numero ++
    }
    return numero
};
console.log("Numero de veces que se ha impreso el contador:",tarea_Extra())
