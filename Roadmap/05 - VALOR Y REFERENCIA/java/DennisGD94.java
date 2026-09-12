import java.util.ArrayList;
import java.util.Arrays;

public class DennisGD94 {
    public static void main(String[] args) {


        System.out.println("-------------VALOR Y REFERENCIA-------------");


        int a = 10;
        int b = a;

        b = 20;

        System.out.println(a);
        System.out.println(b);

        ArrayList<String> list = new ArrayList<>();

        list.add("java");

        ArrayList<String> list1 = list;

        list1.add("Spring");

        System.out.println(list);

        System.out.println(list1);

        int number = 10;

        changeValue(number);
        System.out.println(number);

        ArrayList<String> names = new ArrayList<>();
        names.add("Dennis");

        changeList(names);

        System.out.println(names);


        System.out.println("--------DIFICULTAD EXTRA--------");


        int x = 50;
        int y = 40;
        int[] newValue = swapValues(x, y);

        System.out.println("Variables originales: " + "X = " + x +" " + "Y = " + y);


        System.out.println("Variables nuevas: X = " + newValue[0] + " Y = " + newValue[1]);


        ArrayList<String> name =  new ArrayList<>();
        name.add("Dennis");
        ArrayList<String> name1 =  new ArrayList<>();
        name1.add("Fabio");
        System.out.println("Listas originales: ");
        System.out.println(name);
        System.out.println(name1);

        System.out.println("Listas neuvas intercambiadas: ");
        ArrayList<String>[] swap = swapValues(name, name1);

        System.out.println(Arrays.toString(swap));










    }


    public static void changeValue(int number){

        number = 50;
    }

    public static void changeList(ArrayList<String> list){
        list = new ArrayList<>();
        list.add("Spring");
        System.out.println(list);
    }
    public static int[] swapValues(int x , int y){


        int temp = x;
        x = y;
        y = temp;



        return new int[]{x, y};
    }

    public static ArrayList<String>[] swapValues(ArrayList<String> list, ArrayList<String> list1){

        ArrayList<String> temp = list;
        list = list1;
        list1 = temp;

        ArrayList<String>[] result = new ArrayList[]{list, list1};
        return result;
    }
}
