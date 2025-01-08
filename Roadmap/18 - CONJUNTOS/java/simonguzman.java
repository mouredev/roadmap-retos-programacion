import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class simonguzman {
    public static void main(String[] args) {
        testArrayList();
        extraExercise();
    }
    
    static void testArrayList() {
        ArrayList<Integer> list = new ArrayList<>();

        addElementFinal(list);
        addElementInitial(list);        

        System.out.println("Contenido de la lista después de añadir elementos al final e inicial: " + list);

        addElementsFinalBlock(list);
        addElementsBlockPositionConcrete(list);

        System.out.println("Contenido de la lista después de añadir varios elementos al final y en una posición concreta: " + list);

        deleteElementConcretePosition(list);

        System.out.println("Contenido de la lista después de eliminar un elemento en una posición concreta: " + list);

        updateValueConcretePosition(list);

        System.out.println("Contenido de la lista después de actualizar el valor de un elemento en una posición concreta: " + list);

        containsElement(list);

        System.out.println("Contenido de la lista después de comprobar si un elemento está en el conjunto: " + list);

        deleteAll(list);

        System.out.println("Contenido de la lista después de eliminar todo el contenido del conjunto: " + list);
    }

    static void addElementFinal(ArrayList<Integer> list){
        list.add(10);
    }

    static void addElementInitial(ArrayList<Integer> list){
        list.add(0, 10);
    }

    static void addElementsFinalBlock(ArrayList<Integer> list){
        list.addAll(Arrays.asList(10,20,30));
    }

    static void addElementsBlockPositionConcrete(ArrayList<Integer> list){
        list.addAll(0, Arrays.asList(10,20,30));
    }

    static void deleteElementConcretePosition(ArrayList<Integer> list){
        list.remove(2);
    }

    static void updateValueConcretePosition(ArrayList<Integer> list){
        list.set(2, 40);
    }

    static void containsElement(ArrayList<Integer> list){
        boolean containsElem = list.contains(10);
    }

    static void deleteAll(ArrayList<Integer> list){
        list.clear();
    }

    static void extraExercise(){
        Set<String> setA = new HashSet<>();
        Set<String> setB = new HashSet<>();
        createSets(setA, setB);
        setUnion(setA, setB);
        setIntersection(setA, setB);
        setDifference(setA, setB);
        setSymmetricalDifference(setA, setB);
    }

    static void createSets(Set<String>setA, Set<String>setB){
        setA.add("A");
        setA.add("B");
        setA.add("C");
        setB.add("B");
        setB.add("C");
        setB.add("D");
    }

    static void setUnion(Set<String>setA, Set<String>setB){
        Set<String> union = new HashSet<>(setA);
        union.addAll(setB);
        System.out.println("Union: "+union);
    }

    static void setIntersection(Set<String>setA, Set<String>setB){
        Set<String> intersection = new HashSet<>(setA);
        intersection.retainAll(setB);
        System.out.println("Interseccion: "+intersection); 
    }

    static void setDifference(Set<String>setA, Set<String>setB){
        Set<String> difference = new HashSet<>(setA);
        difference.removeAll(setB);
        System.out.println("Diferencia: "+difference);
    }

    static void setSymmetricalDifference(Set<String>setA, Set<String>setB){
        Set<String> symmetricalDifference = new HashSet<>(setA);
        symmetricalDifference.addAll(setB);
        Set<String> tmp = new HashSet<>(setA);
        tmp.retainAll(setB);
        symmetricalDifference.removeAll(tmp);
        System.out.println("Diferencia simetrica: "+symmetricalDifference);
    }
}
