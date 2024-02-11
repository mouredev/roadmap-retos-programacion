// FUNCIONES Y ALCANCE


/*
 * Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * */

// --- Sin parámetros ni retorno
console.log('*** Sin parámetros ni retorno ***');
function myFuncion() {
  console.log('Hello Word');
}
myFuncion();

// --- con uno o varios parámetros
console.log('*** Con uno o varios parámetros ***');
function saludo(nombre) {
  console.log(`Hola ${nombre}`);
}
saludo('Arbenis');

// con retorno
console.log('*** Con retorno ***');
function retornoSuma(num1, num2) {
  return num1 + num2;
}
const resultado = retornoSuma(1, 2);

console.log(resultado);

// ---- Comprueba si puedes crear funciones dentro de funciones.
console.log('***Función dentro de otra Función***');
function multiplicar(valor1) {
  return function (valor2) {
    return valor1 * valor2;
  }
}

let duplicar = multiplicar(2);
console.log(duplicar(5));

// ---- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
console.log('***Utiliza algún ejemplo de funciones ya creadas en el lenguaje***');

let aleatorio = Math.random(); // Funcion Math.random Devuelve un número flotante aleatorio entre 0 y 1 (sin incluir el 1):¿
console.log(aleatorio); // funcion console.log() Escribe un mensaje en la consola web o en el intérprete de JavaScript

// ---- - Pon a prueba el concepto de variable LOCAL y GLOBAL.

var x = "función externa declarada"; // Variable Global

scopeFunction();

function scopeFunction() {
  let interna = "funcion interna" // Variable local
  console.log(interna);
  console.log(x);
}

console.log("funcion externa");
console.log(x);


// ---- EXTRA ----

/**
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 */



function ejercicioExtra(parametro1, parametro2) {
  let contador = 0;
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(parametro1 + parametro2);
    } else if (i % 3 === 0) {
      console.log(parametro1);
    } else if (i % 5 === 0) {
      console.log(parametro2);
    } else {
      contador += 1;
    }
  }
  return contador;
}

let impreso = ejercicioExtra("Pin", "Pon");
console.log(`Número de veces que se imprimió el número: ", ${impreso}` );
