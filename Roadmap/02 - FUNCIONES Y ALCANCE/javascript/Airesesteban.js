/*
Crea ejemplos de funciones básicas que representen las diferentes
posibilidades del lenguaje:
Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
*/

// Funciones declaradas

function hello(){
    console.log("Hola!")
}
hello()

// Funciones expresadas

const helloExpresada = function(){
    console.log("Hola desde una funcion expresada")
}
helloExpresada()

// Función con retorno

function multiplicar(a,b) {
    return a * b
}
let result = multiplicar(2,3)
console.log(result)

// Uso de una función ya creada en el lenguaje

let numeroAleatorio = Math.random()
console.log(`Número aleatorio generado: ${numeroAleatorio}`)

// Funciones de flecha (Arrow functions)

const helloArrow = () => {
    console.log("Hola desde una arrow function")
}
helloArrow()


// Funciones de método
const objeto= {
    greet(){
        console.log("Hola desde funcion metodo")
    }
}
objeto.greet()

// Funciones constructoras

/* function Persona(nombre){
    this.nombre = nombre
}
const persona = new persona("Esteban")
console.log(persona.nombre)
 */

// Variable local y global

let variableGlobal = "Soy global"
function scope(){
    let variableLocal = "Soy Local"
    console.log(variableGlobal)
    console.log(variableLocal)
}

scope()
//console.log(variableLocal); // Esto dará un error porque variableLocal es local a la función

// Funciones anidadas

/*
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/

function multiplos(text1,text2){
    let count = 0
    for(let i=1; i<=100; i++){
        if (i % 3 == 0 && i % 5 == 0){
            console.log(text1+text2)
        }else if(i % 3 == 0){
            console.log(text1)
        }else if(i % 5 == 0 ){
            console.log(text2)
        }else{
            console.log(i)
            count ++
        }
    }
    return count
}

let contador = multiplos("Fizz", "Buzz")
console.log(contador)