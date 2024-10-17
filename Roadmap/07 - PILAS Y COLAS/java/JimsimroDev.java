
/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Stack;

public class JimsimroDev {

  private static final String DIV_LINE = ":::::::::::::";
  private Stack<Integer> miPila = new Stack<>();
  private LinkedList<Integer> miCola = new LinkedList<>();

  private void push(int elemento) {
    miPila.push(elemento);
  }

  private void peek() {
    if (!miPila.isEmpty()) {
      System.out.println("•Elemento: " + miPila.peek());
    } else {
      System.out.println("❌Pila Esta vacia");
    }
  }

  private void pop() {
    if (!miPila.isEmpty()) {
      miPila.pop();
    } else {
      System.out.println("Ya esta vacia");
    }
  }

  private void colas(Integer elemento) {
    miCola.push(elemento);

  }

  private void colaPop(LinkedList<Integer> cola) {
    if (!miCola.isEmpty()) {
      miCola.remove(0);
    } else {
      System.out.println("Cola vacia");
    }
  }

  private void peekCola() {
    System.out.print("Elemento en la cola " + miCola);
  }

  private void agregarElementosPila(int cantidad) {
    for (int i = 0; i < 6; i++) {// agrego 6 elemento en la pila de 0 a 5
      push(i);
      // Muestra la posicion actual de la pila
      peek();
    }
  }

  private void elimanarDeLaPila(int cantidad) {
    // Elimina y Muestra la posicion actual antes y despues de elminar los elemento
    for (int i = 0; i < 6; i++) {// elimino los 6 elemento en la pila de 0 a 5
      // Muestra la posicion actual de la pila
      peek();
      // Elimina el ultimo elemento ingresado a la pila
      pop();
    }
    peek();
  }

  private void agregarElementosCols(Integer cantidad) {
    for (int i = 0; i < 4; i++) {
      colas(i);
    }
    colaPop(miCola);
    peekCola();
  }

  public static void main(String[] args) {
    JimsimroDev pilas = new JimsimroDev();
    JimsimroDev colas = new JimsimroDev();
    // Las pilas(stacks - LIFO) Nos permite con push agregar elementos a la pila
    // pop para eliminar y peek para saber en que posicion de la pila estamos
    // solo esas opciones nos permita las pilas

    // Pilas(stacks - LIFO)
    System.out.println(DIV_LINE);
    System.out.println("Agrega elemento a la pila");
    pilas.agregarElementosPila(6);

    System.out.println(DIV_LINE);
    System.out.println("Muestra y elimino posicion actual");
    pilas.elimanarDeLaPila(6);

    // Cola
    colas.agregarElementosCols(4);

    System.out.println();
    // EXTRA
    System.out.println(DIV_LINE);
    System.out.println("Pagina EXTRA");
    Scanner in = new Scanner(System.in);
    String menu = """
        :::::::: MENU ::::::::
        Digita la pagina web a visitar
        Digita adelante
        Digita atras
        Digita Salir
        """;
    String apcion;

    Stack<String> miPila = new Stack<>();

    while (true) {
      System.out.println(menu);
      apcion = in.nextLine();

      if ("salir".equals(apcion)) {
        System.out.println("Cerrando la pagina web");
        in.close();
        return;
      } else if ("atras".equals(apcion) && !miPila.isEmpty()) {
        miPila.pop();
        if (!miPila.isEmpty()) {
          System.out.println("Navegaste a la web " + miPila.peek());
        } else {
          System.out.println("Estas en la pagina principal ");
        }
      } else if ("adelante".equals(apcion)) {
        System.out.println("Esata opcon esta deshabilitada intenta con otra");
      } else {
        miPila.push(apcion);
        if (!miPila.isEmpty()) {
          System.out.println("Navegaste a la web " + miPila.peek());
        } else {
          System.out.println("Estas en la pagina principal ");
        }
      }
    }
  }
}
