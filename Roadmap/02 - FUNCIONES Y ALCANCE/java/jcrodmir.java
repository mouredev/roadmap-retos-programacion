public class Main {
    static int globalVariable=2;

    public static void main(String[] args) {

        //Not parameters, not return/kein Parameter keine Rückgabe
        initialMessage();
        //Parameters, not return/Parameter keine Rückgabe
        numberChallenge(globalVariable);

        //Not parameters, with return/kein Parameter mit Rückgabe
        System.out.println(stringReturn());
        //Parameters with return /  Parameter mit Rückgabe
        System.out.println("4 + 5 is: " + plusOperation(4,5));

        //Example of function that is too created./Beispiel für eine Funktion, die zu viel erstellt wurde.
        System.out.println("The maximum is 8 not 5: " + Math.max(5,8));

        System.out.println(oneToHunderd("Hello","Everyone"));
    }
    public static void initialMessage(){
        //local variable/lokale Variabel.
        int localVariable=2;
        System.out.println("Welcome to the MoureDev RoadMap challenge" + localVariable);
    }
    public static void numberChallenge (int number){
        System.out.println("Challenge number: " + number);
    }
    public static String stringReturn (){
        return "This is a return Message";
    }
    public static int plusOperation (int a, int b){
        //It´s  possible create function inside function in Java but only inside a new class
        //Es ist möglich, eine Funktion innerhalb einer Funktion in Java zu erstellen, aber nur innerhalb einer neuen Klasse

        class NewClass{
            public  void functionInsideFunction(){
                System.out.println("You can create a function inside a other function only with a new Class");
            }
        }
        NewClass newClass= new NewClass();
        newClass.functionInsideFunction();
        return a + b;
    }


    //EXTRA
    public static int oneToHunderd (String a, String b){
        int count=0;
        for (int i = 0; i < 101; i++) {
            System.out.print(i+": ");
            if(i%5==0 && i%3==0){
                System.out.println(a+" "+b);
            } else if (i%5==0) {
                System.out.println(b);
            } else if (i%3==0) {
                System.out.println(a);
            }
            else{
                count++;
                System.out.print("\n");
            }

        }
        return count;
    }


}