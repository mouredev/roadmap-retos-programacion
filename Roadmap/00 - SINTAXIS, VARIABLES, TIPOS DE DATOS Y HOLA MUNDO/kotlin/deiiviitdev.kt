// https://kotlinlang.org/

// One line comment

/*
   Multiple line comment
*/

/**
 * This is a documentation comment
 */

val drink = "Cafe"
const val dish = "Pizza"


/**
 * Basic types
 */
// Integer types
val one: Int = 1
val threeBillions: Long = 3000000000
val oneByte: Byte = 1
val oneShort: Short = 1

// Floating point types
val pi: Float = 3.14f
val e: Double = 2.71828

// Unsigned types
val oneUByte: UByte = 1u
val oneUShort: UShort = 1u
val oneUInt: UInt = 1u
val oneULong: ULong = 1u

// Boolean type
val isTrue: Boolean = true

// Character type
val a: Char = 'a'

// String type
val hello: String = "Hello"

// Array type
val oneToFive: Array<Int> = arrayOf(1, 2, 3, 4, 5)
val oneToFive2: IntArray = intArrayOf(1, 2, 3, 4, 5)

/**
 * Print "Hola, Kotlin" to the console
 */
fun main() {
    println("Hola, Kotlin")
}