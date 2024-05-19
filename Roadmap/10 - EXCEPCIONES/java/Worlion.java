import java.util.Arrays;
import java.util.List;

public class Worlion {
    

    public static final String GREEN = "\u001B[32m";
    public static final String RED = "\u001B[31m";
    public static final String RED_BACKGROUND = "\u001B[41m";
    public static final String ANSI_RESET = "\u001B[0m";

    public static void main(String[] args) {
        new Worlion().run();
    }

    public void run() {
        System.out.println("Resultado obtenido: "+div(7, 0));

        testArray();
        
    }
/*
 * EJERCICIO: Excepciones en Java
 */

    public int div(int a, int b) {
        System.out.println("\nDividimos "+a+" entre "+ b+":");
        int result = 0;
        try {
            result = a/b;
        } catch (ArithmeticException e) {
            System.err.println(RED +"ERROR:"+ ANSI_RESET+" You can not divide by 0");
        }
        return result;
    }

    public void testArray() {
        List<String> list = Arrays.asList(new String[]{"A", "B", "C"});
        System.out.println("\nRecorremos la lista "+list);
        try{
            for(int i = 0; i <= list.size(); i++) {
                System.out.println("Position: "+i+" - Value: "+list.get(i));
            }
        }
        catch (ArrayIndexOutOfBoundsException e) {
            System.err.println(RED +"ERROR:"+ ANSI_RESET + e);
        }
        System.out.println("Chimpun!");
    }

}
