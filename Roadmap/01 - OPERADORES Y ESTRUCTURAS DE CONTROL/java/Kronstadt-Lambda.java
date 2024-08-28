/**
 * @author KronstadtLambda
 * @version 1.0
 */

// package roadmap.java.r01;

public class KronstadtLambda {

    public static int suma(int a, int b) {
        return a + b; // Return the sum of a and b
    }
    public static void main(String[] args) {
        
        // Initialize variables
        float float_a = 2.0f;
        float float_b = 2.0f;
        int bit_a = 0b01000001;
        int bit_b = 0b01010011;
        String day = "Monday";
        int edad = 1;
        boolean isBool;
        int[] numbers = {1, 2, 3, 4, 5};

        /*
         * Operators in Java
         */
        // Arithmetic operators
        System.out.println("float_a + float_b = " + (float_a + float_b));
        System.out.println("float_a - float_b = " + (float_a - float_b));
        System.out.println("float_a * float_b = " + (float_a * float_b));
        System.out.println("float_a / float_b = " + (float_a / float_b));
        System.out.println("float_a % float_b = " + (float_a % float_b)); // Remainder of the division
        System.out.println("float_a++ = " + (float_a++)); // Post-increment
        System.out.println("float_a-- = " + (float_a--)); // Post-decrement
        System.out.println("++float_a = " + (++float_a)); // Pre-increment
        System.out.println("--float_a = " + (--float_a)); // Pre-decrement

        // Assignment operators
        System.out.println("float_a += float_b -> " + (float_a += float_b)); // float_a = float_a + float_b
        System.out.println("float_a -= float_b -> " + (float_a -= float_b)); // float_a = float_a - float_b
        System.out.println("float_a *= float_b -> " + (float_a *= float_b)); // float_a = float_a * float_b
        System.out.println("float_a /= float_b -> " + (float_a /= float_b)); // float_a = float_a / float_b
        System.out.println("float_a %= float_b -> " + (float_a %= float_b)); // float_a = float_a % float_b
        System.out.println("bit_a &= bit_b -> " + (bit_a &= bit_b)); // bit_a = bit_a & bit_b (bitwise AND)
        System.out.println("bit_a |= bit_b -> " + (bit_a |= bit_b)); // bit_a = bit_a | bit_b (bitwise OR)
        System.out.println("bit_a ^= bit_b -> " + (bit_a ^= bit_b)); // bit_a = bit_a ^ bit_b (bitwise XOR)
        System.out.println("bit_a >>= 1 -> " + (bit_a >>= 1)); // bit_a = int_a >> 1 (bitwise right shift)
        System.out.println("bit_a <<= 1 -> " + (bit_a <<= 1)); // bit_a = int_a << 1 (bitwise left shift)

        // Comparison operators
        System.out.println("float_a == float_b -> " + (float_a == float_b)); // Equal to 
        System.out.println("float_a != float_b -> " + (float_a != float_b)); // Not equal to 
        System.out.println("float_a > float_b -> "  + (float_a > float_b)); // Greater than 
        System.out.println("float_a < float_b -> "  + (float_a < float_b)); // Less than 
        System.out.println("float_a >= float_b -> " + (float_a >= float_b)); // Greater than or equal to 
        System.out.println("float_a <= float_b -> " + (float_a <= float_b)); // Less than or equal to 

        // Logical operators
        System.out.println("float_a == float_b && float_a != 0 -> " + (float_a == float_b && float_a != 0)); // Logical AND
        System.out.println("float_a == float_b || float_a != 0 -> " + (float_a == float_b || float_a != 0)); // Logical OR
        System.out.println("!(float_a == float_b) -> " + !(float_a == float_b)); // Logical NOT

        // Bitwise operators
        System.out.println("bit_a & bit_b -> " + (bit_a & bit_b)); // Bitwise AND
        System.out.println("bit_a | bit_b -> " + (bit_a | bit_b)); // Bitwise OR
        System.out.println("bit_a ^ bit_b -> " + (bit_a ^ bit_b)); // Bitwise XOR
        System.out.println("~bit_a -> " + (~bit_a)); // Bitwise NOT
        System.out.println("bit_a >> 1 -> " + (bit_a >> 1)); // Bitwise right shift
        System.out.println("bit_a << 1 -> " + (bit_a << 1)); // Bitwise left shift
        System.out.println("bit_a >>> 1 -> " + (bit_a >>> 1)); // Bitwise right shift with zero fill
        
        // Java don't have identity and membership operators

        /*
         * Control structures in Java
         */
        // If, if-else, else statement
        if (float_a == float_b) {
            System.out.println("float_a is equal to float_b");
        } else if (float_a > float_b) {
            System.out.println("float_a is greater than float_b");
        } else {
            System.out.println("float_a is less than float_b");
        }
        // Switch statement
        switch (day) {
            case "Monday":
                System.out.println("Today is Monday");
                break; // Exit the switch statement to avoid fall-through
            case "Tuesday":
                System.out.println("Today is Tuesday");
                break; // Exit the switch statement to avoid fall-through
            case "Wednesday":
                System.out.println("Today is Wednesday");
                break; // Exit the switch statement to avoid fall-through
            case "Thursday":
                System.out.println("Today is Thursday");
                break; // Exit the switch statement to avoid fall-through
            case "Friday":
                System.out.println("Today is Friday");
                break; // Exit the switch statement to avoid fall-through
            case "Saturday":
                System.out.println("Today is Saturday");
                break; // Exit the switch statement to avoid fall-through
            case "Sunday":
                System.out.println("Today is Sunday");
                break; // Exit the switch statement to avoid fall-through
            default: // if none of the above cases are true
                System.out.println("Invalid day");
                break; // Exit the switch statement to avoid fall-through
        }
        // For loop
        for (int i = 10; i >= 0; i--) {
            System.out.println("The loop end in ... " + i);
        }
        // While loop
        while (edad < 18) {
            System.out.println("You are " + edad + " years old");
            edad++;
        }
        // do-while loop
        do {
            isBool = false;
            System.out.println("At least one execution");
        } while (isBool);
        // For-each loop
        for (int number : numbers) {
            System.out.println("Square of " + number + " is " + number * number);
        }
        // break statement
        for (int i = 0; i < 10; i++) {
            if (i == 5) {
                System.out.println("Break in i = " + i);
                break; // Exit the loop
            }
            System.out.println("i = " + i);
        }
        // continue statement
        for (int i = 0; i < 10; i++) {
            if (i == 5) {
                System.out.println("Continue (skip) in i = " + i);
                continue; // Skip the rest of the loop
            }
            System.out.println("Cube of " + i + " is " + i * i * i);
        }
        // return statement
        System.out.println("The sum of 5 and 7 is " + suma(5, 7));
        // try-catch
        try {
            int[] array = {1, 2, 3};
            System.out.println(array[3]); // ArrayIndexOutOfBoundsException
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array index out of bounds");
        }
        // try-catch-finally
        try {
            int[] array = {1, 2, 3};
            System.out.println(array[3]); // ArrayIndexOutOfBoundsException
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array index out of bounds"); // Execute if an exception is thrown
        } finally {
            System.out.println("Finally block executed"); // Necesary for close resources or other actions
        }
        // throw statement
        try {
            throw new ArithmeticException("Arithmetic exception"); // Intentionally throw an exception
            /* 
             * It is useful for testing the behavior of the program when an exception is thrown like error handling.
             */
        } catch (ArithmeticException e) {
            System.out.println(e.getMessage());
        }
        
        /*
         * Extra exercise
         * Create a program that prints to the console all numbers between 10 and 55 (inclusive), even, and that are neither 16 nor multiples of 3
         */
        for (int i = 10; i <= 55; i++) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.println("The solution is " + i);
            }
        }

    }
}