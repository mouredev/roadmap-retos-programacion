import java.time.LocalDateTime;
import java.time.Duration;
import java.lang.Thread;
public class JimsimroDev {
  private static int tareasEjecutadas = 0;
   private static final Object lock = new Object();
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 */
  public static void tarea(String name, int duration) {

    long startTime = System.currentTimeMillis();
    LocalDateTime inicio = LocalDateTime.now();
    imprimirInicio(name, inicio, duration);

    Thread thread = new Thread(() ->{
      try {
        //Simula un esperar durante la duración especificada
          System.out.printf("Tarea: %s en espera durante %d milisegundos %n", name, duration);
        Thread.sleep(duration);
      } catch (InterruptedException e) {
        System.err.println("Tarea interrupted: " + e.getMessage());
      }

      LocalDateTime fin = LocalDateTime.now();
      long endTime = System.currentTimeMillis();

      System.out.printf("Tarea: %s finalizo el %s y su duracion es %d %n", name,fin,duration);

      System.out.printf("Tarea: %s duración en milisegundos %d %n", name, (endTime - startTime));
    });
        thread.start();
  }

/*
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
 */
  public static void crearThreads(String name, int duracion) {
    long startTime = System.currentTimeMillis();

    Thread thread = new Thread(() ->{
      try {
        LocalDateTime inicio = LocalDateTime.now();
        imprimirInicio(name, inicio, duracion);

        Thread.sleep(duracion);
        //Simula un esperar durante la duración especificada
        synchronized (lock){
          ++tareasEjecutadas;
          System.out.printf("Tareas completedas %d%n", tareasEjecutadas);
          lock.notifyAll();
        }
      } catch (InterruptedException e) {
        System.err.println("Tarea interrupted: " + e.getMessage());
      }

      LocalDateTime fin = LocalDateTime.now();
      long endTime = System.currentTimeMillis();

      System.out.printf("Tarea: %s finalizo el %s y su duracion es %d %n", name,fin,duracion);

      System.out.printf("Tarea: %s duración en milisegundos %d %n", name, (endTime - startTime));
    });
        thread.start();
  }

  public static void imprimirInicio(String name, LocalDateTime inicio, int duration){
        System.out.printf("🟢 Tarea: %s inició a las %s (duración: %d ms)%n", name, inicio, duration);
  }
  public static void esperarTareas(int count){
    Thread thread = new Thread(() ->{
          synchronized (lock){
      while (tareasEjecutadas < count){
        try{

            System.out.println("Esperando que tareas sean ejecutadas...");
            lock.wait();
        }catch (InterruptedException e){
          System.err.println("Thread interrupted: " + e.getMessage());
        }
      }
          }
      System.out.println("Las  tres primeras tareas han sido ejecutadas");
      crearThreads("D", 1000);
    });
    thread.start();
  }
  //Extra 
   public static void multiThread() {
      crearThreads("C", 3000);
      crearThreads("B", 2000);
      crearThreads("A", 1000);
      System.out.println("Tareas iniciadas");
  }

    public static void main(String[] args) {

//    tarea("1", 5000);
    //Extra
 multiThread();
 esperarTareas(3);
    }
}
