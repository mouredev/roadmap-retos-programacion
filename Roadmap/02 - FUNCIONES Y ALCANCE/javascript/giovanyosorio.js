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

// Ejemplo de función sin parámetros ni retorno
function saludar() {
  console.log('Hola mundo!');
}

// Ejemplo de función con parámetros y retorno
function sumar(a, b) {
  return a + b;
}

// Ejemplo de función con varios parametros y retorno
function multiplicar(a, b, c) {
  return a * b * c;
}

// Ejemplo de función con parámetros y sin retorno
function imprimirNombre(nombre) {
  console.log(nombre);
}

//Ejemplo de función dentro de función
function funcionExterna() {
  function funcionInterna() {
    console.log('Función interna');
  }
  funcionInterna();
}

//Ejemplo de función ya creada en el lenguaje
function funcionCreada() {
  console.log('Función creada');
}

//Ejemplo de variable global
var variableGlobal = 'Variable global';

//Ejemplo de variable local
function funcionLocal() {
  var variableLocal = 'Variable local';
  console.log(variableLocal);
}

//Ejemplo de función que recibe dos parámetros de tipo cadena de texto y retorna un número
function extra(cadena1, cadena2) {
  for (var i = 1; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      console.log(cadena1 + cadena2);
    } else if (i % 3 == 0) {
      console.log(cadena1);
    } else if (i % 5 == 0) {
      console.log(cadena2);
    } else {
      console.log(i);
    }
  }
  return i;
}