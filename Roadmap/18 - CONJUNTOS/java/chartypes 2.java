import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class chartypes {

  public static void main(String[] args) {
    exercise();
    System.out.println("Extra");
    extra();

  }

  private static void exercise() {
    ArrayList<Integer> numbers = new ArrayList<>();
    // Añade un elemento al final.
    numbers.addLast(1);
    System.out.println(numbers);
    // Añade un elemento al principio.
    numbers.addFirst(5);
    System.out.println(numbers);
    // Añade varios elementos en bloque al final.
    ArrayList<Integer> myList = new ArrayList<>();
    myList.add(1);
    myList.add(2);
    myList.add(3);
    numbers.addAll(myList);
    System.out.println(numbers);
    // Añade varios elementos en bloque en una posición concreta.
    numbers.addAll(1, myList);
    System.out.println(numbers);
    // Elimina un elemento en una posición concreta.
    numbers.remove(1);
    System.out.println(numbers);
    // Actualiza el valor de un elemento en una posición concreta.
    numbers.set(2, 800);
    System.out.println(numbers);
    // Comprueba si un elemento está en un conjunto.
    System.out.println(numbers.contains(800));
    // Elimina todo el contenido del conjunto.
    numbers.clear();
    System.out.println(numbers);
  }

  private static void extra() {
    Set<Integer> A = new HashSet<>();
    Set<Integer> B = new HashSet<>();
    A.add(1);
    A.add(2);
    A.add(3);
    A.add(6);
    B.add(3);
    B.add(4);
    B.add(5);
    B.add(6);

    // * - Unión.
    Set<Integer> union = new HashSet<>(A);
    union.addAll(B);
    System.out.println(union);

    // * - Intersección.
    Set<Integer> intersection = new HashSet<>(A);
    intersection.retainAll(B);
    System.out.println(intersection);
    // * - Diferencia.
    Set<Integer> difference = new HashSet<>(A);
    difference.removeAll(B);
    System.out.println(difference);
    // * - Diferencia simétrica.
    Set<Integer> simetricDifferenceUnion = new HashSet<>(A);
    simetricDifferenceUnion.addAll(B);
    Set<Integer> simetricDifferenceIntersection = new HashSet<>(A);
    simetricDifferenceIntersection.retainAll(B);

    simetricDifferenceUnion.removeAll(simetricDifferenceIntersection);
    System.out.println(simetricDifferenceUnion);

  }

}
