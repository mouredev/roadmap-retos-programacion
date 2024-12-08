import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

// Función para sumar dos números
fun suma(a: Int, b: Int): Int {
    return a + b
}

// Diccionario con información personal
val personalInfo = mapOf(
    "name" to "Eulogio EP",
    "age" to "41",
    "birth_date" to "1981-05-12",
    "programming_languages" to listOf("Kotlin", "Java", "Python")
)

class EjercicioTest {

    @Test
    fun testSuma() {
        assertEquals(5, suma(2, 3))
        assertEquals(0, suma(-1, 1))
        assertEquals(-5, suma(-2, -3))
    }

    @Test
    fun testDiccionarioTieneTodosLosCampos() {
        val camposRequeridos = listOf("name", "age", "birth_date", "programming_languages")
        camposRequeridos.forEach { campo ->
            assertTrue(personalInfo.containsKey(campo), "El diccionario no contiene el campo: $campo")
        }
    }

    @Test
    fun testDatosDiccionarioSonCorrectos() {
        assertEquals("Eulogio EP", personalInfo["name"])
        assertEquals("41", personalInfo["age"])
        assertEquals("1981-05-12", personalInfo["birth_date"])
        
        val lenguajes = personalInfo["programming_languages"] as? List<String>
        assertNotNull(lenguajes)
        assertTrue(lenguajes!!.containsAll(listOf("Kotlin", "Java", "Python")))
    }
}