/*
 * EJERCICIO:
- Crea ejemplos de funciones básicas que representen las diferentes
posibilidades del lenguaje:
- Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el concepto de variable LOCAL y GLOBAL.
- Debes hacer print por consola del resultado de todos los ejemplos.
(y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

 * DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos.

 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

//función sin parámetros ni retorno
fun funcion1() {
    println("Soy una función sin parámetros ni retorno")
}

//función con 1 parámetro
fun funcion2(word: String) {
    println("Soy una función con un parámetro que es: $word")
}

//función con X parámetros
fun funcion3(vararg arg: String) {
    println("Soy una función con varios parámetros, como: ")
    println(arg.joinToString(", "))
}

//función con retorno
fun funcion4(n1:Int, n2:Int): Int {
    return n1 + n2
}

//función lambda
val lambda: (String) -> String = { param: String -> "Soy una función lambda, $param" }

//función recursiva
fun funcion5(num:Int): Int {
    if (num == 0){
        return 1
    } else{
        return num * funcion5(num-1)
    }
}

//función anidada
fun anidada(dig: Int): Int {
    fun suma(): Int{
        return dig +1
    }
    fun resta(): Int{
        return dig -1
    }
    fun multip(): Int{
        return dig *4
    }
    fun div(): Int{
        return multip()/2
    }
    return div()
}

fun ejExtra(t1:String, t2:String): String {
    var countNum = 0
    var countT1 = 0
    var countT2 = 0
    var countT12 = 0
    for (n in 1..100){
        if (n%3 == 0 && n%5 == 0){
            println(t1+t2)
            countT12 += 1
        }
        else if (n%3 == 0){
            println(t1)
            countT1 += 1
        }
        else if (n%5 == 0){
            println(t2)
            countT2 += 1
        }
        else{
            println(n)
            countNum += 1
        }
    }
    return "Hay en total '$countNum números', '$countT1 Kot', '$countT2 Lin', y '$countT12 KotLin'"
}


fun main() {
    println("\n--> Función sin parámetros ni retorno")
    funcion1()

    println("\n--> Función con 1 parámetro y no retorno")
    funcion2("Kotlin")

    println("\n--> Función con varios parámetros y no retorno")
    funcion3("Charmander", "Squirtle", "Bulbasaur")

    println("\n--> Función con retorno")
    println(funcion4(2,3))

    println("\n--> Función lambda")
    println(lambda("soy el parámetro"))

    println("\n--> Función recursiva")
    println(funcion5(5))

    println("\n--> Sí se pueden crear funciones dentro de funciones. Se llaman funciones anidadas")
    println(anidada(5))

    println("\n--> Uso de variables Locales y Globales")
    val name = "Brais"

    fun presentarse() {
        val name = "Rick"
        val age = 26
        println("Soy $name y tengo $age años")
    }
    println(name) //funciona por ser variable global (fuera de la función
    //println(age)  no funciona por ser variable local e intentar llamarla fuera
    presentarse()

    println("\n--> Usando funciones internas de Kotlin")
    val numbers = listOf(1,2,3,4)
    val mapedNumbers = numbers.map { it*2 }
    println(mapedNumbers)

    println('\n'+"*".repeat(5)+"EJERCICIO EXTRA"+"*".repeat(5))
    println(ejExtra("Kot", "Lin"))

}
