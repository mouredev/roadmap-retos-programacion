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


// Sin parametros ni retorno 
let anonima = () =>
    console.log("Mi funcion");

anonima()

// Con uno o varios parametros variando pocision 
function yoSoy({ nombre, edad }) {
    console.log(`Mi nombre es ${nombre} y tengo ${edad} años`)
}

yoSoy({ edad: 35, nombre: "John" });



//Con retorno 
let sumaNumeros = function (num1, num2) {
    return num1 + num2;
}

console.log(`2 y 2 son ${sumaNumeros(2, 2)}`);

// Funcion dentro de otra funcion 
function sumaYdivide(num1, num2) {
    let resultado = num1 + num2
    function divide(num) {
        return resultado / num
    }
    return divide(2)
}
console.log(sumaYdivide(0, 100));

//Funcion creada en lenguaje 
function sumaVarios(...num) {
    return num.reduce((total, actual) => total + actual)
}
console.log(sumaVarios(1, 2, 3, 4, 5));

//Funcion que saluda a todos 
function saludoATodos(...nombres){
    for (let nombre of nombres) {
        console.log(`Hola ${nombre}`);
    }
}

saludoATodos("John","Sofia","Marta")

// Variable local y global 
let miVariable = 1 // Variable global 

function variables() {
    let miVariable = 2 // Variable local
    return miVariable
}

console.log(miVariable);
console.log(variables());


/* DIFICULTAD EXTRA (opcional):
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


function retornaNumero(texto1, texto2) {
    let contador = 0;

    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(i, `${texto1} y ${texto2}`);
        }
        else if (i % 3 === 0) {
            console.log(i, `${texto1}`);
        }
        else if (i % 5 === 0) {
            console.log(i, `${texto2}`);
        }
        else {
            console.log(i);
            contador++;
        }
    }
    console.log("El numero de veces que se han impreso los numeros es " + contador);
    return "El numero de veces que se han impreso los numeros es " + contador;
}

retornaNumero("Es multiplo de 3", "Es multiplo de 5");