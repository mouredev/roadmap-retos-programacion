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
 * 
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */


//TIPOS DE FUNCIONES 

//1. Funciones Declaradas (Function Declarations)

function suma ( a,b){
    return a + b;
}

//2. Funciones Expresadas (Function Expressions)
const resta = function (a,b){ 
    return a - b;
}

//3. Funciones Flecha (Arrow Functions)
const multiplicacion = (a,b) => a * b;

//4. Funciones Anónimas (Anonymous Functions)

function* contador() {
    let i = 0;
    while (true) {
      yield i++;
    }
  }

  //5. Funciones Asíncronas (Async Functions)

  async function miFuncion() {
    const respusta = await fetch('https://api.com');
    return respusta.json();
  }

  // 6. IIFE (Immediately Invoked Function Expressions)

    (function() {
        console.log('Hola!');
      })();

// 7. Funciones dentro de funciones

function personal (name) {
    this.name = name;
}

// 8. Funciones ya creadas en el lenguaje

setTimeout(() => {
    console.log('Hola, mundo!');
},1000);


// DIFICULTAD EXTRA (opcional):
//  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
//  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
//  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
//  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
//  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
//  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

const DF = (string1, string2) => {
    let contador = 0;
    for (let i = 1; i <= 100; i++) {
        switch (true) {
            case i % 3 === 0 && i % 5 === 0:
                console.log(string1 + string2)
                break;
            case i % 3 === 0:
                console.log(string1);
                break;
            case i % 5 === 0:
                console.log(string2);
                break;
            default:
                console.log(i);
                contador++;
                break;
            }
        }
    return contador
}