
/*
El testing nos ayuda a probar diferentes partes de nuestro codigo para comprobar que los resultados
obtenidos son correctos de acuerdo a los parametros que configuramos

Para poder realizar pruebas unitarias en kotlin se usa kotlintest
https://kotlinlang.org/api/latest/kotlin.test/

Los test deben ir en la carpeta src\test\kotlin en intellij para que se puedan ejecutar
los ejemplos que se muestran solo son ejemplos de pruebas unitarios.

el metodo assert nos sirve para indicar que resultado se espera y el resultado real es evaluado
para saber si es correcto o no ademas de evaluar que el resultado sea el esperado tambien puedes evaluar
que el resultado no sea el esperado
*/

// operacion a testear
class Operations{
    fun sum(a: Int, b: Int): Int = a + b
}

/*
 clase que testea la operacion suma

 import kotlin.test.Test
 import kotlin.test.assertEquals

 class SumTest {
    @Test
    fun testSum() {
        val operations = Operations()
        assertEquals(10,operations.sum(5,5))
    }
}

 */

class Backdev{
    private val programingLanguajes = listOf("Java","Kotlin","Python","go","swift")
    val dataDev= mapOf("name" to "blackriper", "age" to 29,"birth_date" to "20/05/1994", "programing_languages" to programingLanguajes)
}

/*
clase para testear el mapa

import kotlin.test.Test
import kotlin.test.assertContains
import kotlin.test.assertFalse
import kotlin.test.assertTrue


class DevTest {

    @Test
    fun testDev() {
      val backdev = Backdev()
      val mockdev = mapOf("name" to "blackriper", "age" to 29,"birth_date" to "20/05/1994", "programing_languages" to listOf("Java","Kotlin","Python","go","swift"))
      val mockdevError = mapOf("nombre" to "blackriper", "age" to 29,"birth_date" to "20/05/1994")
     // comprobar que los datos de  mockdev es igual a backdev.dataDev
     assertTrue { mockdev == backdev.dataDev }
     assertFalse { mockdevError == backdev.dataDev }
     // comprobar campos
      assertTrue { backdev.dataDev.entries.containsAll(mockdev.entries) }
      assertFalse { backdev.dataDev.entries.containsAll(mockdevError.entries) }

    }
}

*/