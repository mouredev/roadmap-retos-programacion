import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class JimsimroDev {

  public static class JimsimroDevException extends RuntimeException {
    public JimsimroDevException(String message) {
      super(message);
    }
  }

  static double divide(double numerator, double denominator) {
    if (denominator == 0) {
      throw new ArithmeticException("No se puede dividir entre 0");
    }
    return numerator / denominator;
  }

  static void procesarParametros(List<Integer> parametros) {
    try {
      System.out.println(parametros.get(2));
      System.out.println(parametros.get(0) / parametros.get(1));
    } catch (IndexOutOfBoundsException | ArithmeticException e) {
      System.out.println(e.getClass().getName() + " generado: " + e.getMessage());
    }
    System.out.println("Finalizando programa...");
  }

  static void procesarParametros2(List<Object> parametros) {
    try {
      validarParametros(parametros);
      System.out.println(parametros.get(2));
      validarParametros(parametros);
      System.out.println((int) parametros.get(0) / (int) parametros.get(1));
      validarParametros(parametros);
      System.out.println((int) parametros.get(2) + 5);
      validarParametros(parametros);

      // Lanzar un NullPointerException en la list
      // parametros.set(1, null);
      // System.out.println(parametros.get(1).toString());
      System.out.println("El programa no tiene errores ...");
    } catch (IndexOutOfBoundsException | ArithmeticException | JimsimroDevException e) {
      System.out.println(e.getClass().getName() + " generado: " + e.getMessage());
    } catch (Exception e) {
      System.out.println(e.getClass().getName() + " Error desconocido: " + e.getMessage());
    } finally {
      System.out.println("Finalizando el programa...");
    }
  }

  static void validarParametros(List<Object> parametros) {
    if (parametros.size() < 3) {
      throw new IndexOutOfBoundsException("Se requieren al menos 3 parámetros");
    }
    if ((int) parametros.get(1) == 0) {
      throw new ArithmeticException("No se puede dividir entre 0");
    }
    if (parametros.get(2) instanceof String) {
      throw new JimsimroDevException("El tercer parámetro no puede ser una cadena");
    }
  }

  public static void main(String[] args) {
    // try con recursos
    try (Scanner scanner = new Scanner(System.in)) {
      System.out.println("Ingrese el numerador: ");
      double numerador = scanner.nextDouble();
      System.out.println("Ingrese el denominador: ");
      double denominador = scanner.nextDouble();
      System.out
          .println(String.format("Dividir %f/%f: %f", numerador, denominador, divide(numerador, denominador)));
    } catch (Exception e) {
      System.out.println("Error aritmético: " + e.getMessage());
    }

    // Division 10/0
    // System.out.println(String.format("Dividir 10/0: %f", divide(10, 0)));

    try {
      System.out.printf("Dividir 10/2: %d", (10 / 2));
      System.out.println();
      // System.out.println(String.format("Dividir 10/0: %f", (10 / 0)));

      List<Integer> list = new ArrayList<>() {
        {
          add(1);
          add(0);
          add(3);
          add(4);
        }
      };

      System.out.println(list.get(4));
      procesarParametros(list);
    } catch (Exception e) {
      System.out.println("Error aritmético: " + e.getMessage());
    }

    // DIFICULTAD EXTRA (opcional):
    List<Object> parametros = new ArrayList<>();
    parametros.add(1);
    parametros.add(2);
    parametros.add(3);
    procesarParametros2(parametros);
  }
}
