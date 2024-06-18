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

// +++++++++ FUNCIÓN SIN PARÁMETROS NI RETORNO +++++++++
function hello() {
  console.log("¡Hola mundo con JavaScript!");
}

hello();

// +++++++++ FUNCIÓN CON PARÁMETROS +++++++++
function addition(firstNumber, secondNumber) {
  console.log(firstNumber + secondNumber);
}

addition(13, 20);

// +++++++++ FUNCIÓN CON PARÁMETROS Y RETORNO +++++++++
function checkAge(age, name) {
  if (age >= 18) {
    return name + " eres mayor de edad."
  } else {
    return "Eres menor de edad " + name + "."
  }
}

console.log(checkAge(17, "Raúl"));

// +++++++++ FUNCIONES ANIDADAS +++++++++
function greet(name, lastName) {
  function fullName() {
    return name + " " + lastName;
  }

  console.log('Hello ' + fullName() + "!");
}

greet("Samus",  "Aran");

// +++++++++ EJEMPLOS DE FUNCIONES EXISTENTES EN JAVASCRIPT +++++++++
// parseInt() y console.log()
var numberAsAString = "16";
var number = parseInt(numberAsAString, 10);
console.log("Tipo de dato antes de utilizar parseInt: " + typeof numberAsAString);
console.log("Tipo de dato después de utilizar parseInt: " + typeof number);

// +++++++++ VARIABLES GLOBAL Y LOCAL +++++++++
var globalMessage = "The last Metroid is in captivity."

function fullMessage(localMessage) {
  var localMessageVariable = localMessage;
  console.log(globalMessage + " " + localMessageVariable);
}

fullMessage("The galaxy is at peace...");
console.log("Este mensaje no se mostrará porque localMessageVariable es una variable local: " + localMessageVariable);

// +++++++++ DIFICULTAD EXTRA +++++++++
var auxiliaryCounter = 0;

function series(textOne, textTwo) {
	for(var index = 1; index <= 100; index++) {
	  if (index % 3 === 0 || index % 5 === 0) {
			if (index % 3 === 0 && index % 5 === 0) {
        console.log(textOne + " y " + textTwo);

      } else if (index % 3 === 0) {
          console.log(textOne);

      } else if (index % 5 === 0) {
        console.log(textTwo);
      }
    } else {
      auxiliaryCounter++;
      console.log(index);
    }
  }

	return auxiliaryCounter;
}

series("Múltiplo de tres", "Múltiplo de cinco");
console.log("Número de veces que se imprimieron números: " + auxiliaryCounter);
