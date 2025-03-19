fun main() {

    // Paso por valor
    var valorUno = 3
    var valorDos = 5

    val variablesValor = variablesValor(valorUno, valorDos)

    val newValorUno = variablesValor.first
    val newValorDos = variablesValor.second

    println("Variables por valor originales: ")
    println("$valorUno $valorDos")
    println("Variables por valor nuevas: ")
    println("$newValorUno $newValorDos")

    // Paso por referencia
    var referenciaUno = arrayOf(2)
    var referenciaDos = arrayOf(4)

    val variablesReferencia = variablesReferencia(referenciaUno, referenciaDos)

    val newReferenciaUno = variablesReferencia.first
    val newReferenciaDos = variablesReferencia.second

    println("Variables por referencia originales: ")
    println("${referenciaUno[0]} ${referenciaDos[0]}")
    println("Variables por referencia nuevas: ")
    println("${newReferenciaUno[0]} ${newReferenciaDos[0]}")
}

fun variablesValor(variableUno: Int, variableDos: Int): Pair<Int, Int> {
    val copyVariableUno = variableUno
    val copyVariableDos = variableDos
    
    return Pair(copyVariableDos, copyVariableUno)
}

fun variablesReferencia(variableUno: Array<Int>, variableDos: Array<Int>): Pair<Array<Int>, Array<Int>> {
    val temp = variableUno[0]
    variableUno[0] = variableDos[0]
    variableDos[0] = temp

    return Pair(variableUno, variableDos)
}