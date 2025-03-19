import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class miguelex {

    public static void main(String[] args) {
        // Arrays

        // Declaración e inicialización
        int[] numbers = new int[5];

        // Asignación
        numbers[0] = 1;
        numbers[1] = 2;
        numbers[2] = 3;
        numbers[3] = 4;

        // Mostramos el array
        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }

        // Añadimos un nuevo elemento
        numbers[4] = 0;
        // Mostramos el array con el nuevo elemento
        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }

        // Editamos un elemento
        numbers[4] = 5;

        // Mostramos el array con el nuevo elemento
        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }

        // Mostramos el array con el nuevo elemento

        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }

        // ordenamos el array

        Arrays.sort(numbers);

        // Mostramos el array con el nuevo elemento

        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }

        // Listas

        // Declaración e inicialización

        List<Integer> numbers3 = new ArrayList<Integer>();

        // Añadimos elementos

        numbers3.add(1);
        numbers3.add(2);
        numbers3.add(3);
        numbers3.add(4);

        // Mostramos la lista

        for (int i = 0; i < numbers3.size(); i++) {
            System.out.println(numbers3.get(i));
        }

        // Añadimos un nuevo elemento

        numbers3.add(0);

        // Mostramos la lista con el nuevo elemento

        for (int i = 0; i < numbers3.size(); i++) {
            System.out.println(numbers3.get(i));
        }

        // Editamos un elemento

        numbers3.set(4, 5);

        // Mostramos la lista con el nuevo elemento

        for (int i = 0; i < numbers3.size(); i++) {
            System.out.println(numbers3.get(i));
        }

        // Borramos un elemento

        numbers3.remove(3);

        // Mapas

        // Declaración e inicialización
        HashMap<String, Integer> mapNumbers = new HashMap<>();
        // Agregando valores al mapa
        mapNumbers.put("one", 1);
        mapNumbers.put("two", 2);
        mapNumbers.put("three", 3);
        mapNumbers.put("four", 4);

        // Mostramos el mapa
        for (Map.Entry<String, Integer> entry : mapNumbers.entrySet()) {
            System.out.println(entry.getKey() + " = " + entry.getValue());
        }

        // Añadimos un nuevo elemento
        mapNumbers.put("zero", 0);
        
        // Recorremos el mapa para mostrarlo

        for (Map.Entry<String, Integer> entry : mapNumbers.entrySet()) {
            System.out.println(entry.getKey() + " = " + entry.getValue());
        }

        // Editamos un elemento

        mapNumbers.put("four", 5);

         // Recorremos el mapa para mostrarlo

         for (Map.Entry<String, Integer> entry : mapNumbers.entrySet()) {
            System.out.println(entry.getKey() + " = " + entry.getValue());
        }

        // Borramos un elemento

        Set<Integer> numbers2 = new HashSet<Integer>();
        numbers2.add(5);

        // Mostramos el set
        for (Integer number : numbers2) {
            System.out.println(number);
        }













    }
}
