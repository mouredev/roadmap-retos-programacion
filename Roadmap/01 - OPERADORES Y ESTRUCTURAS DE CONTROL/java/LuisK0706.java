public class Ejercicio01{

    public static void main(String[] args) {
        

        // Operadores aritméticos 
        int num1 = 4, num2 = 2, i = 0, contador = 0;
        Integer num3 = 0;
        String cadena = "";

        // Operador + para una suma
        System.out.println("Operadores aritméticos");
        System.out.println("Suma de 4 + 2 es: " + (num1 + num2));
        // Operador - para una resta
        System.out.println("Resta de 4 - 2 es: " + (num1 - num2));
        // Operador * para una multiplicacion
        System.out.println("Multiplicacion de 4 * 2 es: " + (num1 * num2));
        // Operador / para un division 
        System.out.println("Division de 4 / 2 es: " +  (num1 / num2));
        // Operador % para una division entera
        System.out.println("Modulo de 4 % 2 es: " + (num1 % num2));
        // Doble signo ++ para incrementar una variable
        System.out.println("Incrementando la variable num1: " + (++num1));
        // Doble signo -- para decrementar una variable
        System.out.println("Decrementando la variable num1: " + (--num1) + "\n");


        // Operadores lógicos

        System.out.println("Operadores lógicos");
        // Operador and (&&)
        System.out.println("5 > 2 and 5 < 10 es: " + (5 > 2 && 5 < 10));
        // Operador or (|)
        System.out.println("5 > 2 or 5 < 1 es: " + (5 > 2 | 5 < 1));
        //  Operador not (!)
        System.out.println("not 5 > 2 es: " + (!(5 > 2)));


        // Operadores de comparacion

        System.out.println("Operadores de comparación");
        // Operador mayor que >
        System.out.println("8 mayor que 4 es: " + (8 > 4));
        // Operador menor que <
        System.out.println("8 menor que 4 es: " + (8 < 4));
        // Operador igual ==
        System.out.println("8 igual que 4 es: " + (8 == 4));
        // Operador de diferencia != 
        System.out.println("8 es diferente que 4 es: " + (8 != 4));
        // Operador mayor o igual que >=
        System.out.println("8 mayor o igual que 8 es: " + (8 >= 8));
        // Operador menor o igual que <=
        System.out.println("8 menor o igual que 10 es: " + (8 <= 10) + "\n"); 


        // Operadores de asignación

        System.out.println("Operadores de Asignación");    
        // Suma y asignacion
        num1 += 5;
        System.out.println("num1 + 5 con suma y asignacion es: " + (num1));
        // Resta y asignacion
        num1 -= 5;
        System.out.println("num1 - 5 usando resta y asignación es: " + (num1));
        // Multiplicacion y asignacion 
        num1 *= 5;
        System.out.println("num1 * 5 usando multiplicacion y asignacion es: " + (num1));
        // Division y asignacion 
        num1 /= 5;
        System.out.println("num1 / 5 usando division y asignacion es: " + (num1) + "\n");
        

        // Operadores de identidad

        System.out.println("Operadores de identidad");
        // Operador == 
        System.out.println("Operador (==): " + (num1 == num2));

        //Operador != 
        System.out.println("Operador (!=): " + (num1 != num2) + "\n");
        

        //Operadores de pertenencia

        //Para verificar pertenencia utilizamos instanceof
        System.out.println("Operadores de pertenencia");
        System.out.println("Es una instancia de un entero: " + (num3 instanceof Integer));
        System.out.println("Es una instancia de una cadena: " + (cadena instanceof String) + "\n");


        //Operadores de bits

        System.out.println("Operadores de bits");
        //Operador AND (&)
        System.out.println("Operador AND: " + (num1 & num2));
        //Operador OR (|)
        System.out.println("Operador OR: " + (num1 | num2) + "\n");
        
        //Estructuras de control 

        //Condicionales (if, else if, else)

        System.out.println("Estructuras condicionales");
        if (num1 == num2){
            System.out.println("Los dos numeros son iguales");
        }
        else if (num1 > num2){
            System.out.println("El primer numero es mayor");
        }
        else{
            System.out.println("El segundo numero es mayor");
        }

        //Iterativas (for, while, do whie)

        //Ciclo for
        for (int j = 0; j < 10; j++){
            System.out.println(i);
        }

        //Ciclo while
        while(i < 10){
            System.out.println(i);
            i ++;
        }

        //Ciclo do while
        do {
            System.out.println("Hola que tal");
            contador ++;
        }while(contador < 10);

        //Manejo de excepciones 
        try {
            float division = 10/0;
            System.out.println("El resultado de la división es: " + division);
        } catch (ArithmeticException e) {
            System.out.println("Se produjo un error aritmético: " + e.getMessage());
        }


        /* Reto extra
         * Crea un programa que imprima por consola todos los números comprendidos
         * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
         */


        for (int numero = 10; numero < 56; numero++){
            if (numero % 3 == 0 || numero == 16){
                continue;
            }
            else{
                System.out.println(numero);
            }
        }

    }
}
