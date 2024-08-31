/**
 * @author: Kronstadt-Lambda
 * @version: 1.0
 */

import java.util.Date;

public class KronstadtLambda {

    static void printGreetings() {
        System.out.println("Hello roadmap-retos-programacion!");
    }

    static void printAuthor(String author) {
        System.out.println("Hello " + author + "!");
    }

    static void printSum(int a, int b) {
        System.out.println("The sum of " + a + " and " + b + " is: " + (a + b));
    }

    static void sumFactors(float[] arr) {
        float sum = 0;
        for (float i : arr) {
            sum += i;
        }
        System.out.println("The sum of the factors is: " + sum);
    }

    static String getNameDay() {
        String[] days = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
        Date date = new Date();
        return days[date.getDay()];
    }

    static int getSquare(int a) {
        return a * a;
    }

    static float getAverage(float[] arr) {
        float sum = 0;
        for (float i : arr) {
            sum += i;
        }
        return sum / arr.length;
    }

    static float printOptionalMultiplication(float a, float b, float... c) { // Optional any number of parameters
        float result = a * b;
        for (float i : c) {
            result *= i;
        }
        return result;
    }

    static int printNumbers(String a, String b) {
        int count = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(a + " and " + b);
            } else if (i % 3 == 0) {
                System.out.println(a);
            } else if (i % 5 == 0) {
                System.out.println(b);
            } else {
                System.out.println(i);
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        // Initialize the variables
        float[] arr = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f};
        float[] arr2 = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f, 10.0f};
        int[] arr3 = {1, 8, 3, 4, 5};
        String author = "Kronstadt-Lambda";

        // Function whitout return and parameters
        printGreetings();

        // Function with one parameter and return
        printAuthor(author);

        // Function with many parameters and return
        printSum(5, 10);

        // Function that accepts any number of parameters and don't have return
        sumFactors(arr);
        sumFactors(arr2);

        // Function whitout parameters and whit return
        System.out.println("Today is: " + getNameDay());

        // Function whit one parameter and return
        System.out.println("The square of 5 is: " + getSquare(5));

        // Function that accepts any number of parameters and have return
        System.out.println("The average of the factors is: " + getAverage(arr));
        System.out.println("The average of the factors is: " + getAverage(arr2));

        // Function whit optional parameters and return
        System.out.println("The multiplication of 5, 10, 2 and 3 is: " + printOptionalMultiplication(5, 10, 2, 3));
        System.out.println("The multiplication of 5 and 4 is: " + printOptionalMultiplication(5, 4));

        // Function inside a function: In Java, functions can be defined inside other functions.
        
        // Functions pre-stablished
        // String functions: length(), toUpperCase(), toLowerCase(), trim(), replace()
        System.out.println("length() function: " + "Hello".length());
        System.out.println("toUpperCase() function: " + "Hello".toUpperCase());
        System.out.println("toLowerCase() function: " + "Hello".toLowerCase());
        System.out.println("trim() function: " + "       Hello ".trim());
        System.out.println("replace() function: " + "Hello".replace("H", "J"));
        // Methods of Integer clase: parseInt(), toString(), valueOf()
        System.out.println("parseInt() function: " + Integer.parseInt("10")); // Convert a string to an integer
        System.out.println("toString() function: " + Integer.toString(10)); // Convert an integer to a string
        System.out.println("valueOf() function: " + Integer.valueOf(10)); // Convert an integer to an Integer object

        // Local and global variables
        String global = "Global variable";
        System.out.println("Global variable: " + global);
        {
            String local = "Local variable";
            System.out.println("Local variable: " + local);
            System.out.println("Global variable inside a block: " + global);
        }
        // System.out.println("Local variable inside a block: " + local); // Error: local cannot be resolved to a variable
        System.out.println("Global variable outside a block: " + global);

        /**
         * Extra exercise
         * Create a function that takes two string parameters and returns a number.
         * - The function prints all numbers from 1 to 100. Considering that:
         * - If the number is a multiple of 3, it displays the string of the first parameter.
         * - If the number is a multiple of 5, it displays the string of the second parameter.
         * - If the number is a multiple of 3 and 5, it displays the two strings of text concatenated.
         * - The function returns the number of times the number has been printed instead of the texts.
         */        
        
        System.out.println("The number of times the number has been printed is: " + printNumbers("multiple of 3", "multiple of 5"));

    }
}