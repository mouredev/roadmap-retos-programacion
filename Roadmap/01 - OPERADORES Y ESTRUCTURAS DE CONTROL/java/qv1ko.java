class Qv1ko {

    public static void main(String[] args) {

        double a = 3;
        double b = 4;

        System.out.println("Number A: " + a);
        System.out.println("Number B: " + b);

        double sum = a + b;
        System.out.println("a + b = " + sum);

        double sub = a - b;
        System.out.println("a - b = " + sub);

        double mul = a * b;
        System.out.println("a * b = " + mul);

        double div = a / b;
        System.out.println("a / b = " + div);

        double res = a % b;
        System.out.println("a % b = " + res);

        a += b;
        System.out.println("a += b\t Number A: " + a);

        a -= b;
        System.out.println("a -= b\t Number A: " + a);

        a *= b;
        System.out.println("a *= b\t Number A: " + a);

        a /= b;
        System.out.println("a /= b\t Number A: " + a);

        a %= b;
        System.out.println("a %= b\t Number A: " + a);

        a++;
        System.out.println("a++\t Number A: " + a);

        b--;
        System.out.println("b--\t Number B: " + b);

        if (a == b) {
            System.out.println("Number A equals number B");
        }

        if (a == b) {
            System.out.println("Number A equals number B");
        } else {
            System.out.println("The number A is not equal to the number B");
        }

        System.out.println((a != b) ? "The number A is different from the number B" : "The number A is not different from the number B");

        if (a > b) {
            System.out.println("The number A is greater than the number B");
        } else if (a < b) {
            System.out.println("The number A is less than the number B");
        } else {
            System.out.println("Number A equals number B");
        }

        while (a > 0 && b > 0) {
            System.out.println("Loop while");
            a--;
        }

        do {
            System.out.println("Loop do while");
            a++;
            b++;
        } while (a < 3 || b < 0);

        switch ((int)b) {
            case 1:
                System.out.println("Number B is 1");
                break;

            case 2:
                System.out.println("Number B is 2");
                break;

            case 3:
                System.out.println("Number B is 3");
                break;

            case 4:
                System.out.println("Number B is 4");
                break;

            case 5:
                System.out.println("Number B is 5");
                break;
        
            default:
                break;

        }

        for (int i = 1; i <= 3; i++) {
            System.out.println("Loop for " + i);
        }

        for (Integer num : new int[]{1, 2, 3}) {
            System.out.println("Loop for each " + num);
        }

        try {
            double z[] = new double[2]; 
            z[4] = a;
        } catch (Exception e) {
            System.out.println("Exception caught");
        }

        program();

    }

    private static void program() {
        System.out.println("\nProgram:\n");
        for (int i = 10; i <= 55; i++) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.println(i);
            }
        }
    }

}
