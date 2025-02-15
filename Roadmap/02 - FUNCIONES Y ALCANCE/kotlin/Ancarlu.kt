import org.intellij.lang.annotations.Language


//Variable global
const val name = "Adrian"

fun main() {
    //Fucniones básicas de Kotlin
    //Sin parametros ni retorno
    basic()

    //Con parametros
    param(name)

    //Con retorno
    println(retorno())

    //Con parametro y retorno
    println(both(2, 3))

    //Funciones lambda
    lamba(5, 6) {
        println("El ejemplo de una función lambda da como resultado $it")
    }

    //Funcion dentro de funcion, que en Kotlin se denominan anidadas
    nested()

    //Ejemplos de funciones ya creadas en kotlin
    val z = name.length
    println("Mi nombre tiene " + z + " letras")
    val upper = name.uppercase()
    println(upper)

    println(
        "El numero de veces que se ha impreso el número en lugar de los textos es "
                + exercise2("Kotlin", "Jetpack Compose")
    )
}


fun exercise2(char1: String, char2: String): Int {
    var x = 0

    for (i in 1..100) {
        if (i % 3 == 0 && i % 5 != 0) {
            println(char1)
        } else if (i % 5 == 0 && i % 3 != 0) {
            println(char2)
        } else if (i % 3 == 0 && i % 5 == 0) {
            println(char1 + char2)
        } else {
            println(i)
            x++
        }
    }
    return x
}

fun nested() {
    fun example() {
        //Ejemplo de variable Local
        val kotlin = "Kotlin"
        println("Estoy programando en $kotlin")
    }
    example()
}

fun lamba(x: Int, y: Int, resultado: (result: Int) -> Unit) {
    resultado(x * y)
}

fun both(x: Int, y: Int): String {
    //Variable local
    var suma = x + y
    return "La suma de $x + $y es $suma"
}

fun retorno(): String {
    return "Ejemplo de fuincion devolviendo algun parametro"
}

fun param(name: String) {
    println("Me llamo $name")
}

fun basic() {
    println("Hola a todos")
}
