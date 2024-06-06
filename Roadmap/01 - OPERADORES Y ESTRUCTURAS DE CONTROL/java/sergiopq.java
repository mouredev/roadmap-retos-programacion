public class sergiopq {
    public static void main(String[] args) {

        // Arithmetic operations (Sum, Subtract, Multiplication, Division, Remainder)
        System.out.println("=== Arithmetic operations ===");
        int a = 10;
        int b = 5;
    
        // Sum
        int sum = a + b;
            System.out.println("The sum is: " + sum);
    
        // Subtract
        int subtract = a - b;
            System.out.println("The subtract is: " + subtract);
    
        // Multiplication
        int multiplication = a * b;
            System.out.println("The multiplication is: " + multiplication);
    
        // Division
        int division = a / b;
            System.out.println("The division is: " + division);
    
        // Remainder
        int remainder = a % b;
            System.out.println("The remainder is: " + remainder);



        // Logical operations (AND, OR, NOT)
        System.out.println("\n=== Logical operations ===");

        // AND
        boolean and = true && false;
            System.out.println("The AND is: " + and);

        // OR
        boolean or = true || false;
            System.out.println("The OR is: " + or);

        // NOT
        boolean not = !true;
            System.out.println("The NOT is: " + not);



        // Comparison operations (Equal, Not equal, Greater than, Less than, Greater than or equal, Less than or equal)
        System.out.println("\n=== Comparison operations ===");

        // Equal
        boolean equal = a == b;
            System.out.println("The equal is: " + equal);

        // Not equal
        boolean notEqual = a != b;
            System.out.println("The not equal is: " + notEqual);

        // Greater than
        boolean greaterThan = a > b;
            System.out.println("The greater than is: " + greaterThan);

        // Less than
        boolean lessThan = a < b;
            System.out.println("The less than is: " + lessThan);

        // Greater than or equal
        boolean greaterThanOrEqual = a >= b;
            System.out.println("The greater than or equal is: " + greaterThanOrEqual);

        // Less than or equal
        boolean lessThanOrEqual = a <= b;
            System.out.println("The less than or equal is: " + lessThanOrEqual);



        // Bitwise operations (AND, OR, XOR, NOT, Right shift, Left shift, Unsigned right shift)
        System.out.println("\n=== Bitwise operations ===");

        // Bitwise AND
        int bitwiseAnd = a & b;
            System.out.println("The bitwise AND is: " + bitwiseAnd);

        // Bitwise OR
        int bitwiseOr = a | b;
            System.out.println("The bitwise OR is: " + bitwiseOr);

        // Bitwise XOR
        int bitwiseXor = a ^ b;
            System.out.println("The bitwise XOR is: " + bitwiseXor);

        // Bitwise NOT
        int bitwiseNot = ~a;
            System.out.println("The bitwise NOT is: " + bitwiseNot);

        // Right shift
        int rightShift = a >> 2;
            System.out.println("The right shift is: " + rightShift);

        // Left shift
        int leftShift = a << 2;
            System.out.println("The left shift is: " + leftShift);

        // Unsigned right shift
        int unsignedRightShift = a >>> 2;
            System.out.println("The unsigned right shift is: " + unsignedRightShift);



        // Assignment operations (Simple, Sum, Subtraction, Multiplication, Division, Remainder, Bitwise AND, Bitwise OR, Bitwise XOR, Right shift, Left shift, Unsigned right shift)
        System.out.println("\n=== Assignment operations ===");

        // Simple assignment
        int simpleAssignment = a;
            System.out.println("The simple assignment is: " + simpleAssignment);

        // Sum assignment
        int sumAssignment = a;
        sumAssignment += 3;
            System.out.println("The sum assignment is: " + sumAssignment);

        // Subtraction assignment
        int subtractionAssignment = a;
        subtractionAssignment -= 2;
            System.out.println("The subtraction assignment is: " + subtractionAssignment);

        // Multiplication assignment
        int multiplicationAssignment = a;
        multiplicationAssignment *= 2;
            System.out.println("The multiplication assignment is: " + multiplicationAssignment);

        // Division assignment
        int divisionAssignment = a;
        divisionAssignment /= 2;
            System.out.println("The division assignment is: " + divisionAssignment);

        // Remainder assignment
        int remainderAssignment = a;
        remainderAssignment %= 2;
            System.out.println("The remainder assignment is: " + remainderAssignment);

        // Bitwise AND assignment
        int bitwiseAndAssignment = a;
        bitwiseAndAssignment &= 2;
            System.out.println("The bitwise AND assignment is: " + bitwiseAndAssignment);

        // Bitwise OR assignment
        int bitwiseOrAssignment = a;
        bitwiseOrAssignment |= 2;
            System.out.println("The bitwise OR assignment is: " + bitwiseOrAssignment);

        // Bitwise XOR assignment
        int bitwiseXorAssignment = a;
        bitwiseXorAssignment ^= 2;
            System.out.println("The bitwise XOR assignment is: " + bitwiseXorAssignment);

        // Right shift assignment
        int rightShiftAssignment = a;
        rightShiftAssignment >>= 2;
            System.out.println("The right shift assignment is: " + rightShiftAssignment);

        // Left shift assignment
        int leftShiftAssignment = a;
        leftShiftAssignment <<= 2;
            System.out.println("The left shift assignment is: " + leftShiftAssignment);

        // Unsigned right shift assignment
        int unsignedRightShiftAssignment = a;
        unsignedRightShiftAssignment >>>= 2;
            System.out.println("The unsigned right shift assignment is: " + unsignedRightShiftAssignment);



        // Operators
        System.out.println("\n=== Operators ===");

        // if
        if (a > b) {
            System.out.println("a is greater than b");
        }

        // if else
        if (a > b) {
            System.out.println("a is greater than b");
        } else {
            System.out.println("a is less than b");
        }

        // switch
        int day = b ;
        switch (day) {
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            case 4:
                System.out.println("Thursday");
                break;
            case 5:
                System.out.println("Friday");
                break;
            default:
                System.out.println("Invalid day");
                break;
        }

        // for
        for (int i = 0; i < b; i++) {
            System.out.println("The value of i is " + i);
        }

        // while
        int num = 0;
        while (num < b) {
            System.out.println(num);
            num++;
            if (num == 5) {
                break;
            }
        }

        // do while
        int num2 = a;
        do {
            System.out.println(num2);
            num2--;
        } while (num2 > 10);



        // Extra difficulty
        System.out.println("\n=== Extra difficulty ===");

        for(int i = 10; i <= 55; i++) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.println(i);
            }
        }
    } 
}