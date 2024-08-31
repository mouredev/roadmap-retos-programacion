import java.time.*
import java.time.format.DateTimeFormatter
import java.time.temporal.ChronoUnit

fun main() {
    // Fecha actual
    val fechaActual = LocalDateTime.now()
    
    // Fecha de nacimiento (ejemplo)
    val fechaNacimiento = LocalDateTime.of(1990, 5, 15, 14, 30, 0)
    
    // Cálculo de años transcurridos
    val añosTranscurridos = ChronoUnit.YEARS.between(fechaNacimiento, fechaActual)
    
    println("Años transcurridos: $añosTranscurridos")
    
    // DIFICULTAD EXTRA: Formatear la fecha de nacimiento de 10 maneras diferentes
    val formatters = listOf(
        DateTimeFormatter.ofPattern("dd/MM/yyyy"),
        DateTimeFormatter.ofPattern("HH:mm:ss"),
        DateTimeFormatter.ofPattern("D"),
        DateTimeFormatter.ofPattern("EEEE"),
        DateTimeFormatter.ofPattern("MMMM"),
        DateTimeFormatter.ofPattern("yyyy 'semana' w"),
        DateTimeFormatter.ofPattern("dd MMMM yyyy, HH:mm"),
        DateTimeFormatter.ISO_LOCAL_DATE_TIME,
        DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss"),
        DateTimeFormatter.ofPattern("EEEE, MMMM d, yyyy 'a las' hh:mm a")
    )
    
    println("\nFormatos de fecha de nacimiento:")
    formatters.forEachIndexed { index, formatter ->
        println("${index + 1}. ${fechaNacimiento.format(formatter)}")
    }
}