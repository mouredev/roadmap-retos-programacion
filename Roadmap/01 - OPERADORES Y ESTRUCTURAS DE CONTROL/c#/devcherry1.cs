using System;

class Program
{
    static void Main()
    {
        int ejemplo1 = 15;
        int ejemplo2 = 20;
        int ejemplo3;

        if (ejemplo1 == 15)
        {
            ejemplo1 = ejemplo1 + 19;
            ejemplo2 /= 10;
            ejemplo3 = ejemplo2 % 3;
            Console.WriteLine(ejemplo3);
        }
        else
        {
            ejemplo1 -= 70;
            ejemplo2 = ejemplo2 * 90;
            Console.WriteLine(ejemplo1);
        }
        for (int i = 10; i <= 55; i++ )
        {
            if (i % 2 == 0 && i % 3 != 0 && i != 16)
            {
                Console.WriteLine(i);
            }
        }
    }
}
