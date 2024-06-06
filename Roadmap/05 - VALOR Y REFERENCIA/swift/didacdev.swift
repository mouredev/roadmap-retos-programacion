import Foundation

// Paso por valor
var valorUno: Int = 3
var valorDos: Int = 5

func variablesValor(variableUno: Int, variableDos: Int) ->  (vairableUno: Int, variableDos: Int){
    let copyVariableUno = variableUno
    let copyVariableDos = variableDos

    return (copyVariableDos, copyVariableUno)
}

let variablesValor: (Int, Int) = variablesValor(variableUno: valorUno, variableDos: valorDos)

let newValorUno = variablesValor.0
let newValorDos = variablesValor.1

print("Variables por valor originales: ")
print("\(valorUno) \(valorDos)")
print("Variables por valor nuevas: ")
print("\(newValorUno) \(newValorDos)")

// Paso por referencia
var referenciaUno: Int = 2
var referenciaDos: Int = 4

func variablesReferencia(variableUno: inout Int, variableDos: inout Int) -> (variableUno: Int, variableDos: Int) {
    let copyVariableUno = variableUno
    let copyVariableDos = variableDos

    variableUno = copyVariableDos
    variableDos = copyVariableUno

    return (variableUno, variableDos)
    
}

let variablesReferencia: (Int, Int) = variablesReferencia(variableUno: &referenciaUno, variableDos: &referenciaDos)

let newReferenciaUno = variablesReferencia.0
let newReferenciaDos = variablesReferencia.1

print("Variables por referencia originales: ")
print("\(referenciaUno) \(referenciaDos)")
print("Variables por valor nuevas: ")
print("\(newReferenciaUno) \(newReferenciaDos)")