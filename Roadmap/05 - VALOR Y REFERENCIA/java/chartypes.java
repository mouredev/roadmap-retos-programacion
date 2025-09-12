
import java.util.HashMap;
import java.util.Map;

class chartypes {
    public static void main(String[] args) {
        // Value
        int myNumber = 5;
        System.out.println("myNumber = " + myNumber);
        valueProof(5);
        System.out.println("myNumber after the function was called = " + myNumber);
        System.out.println(" How you can see...this is assigning variables by value");

        // Reference
        Map<String, Integer> dict = new HashMap<>();
        dict.put("cinco", 5);
        System.out.println("Before call the method: " + dict);
        referenceProof(dict);
        System.out.println("After called the method: " + dict);
        System.out.println(" How you can see...this is assigning variables by reference");

        // Exercise

        // Value
        int two = 2;
        int five = 5;
        int[] numbers = exerciseValueProof(two, five);
        int num1 = numbers[0];
        int num2 = numbers[1];
        System.out.println("variable named 'two' = " + two);
        System.out.println("variable named 'five' = " + five);

        System.out.println("new variable named 'num1' = " + num1);
        System.out.println("new variable named 'num2' = " + num2);

        // Reference
        Map<String, Integer> map1 = new HashMap<>();
        Map<String, Integer> map2 = new HashMap<>();
        map1.put("ten", 10);
        map2.put("eleven", 11);

        System.out.println(" my numbers at the begining: ");
        System.out.println(" first Map: " + map1);
        System.out.println(" second Map " + map2);
        exerciseReferenceProof(map1, map2);
        System.out.println(" my numbers after called teh method : ");
        System.out.println(" first Map: " + map1);
        System.out.println(" second Map " + map2);

    }

    static void valueProof(int number) {
        System.out.println("number = " + number);
        number = 8;
        System.out.println("number has been reasigned to: " + number);

    }

    static void referenceProof(Map<String, Integer> map) {
        map.put("cinco", 7);
    }

    static int[] exerciseValueProof(int value1, int value2) {
        int mediator = value1;
        value1 = value2;
        value2 = mediator;
        int[] response = { value1, value2 };

        return response;

    }

    static void exerciseReferenceProof(Map<String, Integer> referValue1, Map<String, Integer> referValue2) {
        referValue1.put("ten", 20);
        referValue2.put("eleven", 123);

    }
}