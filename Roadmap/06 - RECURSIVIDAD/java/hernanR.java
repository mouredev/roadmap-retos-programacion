public class hernanR {
    public static void main(String[] args) {
        recursividad(100);
        System.out.println(factorial(5));
    }

    public static void recursividad(int num) {
        if (num >= 0) {
            System.out.println(num);
            recursividad(num - 1);
        }
    }

    public static int factorial(int num) {
        if (num == 0) {
            return 1;
        } else {
            return num * factorial(num - 1);
        }
    }
}
