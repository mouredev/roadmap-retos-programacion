/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *

 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * JimsimroDev
 */
// La convencion en java para crear una clase es que la primera letra de cada
// palabra sea en mayusculas
public class JimsimroDev {

  // Declarion de los atributos de la clase
  private String nombre;
  private int edad;
  private List<String> stackTecnologico;

  // Metodo constructo vacio
  public JimsimroDev() {
  }

  // Metodo o constructo con parametros para inicializar sus atributos
  public JimsimroDev(String nombre, int edad, List<String> stackTecnologico) {
    this.nombre = nombre;
    this.edad = edad;
    this.stackTecnologico = stackTecnologico;
  }

  // función para imprimir sus atributos
  public void print() {
    System.out.printf("Nombre: %s Edad: %d Stack Tecnologico: %s",
        nombre,
        edad,
        stackTecnologico);
    System.out.println();
  }

  // EXTRA Clase para la crear Pila
  public class Stack<T> {
    private List<T> dato;
    private int posicion = -1;

    public Stack() {
      dato = new ArrayList<>();
    }

    public void push(T elemento) {
      posicion++;
      dato.add(elemento);
    }

    public T pop() {
      if (dato.isEmpty())
        throw new IllegalStateException("None");

      Collections.reverse(dato);
      T resultado = dato.get(posicion);
      dato.remove(posicion);
      posicion--;
      return resultado;
    }

    public T peek() {
      if (dato.isEmpty()) {
        throw new IllegalStateException("La pila esta vacia");
      } else {
        return (T) dato.get(posicion);
      }
    }

    public void print() {
      System.out.println("Cantidad de elemento en la pila " + dato.size());
      Collections.reverse(dato);
      System.out.println(dato);
    }
  }

  public class Queue<T> {
    private List<T> queue;
    private int ps = -1;

    public Queue() {
      queue = new ArrayList<>();
    }

    public void push(T elemento) {
      ps++;
      queue.add(elemento);
    }

    public T pop() {
      T resul = queue.remove(0);
      return resul;
    }

    public void imprimir() {
      System.out.println("Cantidad de elemento en la cola " + queue.size());
      System.out.println(queue);
    }
  }

  public static void main(String[] args) {

    List<String> tecnologias = new ArrayList<>() {
      {
        add("Java");
        add("Spring");
        add("GIT");
        add("Doker");
        add("MySQL");
        add("nvim");
      }
    };
    // Creacion del objeto o istancia
    // Lo puedeo istanciar sin ninguna dato con el constructor vacio
    JimsimroDev ingeniero = new JimsimroDev();
    ingeniero.print();
    // Lo instancio con datos con el constructor que tiene parametros
    JimsimroDev ingenieroBackend = new JimsimroDev("JimsimroDev", 28, tecnologias);
    ingenieroBackend.print();
    ingenieroBackend.edad = 30;// Modifico su edad
    ingenieroBackend.print();

    JimsimroDev.Stack<String> stack = ingeniero.new Stack<>();

    stack.push("Elemento 1");
    stack.push("Elemento 2");
    stack.push("Elemento 3");
    stack.push("Elemento 4");

    // Imprime la posicion del ultimi elemento
    System.out.println(stack.peek());
    stack.print();// Inprime la Cantidad de elemento que tiene
    stack.pop();
    System.out.println(stack.peek());
    stack.print();

    JimsimroDev.Queue<String> queue = ingeniero.new Queue<>();

    queue.push("Elemento 1");
    queue.push("Elemento 2");
    queue.push("Elemento 3");
    queue.push("Elemento 4");
    queue.imprimir();
    queue.pop();
    queue.imprimir();
    queue.pop();
  }
}
