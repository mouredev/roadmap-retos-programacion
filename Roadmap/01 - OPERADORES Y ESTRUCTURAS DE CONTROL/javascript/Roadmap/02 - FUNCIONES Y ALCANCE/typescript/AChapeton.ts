// *** TIPOS DE FUNCIONES ***

//Funcion Autoejecutable
(function () {
  console.log("Autoejecutable");
})();

//Funcion por Declaracion
function saludar(): void{
    return console.log('Hello World!')
}

saludar()

//Funcion por Expresion
const saludo: () => void = function saludar2(){
    return console.log('Hola!')
}

saludo()

//Funcion Anonima
const anonima: () => void = function(){
    return console.log('Sin nombre')
}

anonima()

//Arrow Function
const arrow: () => void = () => {
    return console.log('Arrow function')
}

arrow()

//Callbacks
const funB = function(){
    return console.log('Funcion B ejecutada')
}

const funA = function(callback){
    callback()
}

funA(funB)


// *** FORMAS DE USO DE FUNCIONES ***
//Sin parametros
const sinParametros: () => void = () => {
    return console.log('Sin parametros')
}

//Con uno o varios parametros

const suma: (a: number, b: number) => void = (a: number, b: number){
    return console.log(a+b)
}

suma(4, 3)

//Sin retorno
const sinReturn: () => void = () => {
    console.log('Sin return')
}

sinReturn()

//Con retorno
const conReturn: () => number = () => {
    const sum = 4 + 5
    return sum
}

conReturn()


//Variable Local y Global

let globalVar = 10

const funcLocal: () => void = () => {
    const localVar = 4
    globalVar = 2
    return console.log(localVar + globalVar)
}

//localVar no es accesible fuera de la funcion
//globalVar esta disponible en cualquier lugar de la funcion

funcLocal()


//EJERCICIO EXTRA
const funbun: (firstText: string, secondText: string) => number = (firstText: string, secondText: string) => {
    let count: number = 0
    for(let i: number = 1; i <= 100; i++){
        if(i % 3 === 0 && i % 5 === 0){
            console.log(firstText + secondText)
        }else if(i % 3 === 0){
            console.log(firstText)
        }else if(i % 5 === 0){
            console.log(secondText )
        }else{
            count++
            console.log(i)
        }
    }

    console.log('Numeros impresos: ', count)
    return count
}

funbun('FUN', 'BUN')



