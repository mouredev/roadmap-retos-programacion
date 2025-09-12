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

// Funciones

// Función sin parámetros
console.log("Función sin parámetros:");

function holaMundo() {
  return "Hola Mundo!";
}

let hello = holaMundo(); // Devuelve "Hola Mundo!"
console.log(hello);

// Función con un parámetro
console.log("Función con un parámetro:");

function saludar(name) {
  return "Hola " + name + "!";
}

let saludo = saludar("Marcos"); // Devuelve "Hola Marcos!"
console.log(saludo);
let saludo2 = saludar(); // Devuelve "Hola undefined!"
console.log(saludo2);

// Función con dos parámetros
console.log("Función con dos parámetros:");

function suma(a, b) {
  return a + b;
}

let resultado = suma(5, 9); // Devuelve 14
console.log(resultado);

// Función con parámetros por defecto
console.log("Parámetros por defecto:");

function nuevoSaludo(tipo, nombre) {
  var tipo = tipo || "Hola";
  var nombre = nombre || "JavaScript";
  return tipo + " " + nombre + "!";
}

let bienvenida = nuevoSaludo(); // Devuelve "Hola JavaScript!"
let despedida = nuevoSaludo("Adiós"); // Devuelve "Adiós JavaScript!"
let hola = nuevoSaludo("Hola", "Marcos"); // Devuelve "Hola Marcos!"
console.log(bienvenida);
console.log(despedida);
console.log(hola);

// Ámbitos de una función
console.log("Ámbito de una función:");

let valor = "global";

function funcionLocal() {
  let valor = "local";
  return valor;
}

console.log(valor); // "global"
console.log(funcionLocal()); // "local"
console.log(valor); // "global"

// Funciones anidadas
console.log("Función anidada:");

let a = "Hola, ";

function global() {
  let b = "Qué ";

  function local() {
    let c = "tal?";
    return a + b + c;
  }

  return local();
}

global();

let saludando = global(); // Devuelve "Hola, Qué tal?"
console.log(saludando);

// Dificultad extra

function extra(string1, string2) {
  let contador = 0;

  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(string1 + string2);
      contador++;
    } else if (i % 3 === 0) {
      console.log(string1);
      contador++;
    } else if (i % 5 === 0) {
      console.log(string2);
      contador++;
    }
  }
  return contador;
}

console.log(extra("Cielo", "Razzo"));
