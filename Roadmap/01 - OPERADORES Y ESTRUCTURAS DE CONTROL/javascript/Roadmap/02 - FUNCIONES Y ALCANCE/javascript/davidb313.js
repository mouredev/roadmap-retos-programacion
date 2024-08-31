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

//funcion que no recibe parametros
const funcionSinParametros = () => {
  for (let i = 0; i < 7; i++) {
    console.log(i);
  }
};
funcionSinParametros();

//funcion que recibe parametros
const funcionSumarDosNumeros = (n1, n2) => {
  return n1 + n2;
};
console.log(funcionSumarDosNumeros(4, 7));

const ejercicio = (texto1, texto2) => {
  for (let i = 0; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(i, texto1, texto2);
    } else if (i % 3 === 0) {
      console.log(i, texto1);
    } else if (i % 5 === 0) {
      console.log(i, texto2);
    } else {
      console.log(i);
    }
  }
};
ejercicio("Multiplo de 3", "multiplo de 5");
