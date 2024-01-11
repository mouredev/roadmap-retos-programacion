// Sin parámetros
function saludar() {
    console.log("Yo soy Groot") // Yo soy Groot
}

saludar() // De esta manera se realiza el llamado a la función para que se ejecute

// Con parámetros
let pelicula = "Guardianes de la galaxia"

function cine(pelicula) {
    console.log(`Me gusta mucho ${pelicula}`) // Me gusta mucho Guardianes de la galaxia
}

cine(pelicula) 

// Con retorno
function fiesta(edad) { // Si las variables se escriben directamente en los parámetros no necesitan ser declaradas
    return `Eres menor de edad, tienes ${edad} años, no puedes venir a la fiesta` 
}

let respuesta = fiesta(15)
console.log(respuesta) // Eres menor de edad, tienes 15 años, no puedes venir a la fiesta

// Funciones dentro de funciones
function decirHola(nombre, apellido) {
    
    function nombreApellido(nombreCompleto) {
        return nombreCompleto = `${nombre} ${apellido}`
    }

    console.log("Hello, " + nombreApellido()) // Hello, Alan Walker
}

decirHola("Alan", "Walker") 

// Variable GLOBAL: está FUERA de funciones o estructuras de control
var global = "Soy global"

function varGlobal() {
    console.log(global) // Soy global
}

varGlobal()
console.log(global) // Soy global

// Variable LOCAL: está DENTRO de funciones o estructuras de control
function varLocal() {
    let local = "Soy local"
    console.log(local) // Soy local
}

varLocal()
console.log(local) // local is not defined

//-------------------------------------------------------------------------------------------------------------------------------

/**
 * Funciones anónimas:
 * Las funciones anónimas son aquellas que NO necesitan un nombre, se pueden almacenar directamente en una "variable", por lo cual,
 * el "nombre" de la variable se convierte en el nombre de la función.
*/

// Nota: la variable "sumar" solo almacena la función, más no el valor que retorna.
let sumar = function (a, b, c) {
    return a + b + c
}

let resultado = sumar(2, 4, 5)
console.log(resultado) // 11

/**
 * Las funciones anónimas también pueden ser autoinvocadas, o sea que no necesitan un "nombre", sino que seguido de las llaves se le pasan
 * los valores de sus parámetros y, de esa manera estamos "creando" la función y al mismo tiempo la estamos "ejecutándo".
 */

(function (a, b, c) {
    console.log(a * b * c) // 200
}(10, 4, 5))


/**
 * Funciones como constantes:
 * Las funciones se deben declarar con la palabra reservada “const” porque su funcionalidad nunca va a cambiar (a menos que se refactorice),
 * lo único que cambiará es el valor que retorna, más no su funcionalidad.
 */

const saludar = function (nombre) {
    console.log(`Hola ${nombre}`)
}

saludar("Juan") // Hola Juan

/**
 * Funciones flecha:
 * Se llaman funciones flechas porque permiten "simplificar" la forma en que se escriben las funciones, y para ello se utiliza el operador “⇒”.
 */

// Función constante normal
const restar = function (c, d) {
    return c - d
}

console.log(restar(10, 5)) // 5

/*
Como la función anterior NO tiene nada de lógica, sino que lo que hace es una opereación sencilla y retorna algo inmediatamente,
lo que se puede hacer es reescribir la función anónima quitándole la palabra "function" y las "{}", quedando así:
*/

// Función constante expresada como función flecha
const resta = (a, b) => a - b

console.log(resta(10, 5)) // 5

// Cuando solo se recibe 1 parámetro se pueden borrar los paréntesis, pasando de esto "(nombre)" a esto "nombre", quedando así:
const saludar = nombre => `Hola ${nombre}`

console.log(saludar("Bim Bom")) // Hola Bim Bom

// Para escribir una función flecha más larga se hace así:
const nombre = nombre => {

    if(typeof nombre === "string") {
            console.log(nombre)
    } else {
            console.log("Tipo de dato incorrecto") // Tipo de dato incorrecto
    }
}

nombre(3)

//-------------------------------------------------------------------------------------------------------------------------------

// Ejercicio
function dificultadExtra(cadena1, cadena2) {

    contador = 0;
    for(let i = 1; i < 101; i++) {
        
        if(i % 3 === 0 && i % 5 == 0){
            console.log(`${cadena1} ${cadena2}`)
        } 
        else if(i % 3 === 0) {
            console.log(cadena1)
        } 
        else if(i % 5 === 0) {
            console.log(cadena2)
        } 
        else {
            contador++
            console.log(i)
        }
    }
    return console.log(`El número se ha impreso ${contador} veces`)
}

dificultadExtra("Yo soy...", "Groot")