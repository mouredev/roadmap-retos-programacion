//1 - Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:

// funsion simple -------------------------------
    // Autoejecutable
(function () {
    console.log("Autoejecutable");
  })();
    //declarativa
function hello (){
    console.log('hello word , funcion declarativa')
}


    //  Expresión (anónimas)
const sumFunction = function (a, b){
    return a+ b
}



    // Flecha (arrow)
const arrowFunction = (a, b) => {
    return a * b
} 


// con retorno ------------------------------------

function square(number) {
    return number * number;
  }
//   este return puedo grardarlo en una variable
let area =  square(4)


// con argumento  -----------------------------------
function nombre (nombre)  {
    console.log('mi nombre es ' + nombre)
}



function idioma (idioma, nombre)  {
    console.log(idioma + nombre)
}



// argumento default 

function defaultsuma (a =5, b = 2 ){
    return a*b
}



//Callbacks
var funB = function () {
    return console.log('Funcion B ejecutada');
  };
  var funA = function (callback) {
    callback();
  };


//2 - Comprueba si puedes crear funciones dentro de funciones.
    //Sucesión de Fibonacci complegidad 2^n

function fibonacci (num) {
    if(num < 2) return num
    //funciona en 0 y 1 retorna  num , cuando el numero es mayor , va retrocediendo hasta llegar al 1al llegar al 1 entra en el if y es por eso que se puede parar la recursividad
    
return fibonacci(num-2) + fibonacci(num-1)
}

console.log(fibonacci(10))

//3- Pon a prueba el concepto de variable LOCAL y GLOBAL.
// no esoty seguro si es lo que pide...
// "String.split()String.substring()String.trim()Array.map()Array.push()Array.pop()String.slice()Array.slice()Object.toString()Number.toFixed()parseInt()Math.random()console.log()" 

//4 - Pon a prueba el concepto de variable LOCAL y GLOBAL.

const varGlobal = 10
function sumLocalGlobal (num){
    const local = num
    return local + varGlobal
}

console.log(sumLocalGlobal(5))

// - Debes hacer print por consola del resultado de todos los ejemplos.
hello()
console.log('funcion expersión anónimas : '+ sumFunction( 5, 2))
console.log('funcion de flecha : ' + arrowFunction( 8, 3))
console.log(area)
nombre('David')
idioma('hi', 'david')
idioma('hola', 'david')
console.log(defaultsuma())
console.log(defaultsuma(20 , 10))
funA(funB);


// DIFICULTAD EXTRA (opcional):
// * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
// * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
// *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
// *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
// *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
// *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

// primer intento no funciona 
// function extra (cadena1, cadena2){
//     let contador = 0
// for(let i = 1; i <= 100; i++){
//    if (i % 3 != 0){
//       console.log(cadena1)
//    }
//    if (i % 5 != 0){
//       console.log(cadena2)
//    }
//    if(i%3 != 0 && i%5 !=0){
//      console.log(cadena1 + cadena2)
//    }else
//    contador ++
//    console.log(i)
// }
// return contador
// }

// console.log(extra('dmultiplo3', 'dmultiplo de 5'))

//correcion
function correccionExtra ( multiplo, multiplo2){
let contador = 0
for (let i = 1; i <= 100; i++){
    if (i % 3 === 0 && i % 5 === 0){
        console.log(  ` es ${multiplo} y ${multiplo2}`)
    }else if(i % 5 === 0){
        console.log(multiplo2)
    }else if(i % 3 === 0){
        console.log(multiplo)
    }
    contador ++
    console.log(i)
} return contador
}

console.log(correccionExtra('multiplo de 3', 'multiplo de 5'))
// correcion de coomit
