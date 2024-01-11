fun main() {
    println(("-".repeat(9) + " OPERADORES ARITMÉTICOS " + "-".repeat(9)))

    print("\tOperador '+': 3+6 = ")
    println(3+6)
    print("\tOperador '-': 6-3 = ")
    println(6-3)
    print("\tOperador '*': 3*6 = ")
    println(3*6)
    print("\tOperador '/': 6/3 = ")
    println(6/3)
    print("\tOperador '%': 6%3 = ")
    println(6%3)


    println(('\n'+"-".repeat(9) + " OPERADORES LÓGICOS " + "-".repeat(9)))

    print("\tOperador '&&': true && false = ")
    println(true && false)
    print("\tOperador '||': true || false = ")
    println(true || false)
    print("\tOperador '!': !false = ")
    println(!false)


    println(('\n'+"-".repeat(9) + " OPERADORES DE COMPARACIÓN " + "-".repeat(9)))

    print("\tOperador '<': 3<6 = ")
    println(3<6)
    print("\tOperador '<=': 3<=6 = ")
    println(3<=6)
    print("\tOperador '>': 3>6 = ")
    println(3>6)
    print("\tOperador '>=': 3>=6 = ")
    println(3>=6)
    print("\tOperador '==': 3==6 = ")
    println(3==6)
    print("\tOperador '!=': 3!=6 = ")
    println(3!=6)
    print("\tOperador '===': 3===3 = ")
    println(3===3)

    println(('\n'+"-".repeat(9) + " OPERADORES DE ASIGNACIÓN " + "-".repeat(9)))

    println("\tvar n = 7")
    var n = 7
    print("\tOperador '+=': n += 3 ---> ")
    n+=3
    println(n)
    print("\tOperador '-=': n -= 3 ---> ")
    n-=3
    println(n)
    print("\tOperador '*=': n *= 3 ---> ")
    n*=3
    println(n)
    print("\tOperador '/=': n /= 3 ---> ")
    n/=3
    println(n)
    print("\tOperador '%=': n %= 3 ---> ")
    n%=3
    println(n)


    println(('\n'+"-".repeat(9) + " OPERADORES DE INCREMENTO Y DECREMENTO " + "-".repeat(9)))

    println("\tvar a = 3")
    var a = 3
    print("\tOperador '++': ++a = ")
    println(++a)
    print("\tOperador '--': --a = ")
    println(--a)


    println(('\n'+"-".repeat(9) + " OPERADORES DE BITS " + "-".repeat(9)))

    print("\tOperador 'and()': 3 and 6 = ")
    println(3 and 6)
    print("\tOperador 'or()': 3 or 6 = ")
    println(3 or 6)
    print("\tOperador 'xor()': 3 xor 6 = ")
    println(3 xor 6)
    print("\tOperador 'shl()': 3 shl 6 = ")
    println(3 shl 6)
    print("\tOperador 'shr()': 3 shr 6 = ")
    println(3 shr 6)
    print("\tOperador 'ushr()': 3 ushr 6 = ")
    println(3 ushr 6)
    print("\tOperador 'inv()': (a es la variable del apartado anterior) a.inv = ")
    println(a.inv())


    println(('\n'+"-".repeat(9) + " EJEMPLOS CON ESTRUCTURAS DE CONTROL " + "-".repeat(9)))

    println(("-".repeat(3)) + "EJERCICIO 1" + ("-".repeat(3)))
    while(true) {
        try {
            println("Escribe un número para comprobar si es par o impar: ")
            val num = readln().toInt()

            if (num %2 == 0){
                println("Es par")
            }else{
                println("Es impar")
            }
            break
        }catch(e: Exception){
            println("Que sea un número")
        }
    }

    println(("-".repeat(3)) + "EJERCICIO 2" + ("-".repeat(3)))
    println("Vamos a contar las vocales. Pon una palabra: ")
    val word = readln()
    val vocals = "aeiou"
    val count = mutableListOf<Char>()

    for (letter in word){
        if (letter in vocals){
           count.add(letter)
        }
    }
    println(count.size)

    println(("-".repeat(3)) + "EJERCICIO 3" + ("-".repeat(3)))
    val rangeNum = 1..30
    val numChosen = rangeNum.random()
    var vidas = 5

    do {
        print("Escoge un número entre 1 y 30: ")
        val choose = readln().toInt()

        if(choose > numChosen){
            println("El número es menor. Pon uno más pequeño. Te quedan $vidas")
            vidas -= 1
        }else if(choose < numChosen){
            println("El número es mayor. Pon uno más grande. Te quedan $vidas")
            vidas -= 1
        }
        if (vidas == 0){
            println("Perdiste. El número era $numChosen")
            break
        }
    } while (choose != numChosen)

    if(vidas > 0){
        println("Ganaste!")
    }


    println('\n'+"*".repeat(11)+" EXTRA "+"*".repeat(11))
    val nums = mutableListOf<Int>()

    for (n in 10..55) {
        if (n % 2 == 0 && n % 3 != 0 && n != 16) {
            nums.add(n)
        }
    }
    println(nums)
}
