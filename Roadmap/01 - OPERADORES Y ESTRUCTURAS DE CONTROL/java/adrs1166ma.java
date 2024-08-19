public class adrs1166ma {
    public static void main(String[] args) {
        // Operando1 = a
        // Operando2 = b
        // Respuesta = r
        int a = 5, b = 3, r = 0;
        System.out.println("Numero 1: "+a+" |  Numero 2:"+b);

        // ----------------------------------------------
        System.out.println("/* -- Aritmeticos -- */");
        System.out.println("Suma: "+(a+b));
        System.out.println("Resta: "+(a-b));
        System.out.println("Multiplicacion: "+(a*b));
        System.out.println("Division: "+(a/b));
        System.out.println("Residuo: "+(a%b));

        // ----------------------------------------------
        System.out.println("/* -- Logicos -- */");
        boolean t = true;
        boolean f = false;
        System.out.println(" -- Y [AND] -- ");
        System.out.println("false && false = " + (f && f));
        System.out.println("false && true  = " + (f && t));
        System.out.println("true  && false = " + (t && f));
        System.out.println("true  && true  = " + (t && t));

        System.out.println(" -- O  [OR] -- ");
        System.out.println("false || false = " + (f || f));
        System.out.println("false || true  = " + (f || t));
        System.out.println("true  || false = " + (t || f));
        System.out.println("true  || true  = " + (t || t));

        System.out.println(" -- Negacion [NOT] -- ");
        System.out.println("!true  = " + (!t));
        System.out.println("!false = " + (!f));

        // ----------------------------------------------
        System.out.println("/* -- Comparacion -- */");
        System.out.println("a == b = " + (a == b));
        System.out.println("a != b = " + (a != b));
        System.out.println("a > b = " + (a > b));
        System.out.println("a < b = " + (a < b));
        System.out.println("a >= b = " + (a >= b));
        System.out.println("a <= b = " + (a <= b));


        // ----------------------------------------------
        System.out.println(" -- Asignacion -- ");
        System.out.println("Asignación: " + (a = b));
        System.out.println("Suma y asignación: " + (a += b));
        System.out.println("Resta y asignación: " + (a -= b));
        System.out.println("Multiplicación y asignación: " + (a *= b));
        System.out.println("División y asignación: " + (a /= b));
        System.out.println("Resto y asignación: " + (a %= b));
        System.out.println("AND y asignación: " + (a &= b));
        System.out.println("OR y asignación: " + (a |= b));
        System.out.println("XOR y asignación: " + (a ^= b));
        System.out.println("Desplazamiento a la izquierda y asignación: " + (a <<= b));
        System.out.println("Desplazamiento a la derecha y asignación: " + (a >>= b));
        System.out.println("Desplazamiento a la derecha sin signo y asignación: " + (a >>>= b));

        // ----------------------------------------------

        /* NO IDENTIDAD  |  NO PERTENCIA */

        // ----------------------------------------------

        System.out.println(" -- Bits -- ");
        System.out.println("5 & 2 = " + (a & b));
        System.out.println("5 | 2 = " + (a | b));
        System.out.println("5 ^ 2 = " + (a ^ b));
        System.out.println("~5 = " + (~a));
        System.out.println("5 << 2 = " + (a << 2));
        System.out.println("5 >> 2 = " + (a >> 2));
        System.out.println("5 >>> 2 = " + (a >>> 2));

        // ----------------------------------------------

        /*
         * Estructuras de control
         */

        System.out.println(" -- Ternarios -- ");
        int mayorEdad = 18;
        String msg = mayorEdad >= 18 ? "Eres mayor de edad" : "Eres menor de Edad";
        System.out.println(msg);

        System.out.println(" -- if | else -- ");
        boolean miCondicion = false;
        if (miCondicion == true) {
            System.out.println(" Mi condición es verdadera ");
        } else if (miCondicion == false) {
            System.out.println(" Mi condicion es reconocida ");
        } else {
            System.out.println(" Mi condicion es reconocida ");
        }

        System.out.println(" -- for -- ");
        for (int i = 0; i < 10; i++){
            System.out.println("i = "+i);
        }

        int i = 0;
        System.out.println(" -- while -- ");
        while (i < 10){
            System.out.println("i = "+i);
            i++;
        }

        System.out.println(" -- do while -- ");
        do {
            System.out.println("i = "+i);
            i++;
        } while (i < 5);

        System.out.println(" -- switch -- ");
        switch (a) {
            case 1:
                System.out.println("a es 1");
                break;
            case 2:
                System.out.println("a es 2");
                break;
            case 3:
                System.out.println("a es 3");
                break;
            default:
                System.out.println("a no es 1, 2 o 3");
                break;
        }

        System.out.println(" -- break -- ");
        for (int j=0;j<5;j++){
            if (j==3){
                break;
            }
            System.out.println("j = "+j);
        }

        System.out.println(" -- continue -- ");
        for (int j=0;j<5;j++){
            if (j==3){
                continue;
            }
            System.out.println("j = "+j);
        }

        try {
            int resultado = a/0;
            System.out.println("Resultado: "+resultado);
        } catch (ArithmeticException e){
            System.out.println("Error: Division por cero");
        }

        /*
        * Extra
        */

        for (int x=10;x<=55;x++){
            if (x==16){
                continue;
            } else if ((x%3)==0) {
                continue;
            } else {
                System.out.println(x);
            }
        }
    }
}
