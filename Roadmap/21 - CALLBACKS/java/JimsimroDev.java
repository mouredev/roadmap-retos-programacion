/*
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
 */

public class JimsimroDev {
  private static final String DIV_LINE = ":::::::::::::::::::::::::";
  private static final int MIN = 1000;
  private static final int MAX = 10000;

  interface Noficar {
    void notificacion(String mensaje);
  }

  interface Confirmado {
    void confirmarPedidos(String mensaje);
  }

  interface Listo {
    void pedidoListo(String mensaje);
  }

  interface Entregado {
    void entregarPedidos(String mensaje);
  }

  static void notificacionEnviada(String proceso, Noficar callback) {
    try {
      System.out.println("Iniciando proceso...");
      Thread.sleep(5000);
      callback.notificacion("Proceso completado: " + proceso);
    } catch (InterruptedException e) {
      System.out.println("Erro timeout" + e);
    }

  }

  static int ramdon() {
    return (int) (Math.random() * (MAX - MIN + 1)) + MIN;
  }

  static void procesarPedidos(String plato, Confirmado confirmado, Listo listo, Entregado entregado) {
    Thread hacerPedido = new Thread(() -> {
      try {

        print("Iniciando pedido " + plato +"....");
        Thread.sleep(ramdon());
        confirmado.confirmarPedidos(plato + " Confirmado");

        print("Preparando pedido " + plato + "....");
        print(DIV_LINE);
        Thread.sleep(ramdon());
        listo.pedidoListo(plato + " Listo");

        print("Entregando el plato "+plato);
        print(DIV_LINE);
        Thread.sleep(ramdon());
        entregado.entregarPedidos(plato + " Entregado");

      } catch (InterruptedException e) {
        print("Erro no pedido" + e);
      }
    });
    hacerPedido.start();
  }

  static void hacerOrden(String plato) {
    procesarPedidos(
        plato,
        JimsimroDev::print,
        JimsimroDev::print,
        JimsimroDev::print);
  }

  static void print(Object... args) {
    for (Object s : args) {
      System.out.print(s + " ");
    }
    System.out.println();
  }

  public static void main(String[] args) {
    notificacionEnviada("Enviando SMS ", System.out::println);

    // EXTRA
    hacerOrden("Bandeja Paisa");
    hacerOrden("Lechona");
    hacerOrden("Mote De Queso");
  }
}
