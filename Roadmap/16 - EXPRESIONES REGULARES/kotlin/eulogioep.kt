import kotlin.text.Regex

fun main() {
    // Función para extraer números de un texto
    fun extractNumbers(text: String): List<String> {
        val numberRegex = Regex("\\d+")
        return numberRegex.findAll(text).map { it.value }.toList()
    }

    // Ejemplo de uso
    val sampleText = "Tengo 25 años y mi número de teléfono es 123-456-7890. Mi código postal es 12345."
    val numbers = extractNumbers(sampleText)
    println("Números encontrados: $numbers")

    // DIFICULTAD EXTRA

    // 1. Validar un email
    fun isValidEmail(email: String): Boolean {
        val emailRegex = Regex("^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\$")
        return emailRegex.matches(email)
    }

    // 2. Validar un número de teléfono (formato: XXX-XXX-XXXX)
    fun isValidPhoneNumber(phoneNumber: String): Boolean {
        val phoneRegex = Regex("^\\d{3}-\\d{3}-\\d{4}\$")
        return phoneRegex.matches(phoneNumber)
    }

    // 3. Validar una URL
    fun isValidUrl(url: String): Boolean {
        val urlRegex = Regex("^(https?://)?([\\da-z.-]+)\\.([a-z.]{2,6})([/\\w .-]*)*/?$")
        return urlRegex.matches(url)
    }

    // Ejemplos de uso de las funciones de validación
    println("¿Es válido el email 'usuario@dominio.com'? ${isValidEmail("usuario@dominio.com")}")
    println("¿Es válido el número de teléfono '123-456-7890'? ${isValidPhoneNumber("123-456-7890")}")
    println("¿Es válida la URL 'https://www.ejemplo.com'? ${isValidUrl("https://www.ejemplo.com")}")
}