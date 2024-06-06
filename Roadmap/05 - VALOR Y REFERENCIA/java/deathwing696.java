/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

/**
 *
 * @author death
 */
public class deathwing696 {

    public static void main(String[] args) 
    {
        int variable1 = 1, variable2 = 5;
        IntegerWrapper variable3 = new IntegerWrapper(1);
        IntegerWrapper variable4 = new IntegerWrapper(5);
        
        funcion_por_valor(variable1, variable2);
        
        System.out.println("Después de la ejecución del paso por valor los valores son variable1:" + variable1 + " y variable2:" + variable2);
        
        funcion_por_referencia(variable3, variable4);
        
        System.out.println("Después de la ejecución del paso por referencia los valores son variable3:" + variable3.getValue() + " y variable4:" + variable4.getValue());
    }
    
    static private void funcion_por_valor(int var1, int var2)
    {
        int aux = var1;
        
        var1 = var2;
        var2 = aux;
    }
    
    static private void funcion_por_referencia(IntegerWrapper var1, IntegerWrapper var2)
    {
        IntegerWrapper aux = new IntegerWrapper(var1.getValue());
        
        var1.setValue(var2.getValue());
        var2.setValue(aux.getValue());
    }
    
}

/*Java SIEMPRE pasa los parámetros de los tipos primitivos por valor, si quieres que lo pase por referencia tienes que 
* "inventarte" una especia de wrapper
*/
class IntegerWrapper
{
    private int value;
    
    public IntegerWrapper(int value)
    {
        this.value = value;
    }
    
    public int getValue()
    {
        return value;
    }
    
    public void setValue(int value)
    {
        this.value = value;
    }
}
