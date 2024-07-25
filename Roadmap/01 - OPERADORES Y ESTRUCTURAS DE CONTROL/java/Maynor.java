public class Maynor {

    public static void main(String[] args) {
        //operadores aritmeticas
        /*
        plus "+"
        subtraction "-"
        multiplication "*"
        division "/"
        rest "%"
         */

        int plus = 10 + 10; //20
        int subtract = 10 - 5; // 5
        int div = 6 / 2; // 3
        int mul = 6 * 2; // 12
        int mod = 6 % 2; // 0

        System.out.println(plus + subtract + div + mul + mod);

        /*
            OPERATIONS LOGICS
            return true if both operations are true '&&'
            return true if some of the operations are true '||'
            negates the operand that is passed to it '!'
         */

        boolean and = plus > subtract && subtract == 5;
        if(and){
            System.out.println("esto es correcto " + and);
        }

        boolean or = plus < subtract || subtract == 0;
        if(or){
            System.out.println("una de las condiciones se cumple " + or);
        }

        if (!or){
            System.out.println("una de las condiciones se cumple pero la estamos negando " + and);
        }

        /*
            OPERATIONS relational
            Greater than '>'
            Less than '<'
            Equals '=='
            Distinct '!='
            Greater than or equal to '>='
            Less than or equal to '<='
         */

        boolean Greater = 10 > 5;
        System.out.println(Greater);

        boolean less = 10 < 5;
        System.out.println(less);

        boolean equals = 10 == 5;
        System.out.println(equals);

        boolean notEquals = 10 != 10;
        System.out.println(notEquals);

        boolean greaterOrEquals = 10 >= 5;
        System.out.println(greaterOrEquals);

        boolean lessOrEquals = 10 <= 5;
        System.out.println(lessOrEquals);

        /*
            COMPARISON

            instanceof:
            verify if an object is an instance of a
            class specific or of a subclass
         */

        String hola = "hola";
        boolean isInstanceofClass = Object.class.isInstance(hola);

        /*
            ASSIGNATION or pertinence

            assignation simple '='
            assignation plus '+='
            assignation subtract '-='
            assignation multiplication '*='
            assignation division '/='
            assignation mod '%='
         */

        int simple = 5;
        System.out.println("assign 5 by the variable" + simple);

        plus += 1;
        System.out.println("assign or add 1 " + plus);

        subtract -= 1;
        System.out.println("subtract 1 " + subtract);

        div /= 2;
        System.out.println("div 2 " + div);

        mul *= 2;
        System.out.println("mul 2 " + mul);

        mod %= 2;
        System.out.println("mod 2 " + mod);

        /*
            For bits

            AND bit by bit '&'
            OR bit by bit '|'
            XOR bit by bit '^'
         */

        int a = 5; // 5 in binary is 0101
        int b = 3; // 3 in binary is 0011

        int result = a & b; // 0101 & 0011 = 0001 (1 in decimal)
        System.out.println("Resultado: " + result); //return 1

        int result2 = a | b; // 0101 | 0011 = 0111 ( 7 in decimal)
        System.out.println("Resultado2: " + result2); // return 7

        int result3 = a ^ b; // 0101 ^ 0011 = 0110 (6 in decimal)
        System.out.println("Result3: " + result3); // return 6

        // STRUCTURES OF CONTROL
        // CONDICIONALES

        // if, else

        if (10 < 50){
            System.out.println("if the expression is true return this ");
        }else {
            System.out.println("else if the expression is false return this ");
        }

        //switch

        int option = 2;

        switch (option){
            case 1:
                System.out.println("if the variable is equal of 1 print this");
                break;
                case 2:
                    System.out.println("if the variable is equal of 2 print this");
                    break;
                    case 3:
                        System.out.println("if the variable is equal of 3 print this");
                        break; // This makes the option 3 no longer try to execute what is below
            default:
                System.out.println("does not have a valid option");

        }

        //REPETITIVE
        // while

        int x = 5;
        while (x < 6){
            System.out.println("while the condition meets does this" + x);
        }

        //do while

        do {
            System.out.println("while the condition meets does this" + x);
        }while (x != 5);

        // for

        for (int i = 0; i < 10; i++){
            System.out.println("when the condition is met this will stop");
        }

        //EXTRA
        for (int i = 10; i <= 55; i++){
            if ( i != 16 && i % 3 != 0){
                System.out.println(i);
            }
        }

    }

}
