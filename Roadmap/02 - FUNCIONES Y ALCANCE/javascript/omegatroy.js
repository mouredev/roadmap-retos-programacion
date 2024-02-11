/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...✅
 * - Comprueba si puedes crear funciones dentro de funciones.✅
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.✅
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.✅
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)✅
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

// esto es una funcion mas basica
function holaMundo(){
  console.log('hola mundo')
}
holaMundo()

// esta funcion resive un parametro (nombre) que nosotros se lo pasamos cuando la llamemos
function saludar(nombre){
  console.log(`hola ${nombre}, como estas?`)
}
saludar('OmegaTroy')// <---- aca le estamos pasando el nombre OmegaTroy ala funcion

//esta funcion recive varios parametros ala vez
//tambien es una funcion flecha o arrow function
const resta =(num1,num2,num3)=>{
  console.log(num1 - num2 - num3)
}
resta(11,20,50)

// esta funcion nos retorna el numero 12
function numero(){
  return 12
}
console.log(`el numero es ${numero()}`)


// esta funcion recive dos parametros numeros y nos retorna la suma de estos numeros
const suma =(num1,num2)=>{
  return num1 + num2
}
console.log(suma(2,3))

// esta funcion tiene otro funcion dentro
function funcionUno(param1) {
  function funcionDos(param2) {
      return param1 + param2;
  }
  return funcionDos;
}
console.log(funcionUno(13)(23));

//Funciones ya creadas en el lenguaje
let cadena = `No tiene sentido decir una mentira que te consuele, así que te diré la verdad`;

//La funcion/metodo slice() extrae parte de un string
console.log(cadena.slice(3, 8));
//La funcion/metodo replace() reemplaza la primera ocurrencia que encuentra en la cadena
console.log(cadena.replace("verdad", "mentira"));

//Variable local y global

let global = 'Variable global'

function funcionVariables(){
  let local = ' funcion'
  return global + local
}

console.log(funcionVariables())


function fizzBuzz(str1,str2){
  for(let i = 0; i <= 100; i++) console.log(`${i % 3 ? '' : str1}${i % 5 ? '' : str2}` || i)
}
fizzBuzz('Fizz', 'Buzz')