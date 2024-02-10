package _06_Recursividad;

public class _06_Recursividad {
    /*
     * EJERCICIO:
     * Entiende el concepto de recursividad creando una función recursiva que imprima
     * números del 100 al 0.
     *
     * DIFICULTAD EXTRA (opcional):
     * Utiliza el concepto de recursividad para:
     * - Calcular el factorial de un número concreto (la función recibe ese número).
     * - Calcular el valor de un elemento concreto (según su posición) en la
     *   sucesión de Fibonacci (la función recibe la posición).
     */
    static int numero = 0;
    static void recursividad(int numero){
        if (numero<=100){
            System.out.println(numero);
        }
        else{
            return ;
        }
        recursividad(numero+1);

    }

    //Dificultad Extra
    static int numero2 = 9; //No pongo la opción de ingresar un número porque me da problemas el IDE
    static int factorial(int numero2){
        if(numero2==0){
            return 1;
        }
        else{
            return numero2 * factorial( numero2 - 1);
        }

    }

    static  int posicion = 4; //No pongo la opción de ingresar un número porque me da problemas el IDE
    static int fibonacci(int posicion){
        if(posicion<=1){
            return posicion;

        }
        else{
            return fibonacci(posicion-2)+fibonacci(posicion-1);
        }
    }

    public static void main (String[] args){
        recursividad(numero);
         int resultado =factorial(numero2);
         System.out.println("El numero 9 factorial es: "+resultado);
         int resultado2 = fibonacci(posicion);
         System.out.println("El resultado del valor que ocupa la posición 4 en la sucesión de " +
                 "fibonacci es: "+ resultado2);



    }
}
