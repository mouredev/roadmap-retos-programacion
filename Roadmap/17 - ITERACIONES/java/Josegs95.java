import java.util.ArrayList;
import java.util.Collection;

public class Josegs95 {
    public static void main(String[] args) {
        //Ejercicio
        //iterateFor(1, 10);
        //iterateWhile(1, 10);
        //iterateDoWhile(1, 10);

        //Reto
        retoFinal();
    }

    public static void retoFinal(){
        //Los 3 anteriores
        //iterateRecursive(1, 10);
        iterateForEach(createIntegerList(1, 10));
    }

    public static void iterateFor(int begin, int end){
        for (;begin <= end; begin++){
            System.out.println(begin);
        }
    }

    public static void iterateWhile(int begin, int end){
        while (begin <= end){
            System.out.println(begin);
            begin++;
        }
    }

    public static void iterateDoWhile(int begin, int end){
        do{
            System.out.println(begin);
            begin++;
        }while (begin <= end);
    }

    public static void iterateRecursive(int begin, int end){
        if (begin < end)
            iterateRecursive(begin, end - 1);
        System.out.println(end);
    }

    public static void iterateForEach(Collection<Integer> intList){
        for(int n : intList){
            System.out.println(n);
        }
    }

    private static ArrayList<Integer> createIntegerList(int begin, int end){
        ArrayList<Integer> intList = new ArrayList<>();
        while(begin <= end){
            intList.add(begin);
            begin++;
        }

        return intList;
    }
}
