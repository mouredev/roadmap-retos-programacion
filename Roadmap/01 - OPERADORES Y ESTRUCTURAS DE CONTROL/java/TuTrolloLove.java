public class TuTrolloLove {
    public static void main(String[] args) {
        String op_asignation = "TuTrolloLove";
        int op_arithmetic_minus = -1;
        int op_arithmetic_sum = 1+1;
        int op_arithmetic_subtraction = 2-1;
        int op_arithmetic_multiplication = 2*2;
        int op_arithmetic_division = 4/2;
        int op_arithmetic_modulus = 5%2;

        // Arithmetic operators increment and decrement
        int op_arithmetic = 1;
        for (int i=0;i<1;i++) {
            op_arithmetic++;
            System.out.println("op_arithmetic++: " + op_arithmetic);
            op_arithmetic--;
            System.out.println("op_arithmetic--: " + op_arithmetic);
        }

        // Arithmetic operators combined
        int op_arithmetic_combined = 1;
        op_arithmetic_combined += 1;
        System.out.println("op_arithmetic_combined += 1: " + op_arithmetic_combined);
        op_arithmetic_combined -= 1;
        System.out.println("op_arithmetic_combined -= 1: " + op_arithmetic_combined);
        op_arithmetic_combined *= 2;
        System.out.println("op_arithmetic_combined *= 2: " + op_arithmetic_combined);
        op_arithmetic_combined /= 2;
        System.out.println("op_arithmetic_combined /= 2: " + op_arithmetic_combined);
        op_arithmetic_combined %= 2;
        System.out.println("op_arithmetic_combined %= 2: " + op_arithmetic_combined);

        // Relational operators
        boolean op_relational = 1 == 1;
        System.out.println("1 == 1: " + op_relational);
        op_relational = 1 != 1;
        System.out.println("1 != 1: " + op_relational);
        op_relational = 1 > 1;
        System.out.println("1 > 1: " + op_relational);
        op_relational = 1 < 1;
        System.out.println("1 < 1: " + op_relational);
        op_relational = 1 >= 1;
        System.out.println("1 >= 1: " + op_relational);
        op_relational = 1 <= 1;
        System.out.println("1 <= 1: " + op_relational);

        // Logical operators
        boolean op_logical = !(5==5);
        System.out.println("!(5==5): " + op_logical);
        op_logical = (5==5)|(5<4);
        System.out.println("(5==5)|(5<4): " + op_logical);
        op_logical = (5==5)^(5<4);
        System.out.println("(5==5)^(5<4): " + op_logical);
        op_logical = (5==5)&(5<4);
        System.out.println("(5==5)&(5<4): " + op_logical);
        op_logical = (5==5)||(5<4);
        System.out.println("(5==5)||(5<4): " + op_logical);
        op_logical = (5==5)&&(5<4);
        System.out.println("(5==5)&&(5<4): " + op_logical);

        // Conditional operator
        int op_conditional = 5>4 ? 1 : 0;
        System.out.println("5>4 ? 1 : 0: " + op_conditional);

        // Bitwise operators
        int op_bitwise = ~11;
        System.out.println("~11: " + op_bitwise);
        op_bitwise = 11|12;
        System.out.println("11|12: " + op_bitwise);
        op_bitwise = 11^12;
        System.out.println("11^12: " + op_bitwise);
        op_bitwise = 11<<12;
        System.out.println("11<<12: " + op_bitwise);
        op_bitwise = 11>>12;
        System.out.println("11>>12: " + op_bitwise);
        op_bitwise = 11>>>12;
        System.out.println("11>>>12: " + op_bitwise);

        // Concat operators
        String op_concat = "Hello " + "World!";

        // If, else, else if
        if (1==1) {
            System.out.println("1==1");
        } else if (1==2) {
            System.out.println("1==2");
        } else {
            System.out.println("1!=1");
        }

        // Ternary operator
        String op_ternary = 1==1 ? "1==1" : "1!=1";
        System.out.println("1==1 ? \"1==1\" : \"1!=1\": " + op_ternary);

        // Switch
        switch (1) {
            case 1:
                System.out.println("1");
                break;
            case 2:
                System.out.println("2");
                break;
            default:
                System.out.println("default");
                break;
        }

        // Loops
        for (int i=0;i<1;i++) {
            System.out.println("for: " + i);
        }
        int i = 0;
        while (i<1) {
            System.out.println("while: " + i);
            i++;
        }
        i = 0;
        do {
            System.out.println("do while: " + i);
            i++;
        } while (i<1);
        int [] numbers  = {1,2,3,4,5};
        for (int j:numbers){
            System.out.println("for each: " + j);
        }

        // Break and continue
        for (int j=0;j<5;j++) {
            if (j==2) {
                break;
            }
            System.out.println("break: " + j);
        }
        for (int j=0;j<5;j++) {
            if (j==2) {
                continue;
            }
            System.out.println("continue: " + j);
        }

        // Extra dificult
        for (int j=10;j<56;j++) {
            if(j%2 == 0 && j!=16 && j%3 != 0){
                System.out.println("Extra dificult: " + j);
            }
        }

    }
}
