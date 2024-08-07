public class Karolle {
    // Global variable
    static int globalVariable = 10;

    public static void main(String[] args) {
        // Function without parameters and return value
        printWelcomeMessage();

        // Function with parameters and return value
        int sumResult = addNumbers(5, 7);
        System.out.println("Sum Result: " + sumResult);

        // Function with local variable
        int localVar = 20;
        System.out.println("Local Variable: " + localVar);
        demonstrateScope();

        // Function within a function
        System.out.println("\nFunction within a Function:");
        outerFunction();

        // Using built-in functions
        System.out.println("\nBuilt-in Function Example:");
        String text = "Hello, World!";
        System.out.println("Length of the text: " + text.length());

        // Extra challenge: Function with string parameters and numeric return value
        int printedCount = printNumbersWithText("Fizz", "Buzz");
        System.out.println("\n\nCount: " + printedCount);
    }

    // Function without parameters and return value
    static void printWelcomeMessage() {
        System.out.println("Welcome to Function Example!");
    }

    // Function with parameters and return value
    static int addNumbers(int a, int b) {
        return a + b;
    }

    // Function with local variable to demonstrate scope
    static void demonstrateScope() {
        // Local variable, separate from the one in main
        int localVar = 30;
        System.out.println("Local Variable in demonstrateScope(): " + localVar);
        System.out.println("Global Variable in demonstrateScope(): " + globalVariable);
    }

    // Function within a function
    static void outerFunction() {
        System.out.println("Outer Function");
        innerFunction();
    }

    static void innerFunction() {
        System.out.println("Inner Function");
    }

    // Function with string parameters and numeric return value (Extra challenge)
    static int printNumbersWithText(String text1, String text2) {
        int count = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(text1 + text2);
            } else if (i % 3 == 0) {
                System.out.println(text1);
            } else if (i % 5 == 0) {
                System.out.println(text2);
            } else {
                System.out.println(i);
            }
            count++;
        }
        return count;
    }
}
