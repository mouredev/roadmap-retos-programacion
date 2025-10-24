/**
 * @author Daniel Torres
 */
object Ejercicio00 {
    // Comentario con el sitio oficial: https://www.java.com/es/

    // Comentario Simple

    /*
     * Comentario de varias líneas
     *
     */

    /**
     * Comentario de documentación
     * O en otras palabras, KDoc
     *
     * @param args
     */

    // Declaración de variables y constantes
    var variableEntera: Int = 10 // Variable entera
    const val CONSTANTE_PI: Double = 3.1416 // Constante doble

    @JvmStatic
    fun main(args: Array<String>) {
        // Declaración de otros tipos de datos primitivos
        val cadenaTexto: String = "Hola, Mundo!" // Cadena de texto
        val esVerdadero: Boolean = true // Booleano
        val caracter: Char = 'A' // Carácter
        val numeroDecimal: Float = 5.75f // Número decimal (float)
        val numeroGrande: Long = 123456789L // Número grande (long)
        val numeroPequeño: Byte = 100 // Número pequeño (byte)
        val numeroCorto: Short = 30000 // Número corto (short)
        val numeroDoble: Double = 19.99 // Número doble (double)

        // Imprimir mensaje por terminal
        println("Hola, Kotlin!")
    }
}