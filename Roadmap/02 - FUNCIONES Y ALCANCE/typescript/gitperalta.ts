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

//* EJEMPLOS DE FUNCIONES

// Sin Parametros ni retorno
const sinParametros = () => {
  // Esta función no recibe parametros
  console.log("Esta funcion no retorna nada.");
};
sinParametros();

// Con Parametros y retorno
const conParametros = (a: string, b: string) =>
  // Esta función recibe 2 parametros
  console.log(`Esta función retorna ${a} y ${b}`);
conParametros("Hola", "Mundo");

// Con varios parametro
const conVariosParametros = (...params: number[]) => {
  // Esta función recibe varios parametros
  console.log(params.reduce((acc, ele) => ((acc += ele), 0)));
};
conVariosParametros(...Array.from({ length: 10 }, (_, index) => index + 1));

// CREANDO UNA FUNCIÓN DENTRO DE OTRA
const crearDentroDeOtra = (a: number) => {
  const interna = () =>
    `${a.toString()} al cuadrado e igual ${(a ^ 2).toString()}`;
  console.log(interna());
};
crearDentroDeOtra(4);

//FUNCIONES CREADAS POR EL LENGUAGE
console.log(Date()); // Devuelve la hora y fecha de este momento;
console.log(Math.random()); // Devuelve un numero random entre 0 y 1;
console.log("Hola Mundo".length); // Devuelve el numero de caracteres del string

// VARIABLE LOCAL Y GLOBAL
let a = "Hola Mundo";
const global = () => console.log(`La variable ${a} se puede usar globalmente`);
global();

const local = () => {
  let a = "Chau Mundo";
  return console.log(
    `La variable ${a} solo puede usarse en el scope en el que se encuentra.`
  );
};
local();

// DIFICULTAD EXTRA
const extra = (a: string, b: string): number => {
  let sum = 0;
  for (let i = 1; i <= 100; i++) {
    if (!(i % 5) && !(i % 3)) console.log(a + b);
    if (!(i % 5)) console.log(b);
    if (!(i % 3)) console.log(a);
    if (i % 3 && i % 5) sum++;
  }
  return 0;
};

console.log(extra("Fizz", "Buzz"));
