// #02  FUNCIONES Y ALCANCE

/*
EJERCICIO:
- Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje: Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el concepto de variable LOCAL y GLOBAL.
Debes hacer print por consola del resultado de todos los ejemplos (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos.

Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
*/


// -------> FUNCION SIN PARAMETRO NI RETORNO <----------- //

function saludoSinParametroSinRetorno() {
  console.log(`Hola mundo`);
}

saludoSinParametroSinRetorno();


// ---------> FUNCION CON PARAMETRO SIN RETORNO <--------- //

function saludoConParametro( nombre ) {
  console.log(`Hola ${nombre}`);
}

saludoConParametro('Sebastian');


// --------> FUNCION CON RETORNO Y PARAMETRO <----------- //

function retorno( num1, num2 ) {
  return num1 + num2;
}

console.log(retorno( 10, 15 ));


// --------> FUNCION DENTRO DE OTRA FUNCION <---------- //

function funcionEnOtra(params) {
  function soyOtra() {
    console.log('Hola, soy una funcion dentro de otra');
  }
  return soyOtra();
}

funcionEnOtra();


// --------> FUNCION CON UNA VARIBALE GLOBAL <---------//

let variableGlobal = 'Sebastian';

function llamarGlobal() {
  console.log(variableGlobal);
}

llamarGlobal();


// --------> FUNCIION CON UNA VARIBALE LOCAL <--------//

function llamarLocal() {
  let variableLocal = 'Soy una variable local'
  console.log(variableLocal);
}

llamarLocal();


// ----------> FUNCION YA CREADA <--------------//


function funcionYaCreada() {
  alert('Sebastian :D');
}




//  Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
// - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
// - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
// - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
// - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
// - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

function tarea( str1, str2 ) {
  contador = 0;
  for (let i = 0; i <= 100; i++) {
    if ( i % 5 == 0 && i % 3 == 0 ) {
      console.log( str1, str2 );
    } else if ( i % 5 == 0 ) {
      console.log(str1);
    } else if ( i % 3 == 0 ) {
      console.log(str2);
    } else {
      contador++;
    }
  }
  return contador;
}

console.log(tarea('Sebastian', 'Marquez'));


