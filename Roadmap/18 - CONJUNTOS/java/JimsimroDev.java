/*
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 */

import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

class Conjunto {
  final String DIVLINE = ":::::::::::::::::::::::::::::::::";
  LinkedList<Integer> conjunto = new LinkedList<>();

  // agrega los primeros 6 elementos a la pila
  void agregaPrimerosDatos() {
    for (int i = 1; i <= 6; i++) {
      conjunto.add(i);
    }
  }

  // agrega elemento al final
  void agragarElementoAlFinal(int elemento) {
    conjunto.addLast(elemento);

  }

  // agrega elemento al principio
  void agragarElementoAlPrincipio(int elemento) {
    conjunto.addFirst(elemento);
  }

  // Añade varios elementos en bloque al final.
  void agregaVariosElmentosAlFinal(List<Integer> nuevosElementos) {
    conjunto.addAll(nuevosElementos);
  }

  // Añade varios elementos en bloque en una posición concreta.
  void agregaVariosElmentosSegunPosicionDada(int posicion, List<Integer> elementosNuevos) {
    conjunto.addAll(posicion, elementosNuevos);
  }

  // Elimina un elemento en una posición concreta.
  void eliminarValor(int posicion) {
    try {
      conjunto.remove(posicion);
      IO.println(String.format("Se elimino el elemento en la posición %d ", posicion));
    } catch (Exception e) {
      IO.println(String.format("El conjunto solo tiene %d posiciónes %s", conjunto.size(), e));
    }
  }

  // Actualiza el valor de un elemento en una posición concreta.
  void actualizarElemento(int posicion, int elemento) {
    conjunto.set(posicion, elemento);
  }

  // Validar si el valor existe en el conjunto
  boolean ifValueExist(int valor) {
    for (int i = 0; i < conjunto.size(); i++) {
      if (conjunto.get(i) == valor) {
        return true;
      }
    }
    return false;
  }

  void valorEncotrado(int valor) {
    String valorEncotrado = ifValueExist(valor) ? String.format("El valor %d si esta en el conjunto", valor)
        : String.format("El valor %d no se encuentra en el conjunto", valor);
    IO.println(valorEncotrado);
  }

  // Imprime los valores del conjunto y su posición
  void printConjunto() {
    for (int i = 0; i < conjunto.size(); i++) {
      IO.print(String.format("posición %d valor %d %n ", i, conjunto.get(i)));
    }
  }

  // Inicializa el conjunto y le agrega valores
  void run() {
    agregaPrimerosDatos();

    IO.println(DIVLINE);
    printConjunto();

    agragarElementoAlFinal(7);

    IO.println(DIVLINE);
    printConjunto();
    agragarElementoAlPrincipio(8);
    List<Integer> elementos = List.of(11, 12, 13);
    agregaVariosElmentosAlFinal(elementos);

    IO.println(DIVLINE);
    printConjunto();
    List<Integer> elementosNuevos = List.of(8, 9, 10);
    agregaVariosElmentosSegunPosicionDada(8, elementosNuevos);
    IO.println(DIVLINE);
    printConjunto();

    eliminarValor(0);

    IO.println(DIVLINE);
    printConjunto();

    actualizarElemento(0, 30);
    valorEncotrado(12);
    IO.println(DIVLINE);
    printConjunto();

    conjunto.clear();
    IO.println(DIVLINE);
    IO.println(conjunto);
  }

  void main() {
    run();
    // EXTRA
    IO.println("EXTRA");
    Set<Integer> elementos1 = new HashSet<>();
    elementos1.add(1);
    elementos1.add(2);
    elementos1.add(3);
    elementos1.add(4);
    elementos1.add(5);
    IO.println(elementos1);

    Set<Integer> elementos2 = new HashSet<>();
    elementos2.add(1);
    elementos2.add(2);
    elementos2.add(3);
    elementos2.add(4);
    elementos2.add(6);
    elementos2.add(7);
    IO.println(elementos2);

    // Unión
    Set<Integer> union = new HashSet<>(elementos1);
    union.addAll(elementos2);

    IO.println("Unión");
    IO.println(union);

    // Intersección
    Set<Integer> interseccion = new HashSet<>(elementos2);
    interseccion.retainAll(elementos1);
    IO.println("Intersección");
    IO.println(interseccion);

    // Diferencia
    Set<Integer> diferencia = new HashSet<>(elementos2);
    diferencia.removeAll(elementos1);
    IO.println("Diferencia");
    IO.println(diferencia);

    // Diferencia simétrica
    Set<Integer> diferenciaSimetrica = new HashSet<>(union);
    diferenciaSimetrica.removeAll(interseccion);
    IO.println("Diferencia simétrica");
    IO.print(diferenciaSimetrica);
  }
}
