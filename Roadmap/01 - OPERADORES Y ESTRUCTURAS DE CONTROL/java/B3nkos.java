public class B3nkos {
    public static void main(String[] args) {
        // assignment operators
        int numberOne = 2;
        int numberTwo = 6;
        int numberThree = 9;

        System.out.printf("numberOne = %d\n", numberOne);
        System.out.printf("numberTwo = %d\n", numberTwo);
        System.out.printf("numberThree = %d\n", numberThree);

        System.out.println();

        // arithmetic operator
        System.out.printf("numberOne + numberTwo = %d\n", numberOne + numberTwo);
        System.out.printf("numberThree - numberOne = %d\n", numberThree - numberOne);
        System.out.printf("numberOne * numberThree = %d\n", numberOne * numberThree);
        System.out.printf("numberThree / numberOne = %d\n", numberThree / numberOne);
        System.out.printf("numberThree %% numberOne = %d\n", numberThree % numberOne);
        numberOne++;
        numberThree--;
        System.out.printf("numberOne++ = %d\n", numberOne);
        System.out.printf("numberThree-- = %d\n", numberThree);
        System.out.printf("numberThree+=3 = %d\n", numberThree+=3);

        System.out.println();

        // comparison operators
        System.out.printf("numberThree > numberOne = %b\n", numberThree > numberOne);
        System.out.printf("numberThree <= numberOne = %b\n", numberThree <= numberOne);
        System.out.printf("numberThree >= numberOne = %b\n", numberThree >= numberOne);

        System.out.println();

        // logic operators
        System.out.printf("true and false = %b\n", true && false);
        System.out.printf("true and true = %b\n", true && true);
        System.out.printf("true or false = %b\n", true || false);
        System.out.printf("false or true = %b\n", false || true);
        System.out.printf("!true = %b\n", !true);
        System.out.printf("!false = %b\n", !false);
        System.out.printf("true is equals to true = %b\n", true == true);

        System.out.println();

        // bits operators
        System.out.printf("numberThree >> 2 = %d\n", numberThree >> 2);
        System.out.printf("numberOne << 1 = %d\n", numberOne << 1);

        System.out.println();

        // if control structure

        if (numberThree > numberOne) {
            System.out.printf("%d is greater than %d\n", numberThree, numberOne);
        }

        // switch control structure
        String animal = "Lion";
        switch (animal) {
            case "Dog" -> System.out.println("The animal is a Dog");
            case "Lion" -> System.out.println("The animal is a Lion");
            case "Cat" -> System.out.println("The animal is a Cat");
            default -> System.out.println("Number not found");
        }

        // while loop
        int c = 1;
        while (c <= 5) {
            System.out.printf("While Loop iteration number #%d\n", c);
            c++;
        }

        System.out.println();

        int k = 0;
        do {
            k++;
            System.out.printf("Do-While loop iteration #%d\n", k);
        } while (k < 5);

        System.out.println();

        // for loop
        for (int i = 1; i <= 5; i++) {
            System.out.printf("For Loop iteration number #%d\n", i);
        }

        System.out.println();

        // EXTRA
        for (int i = 10; i <= 55; i++) {
            if (i == 16 || i % 3 == 0 || i % 2 != 0) {
                continue;
            }

            System.out.println(i);
        }
    }
}
