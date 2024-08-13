public class simonguzman {
    public static void main(String[] args){
     
        int number1 = 10;
        int number2 = 2;
        int i = 3;
        int result = +1;
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
        


    }
}
