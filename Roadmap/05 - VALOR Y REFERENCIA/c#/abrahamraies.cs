// Author: Abraham Raies https://github.com/abrahamraies

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

using System;
using System.Collections.Generic;

class Program {
    static void Main(string[] args){
        Console.WriteLine("=== ASIGNACION POR VALOR === \n");

        int a = 10;
        int b = a;

        b += 5;
        Console.WriteLine(a);
        Console.WriteLine(b); // El valor de a no se ve afectado por la modificacion de a.

        Console.WriteLine("=== ASIGNACION POR REFERENCIA === \n");

        int[] array1 = {1,2,3};
        int[] array2 = array1;

        array2[0] = 10;

        Console.WriteLine(array1[0]); // Salida: 10 (El valor del arreglo original se ve afectado por la modificacion de la copia del arreglo original)
        Console.WriteLine(array2[0]); // Salida: 10 (El valor de la copia del arreglo original se ve afectado por la modificacion de la copia del arreglo original)

        Console.WriteLine("=== FUNCIONES CON PARAMETROS POR VALOR === \n");

        int y = 10;
        FuncionPorValor(y);
        Console.WriteLine(y); // Salida: 10 (El valor de y no se ve afectado por la modificacion de y)

        Console.WriteLine("=== FUNCIONES CON PARAMETROS POR REFERENCIA === \n");

        List<int> lista = new List<int> {1,2,3};
        AgregarElemento(lista);
        Console.WriteLine(lista[3]); // Salida: 4 (El valor de la lista se ve afectado por la modificacion de la lista)

        int x = 10;
        FuncionPorReferencia(ref x);
        Console.WriteLine(x); // Salida: 15 (El valor de x se ve afectado por la modificacion de x)

        ObtenerValores(out int valor1, out int valor2); // Out: se usa para indicar que el valor de la variable se va a modificar dentro de la funcion.
        Console.WriteLine(valor1); // Salida: 10
        Console.WriteLine(valor2); // Salida: 20

        Console.WriteLine("=== EJERCICIO EXTRA === \n");


        Console.WriteLine("=== FUNCION CON PARAMETROS POR VALOR === \n");
        int var1 = 10;
        int var2 = 20;

        int nuevo1,nuevo2;

        IntercambiarPorValor(var1, var2, out nuevo1, out nuevo2);
        Console.WriteLine("Originales: a = {0}, b = {1}", var1, var2);
        Console.WriteLine("Intercambiados: nuevo1 = {0}, nuevo2 = {1}", nuevo1, nuevo2);

        Console.WriteLine("=== FUNCION CON PARAMETROS POR REFERENCIA === \n");
        int var3 = 5;
        int var4 = 10;

        int original3 = var3;
        int original4 = var4;

        IntercambiarPorReferencia(ref var3, ref var4);
        Console.WriteLine("Originales: original3 = {0}, original4 = {1}", original3, original4);
        Console.WriteLine("Intercambiados: var3 = {0}, var4 = {1}", var3, var4);
        
    }

    static void FuncionPorValor(int a){
        a += 5;
    }

    static void FuncionPorReferencia(ref int a){
        a += 5;
    }

    static void ObtenerValores(out int a, out int b){
        a = 10;
        b = 20;
    }

    static void AgregarElemento(List<int> lista){
        lista.Add(4);
    }

    // Función que intercambia dos valores pasados por valor
    static void IntercambiarPorValor(int x, int y, out int nuevoX, out int nuevoY)
    {
        nuevoX = y;
        nuevoY = x;
    }

    // Función que intercambia dos valores pasados por referencia
    static void IntercambiarPorReferencia(ref int x, ref int y)
    {
        int temp = x;
        x = y;
        y = temp;
    }

}