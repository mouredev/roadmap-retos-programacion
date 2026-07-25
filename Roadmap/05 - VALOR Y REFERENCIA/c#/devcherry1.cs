/*
 * *** #05 - C# VALOR Y REFERENCIA  ***
 * 
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 */

using System;

class Program
{
    static void Main()
    {
        string ejem1 = "esta es una variable por valor";
        ejem1 = caps(ejem1);
        Console.WriteLine(ejem1);
        string ejem2 = "esta es una variable por referencia";
        toCaps(ref ejem2);
        Console.WriteLine(ejem2);

        //***Extra***
        string chicaUno = "Rachel";
        string chicaDos = "Phoebe";
        (string chicaIntercambiada1, string chicaIntercambiada2) = Extra.Chicas(chicaUno,chicaDos);
        Console.WriteLine($"Nombres originales: {chicaUno} {chicaDos}" +
                          $"\nNombres intercambiados: {chicaIntercambiada1} {chicaIntercambiada2}");
        
        string chicoUno = "Ross";
        string chicoDos = "Joey";
        (string chicoIntercambiado1, string chicoIntercambiado2) = Extra.Chicos(ref chicoUno, ref chicoDos);
        Console.WriteLine($"Nombres originales: {chicoUno} {chicoDos}" +
                          $"\nNombres intercambiados: {chicoIntercambiado1} {chicoIntercambiado2}");
    }
    static string caps(string cadena)
    {
        string cadenaCaps = cadena.ToUpper();
        return cadenaCaps;
    }
    static void toCaps(ref string cadena)
    {
        cadena = cadena.ToUpper();
    }
}
 /* DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */
class Extra
{
    public static (string, string) Chicas(string persona1, string persona2)
    {
        return (persona2, persona1);
    }
    public static (string, string) Chicos(ref string persona1, ref string persona2)
    {
        return (persona2, persona1);
    }
}
