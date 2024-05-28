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

// Asignación de variables por valor 
var x = 5 // La variable x mantiene su valor 
var y = x // La variable y cambia al valor de la variable x

print(x) // Imprimir en la consola x
print(y) // Imprimir en la consola y

var x = y // La variable x cambia al valor de la variable y
var y = 10 // La variable y mantiene su valor 

print(x) // Imprimir en la consola x
print(y) // Imprimir en la consola y

// Asiganción de varibles por referencia 
struct Person {
    var nombre: String 
}

Person(nombre: "Julio") // Llamar la instancia de la estructura

var perfil1 = Person(nombre: "Julio") // La variable perfil mantiene su referencia 
var perfil2 = perfil1 // La variable perfil2 ahora hace referencia a perfil1

print(perfil1) // Imprimir en la consola perfil1
print(perfil2) // Imprimir en la consola perfil2

// Funciones para asignar valores
func sumar(_ a: Int) -> Int {
    return a + 1
}

var x = sumar(1) // La variable x aunmenta su valor en 1
var y = 5 // La variable y mantiene su valor 

print(x) // Imprimir en la consola x
print(y) // Imprimir en la consola y

func restar(_ a: Int) -> Int {
    return a - 1
}

var x = 5 // La variable x mantiene su valor 
var y = restar(1) // La variable y disminuye su valor en 1

print(x) // Imprimir en la consola x
print(y) // Imprimir en la consola y

// Funciones para asignar referencias 
func Perfil(_ a: String, _ b: String) -> (String, String) {
    return (a, b)
}

var x = Perfil("Carlos", "Pedro") // La varible x hace referencia a la funcion
var y = x // La variable y pasa a tener la refenrecia de x

print(x) // Imprimir en la consola x
print(y) // Imprimir en la consola y








