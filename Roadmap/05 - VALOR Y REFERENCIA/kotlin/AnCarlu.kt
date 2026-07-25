fun main() {
    //Asignacion de variables por valor

    var a = 10
    var b = a //Aqui se copia el valor
    a = 20

    println(
        "Asignación de variable por valor:" +
                "\na=$a, b=$b"
    )

    //Asignacion de variables por referencia
    data class Refer(var value: Int)

    var x = Refer(5)
    var y = x //Aqui ambas apuntan al mismo objeto, lo que se copia es la referencia, no el valor
    y.value = 10
    println(
        "Asignacion de variable por referencia:" +
                "\nAmbas variables apuntan al mismo objeto, " +
                "\npor lo que al cambiar el valor en una de las dos variables" +
                "\nambas se cambian:" +
                "\nx=${x.value}, y=${y.value}"
    )

    //Funciones con paremetros por valor
    fun modiferValue(number: Int): Int {
        return number + 5
    }

    var numero = 10
    println("El numero antes de cambiarlo $numero")
    numero = modiferValue(numero)
    println("Despues de cambiarlo $numero")

    //Funcion con parametro por referencia
    fun modifierRefer(refer: Refer) {
        refer.value = 100
    }

    var newNumber = Refer(50)
    println("Antes de cambiar la referencia ${newNumber.value}")
    modifierRefer(newNumber)
    println("Despues de cambiar la referencia ${newNumber.value}")


    //Extra

    var number1 = 10
    var number2 = 20
    //Programa para intercambiar las variables por valor
    println("Programa para intercambiar variables por valor:")
    fun extraValor(x: Int, y: Int): Pair<Int, Int> {
        /*
        Los parametros en kotlin son inmutables, por lo que no se pueden reasignar,
        para ello primero hay que crear nuevas variables
         */
        var number1 = x
        var number2 = y
        number1 += 5
        number2 += 8
        return Pair(number1, number2)
    }

    println("Valores antes de cambiar $number1 y $number2")
    var changeNumber = extraValor(number1, number2)
    number1 = changeNumber.first
    number2 = changeNumber.second
    println("Valores despues de cambiar $number1 y $number2")

    //Programa para intercambiar los parametros por referencia
    println("Programa para intercambiar parametros por referencia:")
    data class Persona(var nombre: String)

    var myName = Persona("Adrian")
    var yourName = Persona("Jorge")
    fun extraReferencia(a: Persona, b: Persona): Pair<Persona, Persona> {
        a.nombre = "Pepe"
        b.nombre = "Jose"
        var extraName1 = a.nombre
        var extraName2 = b.nombre

        return Pair(Persona(extraName1), Persona(extraName2))
    }

    println("Nombres antes de cambiar ${myName.nombre} y ${yourName.nombre}")
    extraReferencia(myName, yourName)
    println("Nombres despues de cambiar ${myName.nombre} y ${yourName.nombre}")
}