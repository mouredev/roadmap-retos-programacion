
import java.util.Scanner;

import java.util.Set;

public class FreedAInew {
    public static void main(String[] args) throws Exception {

        //operators
        //Arithmetic operators

        var A= 10;
        int B= 5;

        System.out.println("Sum: " + (A + B)); 
        System.out.println("Remainder: " + (A - B)); 
        System.out.println("Multiplication: " + (A * B)); 
        System.out.println("Division: " + (A / B)); 
        System.out.println("Module: " + (A % B));



        //Assignment Operators

        // Prefix increment 
        System.out.println("A++: " + (A++)); // Print 10, then increment x to 11 
        // Postfix increment 
        System.out.println("A++: " + (A++)); // Print 11, then increment x to 12 
        System.out.println("A: " + A); // Print 12

        // Decrement prefix 
        System.out.println("B--: " + (B--)); // Print 5, then decrement y to 4 
        // Postfix decrement 
        System.out.println("B--: " + (B--)); // Print 4, then decrement y to 3 
        System.out.println("B: " + B); // Print 3




        //Comparison Operators or Relational Operators 

        System.out.println("A == B: " + (A == B)); // Output: false
        System.out.println("A != B: " + (A != B)); // Output: true
        System.out.println("A < B: " + (A < B)); // Output: false
        System.out.println("A <= B: " + (A <= B)); // Output: false
        System.out.println("A > B: " + (A > B)); // Output: true
        System.out.println("A >= B: " + (A >= B)); // Output: true



        //Logical Operators

        boolean isSunny = true;
        boolean hasUmbrella = false;

        // AND (&&) - Both conditions must be true
        System.out.println("Need umbrella (sunny && !hasUmbrella): " + (isSunny && !hasUmbrella)); // Output: true (sunny and no umbrella)

        // OR (||) - At least one condition must be true
        int age = 20;
        boolean isStudent = true;
        System.out.println("Can vote (age >= 18 || isStudent): "+ (age >= 18 || isStudent)); // Output: true (either age or student status qualifies)

        // NOT (!) - Negates the condition
        boolean isOnline = false;
        boolean isOffline = true;
        System.out.println("Is offline (!isOnline): " + (!isOnline)); // Output: true (not online)
        System.out.println("Is offline (!isOnline): " + (!isOffline)); // Output: false (not online)


        //Identity Operators

        System.out.println(A == B); //Output: false (reference inequality)



        //Membership Operators


        // Create a Set of animals
        Set<String> animals = Set.of("manatee", "Beluga", "Quokka");

        // Check if a specific animal is present (corrected comment)
        boolean isManateePresent = animals.contains("manatee");
        System.out.println("Is manatee present: " + isManateePresent); // Output: true


        // Check if a non-existent animal is present (corrected comment)
        boolean isQuokkaPresent = animals.contains("Quokka");
        System.out.println("Is Quokka present: " + isQuokkaPresent); // Output: false


         //Bitwise Operators

        int a = 6; // 0b110
        int b = 3; // 0b011

         // AND
        int resultAND = a & b;
        System.out.println("AND: " + resultAND); // 2

        // OR
        int resultOR = a | b;
        System.out.println("OR: " + resultOR); // 7

        // XOR
        int resultXOR = a ^ b;
        System.out.println("XOR: " + resultXOR); // 5

        // NOT
        int resultNOT = ~a;
        System.out.println("NOT: " + resultNOT); // -7

        // Left shift
        int resultLeftShift = a << 2;
        System.out.println("Left shift: " + resultLeftShift); // 24

        // Right shift
        int resultRightShift = a >> 2;
        System.out.println("Right shift: " + resultRightShift); // 1

        //Extended range operator

        int lowerBound = 5;
        int upperBound = 15;
        boolean excludeUpperBound = true;

        for (int i = lowerBound; i < (excludeUpperBound ? upperBound : upperBound + 1); i++){ 
            System.out.println(i);}


         //Control Structures


         //Simple Sequential Structure

         // Initialize variables
        int num1 = 10;
        int num2 = 20;

        
        int sum = num1 + num2;// Calculate the sum

        
        System.out.println("The sum of " + num1 + " and " + num2 + " is: " + sum); // Print the sum

         //Conditional structures

         boolean peopleCareAboutWars = false; // Assuming people don't care about wars
         boolean peopleEvadeTaxes = true; // Assuming people evade taxes

        // Check if people care about wars

        if (peopleCareAboutWars) {
            System.out.println("Since people care about wars, they should never pay taxes.");
        } else {
            System.out.println("Since people don't seem to care about wars, they might pay taxes.");

        // Check if people evade taxes
        if (peopleEvadeTaxes) {
            System.out.println("Despite their apathy towards wars, people are still evading taxes.");
        } else {
            System.out.println("If people don't care about wars and they pay taxes honestly, there could be positive outcomes.");
        } }
    



         //Repetitive Control Structure

         Scanner scanner = new Scanner(System.in); // Create Scanner for user input

         System.out.print("Enter body type (Ectomorph, Mesomorph, Endomorph): ");
         String bodyType = scanner.nextLine().toUpperCase(); // Get user input and convert to uppercase
 
         // Display information based on user input
         switch (bodyType) {
             case "ECTOMORPH":
                 System.out.println("**Body Type: Ectomorph**");
                 System.out.println("Characteristics:");
                 System.out.println("- Slender frame");
                 System.out.println("- Thin limbs");
                 System.out.println("- Fast metabolism");
                 System.out.println("- Difficulty gaining muscle mass");
                 break;
             case "MESOMORPH":
                 System.out.println("**Body Type: Mesomorph**");
                 System.out.println("Characteristics:");
                 System.out.println("- Athletic build");
                 System.out.println("- Well-defined muscles");
                 System.out.println("- Balanced metabolism");
                 System.out.println("- Responds well to both strength and endurance training");
                 break;
             case "ENDOMORPH":
                 System.out.println("**Body Type: Endomorph**");
                 System.out.println("Characteristics:");
                 System.out.println("- Rounded physique");
                 System.out.println("- Higher body fat percentage");
                 System.out.println("- Slower metabolism");
                 System.out.println("- Prone to storing fat");
                 break;
             default:
                 System.out.println("Invalid body type.");
         }
 
         scanner.close(); // Close Scanner after use

         

         //Exception Handling:

         try {
            int result = 10 / 0; // Division by zero (ArithmeticException)

            System.out.println("Result: " + result);
          } catch (ArithmeticException e) {
            System.out.println("Error: Division by zero.");
          } finally {
            System.out.println("Program execution complete."); // Always executes
          }


        System.out.println("see you tomorrow!");


    }
}

