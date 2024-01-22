public class Karolle {
    public static void main(String[] args) {
        // Arithmetic operators
        int a = 10, b = 5;
        System.out.println("Arithmetic Operators:");
        System.out.println("Addition: " + (a + b));
        System.out.println("Subtraction: " + (a - b));
        System.out.println("Multiplication: " + (a * b));
        System.out.println("Division: " + (a / b));
        System.out.println("Modulus: " + (a % b));

        // Logical operators
        boolean x = true, y = false;
        System.out.println("\nLogical Operators:");
        System.out.println("Logical AND: " + (x && y));
        System.out.println("Logical OR: " + (x || y));
        System.out.println("Logical NOT: " + (!x));

        // Comparison operators
        System.out.println("\nComparison Operators:");
        System.out.println("Equal: " + (a == b));
        System.out.println("Not Equal: " + (a != b));
        System.out.println("Greater Than: " + (a > b));
        System.out.println("Less Than: " + (a < b));
        System.out.println("Greater Than or Equal To: " + (a >= b));
        System.out.println("Less Than or Equal To: " + (a <= b));

        // Assignment operators
        int c = 15;
        System.out.println("\nAssignment Operators:");
        c += 5;
        System.out.println("+= Operator: " + c);

        // Conditional statements
        System.out.println("\nConditional Statements:");
        if (a > b) {
            System.out.println("a is greater than b");
        } else {
            System.out.println("b is greater than or equal to a");
        }

        // Iterative structure
        System.out.println("\nIterative Structure:");
        for (int i = 10; i <= 55; i++) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.print(i + " ");
            }
        }

        // Exception handling
        System.out.println("\n\nException Handling:");
        try {
            int result = a / 0; // Division by zero
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Error: Division by zero");
        }
    }
}
