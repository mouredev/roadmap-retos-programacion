import java.util.*

/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 */

fun main() {
    val pila = ArrayDeque<String>()

    pila.push("Pepe")
    pila.push("Juan")
    pila.push("Pedro")

    println("Pila: $pila")

    val eliminadoPila = pila.pop()
    println("Eliminado: $eliminadoPila")

    println("Pila: $pila")

    val tope = pila.peek()
    println("Tope: $tope")

    println("Pila: $pila")

    pila.clear()

    if (pila.isEmpty()) println("Pila vacia") else println(pila)

    val cola = ArrayDeque<String>()

    cola.addLast("Adri")
    cola.addLast("Jose")
    cola.addLast("Kevin")

    println("\nCola: $cola")

    val eliminadoCola = cola.removeFirst()
    println("Eliminado: $eliminadoCola")

    println("Cola: $cola")

    val front = cola.peek()
    println("Front: $front")

    println("Cola: $cola")

    //cola.clear()

    if (cola.isEmpty()) println("Cola vacia") else println(cola)

    navegadorWeb()
    impresora()
}

fun impresora() {

    /* Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
       impresora compartida que recibe documentos y los imprime cuando así se le indica.
       La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
       interpretan como nombres de documentos. */

    val cola = ArrayDeque<String>()
    var accion: String?

    while (true) {
        println("Introduce nombre de documento, imprimir o salir")
        accion = readLine()?.trim()?.lowercase()

        when {
            accion == "salir" -> {
                println("Saliendo...")
                return
            }

            accion == "imprimir" -> {
                if (cola.isNotEmpty()) {
                    println("Imprimiendo documento: ${cola.peek()}")
                    cola.removeFirst()
                } else {
                    println("No hay ningun documento pendiente de imprimir !")
                }
            }

            !accion.isNullOrEmpty() -> {
                cola.addLast(accion)
                println("Documento $accion añadido a la cola de impresion...")
            }

            else -> {
                println("Comando invalido...")
            }
        }
    }
}

fun navegadorWeb() {

    /* - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
    *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
    *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
    *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
    *   el nombre de una nueva web. */

    val historial = ArrayDeque<String>()
    val adelante = ArrayDeque<String>()

    var paginaActual: String? = null

    while (true) {

        if (paginaActual != null) {
            println("Pagina actual: $paginaActual")
        } else {
            println("Error 404")
        }

        println("Introduce nombre de web, adelante, atras o salir")
        val accion = readlnOrNull()?.trim()?.lowercase()

        when {
            accion == "salir" -> {
                println("Saliendo...")
                return
            }

            accion == "atras" -> {
                if (historial.isNotEmpty() && paginaActual != null) {
                    adelante.push(paginaActual)
                    paginaActual = historial.pop()
                    println("Navegando a $paginaActual")
                } else {
                    println("No hay ninguna pagina en la pila historial")
                }
            }

            accion == "adelante" -> {
                if (adelante.isNotEmpty() && paginaActual != null) {
                    historial.push(paginaActual)
                    paginaActual = adelante.removeFirst()
                    println("Navegando a $paginaActual")
                } else {
                    println("No hay ninguna pagina en la pila adelante")
                }
            }

            !accion.isNullOrEmpty() -> {
                if (paginaActual != null) {
                    historial.push(paginaActual)
                }
                paginaActual = accion
                adelante.clear()
                println("Navegando a $paginaActual")
            }

            else -> {
                println("Comando invalido...")
            }
        }
    }
}
