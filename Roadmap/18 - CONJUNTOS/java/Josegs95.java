import java.util.*;

public class Josegs95 {
    public static void main(String[] args) {
        //Lo mas parecido a un conjunto en java son los Set.
        //Pero para la parte del ejercicio, voy a usar una lista, ya que hay operaciones que
        //ninguna implementación de Set puede hacer de forma nativa.
        List<String> elementList = new ArrayList<>();
        elementList.add("1");
        elementList.add("2");
        elementList.add("3");
        System.out.println(elementList);


        //Añadir elemento al final
        elementList.add("Final");
        System.out.println("1. " + elementList);

        //Añadir elemento al principio
        elementList.add(0, "Principio");
        System.out.println("2. " + elementList);

        //Añadir varios elementos al final
        elementList.addAll(Arrays.asList("Final1", "Final2"));
        System.out.println("3. " + elementList);

        //Añadir varios elementos en una posición
        elementList.addAll(2, Arrays.asList("1.3", "1.6"));
        System.out.println("4. " + elementList);

        //Eliminar elemento por posición
        elementList.remove(2);
        System.out.println("5. " + elementList);

        //Actualizar elemento por posición
        elementList.set(5, "FinalActualizado");
        System.out.println("6. " + elementList);

        //Comprobar si existe un elemento en el conjunto
        System.out.println("7. Existe el elemento '4': " + elementList.contains("4"));

        //Elimina el contenido del conjunto
        elementList.clear();
        System.out.println("8. " + elementList);

        //Reto
        retoFinal();
    }

    public static void retoFinal(){
        Set<String> set1 = new HashSet<>(Arrays.asList("1", "2", "4", "6"));
        Set<String> set2 = new HashSet<>(Arrays.asList("1", "3", "6", "9"));
        System.out.println("Set1: " + set1);
        System.out.println("Set2: " + set2);

        //Union
        Set<String> union = new HashSet<>(set1);
        union.addAll(set2);
        System.out.println("Set1 U Set2: " + union);

        //Intersección
        Set<String> intersection = new HashSet<>(set1);
        intersection.retainAll(set2);
        System.out.println("Set1 ∩ Set2: " + intersection);

        //Diferencia
        Set<String> difference = new HashSet<>(set1);
        difference.removeAll(set2);
        System.out.println("Set1 - Set2: " + difference);

        //Diferencia simétrica
        Set<String> symmetricDifference = new HashSet<>(union);
        symmetricDifference.removeAll(intersection);
        System.out.println("Set1 Δ Set2: " + symmetricDifference);
    }
}
