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
 *  */
function optNoReturn() {
    console.log('Esta función sin params y no retorna nada, solo imprime.');
  }
  
  function optWithReturn() {
    const str = 'Esta otra función retorna una string, que se puede imprimir';
    return str;
  }
  
  function optWithParamsAndNoReturn(printThis) {
    console.log(printThis);
  }
  
  function optWithParamsWithReturnDouble(returnThis) {
    return returnThis * 2;
  }
  
  const doubleThis = optWithParamsWithReturnDouble(4)

  function higherOrderFunction(value){
    return function insideFunction(factor){
        return value * factor
    }
  }
  
  var iAmGlobal = "soy una variable global"
  
  function defineScope(){
      let iAmLocal = "Soy una variable local"
  
      console.log({iAmGlobal})
      console.log({iAmLocal})
  }
  
  optNoReturn();
  console.log(optWithReturn());
  optWithParamsAndNoReturn('Whaaaat?');
  console.log(optWithParamsWithReturnDouble(2));
  console.log(doubleThis)

  // Uso de función que retorna otra función
const doubleThisAgain = higherOrderFunction(2);
console.log(doubleThisAgain(4));  // Outputs: 8

defineScope();
console.log("esto no funciona: ", {iAmLocal})




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
 */

function extraJob(string1, string2) {
    let counter = 0;
    let min = 1;
    let max = 100;

    for (let i = min; i <= max; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(string1 + string2);
        } else if (i % 3 === 0) {
            console.log(string1);
        } else if (i % 5 === 0) {
            console.log(string2);
        } else {
            console.log(i);
            counter += 1;
        }
    }

    return counter;
}

// Llamada de ejemplo a la función
console.log("Número de veces que se ha impreso el número:", extraJob("Ola", "Kease"));