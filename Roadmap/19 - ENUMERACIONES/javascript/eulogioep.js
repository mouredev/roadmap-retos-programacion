/**
 * TEORÍA SOBRE ENUMERACIONES EN JAVASCRIPT
 *
 * JavaScript no tiene un tipo de dato nativo para enumeraciones como Java,
 * pero hay varias formas de implementarlas:
 *
 * 1. Usando Object.freeze() para crear objetos inmutables
 * 2. Utilizando símbolos (Symbol)
 * 3. Creando clases con getters
 *
 * En este ejercicio, usaremos Object.freeze() para crear enumeraciones
 * similares a las que encontraríamos en otros lenguajes.
 */

// Enumeración para los días de la semana
const DiaSemana = Object.freeze({
  LUNES: 1,
  MARTES: 2,
  MIERCOLES: 3,
  JUEVES: 4,
  VIERNES: 5,
  SABADO: 6,
  DOMINGO: 7,

  // Método para obtener el nombre del día por número
  obtenerNombre(numero) {
    const dias = Object.entries(this).find(([_, value]) => value === numero);
    return dias ? dias[0] : "Número inválido. Debe estar entre 1 y 7.";
  },
});

// Enumeración para los estados de un pedido
const EstadoPedido = Object.freeze({
  PENDIENTE: "PENDIENTE",
  ENVIADO: "ENVIADO",
  ENTREGADO: "ENTREGADO",
  CANCELADO: "CANCELADO",
});

// Clase para gestionar pedidos
class Pedido {
  constructor(id) {
    this.id = id;
    this.estado = EstadoPedido.PENDIENTE;
  }

  // Método para enviar el pedido
  enviarPedido() {
    if (this.estado === EstadoPedido.PENDIENTE) {
      this.estado = EstadoPedido.ENVIADO;
      return true;
    }
    return false;
  }

  // Método para cancelar el pedido
  cancelarPedido() {
    if (
      this.estado === EstadoPedido.PENDIENTE ||
      this.estado === EstadoPedido.ENVIADO
    ) {
      this.estado = EstadoPedido.CANCELADO;
      return true;
    }
    return false;
  }

  // Método para entregar el pedido
  entregarPedido() {
    if (this.estado === EstadoPedido.ENVIADO) {
      this.estado = EstadoPedido.ENTREGADO;
      return true;
    }
    return false;
  }

  // Método para obtener descripción del estado
  obtenerDescripcionEstado() {
    switch (this.estado) {
      case EstadoPedido.PENDIENTE:
        return `El pedido ${this.id} está pendiente de envío.`;
      case EstadoPedido.ENVIADO:
        return `El pedido ${this.id} ha sido enviado y está en camino.`;
      case EstadoPedido.ENTREGADO:
        return `El pedido ${this.id} ha sido entregado con éxito.`;
      case EstadoPedido.CANCELADO:
        return `El pedido ${this.id} ha sido cancelado.`;
    }
  }
}

// Función principal para probar la funcionalidad
function main() {
  console.log("=== PRUEBA DE DÍAS DE LA SEMANA ===");
  for (let i = 1; i <= 7; i++) {
    console.log(`Día ${i}: ${DiaSemana.obtenerNombre(i)}`);
  }

  console.log("\n=== PRUEBA DE GESTIÓN DE PEDIDOS ===");

  const pedido1 = new Pedido(1);
  const pedido2 = new Pedido(2);

  // Mostrar estado inicial
  console.log(pedido1.obtenerDescripcionEstado());

  // Enviar pedido1
  pedido1.enviarPedido();
  console.log(pedido1.obtenerDescripcionEstado());

  // Intentar entregar pedido2 (debería fallar)
  if (!pedido2.entregarPedido()) {
    console.log("No se puede entregar el pedido 2 porque no ha sido enviado.");
  }

  // Entregar pedido1
  pedido1.entregarPedido();
  console.log(pedido1.obtenerDescripcionEstado());

  // Cancelar pedido2
  pedido2.cancelarPedido();
  console.log(pedido2.obtenerDescripcionEstado());
}

// Ejecutar el programa
main();
