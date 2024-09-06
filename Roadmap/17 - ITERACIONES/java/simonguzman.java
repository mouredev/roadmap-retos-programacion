public class simonguzman {
    public static void main(String[] args) {
        //bucleFor();
        bucleWhile();
        bucleForEachArray();
    }

    static void bucleFor(){
        for (int i = 1; i <= 10; i++){
            System.out.println(i);
        }
    }

    static void bucleWhile(){
        int i = 1;
        while(i <=10){
            System.out.println(i);
            i++;
        }
    }

    static void bucleForEachArray(){
        int [] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        for (int number : numbers){
            System.out.println(number);
        }
    }
}
