// Crea una función que se encargue de sumar dos números y retornar
// * su resultado.
// * Crea un test, utilizando las herramientas de tu lenguaje, que sea
// * capaz de determinar si esa función se ejecuta correctamente.

const assert = require('assert');

// Función a probar
function suma(a, b) {
    return a + b;
  }
 
  
  // Prueba para sumar 5 + 5
  function pruebasumar5y5() {
    const resultado = suma(5, 5);
    const esperado = 10;
    assert.strictEqual(resultado, esperado, '5 + 5 debería ser 10');
    console.log('Prueba sumar 5 + 5 pasó correctamente');
  }
  
  // Ejecutar la prueba
  pruebasumar5y5();

//   ---------------------

  //sumar cualquier numero con suma y resultado como argumento
  

  
  console.log('Todas las pruebas completadas');

  let suma1 = suma(7, 4)
  let resultado = 11
  let clg = '7 + 4 = 11'
  let suma2 = suma(8, 8)
  // let resultado2 = 16
  let clg1 = '8 + 8 = 16'
//   let suma3 = suma(2, 4)
//   let resultado3 = 5 //error forzado
//   let clg2 = '2 + 4 = 5, el resultado deberia ser 6' //crea un error y se cierra el programma
  
  function cuaquierSuma(suma, resultado, clg){
    assert.strictEqual(suma, resultado, 'son iguales')
    console.log(clg)
  }

  cuaquierSuma(suma1, resultado, clg)
  cuaquierSuma(suma2, 16, clg1)
//   cuaquierSuma(suma3, resultado3, clg2)

  //Ejercicio


const diccionario = {
    name : 'David',
    age : 30,
    birth_date : new Date("1987-04-29"),
    programming_languages : ['javaScript', 'Python', 'typeScript']

}

console.log(Object.values(diccionario))
console.log(Object.keys(diccionario))

//  * Crea dos test:
//  * - Un primero que determine que existen todos los campos.
//  * - Un segundo que determine que los datos introducidos son correctos.



// primer intento xd -----------------
// function test1 (valores1) {
//     const resultados = Object.values(valores1)
//     const respuestas = ['David', 30, '05 / 05 /92', [ 'javaScript', 'Python', 'typeScript' ]]
//     assert.strictEqual(resultados, respuestas)
//     console.log('son iguales' )
// }
// test1(diccionario)

function campos (obj) {
    const arr = Object.keys(obj)
    console.log( 'incluye name?' + arr.includes('name'))
    assert.strictEqual(arr[0], 'name')
    console.log('test pasado de name')
    console.log( 'incluye age?' + arr.includes('age'))
    assert.strictEqual(arr[1], 'age')
    console.log('test pasado de age')
    console.log( 'incluye birth_date?' + arr.includes('birth_date'))
    assert.strictEqual(arr[2], 'birth_date')
    console.log('test pasado de birth_date')
    console.log( 'incluye programming_languages?' + arr.includes('programming_languages'))
    assert.strictEqual(arr[3], 'programming_languages')
    console.log('test pasado de programming_languages')
    console.log('fin de el test 1')
}

campos(diccionario)

// test2 datos son correctos- -----------------------
// primer intento , debe estar en un bucle para que pueda ir preguntando cada que valor cambie de valor, por que sino entra en la primer if y despues se cierra el profeama (bucle for valor[i])


// function datos (obj){
//   const key = Object.keys(obj)
//   const valor = Object.values(obj)
//   if(key[0] === 'name' ){
//     if(typeof key[0] === 'string' ){
//       console.log('name es un string')
//     }else{
//       console.log('debes introducir un estring en name')
//     }
//   }else if(key[1] === 'age' ){
//     console.log('es toy en age')
//   }
// }

// datos(diccionario)


function datos1 (obj){
  const key = Object.keys(obj)
  const valor = Object.values(obj)
  console.log(  'el valor de ' + key[0] + ' debe ser un string : ' + typeof valor[0])
  assert.strictEqual(typeof valor[0], 'string')
    console.log('test pasado de string')
  console.log( 'el valor de ' + key[1] + ' debe ser un number : ' + typeof valor[1])
  assert.strictEqual(typeof valor[1], 'number')
    console.log('test pasado de number')
  console.log( 'el valor de ' + key[2] + ' debe ser un fecha : ' + (valor[2] instanceof Date))
  assert.strictEqual(typeof valor[2], 'object')
    console.log('test pasado de date')
  console.log( 'el valor de ' + key[3] + ' debe ser un array : ' +  Array.isArray(valor[3]) )
  assert.strictEqual(typeof valor[3], 'object')
    console.log('test pasado de array')
    console.log('fin de el test 2')
}

datos1(diccionario)


