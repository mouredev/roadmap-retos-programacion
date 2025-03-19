import Foundation

/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */


// Asignación por valor
var x = 10 // x es de tipo Int, que es un tipo de valor
var y = x // y es una copia de x
x = 20 // cambiamos el valor de x
print(x) // imprime 20
print(y) // imprime 10, no se ve afectado por el cambio de x


// Asignación por valor
var x = 10 // x es de tipo Int, que es un tipo de valor
var y = x // y es una copia de x
x = 20 // cambiamos el valor de x
print(x) // imprime 20
print(y) // imprime 10, no se ve afectado por el cambio de x


// Paso por valor
func incrementar(_ n: Int) -> Int { // n es una copia del valor que se pasa como argumento
    return n + 1
}

var a = 5 // a es de tipo Int, que es un tipo de valor
var b = incrementar(a) // b es el resultado de la función incrementar con a como argumento
print(a) // imprime 5, no se ve afectado por la función
print(b) // imprime 6


// Paso por valor
func incrementar(_ n: Int) -> Int { // n es una copia del valor que se pasa como argumento
    return n + 1
}

var a = 5 // a es de tipo Int, que es un tipo de valor
var b = incrementar(a) // b es el resultado de la función incrementar con a como argumento
print(a) // imprime 5, no se ve afectado por la función
print(b) // imprime 6



// Solución para el caso de parámetros por valor
func intercambiarPorValor(_ x: Int, _ y: Int) -> (Int, Int) {
    // Esta función recibe dos parámetros por valor y los intercambia entre ellos
    // Retorna una tupla con los valores intercambiados
    return (y, x)
}

var r = 3 // r es de tipo Int, que es un tipo de valor
var s = 4 // s es de tipo Int, que es un tipo de valor
print("Antes del intercambio:")
print("r = \(r)") // imprime r = 3
print("s = \(s)") // imprime s = 4
var (t, u) = intercambiarPorValor(r, s) // llamamos a la función intercambiarPorValor con r y s como argumentos, y asignamos su retorno a dos nuevas variables t y u
print("Después del intercambio:")
print("r = \(r)") // imprime r = 3, no se ve afectado por la función
print("s = \(s)") // imprime s = 4, no se ve afectado por la función
print("t = \(t)") // imprime t = 4, tiene el valor de s
print("u = \(u)") // imprime u = 3, tiene el valor de r


// Solución para el caso de parámetros por referencia
func intercambiarPorReferencia(_ x: inout Persona, _ y: inout Persona) -> (Persona, Persona) {
    // Esta función recibe dos parámetros por referencia y los intercambia entre ellos
    // Retorna una tupla con las referencias intercambiadas
    let temp = x // guardamos la referencia de x en una variable temporal
    x = y // asignamos la referencia de y a x
    y = temp // asignamos la referencia de la variable temporal a y
    return (x, y)
}

var v = Persona(nombre: "Mario") // v es una instancia de Persona
var w = Persona(nombre: "Laura") // w es una instancia de Persona
print("Antes del intercambio:")
print("v.nombre = \(v.nombre)") // imprime v.nombre = Mario
print("w.nombre = \(w.nombre)") // imprime w.nombre = Laura
var (x, y) = intercambiarPorReferencia(&v, &w) // llamamos a la función intercambiarPorReferencia con v y w como argumentos, usando el operador & para indicar que se pasan por referencia, y asignamos su retorno a dos nuevas variables x y y
print("Después del intercambio:")
print("v.nombre = \(v.nombre)") // imprime v.nombre = Laura, se ve afectado por la función
print("w.nombre = \(w.nombre)") // imprime w.nombre = Mario, se ve afectado por la función
print("x.nombre = \(x.nombre)") // imprime x.nombre = Mario, tiene la referencia de w
print("y.nombre = \(y.nombre)") // imprime y.nombre = Laura, tiene la referencia de v
