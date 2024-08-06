public class Qv1ko {

    public static int a = 3;
    
    public static void main(String[] args) {
        
        function1();

        System.out.println(function2());

        function3(a, "\nParameterized and non-return function:\nGlobal variable A: ");

        System.out.println(function4(4, "\nFunction with return and with parameters:\nGlobal variable A: "));

        System.out.println("\nProgram:\n");
        System.out.println("\nNumber of times a text was not printed: " + program("zip", "zap"));

    }

    private static void function1() {
        int b = 4;
        System.out.println("\nFunction without return and without parameters:\nGlobal variable A: " + a + "\nLocal variable B: " + b);
    }

    private static String function2() {
        return "\nFunction with return and without parameters:\nGlobal variable A: " + a;
    }

    private static void function3(int num, String str) {
        System.out.println(str + num);
    }

    private static String function4(int num, String str) {
        return str + a + "\n" + num +" to the power of " + a + " = " + (int)Math.pow(num, a);
    }

    private static int program(String zip, String zap) {

        int count = 0;

        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(zip + zap);
            } else if (i % 3 == 0) {
                System.out.println(zip);
            } else if (i % 5 == 0) {
                System.out.println(zap);
            } else {
                count++;
            }
        }

        return count;

    }
    
}
