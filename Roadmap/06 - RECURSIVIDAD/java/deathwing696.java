/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una funci�n recursiva que imprima
 * n�meros del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un n�mero concreto (la funci�n recibe ese n�mero).
 * - Calcular el valor de un elemento concreto (seg�n su posici�n) en la 
 *   sucesi�n de Fibonacci (la funci�n recibe la posici�n).
 */

/**
 *
 * @author death
 */
public class deathwing696 {

    public static void main(String[] args) 
    {        
        System.out.println(CuentaRecursivo(100));
        
        var num = 3;
        
        System.out.println("El factorial de " + num + "! es " + factorial(num));
        
        var pos = 14;
        
        System.out.println("El valor de la posici�n " + pos + " en la serie de fibonacci es " + fibonacci(pos));
    }
    
    static private int CuentaRecursivo(int num)
    {
        if (num == 0)
        {
            return 0;            
        }            
        else
        {
            System.out.println(num);
            
            return CuentaRecursivo(num - 1);
        }
    }
    
    static private int factorial(int num)
    {
        if (num == 1)
            return 1;
        else
            return num * factorial(num - 1);
    }
    
    static private int fibonacci(int pos)
    {
        return switch (pos) 
        {
            case 0 -> 0;
            case 1 -> 1;
            default -> fibonacci(pos - 1) + fibonacci(pos - 2);
        };
    }
}
