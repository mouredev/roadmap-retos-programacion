public class Qv1ko {

    public static void main(String[] args) {
        
        int a = 3, b = 4;
        Reference x = new Reference(5), y = new Reference(6);

        int newA = program1(a, b);
        Reference newX = program2(x, y);

        System.out.println("A value: " + a);
        System.out.println("X value: " + x.getNum());
        System.out.println("New A value: " + newA);
        System.out.println("New X value: " + newX.getNum());

    }

    private static int program1(int a, int b) {

        int temp = a;

        a = b;
        b = temp;

        return a;

    }

    private static Reference program2(Reference x, Reference y) {

        Reference temp = x;

        x = y;
        y = temp;

        return x;

    }

}

class Reference {

    int num;

    Reference(int num) {
        this.num = num;
    }

    public int getNum() {
        return num;
    }

}
