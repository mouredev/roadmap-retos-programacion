// #31 SIMULADOR JUEGOS OLÍMPICOS - SisaRoot

import kotlin.random.Random

data class Participant(val name: String, val country: String)
data class Event(val name: String, val participants: MutableList<Participant> = mutableListOf())
data class CountryMedals(val country: String, var gold: Int = 0, var silver: Int = 0, var bronze: Int = 0) {
    fun total() = gold + silver + bronze
}

val events = mutableListOf<Event>()
val medalTable = mutableMapOf<String, CountryMedals>()

fun addMedal(country: String, type: String) {
    val cm = medalTable.getOrPut(country) { CountryMedals(country) }
    when (type) { "gold" -> cm.gold++; "silver" -> cm.silver++; else -> cm.bronze++ }
}

fun registerEvent() {
    print("Nombre del evento: ")
    val name = readLine()?.trim() ?: return
    if (events.any { it.name.equals(name, true) }) { println("Ya existe."); return }
    events.add(Event(name)); println("Evento '$name' registrado.")
}

fun registerParticipant() {
    if (events.isEmpty()) { println("No hay eventos."); return }
    events.forEachIndexed { i, e -> println("  ${i+1}. ${e.name}") }
    val idx = readLine()?.trim()?.toIntOrNull() ?: 0
    if (idx < 1 || idx > events.size) { println("Invalido."); return }
    val ev = events[idx - 1]
    print("Nombre: "); val pname = readLine()?.trim() ?: ""
    print("País: "); val country = readLine()?.trim() ?: ""
    ev.participants.add(Participant(pname, country))
    println("'$pname ($country)' añadido a '${ev.name}'.")
}

fun simulateEvents() {
    if (events.isEmpty()) { println("No hay eventos."); return }
    for (ev in events) {
        println("\n=== Simulando: ${ev.name} ===")
        if (ev.participants.size < 3) { println("  Necesita >=3. Saltando."); continue }
        val s = ev.participants.shuffled(Random)
        println("  🥇 ${s[0].name} (${s[0].country})")
        println("  🥈 ${s[1].name} (${s[1].country})")
        println("  🥉 ${s[2].name} (${s[2].country})")
        addMedal(s[0].country, "gold"); addMedal(s[1].country, "silver"); addMedal(s[2].country, "bronze")
    }
}

fun showReport() {
    println("\n== INFORME FINAL ==")
    if (medalTable.isEmpty()) { println("Sin resultados."); return }
    medalTable.values.sortedWith(compareByDescending<CountryMedals>{it.gold}.thenByDescending{it.silver}.thenByDescending{it.bronze})
        .forEachIndexed { i, c -> println("${i+1}. ${c.country.padEnd(20)} Oro:${c.gold} Plata:${c.silver} Bronce:${c.bronze} Total:${c.total()}") }
}

fun main() {
    while (true) {
        println("\n====== SIMULADOR JJOO ======\n1. Registrar evento\n2. Registrar participante\n3. Simular\n4. Informe\n5. Salir")
        when (readLine()?.trim()) {
            "1" -> registerEvent(); "2" -> registerParticipant()
            "3" -> simulateEvents(); "4" -> showReport()
            "5" -> { println("Hasta luego!"); return }
            else -> println("Invalido.")
        }
    }
}
