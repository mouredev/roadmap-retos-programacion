package com.mdoce.androidtutorial.mouredevretos

var global = 10

fun main() {
    saludo()
    saludoPersonalizado("Brais")
    println("7 + 5 = " + suma(5, 7))

    println(global)
    global = 20
    println(global)

    var total = dificultadExtra("m", "doce")
    println("Total = $total")
}

fun saludo() {
    println("Hola gente!")
}

fun saludoPersonalizado(nombre: String) {
    println("Hola $nombre!")
}

fun suma(numA: Int, numB: Int): Int {
    return numA + numB
}

fun dificultadExtra(nombre: String, apellido: String): Int {
    var contador: Int = 0

    for(i in 1..100) {
        if(i % 3 == 0 && i % 5 == 0) {
            println("$nombre $apellido")
        }
        else if(i % 3 == 0) {
            println("$nombre")
        }
        else if(i % 5 == 0) {
            println("$apellido")
        }
        else {
            println(i)
            contador++
        }
    }

    return contador
}