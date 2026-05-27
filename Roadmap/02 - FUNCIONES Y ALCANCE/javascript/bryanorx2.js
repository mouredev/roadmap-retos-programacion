//Función sin parámetro ni retorno
function saludar() {
    console.log("Hola mundo")
}
saludar()

//Función con parámteros, sin retorno
function saludarPersona(nombre) {
    console.log(`Hola, ${nombre}`)
}
saludarPersona("Bryan")

//Función con retorno
function sumar(a, b) {
    let suma = a + b
    return suma
}
let resultado = sumar(4,7)
console.log(resultado)

//Función con varios parámetros y retorno
function calcularPromedio(a, b, c) {
    let promedio = (a + b + c)/3
    return promedio
}
console.log(calcularPromedio(8, 6, 10))

//Función dentro de función
function operacion(num) {
    function doble(numero) {
        return numero*2
    }
    return doble(num)
}
console.log(operacion(5))

//Funciones ya creadas en el lenguaje
let max = Math.max(3, 7, 2)
console.log(max)

let mayus = "hola mundo"
console.log(mayus.toUpperCase())

let arrayNumbers = [5, 1, 3]
console.log(arrayNumbers.toSorted())

//Variable LOCAL vs GLOBAL
let mensaje = "Soy global"
function message() {
    let mensaje = "Soy local"
    console.log(mensaje)
}
message()
console.log(mensaje)

//FizzBuzz

function fizzBuzz(param1, param2) {
    let veces = 0
    for (let numero = 1; numero <= 100; numero++) {
        if (numero % 3 === 0 && numero % 5 === 0){
            console.log(param1+param2)
        } else if (numero % 3 === 0){
            console.log(param1)
        } else if (numero % 5 === 0) {
            console.log(param2)
        } else {
            console.log(numero)
            veces++
        }
    }
    return veces
}
let numVeces = fizzBuzz("Fizz", "Buzz")
console.log(numVeces)