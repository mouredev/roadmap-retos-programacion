import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class danhingar {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
        numbers.add(4);
        numbers.add(5);
        numbers.add(6);

        // Añade elemento al final
        numbers.add(7);
        System.out.println(numbers);

        // Añade elemento al principio
        numbers.addFirst(0);
        System.out.println(numbers);

        // Añade varios elementos en bloque al final.
        numbers.addAll(List.of(8, 9, 10));
        System.out.println(numbers);

        // Añade varios elementos en bloque en una posición concreta.
        numbers.addAll(2, List.of(11, 12));
        System.out.println(numbers);

        // Elimina un elemento en una posición concreta.
        numbers.remove(3);
        System.out.println(numbers);

        // Actualiza el valor de un elemento en una posición concreta.
        numbers.set(3, 20);
        System.out.println(numbers);

        // Comprueba si un elemento está en un conjunto.
        System.out.println(numbers.contains(9));

        // Elimina todo el contenido del conjunto.
        numbers.clear();
        System.out.println(numbers);

        // Extra
        List<String> letters1 = new ArrayList<>(List.of("A", "B", "C", "D"));
        List<String> letters2 = new ArrayList<>(List.of("D", "C", "V", "T"));

        // Union
        List<String> letters3 = new ArrayList<>(letters1);
        letters3.addAll(letters2);
        System.out.println("Unión: " + new HashSet<>(letters3));

        // Interseccion
        List<String> letters4 = new ArrayList<>(letters1);
        letters4.retainAll(letters2);
        System.out.println("Intersección: " + new HashSet<>(letters4));

        // Diferencia 1
        List<String> letters5 = new ArrayList<>(letters1);
        letters5.removeAll(letters4);
        System.out.println("Diferencia : " + new HashSet<>(letters5));

        // Diferencia 2
        List<String> letters6 = new ArrayList<>(letters2);
        letters6.removeAll(letters4);
        System.out.println("Diferencia : " + new HashSet<>(letters6));

        // Diferencia simétrica
        letters3.removeAll(letters4);
        System.out.println("Diferencia: " + new HashSet<>(letters3));

    }
}
