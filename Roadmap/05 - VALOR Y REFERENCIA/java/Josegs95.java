import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Josegs95 {
    public static void main(String[] args) {
        //Asignación por valor. Propio de las variables de tipo primitivo
        int a = 18;
        int b = 5;
        System.out.println("a: " + a); //Out: 'a: 18'
        System.out.println("b: " + b); //Out: 'b: 5'
        b = a;
        a += 3;
        System.out.println("a: " + a); //Out: 'a: 21'
        System.out.println("b: " + b); //Out: 'b: 18'

        //Asignación por referencia. Propio de los objetos
        List<String> listA = new ArrayList<>();
        listA.add("Paloma");
        listA.add("Loro");
        listA.add("Águila");
        List<String> listB = listA;
        System.out.println("listA: " + listA); //Out: [Paloma, Loro, Águila]
        System.out.println("listB: " + listB); //Out: [Paloma, Loro, Águila]
        listA.add("Gorrión");
        listB.add("Cuervo");
        System.out.println("listA: " + listA); //Out: [Paloma, Loro, Águila, Gorrión, Cuervo]
        System.out.println("listB: " + listB); //Out: [Paloma, Loro, Águila, Gorrión, Cuervo]

        //Métodos de ejemplo
        int c = 15;
        System.out.println("c before: " + c); //Out: 'c: 15'
        modifyInteger(c); //Out: 'n: 25'
        System.out.println("c after: " + c); //Out: 'c: 15'

        int[] array = new int[5];
        array[0] = 2;
        array[1] = 6;
        array[2] = 3;
        array[3] = 8;
        System.out.println("array before: " + Arrays.toString(array)); // Out: [2, 6, 3, 8, 0]
        modifyArray(array); // Out: [0, 6, 3, 8, 0]
        System.out.println("array after: " + Arrays.toString(array)); // Out: [0, 6, 3, 8, 0]

        //Reto
        System.out.println("\n");
        retoFinal();
    }

    public static void modifyInteger(int n){
        n += 10;
        System.out.println("n: " + n);
    }

    public static void modifyArray(int[] array){
        array[0] = 0;
        System.out.println("array modified: " + Arrays.toString(array));
    }

    public static void retoFinal(){
        int n1 = 8;
        int n2 = 12;
        int[] result = exchangeValues(n1, n2);
        int n3 = result[0];
        int n4 = result[1];
        System.out.println("n1: " + n1 + " - n2: " + n2);
        System.out.println("n3: " + n3 + " - n4: " + n4);

        List<Integer> l1 = new ArrayList<>(); //Out: 'n1: 8 - n2: 12'
        List<Integer> l2 = new ArrayList<>(); //Out: 'n3: 12 - n4: 8'
        l1.add(8);
        l1.add(6);
        l1.add(2);
        l2.add(3);
        l2.add(5);
        Object[] resultArray = exchangeValuesRef(l1, l2);
        List<Integer> l3 = (ArrayList) resultArray[0];
        List<Integer> l4 = (ArrayList) resultArray[1];
        System.out.println("l1: " + l1 + " - l2: " + l2); //Out: 'l1: [8, 6, 2] - l2: [3, 5]'
        System.out.println("l3: " + l3 + " - l4: " + l4); //Out: 'l3: [3, 5] - l4: [8, 6, 2]'
    }

    private static int[] exchangeValues(int a, int b){
        int c = b;
        b = a;
        a = c;
        int[] array = {a, b};
        return array;
    }

    private static Object[] exchangeValuesRef(List list1, List list2){
        List list3 = list1;
        list1 = list2;
        list2 = list3;
        Object[] array = {list1, list2};

        return array;
    }
}
