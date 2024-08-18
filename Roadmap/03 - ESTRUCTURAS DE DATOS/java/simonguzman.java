import java.lang.reflect.Array;
import java.util.*;
import java.util.PriorityQueue;

public class simonguzman {
    public enum Dias{
        Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, Domingo
    }
    public static void main(String[] args) {
        
        /*//*********************Arrays*********************
        int [] numbers = {1,2,3,4,5}; 
        int newLength = 8;
        //update
        numbers[0] = 13;
        //sort
        Arrays.sort(numbers);
        //Insertion
        int [] newArray = new int[newLength];
        for (int i = 0; i < numbers.length; i++) {
            newArray[i] = numbers[i];
        }
        numbers = newArray;
        //Delete
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = 0;
        }
        //Show the array
        System.out.println(Arrays.toString(numbers));
        //Alternative to show the array
        for (int i = 0; i < numbers.length; i++){
            System.out.println(numbers[i]);
        }

        ////*********************Bidimensional Array****************
        int [][] numId = new int[2][2];

        //Insertion
        numId[0][0] = 0;
        numId[0][1] = 1;
        numId[1][0] = 2;
        numId[1][1] = 3;
        //update
        numId[0][1] = 4;
        //Delete
        numId[1][1] = 0;
        //Alternative delele
        for (int i = 0; i < numId.length; i++){
            for (int j = 0; j < numId[i].length; j++){
                numId[i][j] = 0;
            }
        }

        //Show the bidimensional array
        for (int i = 0; i < numId.length; i++){
            for (int j = 0; j < numId[i].length; j++){
                System.out.println(numId[i][j]);
            }
        }


        //*********************Lists*********************
        ArrayList<String> names = new ArrayList<>();
        //Insertion
        names.add("Simon");
        names.add("Julian");
        names.add("Camilo");
        names.add("Santiago");
        names.add("Carlos");
        //Delete    
        names.clear();
        //Update
        names.set(2, "Juliana");
        //Sort
        Collections.sort(names);
        //Show the list
        System.out.println(names);

        //LinkedList
        LinkedList<String> lista = new LinkedList<>();

        //Insertion
        lista.add("Primer elemento");
        lista.add("Segundo elemento");
        lista.add("Tercer elemento");
        lista.add("Cuarto elemento");
        lista.add("Ultimo elemento");
        //Update
        lista.set(4, "Nuevo elemento");
        //Delete
        lista.remove(3);
        lista.remove("Tercer elemento");
        //Alternative of delete
        //lista.removeFirst();
        //lista.removeLast();
        //lista.removeAll(lista);
        //Sort
        Collections.sort(lista);
        //Show linked list
        for(String item: lista){
            System.out.println(item);
        }

        //*********************Maps*********************
        HashMap<String, Integer> infoPersonal = new HashMap<>();
        //Insertion
        infoPersonal.put("Simon", 20);
        infoPersonal.put("Julian", 22);
        infoPersonal.put("Camilo", 24);
        infoPersonal.put("Santiago", 21);
        infoPersonal.put("Carlos", 28);
        //Uodate
        infoPersonal.put("Juliana", 22);
        //Delete
        infoPersonal.remove("Camilo");
        //Show the map
        System.out.println(infoPersonal.keySet() + " " + infoPersonal.values());
        //Alternative option
        for(Map.Entry<String, Integer> entry : infoPersonal.entrySet()){
            System.out.println(entry.getKey() + " " + entry.getValue());
        }

        //*********************Colections*********************
        ArrayList<Integer> edades = new ArrayList<>();
        //Insertion
        edades.add(22);
        edades.add(30);
        edades.add(21);
        edades.add(24);
        //update
        edades.set(1, 29);
        //Delete
        edades.remove(2);
        //Sort
        Collections.sort(edades);
        //Show the colections
        int age = edades.get(0);
        System.out.println(age);
        for (int i = 0; i < edades.size(); i++){
            System.out.println(edades.get(i));
        }

        //*********************TreeSet*********************
        TreeSet<Integer> set = new TreeSet<>();

        //Insertion
        set.add(10);
        set.add(11);
        set.add(12);
        set.add(13);
        set.add(14);
        set.add(15);
        //Delete
        set.remove(13);
        //Show the TreeSet
        for(Integer i: set){
            System.out.println(i);
        }

        //*********************HashSet*********************
        HashSet<String> names = new HashSet<>();
        //Insertion
        names.add("Juan");
        names.add("Maria");
        names.add("Adriano");
        //Update
        names.remove("Maria");
        //Show HashSet
        for(String name : names){
            System.out.println(name);
        }*/

        //*********************Enum*********************
        Dias dia = Dias.Lunes;

        switch (dia) {
            case Lunes:
                System.out.println("Es el dia lunes");
                break;
            case Martes:
                System.out.println("Es el dia martes");
                break;
            case Miercoles:
                System.out.println("Es el dia miercoles");
                break;
            case Jueves:
                System.out.println("Es el dia jueves");
                break;
            case Viernes:
                System.out.println("Es el dia viernes");
                break;
            case Sabado:
                System.out.println("Es el dia sabado");
                break;
            case Domingo:
                System.out.println("Es el dia domingo");
                break;
            default:
                System.out.println("El dia no existe");
                break;
        }
    }
}
