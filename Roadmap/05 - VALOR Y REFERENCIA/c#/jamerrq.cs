using System;
class ValueAndReferences
{
    // Ejemplo de asignación de variables por valor y por referencia
    static void VarsByValueAndReference()
    {
        // Asignación por valor
        int a = 5;
        int b = a;
        b = 10;
        Console.WriteLine("int a = 5; int b = a; b = 10;");
        Console.WriteLine(a); // 5
        Console.WriteLine(b); // 10

        // Asignación por referencia
        int[] c = { 5 };
        int[] d = c;
        d[0] = 10;
        Console.WriteLine("int[] c = { 5 }; int[] d = c; d[0] = 10;");
        Console.WriteLine(c[0]); // 10
        Console.WriteLine(d[0]); // 10
    }

    // Ejemplo de función con variables que se les pasan por valor y por referencia
    static void FuncByValue(int value1, int value2)
    {
        int tmp = value1;
        value1 = value2;
        value2 = tmp;
        Console.WriteLine("FuncByValue(5, 10);");
        Console.WriteLine(value1); // 10
        Console.WriteLine(value2); // 5
    }

    static void FuncByReference(ref int value1, ref int value2)
    {
        int tmp = value1;
        value1 = value2;
        value2 = tmp;
        Console.WriteLine("FuncByReference(ref 5, ref 10);");
        Console.WriteLine(value1); // 10
        Console.WriteLine(value2); // 5
    }

    static void Extra()
    {
        int a = 5;
        int b = 10;
        int c = a;
        int d = b;
        FuncByValue(c, d);
        Console.WriteLine(a); // 5
        Console.WriteLine(b); // 10
        FuncByReference(ref c, ref d);
        Console.WriteLine(a); // 10
        Console.WriteLine(b); // 5
    }

    static void Main()
    {
        Console.WriteLine("========================================");
        Console.WriteLine("==== VARIABLES POR VALOR Y REFERENCIA ==");
        Console.WriteLine("========================================\n");
        VarsByValueAndReference();
        Console.WriteLine("\n========================================\n");
        Console.WriteLine("==== FUNCIONES POR VALOR Y REFERENCIA ===");
        Console.WriteLine("========================================\n");
        FuncByValue(5, 10);
        int x = 5;
        int y = 10;
        FuncByReference(ref x, ref y);
        Console.WriteLine("\n========================================\n");
        Console.WriteLine("============ EJERCICIO EXTRA ===========");
        Console.WriteLine("========================================\n");
        Extra();
    }
}
