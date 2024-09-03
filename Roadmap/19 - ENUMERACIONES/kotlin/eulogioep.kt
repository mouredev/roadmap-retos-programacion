enum class EstadoPedido {
    PENDIENTE, ENVIADO, ENTREGADO, CANCELADO
}

class Pedido(val id: Int) {
    var estado: EstadoPedido = EstadoPedido.PENDIENTE
        private set

    fun enviar() {
        if (estado == EstadoPedido.PENDIENTE) {
            estado = EstadoPedido.ENVIADO
            println("Pedido $id enviado.")
        } else {
            println("No se puede enviar el pedido $id. Estado actual: $estado")
        }
    }

    fun cancelar() {
        if (estado != EstadoPedido.ENTREGADO) {
            estado = EstadoPedido.CANCELADO
            println("Pedido $id cancelado.")
        } else {
            println("No se puede cancelar el pedido $id. Ya ha sido entregado.")
        }
    }

    fun entregar() {
        if (estado == EstadoPedido.ENVIADO) {
            estado = EstadoPedido.ENTREGADO
            println("Pedido $id entregado.")
        } else {
            println("No se puede entregar el pedido $id. Estado actual: $estado")
        }
    }

    fun mostrarEstado() {
        val descripcion = when (estado) {
            EstadoPedido.PENDIENTE -> "El pedido está pendiente de envío."
            EstadoPedido.ENVIADO -> "El pedido ha sido enviado y está en camino."
            EstadoPedido.ENTREGADO -> "El pedido ha sido entregado con éxito."
            EstadoPedido.CANCELADO -> "El pedido ha sido cancelado."
        }
        println("Estado del pedido $id: $descripcion")
    }
}

fun main() {
    val pedido1 = Pedido(1)
    val pedido2 = Pedido(2)

    pedido1.mostrarEstado()
    pedido1.enviar()
    pedido1.mostrarEstado()
    pedido1.entregar()
    pedido1.mostrarEstado()

    println()

    pedido2.mostrarEstado()
    pedido2.cancelar()
    pedido2.mostrarEstado()
    pedido2.enviar()  // Esto no debería funcionar
    pedido2.entregar()  // Esto no debería funcionar
}