/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */
public class JimsimroDev {
  private static final String DIV_LINE = "::::::::";

  public static void recursiCount(int number) {
    if (number < 0) {
      return;
    }
    System.out.println(number);
    recursiCount(number - 1);
  }

  public static Long factorialRecursiv(Long n) {
    if (n < 1L) {
      return 1L;
    }
    return n * factorialRecursiv(n - 1);
  }

  public static int fibonacciRecursive(int number) {
    if (number < 0) {
      return 0;
    } else if (number == 1) {
      return 1;
    } else if (number == 2) {
      return 1;
    }
    return fibonacciRecursive(number - 1) + fibonacciRecursive(number - 2);
  }

  public static void main(String[] args) {
    System.out.println(DIV_LINE);
    recursiCount(100);
    for (Long i = 1L; i <= 9; i++) {
      System.out.printf("%d! = %d\n", i, factorialRecursiv(i));
    }
    System.out.println(DIV_LINE);
    System.out.println(factorialRecursiv(0L));
    System.out.println(DIV_LINE);
    int x = 10;
    for (int n = 0; n <= x; n++) {
      System.out.print(fibonacciRecursive(n));
      System.out.print(" ");
    }
    System.out.println();
    System.out.println(DIV_LINE);
    System.out.println(fibonacciRecursive(0));
    System.out.println(fibonacciRecursive(1));
    System.out.println(fibonacciRecursive(2));
    System.out.println(fibonacciRecursive(3));
    System.out.println(fibonacciRecursive(10));
  }
}
