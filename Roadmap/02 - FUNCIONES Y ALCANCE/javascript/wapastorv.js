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
  console.log('Hola!');
}
saludar(); // Imprime: Hola!

// Ejemplo de función con un parámetro y sin retorno
function saludarPersona(nombre) {
  console.log ('Hola ' + nombre + '!');
}
saludarPersona('Carlos'); // Imprime: Hola Carlos!

// Ejemplo de función con varios parámetros y sin retorno
function sumar(a, b) {
  console.log("La suma es: "+ (a + b));
}
sumar(2, 3); // Imprime: La suma es: 5

// Ejemplo de función con retorno y sin parámetros
function obtenerMensaje() {
  return 'Este es un mensaje';
}
console.log(obtenerMensaje()); // Imprime: Este es un mensaje

// Ejemplo de función con varios parámetros y con retorno
function multiplicar(a, b) {
  return a * b;
}
let multiplicarResultado = multiplicar(2, 3);
console.log('El resultado de la multiplicación es: ' + multiplicarResultado); // Imprime: El resultado de la multiplicación es: 6

// Ejemplo de función dentro de función(anidada)
function operacionCompleja(a, b) {
  function sumar(x, y) {
    return x + y;
  }
  function multiplicar(x, y) {
    return x * y;
  }
  
  let suma = sumar(a, b);
  let multiplicacion = multiplicar(a, b);

  console.log('La suma es: ' + suma);
  console.log('La multiplicación es: ' + multiplicacion);
}
operacionCompleja(2, 3); // Imprime: La suma es: 5, La multiplicación es: 6

// Ejemplo de función ya creada en el lenguaje
let texto = 'Hola, soy un texto de ejemplo para mostrar la longitud';
console.log(texto.length); // Imprime: 54
let numeros = [1, 2, 3, 4, 5];
let numerosInvertidos = numeros.reverse();
console.log(numerosInvertidos); // Imprime: [5, 4, 3, 2, 1]
let numerosOrdenados = numeros.sort();
console.log(numerosOrdenados); // Imprime: [1, 2, 3, 4, 5]
let numerosDobles = numeros.map(numero => numero * 2);
console.log(numerosDobles); // Imprime: [2, 4, 6, 8, 10]

// Ejemplo de variable LOCAL y GLOBAL

// Variable GLOBAL
let variableGlobal = 'Soy una variable global';
function mostrarVariableGlobal() {
  console.log(variableGlobal);
}
mostrarVariableGlobal(); // Imprime: Soy una variable global

// Variable LOCAL
function mostrarVariableLocal() {
  let variableLocal = 'Soy una variable local';
  console.log(variableLocal);
}
mostrarVariableLocal(); // Imprime: Soy una variable local

// Variable Global y Local en el mismo ámbito
let mensajeGlobal = 'Soy una variable global';

function mostrarMensaje() {
  let mensajeLocal = 'Soy una variable local';
  console.log(mensajeGlobal);// Puede acceder a la variable global
  console.log(mensajeLocal); // Puede acceder a la variable local
}
mostrarMensaje(); // Imprime: Soy una variable global, Soy una variable local
//console.log(mensajeLocal); // Genera un error porque la variable es local y no se puede acceder desde fuera de la función

// Ejemplos de sombra de variables (shadowing)
let mensaje = 'Soy una variable global';

function mostrarMensaje() {
  let mensaje = 'Soy una variable local';
  console.log(mensaje); // Imprime: Soy una variable local, porque se está accediendo a la variable local "shadowing"
}
mostrarMensaje();
console.log(mensaje); // Imprime: Soy una variable global, porque se está accediendo a la variable global

// Función que modifica una variable global
let contador = 0;

function incrementarContador() {
  contador++;
}
incrementarContador();// Incrementa el contador en 1
incrementarContador();// Incrementa el contador en 2
incrementarContador();// Incrementa el contador en 3
console.log("El valor del contador(global): "+contador); // Imprime: 3

// Función que modifica una variable local
function incrementarContadorLocal() {
  let contadorLocal = 0;
  contadorLocal++;
  return contadorLocal;
}
let contadorLocal = incrementarContadorLocal(); // Incrementa el contador en 1
console.log("El valor del contador(local): "+contadorLocal); // Imprime: 1

// Función que modifica una variable global y local
let contadorGlobal = 0;
function incrementarContadores() {
  contadorGlobal++;
  let contadorLocal = 0;
  contadorLocal++;
  return contadorLocal;
}
incrementarContadores(); // Incrementa el contador global en 1 y el contador local en 1
incrementarContadores(); // Incrementa el contador global en 2 y el contador local en 1
incrementarContadores(); // Incrementa el contador global en 3 y el contador local en 1
console.log("El valor del contador(global): "+contadorGlobal); // Imprime: 3
console.log("El valor del contador(local): "+incrementarContadores()); // Imprime: 1

// Función que utiliza let y const para ver el enlace de bloque
function mostrarVariables(){
    if (true) {
        var variableVar = 'Soy una variable var'; // Al ser var, se puede acceder desde fuera del bloque
        let variableLet = 'Soy una variable let'; // Al ser let, solo se puede acceder dentro del bloque
        const variableConst = 'Soy una variable const'; // Al ser const, solo se puede acceder dentro del bloque
        console.log(variableVar); // Imprime: Soy una variable var
        console.log(variableLet); // Imprime: Soy una variable let
        console.log(variableConst); // Imprime: Soy una variable const
    }
    console.log(variableVar); // Funciona porque es una variable var y se pue// Imprime: Soy una variable var, Soy una variable let, Soy una variable const, Soy una variable varde acceder desde fuera del bloque
    //console.log(variableLet); // Genera un error porque es una variable let y no se puede acceder desde fuera del bloque
    //console.log(variableConst); // Genera un error porque es una variable const y no se puede acceder desde fuera del bloque
}
mostrarVariables();


// Ejericio extra de función que recibe dos parámetros de tipo cadena de texto y retorna un número

function mostrarNumeros(cadena1, cadena2) {
  let contadorNumeros = 0;
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(cadena1 + cadena2);
    } else if (i % 3 === 0) {
      console.log(cadena1);
    } else if (i % 5 === 0) {
      console.log(cadena2);
    } else {
      console.log(i);
      contadorNumeros++;
    }
  }
  return contadorNumeros;
}
let contadorNumeros = mostrarNumeros('Múltiplo de 3', 'Múltiplo de 5');
console.log('El número de veces que se ha impreso un número es: ' + contadorNumeros); 

