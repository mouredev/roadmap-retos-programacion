using System:

class Program 
{
    static void Main(string[] args)
    {

        //Asignacion por valor
        int valor1 = 10;
        int valor2 = valor1;
        valor2 = 20;
        console.WriteLine($"Asignacion por: valor1 = {valor1}, valor2 = {valor2}   ")
    

        //Asignacion por referencia
        int[] array1 = { 1, 2, 3 };
        int[] array2 = array
        array2 [0] = 10;
        Console.WriteLine($"Asignacion por referencia: array1[0] = {array1[0]}, array2[0] = {array2[0]}")

        //Funcion con parametro por valor
        int numero = 5;
        ModificarPorValor(numero);
        Console.WriteLine($"Despues de ModificarPorValor: numero = {numero}");

        // Función con parámetro por referencia
        int numeroRef = 5;
        ModificarPorReferencia(ref numeroRef);
        Console.WriteLine($"Después de ModificarPorReferencia: numeroRef = {numeroRef}");

        //Funcion con parametro de salida
        int numeroOut;
        Console.WriteLine($"Despues de modificarPorSalida: numeroOut = {numeroOut}");
    }

    static void ModificarPorValor(int num)
    {
        num = 10;
        Console.WriteLine($"Dentro de modificarPorValor: num = {num}");
    }

    static void ModificarPorReferencia(ref int num)
    {
        num = 10;
        Console.WriteLine($"Dentro de modificarPorReferencia: num = {num}");
    }

    static void modificarPorSalida(out int num)
    {
        num = 10;
        Console.WriteLine($"Dentro de ModificarPorSalida: num = {num}");
    }

/*
-Explicación

Asignación por valor:
Se crea una copia del valor y se asigna a la nueva variable. Modificar la nueva variable no afecta a la original.

Asignación por referencia:
Se asigna una referencia al mismo objeto en memoria. Modificar la nueva variable también afecta a la original.

Función con parámetro por valor:
Se pasa una copia del valor a la función. Modificaciones dentro de la función no afectan a la variable original.

Función con parámetro por referencia:
Se pasa una referencia a la variable original. Modificaciones dentro de la función afectan a la variable original.

Función con parámetro de salida:
Similar a la referencia, pero obliga a la función a asignar un valor antes de salir.

-Ejecución del Código

Asignación por valor:
valor1 y valor2 son independientes. Modificar valor2 no afecta a valor1.

Asignación por referencia:
array1 y array2 apuntan al mismo arreglo. Modificar array2[0] afecta a array1[0].

Funciones:
ModificarPorValor modifica una copia, no afecta a numero.
ModificarPorReferencia modifica la variable original numeroRef.
ModificarPorSalida asigna un valor a numeroOut.
*/

}
