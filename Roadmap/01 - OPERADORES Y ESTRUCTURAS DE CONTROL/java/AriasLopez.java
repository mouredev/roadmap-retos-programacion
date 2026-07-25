public class AriasLopez01 {

    /**
     * @param args
     */
    public static void main(String[] args) {


        /*
         * OPERADORES ARITMETICOS
         */
        System.out.println("Esta es una suma, 5 + 2 = " + (5 + 2));
        System.out.println("Esta es una resta, 5 - 2 = " + (5 - 2));
        System.out.println("Esta es una multiplicacion, 5 * 2 = " + (5 * 2));
        System.out.println("Esta es una division, 5 / 2 = " + (5 / 2));
        System.out.println("Esto es un modulo, 5 % 2 = " + (5 % 2));
        
        // OPERADORES RELACIONALES

        System.out.println("5 IGUAL 10 = " + (5 == 10));
        System.out.println("5 DESIGUALDAD 10 = " + (5 != 10));
        System.out.println("5 MENOR QUE 10 = " + (5 < 10));
        System.out.println("5 MAYOR QUE 10 = " + (5 > 10));
        System.out.println("5 MAYOR O IGUAL QUE 10 = " + (5 >= 10));
        System.out.println("5 MENOR O IGUAL QUE 10 = " + (5 <= 10));
        System.out.println("10 MAYOR O IGUAL QUE 10 = " + (10 >= 10));

        // OPERADORES LOGICOS

        System.out.println("&& AND: 3 < 8 AND 5 < 7 (" + ((3 < 8) && (5 < 7)) + ")");
        System.out.println("&& AND: 3 <= 3 AND 5 == 7 (" + (3 <= 3  && 5 == 7) + ")");
        System.out.println("|| OR: 3 + 3 = 8 || 2 < 4 (" + (3 + 3 == 8 || 2 < 4) + ")");
        System.out.println("|| OR: 3 + 3 = 8 || 2 > 7 (" + (3 + 3 == 8 || 2 > 7) + ")");
        System.out.println("! NOT: 3 + 7 = 8 (" + !(3 + 7 == 8 ) + ")");
        System.out.println("! NOT: 3 < 8 (" + !(3 < 8 ) + ")");


        // OPERADORES DE ASIGNACION

        int numero1 = 10;
        System.out.println(numero1);

        numero1 += 2;
        System.out.println(numero1);

        numero1 -= 1;
        System.out.println(numero1);

        numero1 *= 10;
        System.out.println(numero1);
        
        numero1 %= 8;
        System.out.println(numero1);
        
        numero1 /= 2;
        System.out.println(numero1);

        numero1 ^= 10;
        System.out.println(numero1);


        /* 
         * ESTRUCTURAS DE CONTROL
         */
          
         int edad = 6;

        if (edad >= 18 ) {
            System.out.println("Es mayor de edad, puede viajar solo.");
        } else if (edad <=5) {
            System.out.println("Aun es un bebe, debe ir acompañado y no paga el pasaje.");  
        } else {
            System.out.println("El pasajero debe ir acompañado.");
        }



        for (int i = 0; i <= 18; i++){
            System.out.println(i);   
        }

        
        for (int i = 0; i <= 56; i++){
            if (i %2 == 0 && i != 16 && i %3 == 0 ) {
                System.out.println(i);
            } 
        }
    }

}
