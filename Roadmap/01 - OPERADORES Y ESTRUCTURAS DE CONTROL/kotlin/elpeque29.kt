@file:Suppress("KotlinConstantConditions")

package `100-Dias-de-Kotlin`.`Dia-002`.`01-OperadoresYEstructurasDeControl`

fun main() {
// Operators
// https://kotlinlang.org/docs/keyword-reference.html#operators-and-special-symbols

    mathOperators()
    augmentedAssignmentsOperators()
    incrementAndDecrementOperators()
    logicalOperators()
    equalityOperators()
    referentialEqualityOperators()
    comparisonOperators()
    indexedAccessOperator()
    nonNullable()
    safeCalls()
    elvisOperator()
    rangeOperator()

// Control Flow
// https://kotlinlang.org/docs/control-flow.html

    ifExpression()
    whenExpression()
    forLoops()
    whileLoops()
    doWhileLoops()
}

/* Operators */

fun mathOperators() {
    val adition = 0 + 1
    val substraction = 1 - 1
    val multiplication = 2 * 2
    val division = 25 / 5
    val rest = 5 % 5
    println(listOf(adition,substraction,multiplication,division,rest))
}

fun augmentedAssignmentsOperators() {
    var value = 3
    value += 1
    println(value)
    value -= 1
    println(value)
    value *= 2
    println(value)
    value /= 2
    println(value)
    value %= 2
    println(value)
}

fun incrementAndDecrementOperators() {
    var otherValue = 5
    otherValue++
    println(otherValue)
    otherValue--
    println(otherValue)
}

fun logicalOperators() {
    val logic = true
    val notLogic = false
    println(listOf(logic && notLogic, logic || notLogic, !logic))
}

fun equalityOperators() {
    val a = "String"
    val b = "string"
    val c = a
    println(a == c)
    println(a != b)
}

fun referentialEqualityOperators() {
    val a = 5
    val b = 1
    val c = a

    println(a === b)
    println(a !== c)
}

fun comparisonOperators() {
    val d = 50
    val e = 4
    val f = 15
    val g = e
    println(d > f)
    println(e < f)
    println(e >= g)
    println(e <= f)
}

fun indexedAccessOperator() {
    val array = arrayOf("a", "b")
    println(array[0])
}

fun nonNullable() {
    val nullableString: String?
    nullableString = "Hello"
    val length = nullableString!!.length // Here, you're certain that nullableString isn't null
    println(length)
}

fun safeCalls() {
    val b: String? = null
    println(b?.length)
}

fun elvisOperator() {
    // instead of using val l: Int = if (b != null) b.length else -1 you can use the Elvis Operator
    val b = "String"
    val l = b?.length ?: -1
    println(l)
}

fun rangeOperator() {
    println(4 in 1..4)
}

/* Control Flow */

fun ifExpression() {
    val bushiHasSlaves = false
    if (bushiHasSlaves) println("Yup, don't say it loud. He can hear us.") else println("Nah, he pays you with honor and recognition.")
}

fun whenExpression() {
    when (30) {
        1 -> print("1")
        2 -> print("2")
        else -> {
            println("x is neither 1 nor 2")
        }
    }
}

fun forLoops() {
    for (x in 1..3) {
        println(x)
    }
}

fun whileLoops() {
    var x = 10
    while (x > 0) {
        x--
        println(x)
    }
}

fun doWhileLoops() {
        var number = 6
        var factorial = 1
        do {
            factorial *= number
            number--
        }while(number > 0)
        println("Factorial of 6 is $factorial")
}
