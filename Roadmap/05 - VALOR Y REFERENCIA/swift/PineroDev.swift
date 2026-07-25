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

import Foundation

// Variables por Valor
var palabra: String = "Hola"
var numero: Int = 32
var myArray: [Int] = [1, 2, 3]
var miDiccionario: [Int : String] = [1: "Casa", 2: "Chalet"]

struct NumModel{
    var miNumero: Double
    var esPar: Bool
}
var num1 = NumModel(miNumero: 10.5, esPar: true)
var num2 = NumModel(miNumero: 20.5, esPar: false)

enum CarMode{
    case Honda
    case Lancia
}

var car1 = CarMode.Honda
var car2 = CarMode.Lancia

// Variables por referencia

class VentanaApp{
    let titulo: String
    var esVisible: Bool
    
    init(titulo: String, esVisible: Bool){
        self.titulo = titulo
        self.esVisible = esVisible
    }
}


// Dificultad Extra

var valor1: Int = 5
var valor2: Int = 7
var numeroValor1: Int = 0
var numeroValor2: Int = 0


func cambiarValores(valor1 : Int, valor2 : Int) -> (Int, Int)   {
    let nuevoValor1 = valor2
    let nuevoValor2 = valor1
    return (nuevoValor1, nuevoValor2)
}

var valores = cambiarValores(valor1: valor1, valor2: valor2)
numeroValor1 = (valores.0)
numeroValor2 = (valores.1)

print("Valores originales: valor1: \(valor1), valor2: \(valor2)")
print("Valores cambiados: valor1: \(numeroValor1), valor2: \(numeroValor2)")

class ClaseReferencias{
    var valor: Int = 0
    
    init(valor: Int) {
        self.valor = valor
    }
}

var valorClase1 = ClaseReferencias(valor: 13)
var valorClase2 = ClaseReferencias(valor: 25)
var valorCambiado1 = ClaseReferencias(valor: 0)
var valorCambiado2 = ClaseReferencias(valor: 0)


func cambiarValoresClase(valorClase1: ClaseReferencias, valorClase2: ClaseReferencias) -> (Int, Int) {
    let nuevoValorClase1 = valorClase2.valor
    let nuevoValorClase2 = valorClase1.valor
    return (nuevoValorClase1, nuevoValorClase2)
}

var valoresClase = cambiarValoresClase(valorClase1: valorClase1, valorClase2: valorClase2)
valorCambiado1.valor = (valoresClase.0)
valorCambiado2.valor = (valoresClase.1)

print("Valores originales: valor1: \(valorClase1.valor), valor2: \(valorClase2.valor)")
print("Valores cambiados: valor1: \(valorCambiado1.valor), valor2: \(valorCambiado2.valor)")
