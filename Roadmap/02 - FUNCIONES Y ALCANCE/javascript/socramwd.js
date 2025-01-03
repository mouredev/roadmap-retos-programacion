/*
    Funciones definidas por el usuario
*/

console.log('/* Función simple */')
function greet() {
    console.log('Hola Javascript')
}
greet()


console.log('**********-**********-**********-**********-**********')

console.log('/* Función con retorno */')
function returnGreet() {
    return 'Hola Javascript'
}
console.log(returnGreet())

console.log('**********-**********-**********-**********-**********')


console.log('/* Función con argumento */')
function argGreet(name) {
    console.log('Hola,', name)
}
argGreet('Marcos')

console.log('**********-**********-**********-**********-**********')


console.log('/* Función con argumentos */')
function argsGreet(greet, name) {
    console.log(greet, name)
}
argsGreet('Hola,', 'Marcos')


console.log('**********-**********-**********-**********-**********')


console.log('/* Función con argumentos por defecto */')
function defaultArgGreet(name = 'SocramDev') {
    console.log( 'Hola,', name)
}
defaultArgGreet()


console.log('**********-**********-**********-**********-**********')

console.log('/* Función con argumentos y retorno */')
function returnArgsGreet(greet, name) {
    return greet + ', ' + name
}
console.log(returnArgsGreet('Hola', 'Marcos'))


console.log('**********-**********-**********-**********-**********')


console.log('/* Función con retorno de varios valores */')
function multipleReturns() {
    return {
        greetVar: 'Hola',
        nameVar: 'Javascript'
    }
}
const { greetVar, nameVar } = multipleReturns()
console.log(greetVar)
console.log(nameVar)


console.log('**********-**********-**********-**********-**********')


/*
    Funciones definidas por el usuario
*/

console.log('/* Función dentro de función */')
function outerGreet() {
    innerGreet()
    console.log('Hola Outer Javascript')
}
function innerGreet() {
    console.log('Hola Inner Javascript')
}
outerGreet()


console.log('**********-**********-**********-**********-**********')


/*
    Funciones del lenguaje
*/

console.log('/* Length => cuenta los caracteres, incluídos los espacions */')
const completeName = 'Marcos Pérez'
console.log( completeName.length )

console.log('/* typeOf => tipo de dato */')
console.log(typeof(completeName))

console.log('/* toUpperCase => convierte el texto a mayúsculas */')
console.log(completeName.toUpperCase())


console.log('**********-**********-**********-**********-**********')


/*
    Scope - Variables locales y globales
*/
const globalVariable = 'Javascript'
console.log(globalVariable)
function helloJavascript() {
    const localVariable = 'Hola'
    console.log(localVariable, globalVariable)
}
helloJavascript()
// console.log(localVariable) => no se puede acceder fuera de la función


console.log('**********-**********-**********-**********-**********')


/*
    Extra
*/
function printNumbers( text_1, text_2 ) {
    let count = 0

    for (let i = 1; i < 101; i++) {
        if( i % 3 === 0 && i % 5 === 0) {
            console.log( i, ':', text_1, '', text_2 )
        } else if( i % 3 === 0 ) {
            console.log( i, ':', text_1 )
        } else if( i % 5 === 0 ) {
            console.log( i, ':', text_2 )
        } else {
            console.log( i )
            count++
        }
    }
    
    return count
}
console.log( 'El numero de veces que no hay texto es: ', printNumbers('Múltiplo de 3', 'Múltiplo de 5'))
