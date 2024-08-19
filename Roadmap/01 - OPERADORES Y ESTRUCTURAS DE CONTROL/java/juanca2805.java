public class juanca2805 {

    public static void main(String[] args) {
        /*
         Operadores logicos
         */
        int Numero1 = 5;
        int Numero2 = 7;

        // operadores  arigmeticos usados con variables y sin variables
        System.out.println( "LA SUMA DEl " + Numero1 + " + "  + Numero2 + " es");
        System.out.println(Numero1 + Numero2);
        System.out.println("LA Resta DEl " + Numero1 + " + "  + Numero2 + " es");
        System.out.println(Numero1 - Numero2);
        System.out.println(20 / 3);
        System.out.println(20 * 3);
        System.out.println(20 % 10);

        //Operaciones de comparacion
        System.out.println(20 == 10);
        System.out.println(20 != 10);
        System.out.println(Numero1 > Numero2);
        System.out.println(Numero1 >= Numero2);

        //operadores logicos
        boolean a;
        boolean b;

        a = false;
        b = true;
        // Operador AND
        System.out.println("AND(&&): " + (a && b));
        // Operador OR
        a = true;
        b = false;
        System.out.println("OR(||): " + (a || b));
        // Operador NOT
        System.out.println("NOT(!): " + (!b));
      
        //operador ternario 
        int edad = 18;
        String mensaje = (edad >= 18) ? "Eres mayor de edad" : "Eres menor de edad";
        System.out.println(mensaje);

         //operadores de asignacion
    Numero1 += 10;
    System.out.println(Numero1);
        //OPERADOR DE BITS 
          System.out.println("Operadores de bits -------------------------------");

        int cinco = 5;                      // 0101 en binario
        int tres =3;                        // 0011 en binario
        
        int bitAnd = cinco & tres;          // 0001 (1) Operación lógica AND 
        System.out.println(bitAnd);
        int bitOr = cinco | tres;           // 0111 (7) Operción lógica OR  

        System.out.println(bitOr);
        int bitXor = cinco ^ tres;          // 0110 (6) Operación OR exclusiva 
        System.out.println(bitXor);

        /*Estructuras de control
         * 
         * Condicionales
         * 
         * 
        */

    String Nombre = "camilo";

    if (Nombre == "camilo") {
        System.out.println("Pase señor " + Nombre );
    }
    if (Nombre == "pepe") {
        System.out.println("usted no es bienvenido señor " + Nombre );
    } 
    else{
        System.out.println("Usted no es el señor " + Nombre);
    }
    
    // Iterativos

    for(int i = 1; i <= 10 ; i++){
        System.out.print(" "+ i );
    };
    
    extra();


    /* * DIFICULTAD EXTRA (opcional):
     Crea un programa que imprima por consola todos los números comprendidos
      entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
     */
    
    

    }
    public static void extra() {
        for(int i = 10; i < 56; i++) {
            if((i != 16) && (i % 3 != 0) && (i % 2 == 0)) {
                System.out.println(i);
            }
        }
    }

    
    

    }

   


