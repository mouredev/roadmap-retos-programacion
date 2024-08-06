/**
 * Solución del reto #01 #01 OPERADORES Y ESTRUCTURAS DE CONTROL
 * 
 * @author rocha30
 */

public class rocha30 {

    
    public static void main(String[] args) {
        /*Operadores aritméicos: estos pueden ser aplicados sobre números enteros o decimales (float)
         * De estos hay dos tipos, que son los binarios y los unarios
        */

        //Operadores aritméticos binarios. 
        /*
         * Suma (+)
         * Resta (-)
         * Multiplicación (*)
         * División (/)
         * Módulo (%) (Valor absoluto |x|)
         */

         int a = 10; 
         int b = 3; 

         System.out.println("Operadores aritméticos en binario.");
         System.out.println("Suma: " + (a+b));
         System.out.println("Resta: "+ (a-b));
         System.out.println("Multiplicación: " + (a*b));
         System.out.println("División: " + (a/b));
         System.out.println("Modulo (valor absoluto): " + (a%b));

         System.out.println();

         /*
          * Operadores unarios: 
          * Mantiene el signo del operando (+)
          * Le cambia el signo del operando (-)
          * Autoincremento de valor (++)
          * Autodrcremento de valor (--)
          */

          System.out.println("\nOperadores unarios. ");
          System.out.println("Mantener el signo: " + (+b));
          System.out.println("Cambiar el signo : "+ (-b));
         System.out.println("Autoincremento : " + (++b));
         System.out.println("Autodecremento : " + (--b));
         System.out.println();



         /*Operadores relacionales: para hacer comparaciones. 
          * Mayor que (>)
          * Mayor igual que (>=)
          * Menor que (<)
          * Menor igual que <=
          * Igual que (==)
          * Distinto de (!=)
          */

          System.out.println("\nOperadores relacionales: ");
          System.out.println("¿3 es mayor que 10?" + (b>a));
          System.out.println("¿3 es mayor o igual que 10?" + (b>=a));
          System.out.println("¿3 es menor que 10?" + (b<a));
          System.out.println("¿3 es menor o igual que 10?" + (b<a));
          System.out.println("¿3 es menor o igual que 10?" + (b<=a));
          System.out.println("¿3 es igual que 10?" + (b==a));
          System.out.println("¿3 es distino de 10?"+ (b!=a));
          

        /*
         * Operador sobre cadena de caractéres (+): Sirven para concatenar cadenas de caracteres. 
         * 
         */

         String txt1 = "Hola "; 
         String txt2 = "Mundo"; 

         System.out.println("\nOperadores sobre cadena de caractáres: ");
         System.out.println(txt1+txt2);


         /*
          * Operadores de asignación y lógicos: para darle un valor a una variable: 
          * +=: Suma la variable y sobre escirbe el valor de la variable con el resultado 
          * -=: Resta la variable y sobre escribe el valor de la variable con el resultado
          * *=: Multiplica la variable y sobre escrible el valor de la variable con el resultado
          * /=: Divide la variable y sobre escribe el valor de la variable con el resultado
          * %=: hace el modulo de la variable y sobre escribe el valor de la variable con el resultado 
          * &=: Hace un AND lógico a la variable y sobre escribe el valor de la variable con el resultado. tambien se puede usar (x && y:)
          * |=: Hace un OR lógico a la variable y sobre escribe el valor de la variable con el resultado. tambien se puede usar (x || y:)
          * !=: Hace un NOT lógico a a la variable y sobre escribe el valor de la variable con el resultado. tambien se puede usar (!x:)
          */

          int i; 
          boolean t = true; 

          System.out.println("Operadores de asignación: para darle un valor a una variable:");
          System.out.println("Se le da un valor a la variable i = " + (i=1));
          System.out.println("Sumar y asignar: " + (i+=2));
          System.out.println(("Resta y asignar: " + (i-=2)));
          System.out.println("Multiplicar y asignar: " + (i*=2));
          System.out.println(("Dividir y asignar: " + (i/=2)));
          System.out.println("Modulo y asigna " + (i%=2));
          System.out.println("AND logico " + (t&=true));
          System.out.println("OR logico "+ (t|=false));
          System.out.println("NOT logico y asignar " + (t!=true));

        

          /*Operadores de bits 
           * Tipos: 
           * AND(&): Operador AND a nivel de bits (1 y 1 = 1 )
           * OR (|): Operador OR a nivel de bits (1 ó 1 = 1)
           * XOR (^): Operador XOR a nivel de bits (1 y 1 = 0 )
           * Complemento (~): Invierte el valor de cada bit 
           * >>: Desplaza cada bit a la derecha 
           * <<: Desplaza bits a la izquierda 
           * >>>: Desplaza bits a la derecha sin signo
           */

           System.out.println("\nOperadores de bits ");

           System.out.println("a : " + Integer.toBinaryString(a));
           System.out.println("b : " + Integer.toBinaryString(b));

           System.out.println("\n b AND a: " + Integer.toBinaryString(a&b));
           System.out.println(" b OR a : " + Integer.toBinaryString(a|b));
           System.out.println(" b XOR a: " + Integer.toBinaryString(a^b));
           System.out.println("Complemento de a = " + Integer.toBinaryString(~a));
           System.out.println("Complemento de b = " + Integer.toBinaryString(~b));
           System.out.println("Desplazamiento de bits de a a la derecha de b : " + Integer.toBinaryString(a>>b));
           System.out.println("Desplazamiento de bits de a a la izquierda de b: " + Integer.toBinaryString(a<<b));
           System.out.println("Desplazamieto de bits de a a la derecha de b (sin signo): " + Integer.toBinaryString(a>>>b));



           /*
            * Estructura switch 
            * sirve para verificar cada caso dependiendo de la variable que se le ingrese 
            */

            int dia = 3; 
            switch (dia) {
                case 1:
                    System.out.println("\nLunes ");
                    
                    break;
                case 2: 
                    System.out.println("\nMartes");
                    break; 
                case 3 : 
                    System.out.println("\nMiercoles");
                    break; 
                case 4: 
                    System.out.println("\nJueves");
                    break; 
                case 5: 
                    System.out.println("\nViernes");
                    break; 
                case 6: 
                    System.out.println("\nSabado");
                    break; 
                case 7: 
                    System.out.println("\nDomingo");
                    break; 
            
                default:
                    System.out.println("\nEl numero del dia de la semana no es valido");
                    break;
            }
           /* DIFICULTAD EXTRA (opcional):
           * Crea un programa que imprima por consola todos los números comprendidos
           * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
           *
           * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
           */
           System.out.println("\n--------------------------");
           System.out.println(" \n Programa extra: ");
           System.out.println("---------------------------");
           System.out.println("\n Estos son los numeros: ");

           for (int h = 10; h<=55; h++){
            if (h%2==0 && h!= 16 && h%3!=0){
                System.out.println(h);
            }
           }




    }
}
