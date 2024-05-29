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

console.log('== Funciones en Javascript ==');

console.log('== Funciones sin parámetros ni retorno ==');

function functionSinParametros() {
  console.log("Esta es una función que no recibe parámetros.");
  console.log("Y que no retorna ningun valor especifico.");
}
functionSinParametros();

console.log('== Funciones sin parámetros con retorno ==');

function functionConRetorno() {
  console.log('Esta función retorna el valor del número PI.');
  return Math.PI;
}
console.log(functionConRetorno());

console.log('== Funciones con parámetros ==');

function functionConString(string){
  console.log('Esta función coge una string como parámetro.');
  console.log(`Este es el parametro introducido: ${string}.`);
}
functionConString('Programación');
function functionConNumeros(num1, num2){
  console.log(`Esta función recoge dos parámetros: ${num1} y ${num2} y los suma.`)
  return num1 + num2;
}
console.log(functionConNumeros(2,5));

function functionConStringYNumeros(string, num1, num2) {
  console.log("Establece un string con la operación y dos numeros:")
  if (string === 'suma') {
    console.log(`Suma de ${num1} y ${num2}:`);
    return num1 + num2;
  }
  else if (string === 'resta') {
    console.log(`Resta de ${num1} y ${num2}:`);
    return num1 - num2;
  }
  else if (string === 'multiplicacion') {
    console.log(`Multiplicación de ${num1} y ${num2}:`)
    return num1 * num2;
  }
}

console.log(functionConStringYNumeros('suma', 8, 5));
console.log(functionConStringYNumeros('resta', 10, 3));
console.log(functionConStringYNumeros('multiplicacion', 2, 3));

console.log('== Funciones dentro de funciones ==');

function suma(num1, num2) {
  return num1 + num2;
}

function sumaDosNumeros(suma, num1, num2){ // En este caso utilizamos una función como argumento.
  return suma(num1, num2);
}

console.log(sumaDosNumeros(suma, 2, 6));

function restaDosNumeros(num1, num2) { // En este caso creamos una función dentro de la otra función.
  function resta() {
    return num1 - num2;
  }
  return resta();
}

console.log(restaDosNumeros(10, 5));


console.log('== Funciones del sistema ==');

let str = "Esta es una string de ejemplo.";
console.log(str);
console.log(str.toUpperCase());

console.log('== Variables locales y globales ==');

function showMessage() {
  let message = "¡Hola Javascript!"
  return message;
}
console.log(showMessage());
// console.log(message); no podemos acceder a una variable declarada dentro de la función.

let name = 'Surgeon'

function showName() {
  console.log(`Variable ${name} declarada de forma global.`)
}
showName();
function showName2(){
  name = "DJ";
  console.log(`Cambiamos la variable ${name} dentro de la función.`);
}
showName2();
console.log(name);
function showName3(){
  let name = 'Regis';
  console.log(`Establecemos una variable local: ${name}.`);
}
showName3();
console.log(name);

console.log('== Dificultad Extra ==');

function dificultadExtra(str1, str2) {
  let count = 0;
  for (let i = 1; i <= 100; i++) {
    if(i % 3 === 0 && i % 5 === 0) {
      console.log(str1 + " " + str2);
    }
    else if(i % 3 === 0) {
      console.log(str1);
    }
    else if( i % 5 === 0 ) {
      console.log(str2);
    } 
    else {
      count++
      console.log(i);
    }
  }
  return count;
}

console.log(dificultadExtra('Hola', 'Mundo'));
