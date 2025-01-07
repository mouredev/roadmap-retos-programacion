/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 */
 
 


// Función sin parámetros ni retorno;
// Retorna el valor de la expresión que se le pasa como parámetro.

function felicitar() {
    console.log("¡Felices fiestas!");
}
felicitar();


// Función con un parámetro;
function morning (nombre) {
  console.log("¡Buenos días, "+nombre+ "!");
}
morning("Raúl");


// Función add tiene dos parámetros (a, b). 
// Los argumentos (2, 3) se asignan a los parámetros a y b.
function add (a, b) {
  return a + b;
}
console.log(add(2,3)); 

//Función dentro de función
function calcularAreaTriangulo(base, altura) {
  function calcularArea() {
      return 0.5 * base * altura;
  }
  
  return calcularArea();
}

// Usando la función
let area = calcularAreaTriangulo(5, 3);
console.log("El área del triángulo es:", area);


// Ejemplos de funciones ya creadas en el lenguaje:
console.log("Funciones creadas en javascript");

// Función isFinite() determina si el valor pasado es un número finito. 
// Si el valor no es un número, primero intenta convertirlo a uno. 
// Si es un número finito, devuelve true; en caso contrario, devuelve false.
console.log(isFinite(10));        // true (10 es un número finito)
console.log(isFinite(-5.5));      // true (-5.5 es finito)
console.log(isFinite(Infinity)); // false (Infinity no es finito)
console.log(isFinite(NaN));      // false (NaN no es un número finito)
console.log(isFinite("10"));     // true (El string "10" se convierte a número)
console.log(isFinite("Hello"));  // false (No puede convertirse en número)
console.log(isFinite(undefined));// false (No puede convertirse en número)

//Función isNaN() determina si el valor pasado es NaN (Not-a-Number). 
// Si el valor no es un número, intenta convertirlo. 
// Si después de la conversión sigue siendo NaN, devuelve true; de lo contrario, devuelve false.
console.log(isNaN(NaN));        // true (El valor es NaN)
console.log(isNaN("Hello"));    // true (No puede convertirse a número)
console.log(isNaN(undefined)); // true (No puede convertirse a número)
console.log(isNaN(10));         // false (10 es un número válido)
console.log(isNaN("10"));       // false (El string "10" se convierte a número)
console.log(isNaN(true));       // false (true se convierte a 1, que es un número)

// Función Number.isNaN() es más estricto y devuelve true sólo si el valor es exactamente NaN, sin coerción.
console.log(Number.isNaN("Hello"));  // false (Strict check: "Hello" is not NaN, it's a string)

//Función parseInt() convierte una cadena de texto en un número entero.
// Si la cadena no contiene un número, devuelve el valor de defaultValue.
// Si la cadena contiene un número, devuelve el número. Si la cadena no puede ser convertida a número, devuelve NaN.
console.log(parseInt("10")); // 10
console.log(parseInt("Hello")); // 0
console.log(parseInt("10", 16)); // 16
console.log(parseInt("10", 10)); // 10
console.log(parseInt("0x10", 16)); // 16
console.log(parseInt("010", 2)); // 2


//Variable local, declarada en la función y variable global o declarada fuera de la función.

function globalVariable() {
  var globalVariable = "globalVariable";
  function localVariable() {
    var localVariable = "localVariable";
    console.log(globalVariable); // globalVariable
    console.log(localVariable); // localVariable
  }
  localVariable();
}
globalVariable();


// Global variables
var street = "Calle Mayor";
var city = "Madrid";

function myGlobalAddress() {

  // Local variables
  var country = "España";
  var building = "III";
    
    return building + " " + street + ", " + city + ", " + country; 
}

console.log(myGlobalAddress()); // invocamos desde fuera de la función

function myLocalDetails() {
    var floor = "3rd-floor";
    var flat = "1B";
    var door = "left";
    console.log( floor + " " + flat + " " + door ); // invocamos desde dentro de la función
}

myLocalDetails(); // podemos invocar myLocalDetails desde fuera, pero no podemos acceder a las variables dentro de la función. 
// Las variables son locales de esa función.


/*DIFICULTAD EXTRA (opcional):
* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
* - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
*   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
*   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
*   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
*   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/
function myString (multiploDe3, multiploDe5) {
  let count = 0;
  let i = 1;
    
  while (i <= 100) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(multiploDe3 + " y " + multiploDe5);
      count++;
  } else if (i % 3 === 0) {
      console.log(multiploDe3);
      count++;
  } else if (i % 5 === 0) {
      console.log(multiploDe5);
      count++;
  } else {
      console.log(i);
  }
        i++;
    }
    return count;
}

console.log(myString("Multiplo de 3", "Multiplo de 5"));