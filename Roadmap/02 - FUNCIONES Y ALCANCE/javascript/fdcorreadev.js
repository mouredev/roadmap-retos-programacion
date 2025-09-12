/**
 * Funciones en JavaScript se incia con la palabra funcion + nombre + () + {} y dentro de los {} se pone el codigo necesario para 
 * 
 * La siguientes funcion es simple
 */

function greet() {
    console.log('mi primera impresion por consola dentro de una funcion ¡Hola Mundo!')
}

greet()

/**
 * esta funcion tiene un return que hace el proceso dentro y retorna un valor
 * @returns el saludo
 */

function return_greet() {
    return 'segunda pero retornando un valor ¡Hola Mundo!'
}

console.log(return_greet())

/**
 * funcion con solo un parametro
 * @param {String} name 
 * @returns devuele el saludo
 */
function greet_whit_name(name) {
    return `Hola soy ${name} y esta es la funcion con un paramtero`
}

console.log(greet_whit_name('Fabian Correa'))

/**
 * @param {number} num1 
 * @param {number} num2 
 * @returns 
 * Funcioneas con parametros de entrada en este caso dos valores para que los sume y returna el valor
 */

function sumarValores(num1, num2) {
    return num1 + num2
}
const result = sumarValores(4, 8)
console.log('funcion con dos parametros ' + result)

/**
 * Funcion con parametros por defecto 
 * @param {string} name 
 * @returns 
 */

function defaultValue(name = 'Fabian Correa') {
    return `Hola soy ${name} y esta es la funcion con parametros por defecto`
}

console.log(defaultValue('jose perez'))
console.log(defaultValue())

/**
 * Las funciones tambien se puedes asignar a una variable, o dento de un objeto
 * @returns La funcion guaradad
 */

const saveFunction = function greetSave() {
    return `Hola yo soy la Funcion Guardada`
}

console.log(saveFunction)
console.log(saveFunction())

//funcion que se puede pasar a otra variable

const otherFunction = saveFunction()
console.log('otra funcion guardada dentro de otra variable ', otherFunction)



//funcion guardad dentro de un objeto
const object = {
    methodSave: saveFunction()
}

console.log('funcion dentro de un objeto ', object.methodSave)

//Ejecutar una funncion pasada por parametro a otra funcion
function printOtherFunction(func) {
    console.log(`funcion ejecutada por otra funcion ${func()}`)
}

printOtherFunction(saveFunction)


/**
 * funcion fecha, funciona de igual forma pero no se utiliza la palabra funcion, se coloca () => {} esta es la forma de hacerlo
 */

const arrowFunction = () => {
    return `Hola soy una funcion flecha (arrow Function)`
}

console.log(arrowFunction())

/**
 *  estan un tipo de funciones que son muy importante en javascript que es el async que define una funcion asincronica el cual devuelve un objeto asyncFunction
 * se utiliza la funcion async antes de declararla y cuando esperamos el resultado le ponemos await
 */

function resolveAfter2Seconds(x) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(x)
        }, 2000);
    });
}

async function add1(x) {
    const a = await resolveAfter2Seconds(20);
    const b = await resolveAfter2Seconds(30);
    const z = x + a + b
    return z
}
//la forma de reolverlo es mediante una promesa  utilizando la funcion y then, y en caso alguno el finally que sale primero que la respuesta
//por la espera del await
console.log(add1(20))

add1(10).then((res) => {
    console.log(`mi primera promesa ${res}`)
}).finally(
    console.log('termino la promesa')
)

/**
 * funciones dentro de de otra funcion
 * 
 * te muestro un poco como se utiliza el await ya que esta primero la funcion y como sabemos el codigo va de arriba hacia bajo en este caso
 * cuando corremos el codigo primero se imprime la condicion que la funcion wait.
 */


const principalFunction = (typeFunction, name) => {

    async function wait(name) {
        const print = await name;
        console.log(`pero tambien te imprimo mi nombre ${print}`)
    }
    wait(name)

    if (typeFunction === "clasica") {
        function printName(name) {
            console.log(`${name} esto es una funcion clasica`)
        }
        printName(name)
    } else {
        const arrowFunction = (name) => {
            console.log(`${name} esto es una arrow function`)
        }
        arrowFunction(name)
    }
}

principalFunction('clasica', 'Fabian Correa')

/**
 * funciones propias del lengua en este caso de javascript, existen muchas en este ejemplo pongo pocas pero existen demasiadas
 * asi que les dejo el enlace para que pueda darle una chequeada https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Functions#funciones_predefinidas
 */
console.log("-----------------------------------------------------------Funciones del lenguaje-------------------------------------------")
const valor = '22'
console.log(`funcion para convertir de text a numero ${parseInt(valor)}`)
console.log(typeof parseInt(valor))

const string = 22
console.log(`funcion para convertir de numero a texto ${string.toString()}`)
console.log(typeof valor.toString())

const text = 'HoLa mUnDo! Fabian correa'
console.log(`pasa texto a mayusculas ${text.toUpperCase()}`)
console.log(`pasa texto a minuscula ${text.toLowerCase()}`)

let separarText = text.split(" ")
console.log('funcion para texto separado ', separarText)

separarText.map((palabra, index) => {
    console.log(`palabra ${index} ${palabra}`)
})


/**
 * En los leguajes de programacion existen variables globales y locales en javascript tiene esa parte bastante desarrollada, te explico con unos ejemplos
 * pero esto es para evitar re declarar o remplazar una variable por eso utilizamos solo let y const, porque "var" es bastante global 
 */

console.log('--------------------------GLOBAL Y LOCAL-----------------------------------------------------------------------')

/**
 * en este caso la variable var se deja remplazar.
 */

var texto = 'hola'

texto = 'si se puede'

console.log(texto)

// en este caso si porngo otro var con la misma se dej

var texto = 'si deja declarar de nuevo'

/**
 * en este caso la variable let tambien se deja remplazar.
 */

let varibaleLet = 'hola'

varibaleLet = 'si se puede'

console.log(texto)

// en el caso se let genera un error al igual que const
// let varibaleLet = 'no se deja declarar de nuevo'

/**
 * en este caso la variable const no deja porque hace referencia a constante osea no se modifica debe dar error.
 */

const varibaleConst = 'hola'

// varibaleConst = 'si se puede'

// console.log(texto)

/**
 * entonces con esta pequeña explicación vamos entendiendo un poco la declaraciones de global y local scope
 * como vemos a continuacion nosotros podemos declarar una variable afuera con el mismo nombre y no se ve afectada la de adentro de la funcion
 * pero que pasa si lo hacemos con let
 */

const replaceVariable = 'utilizar variable dento de la funcion'

function variableDeclarar() {
    const replaceVariable = 'esta es una variable nueva'
    return replaceVariable
}
console.log(replaceVariable)
console.log(variableDeclarar())

/**
 * en este caso let se puede utilizar dento de la funcion y remplazar el valor como se muestra en el siguiente ejemplo pero con
 * const no se puede generaria un error. 
 * 
 * en resumen el global es cuando tenemos una variable que podemos utilizar en varios segmentos de codigo y el local solo se puede utilizar dento
 * de un segmento de codigo que es lo ideal por buenas practicas es bueno siempre utilizar const.
 * 
 */

console.log('-----------------------------varibale con Let -------------------------------------------')
let replaceVariableLet = 'utilizar variable dento de la funcion'

function variableDeclararLet() {
    replaceVariableLet = 'esta es una variable nueva'
    return replaceVariableLet
}
console.log('--Anterior--', replaceVariableLet)
console.log(variableDeclararLet())
console.log('--Despues--', replaceVariableLet)


/**
 * Solucion de ejercicio Extra
 */

function Ejercicio02(text1, text2) {
    let coutOtherNumbers = 0
    for (i = 0; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(i, ' ', text1, i, ' ', text2)
        } else if (i % 3 === 0) {
            console.log(i, ' ', text1)
        } else if (i % 5 === 0) {
            console.log(i, ' ', text2)
        } else {
            coutOtherNumbers++;
        }
    }
    return coutOtherNumbers
}

const countValor = Ejercicio02('hola', 'mouredev')

console.log(`numeros que no son multiplos de 5 ni de 3 ${countValor}`)