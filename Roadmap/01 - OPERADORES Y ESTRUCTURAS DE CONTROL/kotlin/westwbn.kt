fun main() {
//    Operadores:
//    #Aritméticos
    var money = 1000
    val numberOne = 5
    val numberTwo = 3
    val addition = numberOne + numberTwo
    val subtraction = numberOne - numberTwo
    val multiplication = numberOne * numberTwo
    val division = numberOne / numberTwo
    val module = numberOne % numberTwo

    println("Suma: $addition \nResta: $subtraction \nMultiplicación: $multiplication \nDivisión: $division \nModulo: $module")

//    #Logicos
    val conditionTrue = true
    val conditionFalse = false
    println()
    println("conditionTrue AND conditionFalse: ${conditionTrue && conditionFalse}")
    println("conditionTrue OR conditionFalse: ${conditionTrue || conditionFalse}")
    println("NOT conditionTrue: ${!conditionTrue}")

//  #Comparación
    println()
    println("$numberOne es igual a $numberTwo?: ${numberOne == numberTwo}")
    println("$numberOne no es igual a $numberTwo?: ${numberOne != numberTwo}")
    println("$numberOne es mayor que $numberTwo?: ${numberOne > numberTwo}")
    println("$numberOne es menor que $numberTwo?: ${numberOne < numberTwo}")
    println("$numberOne es mayor o igual que $numberTwo?: ${numberOne >= numberTwo}")
    println("$numberOne es menor o igual que $numberTwo?: ${numberOne <= numberTwo}")

//    #Asignación
    println()
    println("Actualmente hay $$money")
    money += 1200
    println("Se realizo una venta y se añadieron $1200. El saldo es de $${money}")
    money -= 500
    println("Se descontaron $500 de impuestos, el dinero total disponible es $$money")

//    #Pertenencia
    println()
    val listNumber = listOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    println("2 esta en la lista?: ${2 in listNumber}")
    println("18 no esta en la lista?: ${18 !in listNumber}")

//    Estructuras de control
//    #If
    println()
    if (numberOne in listNumber) {
        println("$numberOne esta en la lista!")
    }

//    #If - Else
    println()
    if (money in listNumber) {
        println("El numero $money esta en la lista")
    } else {
        println("El numero $money no esta en la lista")
    }

//    #When
    val shoppingCart = listOf("Leche", "Galletitas", "Fideos", "Aceite", "Mayonesa", "Gaseosa")
    val favorites = listOf("Carne", "Pollo", "Huevos")

    println()
    println("Selecciona una opción: \n 1) Carrito de compras \n 2) Favoritos \n 3) Menú principal\n")
    val option = readln().toInt()

    when (option) {
        1 -> {
            println("El carrito contiene los siguientes artículos:")
            shoppingCart.forEach { articles -> println(articles) }
        }

        2 -> {
            println("Sus artículos favoritos son:")
            favorites.forEach { articles -> println(articles) }
        }

        3 -> println("Regresando al menu principal..")
        else -> println("Elige una opcion correcta")
    }

//    #For
    println("\nLa cesta contiene:")
    for (article in shoppingCart) {
        println(article)
    }

//    #While
    var loop = 10
    print("\nCuenta regresiva: ")
    while (loop >= 0) {
        print("${loop--}..")
    }
    println("\n")

//    #Do while
    var life = 500
    do {
        val damage = (1..minOf(100, life)).random()

        life -= damage
        println("Daño enemigo: $damage \nSalud: $life")

        if (life < 1) {
            println("++Fin del juego!++")
            break // Salir del bucle cuando la vida es baja
        }

    } while (life > 0)

//    Ejercicio Extra
    extraExercise()
}

fun extraExercise() {
    println()
    println("Resultado del ejercicio extra:")
    for (number in 10..55 step 2) {
        if (number == 16 || number % 3 == 0) {
            continue
        }
        println(number)
    }
}