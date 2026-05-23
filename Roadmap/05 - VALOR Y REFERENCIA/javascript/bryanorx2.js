/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 */

//Asignación por valor
let num1 = 10
let num2 = num1
num2 = 20
console.log(num1, num2)

//Asignación por referencia
let objeto = {"nombre" : "Bryan"}
let objetoNuevo = objeto
objetoNuevo["nombre"] = "Orlando"
console.log(objeto, objetoNuevo)

//Función con parámetro por valor
function sumar(numero) {
    let suma = numero+100
    return suma

}
let number = 10
console.log(number)
console.log(sumar(number))

//Función con parámetros por referencia
function cambio(obj) {
    obj["nombre"] = "Orlando"
    return obj
}
let objNew = {"nombre" : "Bryan"}
console.log(objNew)
console.log(cambio(objNew))

/* DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

//Por Valor
function porValor(c, d) {
    let temp = c
    c = d
    d = temp
    return [c, d]
}
let a = "Hola"
let b = "Mundo"

let [newA, newB] = porValor(a, b)
console.log(a, b)
console.log(newA, newB)

//Por Referencia

function porReferencia(obj3, obj4) {
    let temp = obj3["valor"]
    let copiaObj1 = {...obj3}
    let copiaObj2 = {...obj4}
    copiaObj1["valor"] = copiaObj2["valor"]
    copiaObj2["valor"] = temp
    return {copiaObj1, copiaObj2}
}

let obj1 = {"valor" : "Hola"}
let obj2 = {"valor" : "Mundo"}

let {copiaObj1, copiaObj2} = porReferencia(obj1, obj2)
console.log(obj1, obj2)
console.log(copiaObj1, copiaObj2)