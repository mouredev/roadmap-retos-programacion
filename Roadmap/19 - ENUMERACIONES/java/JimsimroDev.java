
/*
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
 */

enum DiasSemana {
  LUNES(1),
  MARTES(2),
  MIERCOLES(3),
  JUEVES(4),
  VIERNES(5),
  SABADO(6),
  DOMINGO(7);

  private final int numero;

  private DiasSemana(int numero) {
    this.numero = numero;
  }
}

DiasSemana getDia(int numero) {
  if (numero < 1 || numero > 7) {
    throw new IllegalArgumentException("El número debe se entre 1 y 7");
  }
  DiasSemana[] dias = DiasSemana.values();
  for (int i = 0; i < DiasSemana.values().length; i++) {
    if (dias[i].numero == numero) {
      return dias[i];
    }
  }
  return null;
}

class Pedido {
  private Long id;
  private Estados estado;

  public Pedido(Long id) {
    this.id = id;
    this.estado = estado.PENDIENTE;
  }

  void enviado() {
    if (estado != Estados.PENDIENTE) {
      IO.println("No puedes cambiar el estado");
      return;
    }
    estado = Estados.ENVIADO;
    IO.println("El estado a sido cambiado a " + estado);
    printPedido();
  }

  void entregado() {
    if (estado != Estados.ENVIADO) {
      IO.println("El estado aun no a sido enviado");
      return;
    }
    estado = Estados.ENTREGADO;
    IO.println("El estado a sido cambiado a " + estado);
    printPedido();
  }

  void cancelar() {
    if (estado == Estados.ENTREGADO) {
      IO.println("El pedido ya se encuentra " + estado + " No se puede cancelar");
      return;
    }
    estado = Estados.CANCELADO;
    IO.println("El pedido a sido " + estado);
    printPedido();
  }

  void printPedido() {
    IO.println(String.format("El estado del pedido %d es %s ", id, estado));
  }

  /*
   *
   * - Pedido enviado
   * - Pedido cancelado
   * - Pedido entregado
   * (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado,
   * etc...)
   * - Implementa una función para mostrar un texto descriptivo según el estado
   * actual.
   * - Crea diferentes pedidos y muestra cómo se interactúa con ellos.
   */
}

enum Estados {

  PENDIENTE(1), ENVIADO(2), ENTREGADO(3), CANCELADO(4);

  private final int numero;

  private Estados(int numero) {
    this.numero = numero;
  }
}

void main() {
  DiasSemana dia = getDia(1);
  DiasSemana dia1 = getDia(7);
  IO.println(dia);
  IO.println(dia1);

  // EXTRA
  Pedido pedido = new Pedido(1L);
  pedido.printPedido();

  pedido.enviado();

  pedido.cancelar();

  pedido.entregado();

}
