using System;

class Program
{
    static void Main()
    {
        Console.WriteLine(nombres("Juan", "Pablo"));
        int conteo = extra("Multiplo de 3", "Multiplo de 5");
        Console.WriteLine($"Conteo es: " + conteo);
    }
    static int nombres(string parametro1, string parametro2)
    {
        int count;
        count = parametro1.Length;
        count += parametro2.Length;
        return count;
    }
    static int extra(string parametro1, string parametro2)
    {
        int conteo = 0;
        for( int i = 0 ; i <= 100 ; i++ )
        {
            if( i % 3 == 0 && i % 5 == 0)
            {
                Console.WriteLine("El numero " + i + " es " + parametro1 + " & " + parametro2);
            }
            else if (i % 3 == 0){
                Console.WriteLine("El numero " + i + " es " + parametro1);
            }
            else if (i % 5 == 0){
                Console.WriteLine("El numero " + i + " es " + parametro2);
            }
            else
            {
                conteo += 1;
                Console.WriteLine(i);
            }
        }
        return conteo;
    }
}
