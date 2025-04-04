/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

import Foundation

func funSimple() {
    print("Función sin parámetros ni retorno.")
}

func conParamentro(valor1: Int, valor2: Int) {
    print(valor1 + valor2)
}

func conRetorno(valorD1: Double, valorD2: Double) -> Double {
    return valorD1 + valorD2
}

// Llamada a funcion funSimple
funSimple()

// Llamada a funcion ConParametro
var valor1 = 9
var valor2 = 7
conParamentro(valor1: valor1, valor2: valor2)

// Llamada a conRetorno
var total = 0.0
var valorD1 = 3.5
var valorD2 = 6.2
total = conRetorno(valorD1: valorD1, valorD2: valorD2)
print(total)


// Funcion con funciones dentro y datos locales
let isUserName: Bool = true
let isPremium: Bool = false

func comprobarUser (isUserName: Bool, isPremium: Bool){
    var correcto: String  = ""
    var incorrecto: String  = ""
    
    func bienvenido() -> String{
        return "Bienvenido usuario Premium"
    }
    func noPremium() -> String{
        return "No eres Premium"
    }
    
    if isUserName && isPremium {
        correcto = bienvenido()
        print(correcto)
    }else {
        incorrecto = noPremium()
        print(incorrecto)
    }
}
comprobarUser(isUserName: isUserName, isPremium: isPremium)

//------------------------------------------

//DIFICULTAD EXTRA

func imprimirNum(parametro1: String, parametro2: String) -> Int{
    var cont: Int = 0
    for i in 1...100{
        if i % 3 == 0 && i % 5 == 0{
            print(parametro1+parametro2+" \(i)")
        }else if i % 3 == 0{
            print(parametro1+" \(i)")
        }else if i % 5 == 0{
            print(parametro2+" \(i)")
        }else{
            cont += 1
        }
    }
    return cont
}

let resultado = imprimirNum(parametro1: "Papaya", parametro2: "Higos")
print("Cantidad de numero que no son multiplos de 3, 5 y 3 y 5 conjuntamente: \(resultado)")
