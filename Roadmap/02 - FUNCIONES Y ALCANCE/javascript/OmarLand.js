// 02# - Funciones y Alcance
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


// Función sin parámetros ni retorno:
const Saludar = () =>{
    let localVar = "Soy una variable local"
    console.log("Soy una función básica");
}
Saludar();

// Función con parámetros y retorno
const Suma = (a, b) => {
 return a + b;
}
console.log("Función con parámetros y retorno: ", Suma(10, 5) );

// Función dentro de una función
//Calculo total de un impuesto

const calcularTotalConImpuesto = (monto) => {
    const tasaImpuesto = 0.21;

    // Función interna para calcular el impuesto
    const agregarImpuesto = (monto) => {
        return monto * tasaImpuesto;
    }

    // Calcular el total sumando el monto original más el impuesto
    const total = monto + agregarImpuesto(monto);
    return total;
}

const totalConImpuesto = calcularTotalConImpuesto(100); // Por ejemplo, para un monto de 100
console.log(`El total después de impuestos es: ${totalConImpuesto}`);

//  función ya creadas en el lenguaje.

let cadena = "hola soy javascript, un lenguaje de programación poderoso"

console.log("Cambio en mayusculas la cadena:");
console.log("Cadena original: ", cadena);
console.log("Cadena cambiada>>> ", cadena.toUpperCase() );


/* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 */


let varGlobal = "Soy Global";

const returnStr = (str1, str2) => {
  let varLocal = "Soy Local";
  let contador = 0;
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(str1 + str2);
      contador++;
    }
    if (i % 3 === 0) {
      console.log(str1);
      contador++;
    }
    if (i % 5 === 0) {
      console.log(str2);
      contador++;
    }
    if (i % 3 !== 0 && i % 5 !== 0) {
      console.log(i);
      contador++;
    }
  }

  return contador;
};

console.log( ` Hola ${localVar} ` );
console.log( ` Hola ${globalVar} ` );


returnStr( "Fizz","Buzz" );