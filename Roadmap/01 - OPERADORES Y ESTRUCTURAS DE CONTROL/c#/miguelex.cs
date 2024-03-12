class miguelex
{
    static void Main(string[] args)
    {
        // Operadores de asignación
        int a = 5;
        int b = 3;

        Console.WriteLine("a + b =  " + (a+b));
        Console.WriteLine("a - b =  " + (a-b));
        Console.WriteLine("a * b =  " + (a*b));
        Console.WriteLine("a / b =  " + (a/b));
        Console.WriteLine("a % b =  " + (a%b));

        // Operadores de comparación

        Console.WriteLine("a == b =  " + (a==b));
        Console.WriteLine("a != b =  " + (a!=b));
        Console.WriteLine("a > b =  " + (a>b));
        Console.WriteLine("a < b =  " + (a<b));
        Console.WriteLine("a >= b =  " + (a>=b));
        Console.WriteLine("a <= b =  " + (a<=b));

        // Operadores lógicos

        bool c = true;
        bool d = false;

        Console.WriteLine("c && d =  " + (c&&d));
        Console.WriteLine("c || d =  " + (c||d));
        Console.WriteLine("!c =  " + (!c));

        // Operadores de incremento y decremento

        Console.WriteLine("a++ =  " + (a++));
        Console.WriteLine("++a =  " + (++a));
        Console.WriteLine("a-- =  " + (a--));
        Console.WriteLine("--a =  " + (--a));

        // OPeradores bits

        Console.WriteLine("a & b =  " + (a&b));
        Console.WriteLine("a | b =  " + (a|b));
        Console.WriteLine("a ^ b =  " + (a^b));

        // Operadores de desplazamiento

        Console.WriteLine("a << b =  " + (a<<b));
        Console.WriteLine("a >> b =  " + (a>>b));

        // if else

        if (a > b)
        {
            Console.WriteLine("a es mayor que b");
        }
        else
        {
            Console.WriteLine("a es menor que b");
        }

        // switch

        switch (a)
        {
            case 1:
                Console.WriteLine("a es 1");
                break;
            case 2:
                Console.WriteLine("a es 2");
                break;
            default:
                Console.WriteLine("a es mayor que 2");
                break;
        }

        // while

        while (a < 10)
        {
            Console.WriteLine("a es menor que 10");
            a++;
        }

        // do while

        do
        {
            Console.WriteLine("a es menor que 10");
            a++;
        } while (a < 10);

        // foreach

        int[] arr = {1, 2, 3, 4, 5};
        foreach(int i in arr)
        {
            Console.WriteLine(i);
        }

        // Excepciones

        try
        {
            int x = 10;
            int y = 0;
            Console.WriteLine(x/y);
        }
        catch (Exception e)
        {
            Console.WriteLine("Error: " + e.Message);
        }
        finally
        {
            Console.WriteLine("Finally");
        }

        // Extra

        Console.WriteLine("Ejercicio Extra");

        for (int i = 10; i <= 55; i++)
        {
            if (i % 2 == 0 && i != 16 && i % 3 != 0)
            {
                Console.WriteLine(i);
            }
        }
    }
}
