
public class Javi {
    public static void main(String[] args) {
        // ----------------------------Sitio oficial Java------------------------------
        /*
         * "https://www.java.com/es/"
         */

        // ------------------sintaxis existentes para comentarios----------------------
        // Comentario en una linea
        /*
         * comentario en
         * varias líneas
         */

        // -------------------------variable y constante-------------------------------
        // Variable
        System.out.println("-Variable:");
        Object variable;
        variable = 10;
        System.out.println(variable);
        variable = "diez";
        System.out.println(variable);

        // Constante
        System.out.println("-Constante:");
        final Object constante = "valor inmutable";
        System.out.println(constante);

        // -----------------------------datos primitivos--------------------------------
        boolean verdadero = true, falso = false;
        char caracter = 97;
        byte Bminimo = -128, Bmaximo = 127;
        short Sminimo = -32768, Smaximo = 32767;
        int Iminimo = -2147483648, Imaximo = 2147483647;
        long Lminimo = -9223372036854775808L, Lmaximo = 9223372036854775807L;
        float Fminimo = -Float.MAX_VALUE, Fmaximo = Float.MAX_VALUE;
        double Dminimo = Double.MIN_VALUE, Dmaximo = Double.MAX_VALUE;
        System.out.println("¡Hola, Java!");
        System.out.println(Fminimo);
    }
}
