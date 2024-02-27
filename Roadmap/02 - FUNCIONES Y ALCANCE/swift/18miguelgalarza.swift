//: [Previous](@previous)

/*
 * 18miguelgalarza.swift #02 - swift
 * EJERCICIO: #02 FUNCIONES Y ALCANCE
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno... [OK]
 * - Comprueba si puedes crear funciones dentro de funciones. [OK-factible]
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje. [OK]
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.  [OK]
 * - Debes hacer print por consola del resultado de todos los ejemplos. [OK]
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

//Funciones básicas

func simple(){print("Hola Mundo!")}

func conParametros(_ nombre:String, _ apellido:String){

print("Hola \(nombre) \(apellido)!")

}

func operadorAritmetico(_ valor1:Int, _ valor2:Int, _ operacion:String) -> Double{
//Funcion con parametros de entrada y retorno
    
    switch operacion {
    case "suma":
        return Double(valor1 + valor2)
    case "resta":
        return Double(valor1 - valor2)
    case "multiplicacion":
        return Double(valor1 * valor2)
    case "division":
        return Double(valor1 / valor2)
    default:
        return Double(-500)
    }

}

func getSkateboard(){
 //Funcion que indica las partes del skate y el fabricante
    func tabla(){print("Tabla: Zero")}
    func ruedas(){print("Ruedas: Pig Wheels")}
    func truck(){print("Truck: Independent")}
    func lija(){print("Lija: MOB Grip")}
    func estoboles(){print("Estoboles: Spitfire")}
    func rodajes(){print("Rodajes: Bones ABEC 03")}
    
    tabla()
    ruedas()
    truck()
    lija()
    estoboles()
    rodajes()
    
}


var variableGlobal = "Variable global" // Variable global en Swift

func funcionVaribleLocal() { // Variable local en Swift

    let variableLocal = "Variable local"
    print(variableLocal) // variable local puedo ser usado dentro de esta función
    print(variableGlobal) // variable global puedo ser usado afuera y dentro de esta función
}



//Testing
print("********** Funciones Básicas : Testing **********")
simple()
conParametros("Miguel","Galarza")
print("Funcion con parametros de entrada y retorno \(Int(operadorAritmetico(2,2,"suma")))")

funcionVaribleLocal()
//print(variableLocal) // Esto genera error, variableLocal solo es visible dentro de funcionVaribleLocal()
print(variableGlobal) // Imprime: Soy una variable global

getSkateboard()//funciones dentro de otra funcion


print("********** Dificultad Extra **********")
/**
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 */

func dificultadExtra ( _ param01 : String, _ param02 : String ) -> Int {
    
    var contador:Int = 0
    
    for numero in 1...100 {
      
            if (numero % 3) == 0 && (numero % 5) == 0 {
            print("El número \(numero) es multiplo de 3 y 5 -> \(param01) \(param02)")
            contador += 1
            }else if (numero % 3) == 0{
            print("El número \(numero) es multiplo de 3 -> \(param01)")
            contador += 1
            }else if (numero % 5) == 0{
            print("El número \(numero) es multiplo de 5-> \(param02)")
            contador += 1
            }else{
            print("El número \(numero) no tiene coincidencias")
            }
    }
    
    return contador
}

func dificultadExtraVersion02 ( _ param01 : String, _ param02 : String ) -> Int {
    
    var contador:Int = 0

        for i in 1...100{
            switch (i.isMultiple(of: 3), i.isMultiple(of: 5)){
            case(true, true): print("El número \(i) es múltiplo de 3 y 5 -> \(param01) \(param02)"); contador += 1
            case(false, true): print("El número \(i) es múltiplo de 3 -> \(param01)"); contador += 1
            case(true, false): print("El número \(i) es múltiplo de 5-> \(param02)"); contador += 1
            default: print("El número \(i) no es múltiplo con 3 y 5")
            }
        }
    
    return contador
}



print("\nLas veces que se han impreso los textos son :  \( Int(dificultadExtra("Miguel","Galarza"))) veces")
print("\nLas veces que se han impreso los textos son :  \( Int(dificultadExtraVersion02("Miguel","Galarza"))) veces")


let banner = """
             
                                                   hhhhhhh
                                                   h:::::h
                                                   h:::::h
                                                   h:::::h
ppppp   ppppppppp  uuuuuu    uuuuuu     ssssssssss  h::::h hhhhh
p::::ppp:::::::::p u::::u    u::::u   ss::::::::::s h::::hh:::::hhh
p:::::::::::::::::pu::::u    u::::u ss:::::::::::::sh::::::::::::::hh
pp::::::ppppp::::::u::::u    u::::u s::::::ssss:::::h:::::::hhh::::::h
 p:::::p     p:::::u::::u    u::::u  s:::::s  ssssssh::::::h   h::::::h
 p:::::p     p:::::u::::u    u::::u    s::::::s     h:::::h     h:::::h
 p:::::p     p:::::u::::u    u::::u       s::::::s  h:::::h     h:::::h
 p:::::p    p::::::u:::::uuuu:::::u ssssss   s:::::sh:::::h     h:::::h
 p:::::ppppp:::::::u:::::::::::::::us:::::ssss::::::h:::::h     h:::::h
 p::::::::::::::::p u:::::::::::::::s::::::::::::::sh:::::h     h:::::h
 p::::::::::::::pp   uu::::::::uu:::us:::::::::::ss h:::::h     h:::::h
 p::::::pppppppp       uuuuuuuu  uuuu sssssssssss   hhhhhhh     hhhhhhh
 p:::::p
 p:::::p
p:::::::p
p:::::::p
p:::::::p
ppppppppp
                                                                       
                                                                         
"""

print(banner)

