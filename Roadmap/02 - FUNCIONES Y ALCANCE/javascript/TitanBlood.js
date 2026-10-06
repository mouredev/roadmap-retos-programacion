/* 
Funciones en javascript
*/

//Declaracion de funcion normal sin parametros, devolviendo un string
function miFuncion() {
    return 'Este es el retorno de esta primera funcion'
}

let mensaje = miFuncion()
console.log(mensaje)

//Funcion con paramtros
function miFuncion2(a , b){
    let resultado = a ** b //Esta variable es local solo puede ser usada dentro del ambito de la funcion
    return `Este es el resultado ${resultado}`
}

let respuesta = miFuncion2(4, 6)
console.log(respuesta)

//Funcion que no retorna nada pero hace una accion

function miFuncion3(message) {
    console.log('Este es el mensaje que se genera en esta funcion: ', message)
}

miFuncion3('Hola k ase')

// Funciones anonimas asignadas a una variable
let miFuncion4 = function (num1) {
    for (let i=0; i<=num1; i++){
        let cuento = `Han pasado ${i} ovejas`
        console.log(cuento)
    }
}

miFuncion4(11)

//funciones flechas y variables globales y locales

let resultado = 0    //Esta variable puede ser usada dentro de la misma funcion directamente

let miFuncion5 = (num) => {
    let i = 0
    while (i <= num) {
        resultado = `resultado de ${num} * ${i}: ${num * i}`
        i++
        console.log(resultado)
    }
}

miFuncion5(15)

// Parametros por defecto

let miFuncion6 = (num1 = 4, num2 = 5) => {
    console.log(`Primer parametro usado: ${num1}`)
    console.log(`Segundo parametro usado: ${num2}`)
    let resultado = num1 % num2
    return resultado
}

let resultado6 = miFuncion6(8,)
console.log(resultado6)

//Se pueden crear funciones anidadas
function funcionAnidada(message){
    console.log('La funcion externa pasa aqui')
    function funcionDentro(){
        console.log(`Aqui se procesa la funcion interna con este mensaje: ${message}`)
    }
    funcionDentro()
}

funcionAnidada('yo sigo')

// Se puede pasar funciones como parametros se conocen tambien como callbacks y la que la usa se conoce como funcion de orden superior

function funcionSuperior(myfunc, num1, num2){
    console.log('Esta es la funcion de orden superior')
    let total = myfunc(num1, num2)
    return total
}

let resultadoSuperior = funcionSuperior(miFuncion6, 4, 6)
console.log(resultadoSuperior)

console.log('======================')
//Extra

function printNumbersAndText(str1, str2){
    let contNum = 0
    for (let i = 1; i<=100;i++){
        if ((i % 5 == 0) && (i % 3 == 0)){
            console.log(str1+str2)
        } else if (i % 5 == 0){
            console.log(str2)
        } else if (i% 3 == 0){
            console.log(str1)
        } else {
            console.log(i)
            contNum++
        }
    }
    return contNum
}

let numVeces = printNumbersAndText('Cadena1', 'Cadena2')
console.log('El numero de veces que se imprimio un numero son: ', numVeces)