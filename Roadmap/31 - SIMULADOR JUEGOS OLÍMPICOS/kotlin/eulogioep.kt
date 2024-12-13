import kotlin.random.Random

// Definición de las clases principales
data class Evento(val nombre: String, val participantes: MutableList<Participante> = mutableListOf())
data class Participante(val nombre: String, val pais: String, var medallas: MutableMap<String, Int> = mutableMapOf())
data class Resultado(val oro: Participante, val plata: Participante, val bronce: Participante)

// Clase principal que maneja la simulación de los Juegos Olímpicos
class JuegosOlimpicos {
    private val eventos = mutableListOf<Evento>()
    private val participantes = mutableListOf<Participante>()

    // Función para registrar un nuevo evento
    fun registrarEvento(nombre: String) {
        eventos.add(Evento(nombre))
        println("Evento '$nombre' registrado correctamente.")
    }

    // Función para registrar un nuevo participante
    fun registrarParticipante(nombre: String, pais: String) {
        participantes.add(Participante(nombre, pais))
        println("Participante '$nombre' de '$pais' registrado correctamente.")
    }

    // Función para simular todos los eventos
    fun simularEventos() {
        for (evento in eventos) {
            // Seleccionar aleatoriamente al menos 3 participantes para el evento
            val participantesEvento = participantes.shuffled().take(maxOf(3, Random.nextInt(participantes.size)))
            evento.participantes.addAll(participantesEvento)

            // Simular el evento y asignar medallas
            val resultado = simularEvento(evento)
            asignarMedallas(resultado)

            // Mostrar los ganadores del evento
            mostrarGanadoresEvento(evento, resultado)
        }
    }

    // Función para simular un evento individual y determinar los ganadores
    private fun simularEvento(evento: Evento): Resultado {
        val ganadores = evento.participantes.shuffled().take(3)
        return Resultado(ganadores[0], ganadores[1], ganadores[2])
    }

    // Función para asignar medallas a los ganadores
    private fun asignarMedallas(resultado: Resultado) {
        asignarMedalla(resultado.oro, "oro")
        asignarMedalla(resultado.plata, "plata")
        asignarMedalla(resultado.bronce, "bronce")
    }

    // Función auxiliar para asignar una medalla a un participante
    private fun asignarMedalla(participante: Participante, tipoMedalla: String) {
        participante.medallas[tipoMedalla] = participante.medallas.getOrDefault(tipoMedalla, 0) + 1
    }

    // Función para mostrar los ganadores de un evento
    private fun mostrarGanadoresEvento(evento: Evento, resultado: Resultado) {
        println("\nResultados del evento: ${evento.nombre}")
        println("Oro: ${resultado.oro.nombre} (${resultado.oro.pais})")
        println("Plata: ${resultado.plata.nombre} (${resultado.plata.pais})")
        println("Bronce: ${resultado.bronce.nombre} (${resultado.bronce.pais})")
    }

    // Función para generar y mostrar el ranking de países
    fun mostrarRankingPaises() {
        println("\nRanking de países por medallas:")
        val rankingPaises = participantes.groupBy { it.pais }
            .mapValues { (_, participantes) ->
                participantes.sumOf { it.medallas.values.sum() }
            }
            .toList()
            .sortedByDescending { it.second }

        rankingPaises.forEachIndexed { index, (pais, medallas) ->
            println("${index + 1}. $pais: $medallas medallas")
        }
    }
}

// Función principal que maneja la interacción con el usuario
fun main() {
    val juegos = JuegosOlimpicos()
    
    while (true) {
        println("\n--- Juegos Olímpicos París 2024 ---")
        println("1. Registrar evento")
        println("2. Registrar participante")
        println("3. Simular eventos")
        println("4. Mostrar ranking de países")
        println("5. Salir")
        print("Seleccione una opción: ")
        
        when (readLine()) {
            "1" -> {
                print("Ingrese el nombre del evento: ")
                val nombreEvento = readLine() ?: continue
                juegos.registrarEvento(nombreEvento)
            }
            "2" -> {
                print("Ingrese el nombre del participante: ")
                val nombreParticipante = readLine() ?: continue
                print("Ingrese el país del participante: ")
                val paisParticipante = readLine() ?: continue
                juegos.registrarParticipante(nombreParticipante, paisParticipante)
            }
            "3" -> juegos.simularEventos()
            "4" -> juegos.mostrarRankingPaises()
            "5" -> {
                println("¡Gracias por usar el simulador de Juegos Olímpicos París 2024!")
                return
            }
            else -> println("Opción no válida. Por favor, intente de nuevo.")
        }
    }
}