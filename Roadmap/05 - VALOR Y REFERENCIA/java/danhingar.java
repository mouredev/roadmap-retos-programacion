import java.util.*;

public class danhingar {

    public static void main(String[] args) {
        //Tipos de dato por valor
        int number= 1;
        int number2 = number;
        number =2;
        System.out.println(number);
        System.out.println(number2);

        String name1 = "Pepe";
        String name2 = name1;
        name1 = "José";
        System.out.println(name1);
        System.out.println(name2);

        boolean condition1 = true;
        boolean condition2 = condition1;
        condition1 = false;
        System.out.println(condition1);
        System.out.println(condition2);

        //Tipos de datos por referencia -> objetos
        List<Integer> numberList1 = new ArrayList<>(Arrays.asList(1,2,3,4));
        List<Integer> numberList2 = numberList1;
        numberList2.add(5);
        System.out.println(numberList1);
        System.out.println(numberList2);

        int c = 10;
        changeValue(c);
        System.out.println(c);

        List<Integer> numberList3 = new ArrayList<>(Arrays.asList(10,20));
        changeReference(numberList3);
        System.out.println(numberList3);

        String a = "Pepe";
        String b = "Juan";
        String[] result =method1Value(a, b);
        System.out.println(a);
        System.out.println(b);
        System.out.println(result[0]);
        System.out.println(result[1]);

        List<String> nameList = new ArrayList<>(Arrays.asList("Marcos","Jose"));
        List<String> nameList2 = new ArrayList<>(Arrays.asList("Alfonso","Luis"));
        List<List<String>> result2 =method2Reference(nameList, nameList2);
        System.out.println(nameList);
        System.out.println(nameList2);
        System.out.println(result2.get(0));
        System.out.println(result2.get(1));
    }

    //Funcion con datos por valor
    private static void changeValue(int number){
        number = 20;
        System.out.println(number);
    }

    //Funcion con datos por referencia
    private static void changeReference(List<Integer> numbers){
        numbers.add(30);

        List<Integer> numberList4 = numbers;
        numberList4.add(40);
        System.out.println(numbers);
        System.out.println(numberList4);

        //Romper la referencia
        List<Integer> numberList5 = new ArrayList<>(numbers);
        numberList5.add(50);
        System.out.println(numberList5);
    }


    //EJERCICIO EXTRA
    private static String[] method1Value(String name1,String name2){
        String temp = name1;
        name1 = name2;
        name2 = temp;
        return new String[] {name1, name2};
    }

    private static List<List<String>> method2Reference(List<String> name1,List<String> name2){
        List<String> temp = name1;
        name1 = name2;
        name2 = temp;
        return  List.of(name1,name2);
    }
    
}
