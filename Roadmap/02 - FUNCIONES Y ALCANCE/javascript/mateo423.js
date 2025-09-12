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

// Funcion sin parametros;
function saludar() {
  console.log('Hello Word');
};
saludar()


// Funcion con parametros; 
const count_numer = (hasta = 10) => {
  for (let i = 1; i <= hasta; i++) {
    console.log(i);

  };
};
count_numer();
console.log('  ');
// Funcion Callbacks Javascript;

const operacionMatematicas = (operacion, valor1, valor2) => operacion(valor1, valor2);

const sumar = (n1, n2) => n1 + n2;
const restar = (n1, n2) => n1 - n2;

const resultado = operacionMatematicas(sumar, 10, 3);
console.log(resultado);  // Resultado: 13
console.log("  ")

// Funcion Con return;
const despedida = function (lenguaje) {
  let mensaje;
  switch (lenguaje) {
    case 'es':
      mensaje = 'Adios';
      break
    case 'en':
      mensaje = 'Bye';
    default:
      mensaje = 'Tienes que elegir entre es/en'
  }
  return mensaje;
}
console.log(despedida('es'));

// Funciones anidadas;
/*Creador un contador dentro de una funcion anidada */

funcionExterna = function () {
  let contador = 0;
  return function funcionInterna() {
    contador++;
    console.log(contador);

  }
}
const contador = funcionExterna();
contador();
contador();
contador();


//  Variables locales  Variables Globales;

let variable_global = 'Variable Global';

const example = function () {
  let variable_local = 'Variable Local';
  console.log(variable_global);
  console.log(variable_local);
};
example();

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

const dificultad_extra = (mensaje1, mensaje2) => {
  let contador_numero = 0;
  for (let numero = 1; numero <= 100; numero++) {
    if (numero % 3 === 0 && numero % 5 === 0) {
      mensaje1 = 'Fizz';
      mensaje2 = 'Bazz'
      console.log(mensaje1 + mensaje2);
    } else if (numero % 3 === 0) {
      console.log(mensaje1);
    } else if (numero % 5 === 0) {
      console.log(mensaje2)
    } else {
      console.log(numero);
      contador_numero++;
    };
  };
  return contador_numero;

};
const vecesNumero = dificultad_extra('Fizz', 'Bazz');
console.log("El numero de veces que se repitio su numero fue " + vecesNumero);

