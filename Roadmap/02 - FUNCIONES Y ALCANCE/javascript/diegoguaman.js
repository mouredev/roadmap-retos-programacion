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

//Funciones sin parametros ni retorno
function sinParametros() {
  console.log("funcion sin parametros");
}
sinParametros();

//Funcion con paramaetro sin retorno
function conParametros(nombre, edad) {
  console.log(`tu Nombre es: ${nombre} y tu edad es: ${edad} años`);
}
conParametros("Diego", 31);

//Funcion con retorno
function conRetorno(a, b) {
  return a + b;
}

function imprimir(mensaje, algo) {
  console.log(`${mensaje} ${algo}`);
}

imprimir("El suma es: ", conRetorno(1, 2));

//Funciones dentro de funciones
function externa() {
  console.log("funcion externa ejecutada");
  function interna() {
    console.log("Función interna ejecutada");
  }
  interna();
}
externa();

//Uso de funciones nativas del lenguaje
//Variables globales y locales
let word = "Global, fuera de la función ";
function globalLocal() {
  let wordLocal = "Local solo vivi dentro de la función";
  return word + wordLocal;
}
imprimir("Tu funcion es: ", globalLocal());
try {
  console.log(wordLocal);
} catch (error) {
  console.log(
    "No se puede imprimir una variable que ha sido declarada dentro de una función, fuera de la misma"
  );
}

//Extra

function numeros(cadena, cadena1) {
  let num = 0;
  for (let index = 0; index <= 100; index++) {
    if (index % 3 == 0 && index % 5 == 0) {
      console.log(cadena + " " + cadena1);
    } else if (index % 3 == 0) {
      console.log(cadena);
    } else if (index % 5 == 0) {
      console.log(cadena1);
      
    } else {
      console.log(index);
      num++;
    }

  }
  return num;
}

let resutado = numeros("Hola", "Caracola");
imprimir("El número de veces que se ha impreso el número: ", resutado);
