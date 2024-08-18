import java.lang.reflect.Array;
import java.util.*;

public class simonguzman {
    public static void main(String[] args) {
        
        /*//Arrays
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
        }*/

        /* 
        //Lists
        ArrayList<String> names = new ArrayList<>();
        
        //Insertion
        names.add("Simon");
        names.add("Julian");
        names.add("Camilo");
        names.add("Santiago");
        names.add("Carlos");

        //Delete    
        //names.clear();

        //Update
        names.set(2, "Juliana");

        //Sort
        Collections.sort(names);

        //Show the list
        System.out.println(names);*/

        //Maps
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
    }
}
