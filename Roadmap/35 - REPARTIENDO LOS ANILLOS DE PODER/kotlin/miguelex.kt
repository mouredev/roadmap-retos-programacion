fun esPrimo(num: Int): Boolean {
    if (num <= 1) return false
    if (num == 2) return true
    if (num % 2 == 0) return false

    for (i in 3..Math.sqrt(num.toDouble()).toInt() step 2) {
        if (num % i == 0) return false
    }
    return true
}

fun repartirAnillos(totalAnillos: Int): String {
    if (totalAnillos < 4) {
        return "Error: No hay suficientes anillos para cumplir con los requisitos."
    }

    val anillosSauron = 1
    var totalAnillosRestantes = totalAnillos - 1

    var mejorDiferencia = Int.MAX_VALUE
    var mejorReparto: IntArray? = null

    for (anillosElfos in 1..totalAnillosRestantes step 2) {
        for (anillosEnanos in 2..totalAnillosRestantes) {
            if (esPrimo(anillosEnanos)) {
                val anillosHombres = totalAnillosRestantes - anillosElfos - anillosEnanos

                if (anillosHombres > 0 && anillosHombres % 2 == 0) {
                    val diferencia = maxOf(anillosElfos, anillosEnanos, anillosHombres) -
                                     minOf(anillosElfos, anillosEnanos, anillosHombres)

                    if (diferencia < mejorDiferencia) {
                        mejorDiferencia = diferencia
                        mejorReparto = intArrayOf(anillosElfos, anillosEnanos, anillosHombres, anillosSauron)
                    }
                }
            }
        }
    }

    return if (mejorReparto != null) {
        "Reparto exitoso: Elfos = ${mejorReparto[0]}, Enanos = ${mejorReparto[1]}, Hombres = ${mejorReparto[2]}, Sauron = ${mejorReparto[3]}"
    } else {
        "Error: No se encontró una combinación válida para repartir los anillos."
    }
}

fun main() {
    print("Ingresa el número total de anillos: ")
    val totalAnillos = readLine()?.toIntOrNull() ?: 0

    val resultado = repartirAnillos(totalAnillos)
    println(resultado)
}
