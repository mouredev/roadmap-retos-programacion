/*
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
 */
public class JimsimroDev {
  public static interface EncenderAutomovil {
    void encender(String mensaje);
  }

  // Clase concreta que implementa la interfaz
  public static class Automovil implements EncenderAutomovil {
    @Override
    public void encender(String mensaje) {
      System.out.println("El automóvil se ha encendido: " + mensaje);
    }

  }

  public static class DecoradorAutomovil implements EncenderAutomovil {
    private EncenderAutomovil wrappee;
    private String nombreMetodo;
    private int contadorLlamadas = 0;

    private DecoradorAutomovil(EncenderAutomovil wrappee, String nombreMetodo) {
      this.wrappee = wrappee;
      this.nombreMetodo = nombreMetodo;
    }

    @Override
    public void encender(String mensaje) {
      contadorLlamadas++;
      System.out.printf("función %s ha sido llamda %d veces \n", nombreMetodo, getContadorLlamadas());
      wrappee.encender(mensaje);
    }

    public int getContadorLlamadas() {
      return contadorLlamadas;
    }
  }

  public static void main(String[] args) {
    var automóvilPrueba = new Automovil();
    var testlaModelY = new DecoradorAutomovil(automóvilPrueba, "testlaModelY");
    var testlaModelS = new DecoradorAutomovil(automóvilPrueba, "testlaModelS");

    testlaModelY.encender("Arrancando el motor V8");
    testlaModelY.encender("Arrancando el motor V8");
    testlaModelY.encender("Arrancando el motor V8");

    testlaModelS.encender("Arrancando el motor V6");
    testlaModelS.encender("Arrancando el motor V6");
    testlaModelS.encender("Arrancando el motor V6");

    testlaModelY.encender("Arrancando el motor V8");
  }
}
