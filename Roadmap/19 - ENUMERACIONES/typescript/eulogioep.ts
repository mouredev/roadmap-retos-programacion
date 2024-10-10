// Resumen sobre Enumeraciones
// Las enumeraciones (Enums) en TypeScript permiten definir un conjunto de valores con nombre.
// Son útiles para representar datos categóricos que tienen un número limitado de valores, como los días de la semana o el estado de un pedido.

enum DiasSemana {
  Lunes = 1,
  Martes = 2,
  Miercoles = 3,
  Jueves = 4,
  Viernes = 5,
  Sabado = 6,
  Domingo = 7,
}

// Función para obtener el nombre del día a partir de un número entero
function obtenerNombreDia(numeroDia: number): string {
  switch (numeroDia) {
    case DiasSemana.Lunes:
      return "Lunes";
    case DiasSemana.Martes:
      return "Martes";
    case DiasSemana.Miercoles:
      return "Miércoles";
    case DiasSemana.Jueves:
      return "Jueves";
    case DiasSemana.Viernes:
      return "Viernes";
    case DiasSemana.Sabado:
      return "Sábado";
    case DiasSemana.Domingo:
      return "Domingo";
    default:
      return "Número de día inválido";
  }
}

// Ejemplo de uso de la función obtenerNombreDia
console.log(obtenerNombreDia(1)); // Salida: Lunes
console.log(obtenerNombreDia(7)); // Salida: Domingo

// Dificultad Extra: Sistema de gestión del estado de pedidos
enum EstadoPedido {
  Pendiente = "Pendiente",
  Enviado = "Enviado",
  Entregado = "Entregado",
  Cancelado = "Cancelado",
}

class Pedido {
  private id: number;
  private estado: EstadoPedido;

  constructor(id: number, estado: EstadoPedido = EstadoPedido.Pendiente) {
    this.id = id;
    this.estado = estado;
  }

  public enviar(): void {
    if (this.estado === EstadoPedido.Pendiente) {
      this.estado = EstadoPedido.Enviado;
    } else {
      console.log("El pedido no se puede enviar.");
    }
  }

  public entregar(): void {
    if (this.estado === EstadoPedido.Enviado) {
      this.estado = EstadoPedido.Entregado;
    } else {
      console.log("El pedido no se puede entregar.");
    }
  }

  public cancelar(): void {
    if (this.estado !== EstadoPedido.Entregado) {
      this.estado = EstadoPedido.Cancelado;
    } else {
      console.log("El pedido no se puede cancelar.");
    }
  }

  public obtenerDescripcionEstado(): string {
    return `El estado actual del pedido ${this.id} es ${this.estado}.`;
  }
}

// Ejemplo de interacción con diferentes pedidos
const pedido1 = new Pedido(1);
const pedido2 = new Pedido(2);

pedido1.enviar();
console.log(pedido1.obtenerDescripcionEstado()); // Salida: El estado actual del pedido 1 es Enviado.

pedido1.entregar();
console.log(pedido1.obtenerDescripcionEstado()); // Salida: El estado actual del pedido 1 es Entregado.

pedido2.cancelar();
console.log(pedido2.obtenerDescripcionEstado()); // Salida: El estado actual del pedido 2 es Cancelado.

const pedido3 = new Pedido(3);
pedido3.enviar();
pedido3.cancelar(); // Esto no debería ser posible, y se verá reflejado en el mensaje.

console.log(pedido3.obtenerDescripcionEstado()); // Salida: El estado actual del pedido 3 es Enviado.
