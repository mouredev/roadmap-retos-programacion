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

        testExtra();
        
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

/* DIFICULTAD EXTRA (opcional):
 */

        class myCustomException extends Exception {
        public myCustomException(String errorMessage) {
            super(errorMessage);
        }
    }

    private boolean isVocal(char c){
        return c == 'a' ||c == 'e' ||c == 'i' ||c == 'o' ||c == 'u';
    }

    private char exceptionsFunction(String s, int num) throws Exception {
    

        if(s.isEmpty()){
            throw new myCustomException("The string must be not empty");
        }
        char c =  s.charAt(num);
        if(isVocal(c)){
            throw new Exception("Odio las vocales!!");
        }
        return s.charAt(num);
    }

    private void testExtra() {
        System.out.println(" \n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n");

        String[] strings = {"","patata", "carcamusa", "ascapatipucyuelaimepipedo", "choripan"};
        int[] indexes = {2,-1,20, 11, 2};
        int errorCount = 0;

        for (int i = 0; i < strings.length; i++) {
            try {
                System.out.println("Word: " + strings[i] + " - Index: "+ indexes[i] + " - CharAt: "+exceptionsFunction(strings[i], indexes[i]));
            }
            catch (myCustomException e){
                System.err.println(RED +"ERROR - MY CUSTOM EXCEPTION: "+ ANSI_RESET + e);
                errorCount++;
            } 
            catch (StringIndexOutOfBoundsException e){
                System.err.println(RED +"ERROR - NOS HEMOS SALIDO :(: "+ ANSI_RESET + e);
                errorCount++;
            } 
            catch (Exception e) {
                System.err.println(RED +"ERROR - OTRAS: "+ ANSI_RESET + e);
                errorCount++;
            }
        }
        System.out.println("Ejecución terminada. Se han producido (y recuperado) "+errorCount+" errores");
    }
}
