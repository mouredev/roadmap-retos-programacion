import java.util.List;

public class simonguzman {
    public static void main(String[] args){
     
        int number1 = 10;
        int number2 = 2;
        int i = 3;
        int result = +1;
        int bitMask = 0x000F;
        int val = 0x2222;
        String firstString = "This is";
        String secondString = " a concatenated string.";
        String thirdString = firstString + secondString;

        //Aritmetics operators
        System.out.println("10 + 2 = "+ (number1 + number2));
        System.out.println("10 - 2 = "+ (number1 - number2));
        System.out.println("10 * 2 = "+ (number1 * number2));
        System.out.println("10 % 2 = "+ (number1 % number2));
        System.out.println("10 / 2 = "+ (number1 / number2));
        System.out.println("firstString + secondString = "+thirdString);

        //Unary operators
        //Result is 1
        System.out.println(result);
        result--;
        //Result is 0
        result++;
        //Result is 1
        System.out.println(result);
        result = -result;
        //Result is -1
        System.out.println(result);

        boolean success = false;
        //false
        System.out.println(success);
        //true
        System.out.println(!success);
        i++;
        // prints 4
        System.out.println(i);
        ++i;
        // prints 5
        System.out.println(i);
        // prints 6
        System.out.println(++i);
        // prints 6
        System.out.println(i++);
        // prints 7
        System.out.println(i);

        //Equality and relational operators
        boolean equal = number1 == number2;
        System.out.println("The equaly is: "+ equal);
        boolean notEqual = number1 != number2;
        System.out.println("the not equaly is: "+ notEqual);
        boolean greaterThan = number1 > number2;
        System.out.println("the greater than is: "+ greaterThan);
        boolean greaterThanOrEqual = number1 >= number2;
        System.out.println("The greater than or equal is: "+ greaterThanOrEqual);
        boolean lessThan = number1 < number2;
        System.out.println("The less than is: "+ lessThan);
        boolean lessThanOrEqual = number1 <= number2;
        System.out.println("The less than or equal is: "+ lessThanOrEqual);

        //Conditional operators
        boolean ConditionalAnd = number1 == 10 && number2 == 2;
        System.out.println(ConditionalAnd);
        boolean ConditionalOr = number1 == 9 || number2 ==2;
        System.out.println(ConditionalOr);
        boolean ConditionalNot = !ConditionalOr;
        System.out.println(ConditionalNot);

        //Bitwise and Bit Shift operators
        // print 2
        System.out.println(val & bitMask);


        //Control structures
        //if

        int testScore = 76;
        if(testScore >= 70){
            System.out.println("Aproved test score");
        }

        //ifelse
        if(testScore >= 70){
        System.out.println("Aproved test score");
        }else{
            System.out.println("Disaproved test");
        }

        //ifelseif
        char grade;
        if (testScore >= 90){
            grade = 'A';
        }else if (testScore >= 80){
            grade = 'B';
        }else if (testScore >= 70){
            grade = 'C';
        }else if (testScore >= 60){
            grade = 'D';
        }else{
            grade = 'F';
        }
        System.out.println("Grade of the test is: " + grade);
       
        //While
        int count = 1;
        while(count < 11){
            System.out.println("Number: "+count);
            count++;
        }

        //DoWhile
        int count2 = 1;
        do{
            System.out.println("Count is: "+count2);
            count2++; 
        }while(count2 < 11);

        //For
        for (int j = 0; j < 11; j++){
            System.out.println("Count is: "+j);
        }

        //Alternatives to for
        int[] numbers =
             {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
         for (int item : numbers) {
             System.out.println("Count is: " + item);
         }

         //For each
         List<String> names = List.of("Jack", "Paula", "Kate", "Peter");
         for(String name:names){
            System.out.println(name);
         }

         //Switch
         int month = 8;
         String futureMonths;
         switch (month) {
            case 0: System.out.println("January"); break;
            case 1: System.out.println("February"); break;
            case 2: System.out.println("March"); break;
            case 3: System.out.println("April"); break;
            case 4: System.out.println("May"); break;
            case 5: System.out.println("June"); break;
            case 6: System.out.println("July"); break;
            case 7: System.out.println("August"); break;
            case 8: System.out.println("September"); break;
            case 9: System.out.println("October"); break;
            case 10: System.out.println("November"); break;
            case 11: System.out.println("December"); break;
            default:
            System.out.println("Invalid month");
                break;
         }


         /*Ejercicio practico
          * Crea un programa que imprima por consola todos los números comprendidos
          * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
         */

         for (int n = 10; n < 56; n++){
            if( ((n % 2) == 0 ) && (n != 16) && (n % 3 != 0)){
                System.out.println(n);
            }
         }
    }

}
