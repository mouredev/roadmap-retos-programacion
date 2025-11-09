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
  private static  final String DIV_LINE =":::::::::::::::::::::::::";
  private static final int MIN = 1000;
  private static final int MAX = 10000;

  interface Noficar {
    void notificacion(String mensaje);
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

  interface Callback {
    void notificar(String mensaje);
  }

  static int ramdon() {
    return (int) (Math.random() * (MAX - MIN + 1)) + MIN;
  }

  static void procesarPedidos(String plato, Callback callback) {
    try {
      print(DIV_LINE);
      print("Iniciando pedido....");
      Thread.sleep(ramdon());
      callback.notificar(plato + " Confirmado");

      print(DIV_LINE);
      print("Preparando pedido....");
      Thread.sleep(ramdon());
      callback.notificar(plato + " Listo");

      print(DIV_LINE);
      print("Entregando el plato", plato);
      Thread.sleep(ramdon());
      callback.notificar(plato + " Entregado");

    } catch (InterruptedException e) {
      print("Erro no pedido" + e);
    }
  }

  static void hacerOrden(String plato) {
    procesarPedidos(plato, new Callback() {

      @Override
      public void notificar(String mensaje) {
        System.out.println(mensaje);
      }
    });
  }
  static void print(Object... args){
      for (Object s : args){
          System.out.print(s + " ");
      }
      System.out.println();
  }

  public static void main(String[] args) {
    notificacionEnviada("Enviando SMS ", new Noficar() {

      @Override
      public void notificacion(String mensaje) {
        System.out.println(mensaje);
      }
    });

    // EXTRA
    hacerOrden("Bandeja Paisa");
    hacerOrden("Lechona");
    hacerOrden("Mote De Queso");
  }
}
