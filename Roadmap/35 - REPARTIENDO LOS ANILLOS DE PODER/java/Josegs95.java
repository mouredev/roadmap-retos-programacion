import java.util.ArrayList;
import java.util.List;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().ringOfPower();
    }

    private int ringToSauron;
    private int ringToMen;
    private int ringToElves;
    private int ringToDwarves;

    public void ringOfPower(){
        shareRings(20);
        shareRings(51);
        shareRings(101);
        shareRings(117);
    }

    private void shareRings(int ringAmount){
        List<Integer[]> combinations = calculateSharing(ringAmount);
        if (combinations.isEmpty()){
            System.out.println("Error. No ha sido posible hacer la distribución de los " + ringAmount + " anillos");
            return;
        }

        //Ver todas las combinaciones
        int counter = 1;
        for (Integer[] combination : combinations){
            System.out.println(counter + ". Hombres: " + combination[0] + ", Elfos: " +
                    combination[1] + ", Enanos: " + combination[2] + ", Sauron: 1");
            counter++;
        }

        Integer[] combination = combinations.get((combinations.size() / 2) - (combinations.size() % 2 == 0 ? 1 : 0));

        System.out.println("¡Se repartieron los " + ringAmount + " anillos con éxito!");
        System.out.println("Los hombres reciben " + combination[0] + " anillo/s.");
        System.out.println("Los elfos reciben " + combination[1] + " anillo/s.");
        System.out.println("Los enanos reciben " + combination[2] + " anillo/s.");
        System.out.println("Y Sauron recibe 1 anillo.");
    }

    private List<Integer[]> calculateSharing(int ringAmount){
        ringToSauron = 1;
        ringToElves = 0;
        ringToMen = 0;
        ringToDwarves = 0;

        List<Integer[]> possibleSharing = new ArrayList<>();

        for (int a = 0; ringToElves < ringAmount; a++){
            ringToElves = 1 + 2 * a;

            for (int b = 0; ringToMen < ringAmount; b++){
                ringToMen = 2 + 2 * b;

                for (int c = 0; ringToDwarves < ringAmount; c++){
                    ringToDwarves = primeNumber(c);
                    if (checkRingSum() == ringAmount)
                        possibleSharing.add(new Integer[] {ringToMen, ringToElves, ringToDwarves});
                }

                ringToDwarves = 2;
                if (checkRingSum() == ringAmount)
                    possibleSharing.add(new Integer[] {ringToMen, ringToElves, ringToDwarves});
            }

            ringToMen = 2;
            if (checkRingSum() == ringAmount)
                possibleSharing.add(new Integer[] {ringToMen, ringToElves, ringToDwarves});
        }



        return possibleSharing;
    }

    private int primeNumber(int n){
        if (n == 0)
            return 2;

        List<Integer> primeNumberList = new ArrayList<>();
        primeNumberList.add(2);

        numbers:
        for (int i = 3; i < Integer.MAX_VALUE; i+= 2){
            for (int primeNumber : primeNumberList){
                if (i % primeNumber == 0){
                    continue numbers;
                }
            }
            if (--n == 0)
                return i;
            primeNumberList.add(i);
        }

        return -1;
    }

    private int checkRingSum(){
        return ringToSauron + ringToDwarves + ringToElves + ringToMen;
    }
}
