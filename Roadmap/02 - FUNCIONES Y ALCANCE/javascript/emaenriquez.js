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
 */

// funcion sin parametros ni retorno
function holaMundo(){
    console.log('hola mundo');
}

holaMundo();

// funcion con varios parametros
function sumar(num1,num2){
    console.log(num1+num2);
}

sumar(10,20);

// funcion con retorno
function resta(num1,num2) {
    return num1 - num2;
}

let resultado = resta(10,20);

console.log(resultado);

// funciones anidadas
function suma(n) {

    function incrementar(n2) {
        return n + n2;
    }

    return incrementar;
}

// Llama a la función externa y guarda la función devuelta
let sumaCinco = suma (5);

// Llama a la función devuelta con un argumento
console.log (sumaCinco (3)); // Muestra 8

// funcion ya creada en el lenguaje.
let numeroRamdom = Math.random()*100;

console.log(numeroRamdom)


// variable LOCAL y GLOBAL
// grobal
let contador = 10

function recorido() {
    for (let i = 0; i < contador; i++) {
        console.log(i)
    }
}
recorido()

// local
function recorido() {
    
    let contador = 10
    
    for (let i = 0; i < contador; i++) {
        console.log(i)
    }

}

recorido()


//  * DIFICULTAD EXTRA (opcional):
//  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
// * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
// *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
// *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
// *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
// *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
// *
// * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
// * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.


function extra(str1,str2){

    let contador = 0

    for (let i = 0; i <= 100; i++) {

        if (i % 3 == 0 && i % 5 == 0) {
            console.log(str1 + " " + str2);
            continue;
        }

        if ( i % 3 == 0) {
            console.log(str1);
            continue;
        }

        if ( i % 5 == 0) {
            console.log(str2)
            continue;
        }
        
        contador++
    }

    return contador

}

console.log(
    "Número de veces que se ha impreso: ",
    extra("Hola", "JavaScript")
  );