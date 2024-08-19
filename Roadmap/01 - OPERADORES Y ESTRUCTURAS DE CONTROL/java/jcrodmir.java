
public class Main {
    public static void main(String[] args) {
        //Assignment

        System.out.println("***** Simple Assigment Operatos/Einfacher Zuweisungsoperator ***** \n");
        int speed=50;
        speed +=5; //55
        System.out.println(speed);
        speed -=5; //50
        System.out.println(speed);
        speed *=3; //150
        System.out.println(speed);
        speed /=3; //50
        System.out.println(speed);
        speed %= 4; // 0 modulo
        System.out.println(speed + "\n");

        //Bits

        int comparation1= 5;
        int comparation2=3;
        System.out.println("***** Bits Assigment Operatos /Bits-Zuweisungsoperator***** \n");
        comparation1 &= comparation2;//AND Binary operation 0101 and 0011 is equals 0001 ->1
        System.out.println(comparation1);
        comparation1 ^= comparation2; //XOR Binary operation 0001 ,0011 is equals 0010 -> 2
        System.out.println(comparation1);
        comparation1 |= comparation2; //OR Binary operation 0010 ,0011 is equals 0011 -> 3
        System.out.println(comparation1);
        comparation1 <<= 1; //move left with sign  Binary operation 0011 ,1 is equals 0110 -> 6
        System.out.println(comparation1);
        comparation1 >>= 1; //move right with sign Binary operation 0110 ,1 is equals 0011 -> 3
        System.out.println(comparation1);
        comparation1 >>>= 1; //move right without sign change the last 1  for a 0 Binary operation 0011 ,1 is equals 0001 -> 1
        System.out.println(comparation1 + "\n");

        //Arithmetic
        int number1=8;
        int number2=2;
        int result=0;
        System.out.println("***** Aritmetics Operatos/Aritmetischer Operatoren\n ****\n");
        result= number1 + number2;
        System.out.println(result);
        result= number1 - number2;
        System.out.println(result);
        result= number1 * number2;
        System.out.println(result);
        result= number1 / number2;
        System.out.println(result);
        result= number1 % number2;
        System.out.println(result);
        result= number1 + number2;
        System.out.println(result + "\n");

        //Unary
        int unary=8;
        System.out.println("***** Unary Operator/\n" +
                "Unärer Operatoren ****\n");
        System.out.println(++unary);//plus one
        System.out.println(--unary);//minus one
        System.out.println(-unary);//transform negative number
        System.out.println(+unary);//transform positive number
        System.out.println(~unary);//transform all binary numbers 1 <-> 0 in 32 bits for that 8 is -9
        System.out.println(!(unary==8) + "\n");//only with boolean you became the opposite
        //Equality
        System.out.println("***** Equality Operatos/Gleichheitsoperatoren ****\n");
        int equal1=1;
        int equal2=2;
        System.out.println(equal1==equal2);//False
        System.out.println(equal1!=equal2);//True
        System.out.println(equal1>equal2);//False
        System.out.println(equal1<equal2);//True
        System.out.println(equal1>=equal2);//False
        System.out.println(equal1<=equal2);//True
        //Conditional
        System.out.println("***** Conditional Operatos/\n" +
                "Bedingte Operatoren ****\n");
        System.out.println(equal1!=equal2&&equal1<=equal2);//True
        System.out.println(equal1>equal2||equal1!=equal2);//True
        System.out.println("\n");

        //Conditionals statements
        System.out.println("***** Conditional Statements/\n" +
                "Bedingte Anweisungen ****\n");
        System.out.println("***** IF ****\n");
        // IF
        if(5 > 3){
            System.out.println("5 is more than 3");
        }
        //IF-ELSE
        System.out.println("***** IF-ELSE ****\n");
        System.out.println("\n");
        if(5 < 3){
            System.out.println("5 es mayor que 3");
        }
        else {
            System.out.println("5 is more than 3");
        }
        System.out.println("\n");
        //SWITCH
        System.out.println("***** SWITCH ****\n");
        int day= 5;
        switch (day){
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
            case 6:
                System.out.println("Saturday");
                break;
            case 7:
                System.out.println("Sunday");
                break;
            default:
                System.out.println("Invalid day");
                break;
        }
        //Loop statements
        System.out.println("\n");
        System.out.println("***** Loop statements/Schleifen Anweisungen ****\n");
        //WHILE
        System.out.println("\n");
        System.out.println("***** WHILE ****\n");
        int count=1;
        while(count < 5) {
            System.out.println("Count from while: " + count);
            count++;
        }
        //DO-WHILE, executed once at least
        System.out.println("\n");
        System.out.println("***** DO-WHILE ****\n");
        int count2=11;
        do {
            System.out.println("Count from do while: " + count2);
            count2 --;
        }while (count2 > 1 && count2 < 11);

        //FOR
        System.out.println("\n");
        System.out.println("***** FOR ****\n");
        for (int i = 0; i < 5; i++) {
            System.out.println("Count from for:" + i );
        }
        System.out.println("\n");
        System.out.println("***** FOR EACH ****\n");
        int[] arrayNumbers ={1,2,3,4,5,6};
        for(int item:arrayNumbers){
            System.out.println("Count from Array " + item);
        }

        //FOR EACH
        //Jump statements
        System.out.println("\n");
        System.out.println("***** JUMPS STATEMENTS/SPRÜNGE ANWEISUNGEN ****\n");
        //break
        System.out.println("***** BREAK ****\n");
        for(int item:arrayNumbers){
            if(item == 3){
                break;//break the for statements
            }
            System.out.println("Count from break " + item);
        }
        //continue
        System.out.println("\n");
        System.out.println("***** CONTINUE ****\n");
        for(int item:arrayNumbers){
            if(item == 3){
                continue;//continue the for statements but not print "3"
            }
            System.out.println("Count from continue " + item);
        }
        System.out.println("\n");

        //Exceptions
        System.out.println("***** EXCEPTIONS ****\n");
        try {
            System.out.println("Number of array" + arrayNumbers[10]);
        }catch (IndexOutOfBoundsException e){
            System.out.println(e.getMessage());
        }

        //EXTRA
        System.out.println("\n Extra Exercise ");
        for(int i=10 ; i<=55;i++){
            if(i % 2 ==0 && i!=16 && i % 3 !=0){
                System.out.println("Number " + i);
            }
        }
    }
}