package main

import org.testng.AssertJUnit.assertEquals
import org.testng.annotations.Test

/*
* SUM
*/

fun sum(num1: Int, num2: Int): Int {
    return num1 + num2
}

class SumTest {
    @Test
    fun testSum() {
        assertEquals(42, sum(40, 2))
    }
}


/*
* DICTIONARY
* */

val data = mapOf(
    "name" to "Anna",
    "age" to "36",
    "birth_date" to  "13 de octubre",
    "programming_languages" to listOf("Python", "Kotlin")
)

class DictionaryTest {
    @Test
    fun testAllKeysExist() {
        val correctKeys = setOf("name", "age", "birth_date", "programming_languages")
        assertEquals(data.keys, correctKeys)
    }
}