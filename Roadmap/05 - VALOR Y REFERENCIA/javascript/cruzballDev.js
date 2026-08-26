/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 */

// Variables (tipos de datos primitivos) se pasan "por valor".

let a = 3;
let b = 5;
let c = a;
console.log(c)
c = 6;
console.log(c) // Se crea una copia independiente con el mismo valor o con otro valor distinto, ya que cada variable tiene su propio espacio en memoria.
// Todos los tipos de datos primitovos como: string , number, boolean etc... Osea todos lo que no son objetos, se pasan por valor y los que son objetos
// se pasan por referencia como son: Array, funciones, Set, Map, Objet etc...

// Objetos se pasan "por referencia" (todos los que NO son datos primitivos).
let persona1 = {
    nombre: "Juan",
    edad: 35
}
console.log(persona1)

let persona2 = persona1;
console.log(persona2)

persona2.nombre = "Manuel"
console.log(persona2)
console.log(persona1) // Los objetos se pasan por referencia y comparten el mismo espacio en memoria,
                      // por lo cual si se modifica uno también se modifica el otro.

// Funciones con variables que se les pasan "por valor"
let d = 2
let e = 8
function sumar(numero1, nuemero2){
    suma = d + e
    return suma
}

console.log(sumar())

// Funciones con variables que se les pasan "por referencia"
function cambiarNombre(persona) {

    //persona.nombre = "Adolfo" // apunta a usuario, por lo que usuario cambia su valor; Resultado: "Adolfo"

    persona = { // ya no apunta a usuario porque hemos creado un objeto distinto llamdo persona.
        nombre: "Adolfo" // Resultado: "Pablo" ; ya que usuario no cambia su valor porque no entra en la función.
    }
}

let usuario = {
    nombre: "Pablo"
}
console.log(usuario.nombre)

cambiarNombre(usuario)
console.log(usuario.nombre)

/* * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
*/


// Asignar por valor
let f = 7
let g = 10

function intercambioValor(valor1, valor2) {
    let valor3 = valor1
    valor1 = valor2
    valor2 = valor3
    return [valor1, valor2]
}

console.log(f, g)

let resultadoValor = intercambioValor(f, g)

let h = resultadoValor[0]
let i = resultadoValor[1]
console.log(h, i)


// Asignar por referencia

let coche1 = {
    marca: "BMW",
    modelo: "E36"
}

let coche2 = {
    marca: "Ford",
    modelo: "Fiesta"
}
console.log(coche1.marca, coche2.marca)

function intercambiarReferencia(objeto1, objeto2) {
    return [objeto2, objeto1]
}

let resultadoReferencia = intercambiarReferencia(coche1, coche2)

let coche3 = resultadoReferencia[0]
let coche4 = resultadoReferencia[1]

console.log(coche3.marca, coche4.marca)