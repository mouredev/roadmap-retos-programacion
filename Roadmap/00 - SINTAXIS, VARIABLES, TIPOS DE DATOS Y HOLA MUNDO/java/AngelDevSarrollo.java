public class AngelDev {
    public static void main(String[] args) {

        // caracteres
        char caracter = '\u0040';
        char decimal = 64;
        System.out.println("caracter = " + caracter);
        System.out.println("decimal = " + decimal);
        System.out.println("decimal = caracter: " + (decimal == caracter));

        char simbolo = '@';
        System.out.println("simbolo = " + simbolo);
        System.out.println("simbolo = caracter: " + (simbolo == caracter));

        char espacio = '\u0020';
        char retroceso = '\b';
        char tabulador = '\t';
        char nuevaLinea = '\n';
        char retornoCarro = '\r';

        System.out.println("char corresponde en byte:" + System.lineSeparator() + Character.BYTES);
        System.out.println("Char corresponde en bites = " + Character.SIZE);
        System.out.println("Character.MIN_VALUE = " + Character.MIN_VALUE);
        System.out.println("Character.MAX_VALUE = " + Character.MAX_VALUE);


        // Enteros y flotantes
        byte numeroByte = 127;
        System.out.println("numeroByte = " + numeroByte);
        System.out.println("tipo byte corresponde en byte a " + Byte.BYTES);
        System.out.println("tipo byte corresponde en bites a " + Byte.SIZE);
        System.out.println("valor máximo de un byte: " + Byte.MAX_VALUE);
        System.out.println("valor mínimo de un byte: " + Byte.MIN_VALUE);

        short numeroShort = 32767;
        System.out.println("numeroShort = " + numeroShort);
        System.out.println("tipo short corresponde en byte a " + Short.BYTES);
        System.out.println("tipo short corresponde en bites a " + Short.SIZE);
        System.out.println("valor máximo de un short: " + Short.MAX_VALUE);
        System.out.println("valor mínimo de un short: " + Short.MIN_VALUE);

        int numeroInt = 2147483647;
        System.out.println("numeroInt = " + numeroInt);

        System.out.println("tipo int corresponde en byte a " + Integer.BYTES);
        System.out.println("tipo int corresponde en bites a " + Integer.SIZE);
        System.out.println("valor máximo de un int: " + Integer.MAX_VALUE);
        System.out.println("valor mínimo de un int: " + Integer.MIN_VALUE);

        long numeroLong = 9223372036854775807L;
        System.out.println("numeroLong = " + numeroLong);

        System.out.println("tipo long corresponde en byte a " + Long.BYTES);
        System.out.println("tipo long corresponde en bites a " + Long.SIZE);
        System.out.println("valor máximo de un long: " + Long.MAX_VALUE);
        System.out.println("valor mínimo de un long: " + Long.MIN_VALUE);

        var numeroVar = 9223372036854775808f;


        // boleanos
        boolean datoLogico = true;
        System.out.println("datoLogico = " + datoLogico);

        double d = 98765.43e-3; // 98.76543
        System.out.println("d = " + d);

        float f = 1.2345e2f; // 123.45
        System.out.println("f = " + f);

        datoLogico = d < f;
        System.out.println("datoLogico = " + datoLogico);

        boolean esIgual = (3-2 == 1);
        System.out.println("esIgual = " + esIgual);

        String nombre = "AngelDev";


    }
}
