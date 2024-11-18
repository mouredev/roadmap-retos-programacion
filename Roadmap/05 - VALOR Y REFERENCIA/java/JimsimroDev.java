
/* VALOR Y REFERENCIA

 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */
import java.util.ArrayList;
import java.util.List;

public class JimsimroDev {
  static final String DIV_LINE = ":::::::::::::";

  // Funcion o metodo para imprimir tipos de datos por valor
  public static void print(String str, int result) {
    System.out.println(str + " " + result);
  }

  // Funcion o metodo con datos por valor
  public static void intFuncion(int number) {
    number = 30;
    print("number = ", number);
  }

  // Funcion con datos por referencia
  public static void funcionDeLista(List<Integer> miLista) {
    miLista.add(30);

    List<Integer> miLista1 = new ArrayList<>();
    miLista1 = miLista;
    miLista1.add(40);// Esta opción es la mas comun para inciar la lista con valores o asignar
                     // valores
    System.out.println(miLista);
  }

  // Funcion o metodo para intercambiar datos por valor
  public static int[] cambiarValor(int d, int e) {
    int temp = d;
    d = e;
    e = temp;
    return new int[] { d, e };
  }

  // Funcion para intercambiar datos por referencia
  public static List<Integer>[] referencia(List<Integer> cambiarRefD, List<Integer> cambiarRefE) {
    List<Integer> temp = cambiarRefD;
    cambiarRefD = cambiarRefE;
    cambiarRefE = temp;
    return new List[] { cambiarRefD, cambiarRefE };
  }

  public static void main(String[] args) {
    // Los daos primitivos en java se manejava por valor
    // quier decir que cuanod le asignas una variable a otra se copia
    // el valor de esta.

    // Tipos de datos por valor
    System.out.println(DIV_LINE);
    int a = 3;
    print("a=", a);
    System.out.println(DIV_LINE);
    int b = a; // resultado -> 3
    print("b=", b);// Imprime 3
    System.out.println(DIV_LINE);
    b = 10; // resultado -> 10
    print("b=", b);// Imprime 10

    // Funciones con tipos de datos por valor
    System.out.println(DIV_LINE);
    int c = 15;
    intFuncion(c);
    System.out.println(DIV_LINE);
    print("c = ", c);

    // Tipos de datos por referencia
    System.out.println(DIV_LINE);
    List<Integer> miLista = new ArrayList<>() {
      {
        add(10);
        add(20);// esta es otra manera de inciar valors mutables a la lista
      }
    };
    funcionDeLista(miLista);
    System.out.println(DIV_LINE);
    miLista.set(2, 60);// reemplaza el valor que esta en posición 2
    System.out.println(miLista);

    // EXTRA
    // Por valor
    System.out.println(DIV_LINE);
    int d = 80;
    int e = 90;
    System.out.printf("d = %d e = %d\n", d, e);
    System.out.println("d = " + cambiarValor(d, e)[0] + " e = " + cambiarValor(d, e)[1]);

    // Por referencia
    System.out.println(DIV_LINE);
    List<Integer> listaD = new ArrayList<>() {
      {
        add(20);
        add(30);
      }
    };
    List<Integer> listaE = new ArrayList<>();
    listaE.add(40);
    listaE.add(50);
    System.out.println("listaD = " + listaD);
    System.out.println("listaE = " + listaE);
    System.out.println("listaE = " + referencia(listaD, listaE)[0] + " listaD = " + referencia(listaD, listaE)[1]);
  }
}
