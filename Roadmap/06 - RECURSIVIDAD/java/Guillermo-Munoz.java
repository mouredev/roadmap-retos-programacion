/**
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 * 
 * @version v1.0
 * @since 05/03/2026
 * @author Guillermo-Munoz
 * 
 */
public class GuillermoMunoz {


    public static void main(String[] args) {

        countDown(100);
        System.out.println("Factorial de 5: " + factor(5));
        System.out.println("Segun la posición de fibonacci 10 el valor es: " + fibonacci(5));
    }

    //Funcion recursiva cuenta decreciente de 100 a 0

    public static void countDown(int num){
        System.out.println(num);
        if(num > 0){
            --num;
            countDown(num);
        }
    }

    //Calcular el factorial de un número concreto (la función recibe ese número).

    public static int factor(int num){
    
        if(num < 0){
            System.out.println("Los numeros negativos no son validos");
        }else{
            if(num == 0){
                return 1;
            }
        }
    
        return num * factor(num - 1);
    }

    //Calcular el valor de un elemento concreto (según su posición) en la 
    //sucesión de Fibonacci (la función recibe la posición).

    public static int fibonacci(int num){

        
        if(num < 0){
            System.out.println("No se admiten numeros negativos");
            return 0;
        }else if(num < 2){
            return 1;
        }else{
            return  fibonacci(num - 1) + fibonacci(num - 2);
        }
        
    }


    
}
