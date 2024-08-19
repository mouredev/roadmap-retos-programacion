/*
 * EJERCICIO:
 1 - Crea ejemplos de funciones básicas que representen las diferentes
     posibilidades del lenguaje: Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
  - Comprueba si puedes crear funciones dentro de funciones.
  - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
  - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
    (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)


 1.1 DIFICULTAD EXTRA (opcional):
 1.2 Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 * 
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

 // 1

// Funcion basica

    function suma (a, b) {
        return a + b
    }

    console.log(suma(-2, 6)) // 4
    console.log(suma(3, 6)) // 9


//Funciones anidadas

    function alCuadrado(a, b) {
        function cuadrado (x) {
          return x * x
        }
        return cuadrado(a) + cuadrado(b)
      }
      
      console.log(alCuadrado(2, 3)) // 13
      console.log(alCuadrado(5, 10)) // 125

// Funcion flecha

    const suma2 = (a, b) => a + b

    console.log(suma2(-2, 6)) // 4
    console.log(suma2(3, 6)) // 9

// Varible Global

    let counter = 2
        
    function counterPlus() {
    return counter++
    }

    console.log(counterPlus()); // 2
    console.log(counter); // 3 

// Variable local

    function saludar() {
        let saludo = "Hola"
        console.log(saludo)
    }

    saludar()
// console.log(saludo) // <- ReferenceError: saludo is not defined

// 1.1 Dificultad Extra

function contador (string1, string2) {
    let count = 0
    for (let i = 1; i <= 100; i++) {
       if ( i % 3 === 0 && i % 5 === 0 ) {
          console.log(string1 + string2)
     } else if (i % 3 === 0){
      console.log(string1)
    } else if (i % 5 === 0){
        console.log(string2)
    } else {
      console.log(i)
      count++
    }
  }
    return count;
  }
  
  // Llama a la función con los parámetros de ejemplo
  let resultado = contador("fizz", "buzz");
  console.log("Cantidad de números impresos:", resultado);