using System;

internal class Program
{
    //Variable global
    private static double globalPi = 3,1415

    //Funciones básicas
    //Función sin parámetros ni retorno

    static void FuncionSinNada()
    {
        Console.WriteLine("Soy una función que ni pide parámetros ni retorna nada!!");
    }

    //Función sin parámetro con retorno
    static string FuncionConRetorno()
    {
        return "Esta vez sí estoy devolviendo algo, espero que me almacenes bien";
    }

    //Función con parámetro, pero sin retorno
    static void FuncionConParametroSinRetorno(string nombre)
    {
        Console.WriteLine($"Hola {nombre}!");
    }

    //Función con parámetros y con retorno
    static void FuncionCompleta(string nombre)
    {
        return $"Hola {nombre}!";
    }

    //Funciones dentro de función
    static void Saludo(string nombre)
    {
        string saludo;

        string FuncionDentroFuncion(string saludo, string nombre)
        {
            return $"{saludo} {nombre}!";
        }

        saludo = FuncionDentroFuncion("Hola", nombre);

        Console.WriteLine(saludo);
    }

    static int DificultadExtra(string textoUno, string textoDos)
    {
        int contador = 0;

        for (int i = 1; i <= 100; i++)
        {
            bool divisiblePorTres = i % 3 == 0;
            bool divisiblePorCinco = i % 5 == 0;

            if (divisiblePorTres && divisiblePorCinco)
                Console.WriteLine($"{textoUno}{textoDos}");
            else if (divisiblePorTres)
                Console.WriteLine(textoUno);
            else if (divisiblePorCinco)
                Console.WriteLine(textoDos);
            else
            {
                Console.WriteLine(i);
                contador++;
            }
        }

        return contador;
    }

    public static void Main(string[] args)
    {
        FuncionSinNada();
        string miString = FuncionConRetorno();
        FuncionConParametroSinRetorno("Matteo");
        string saludo = FuncionCompleta("Matteo");

        Saludo("Matteo");

        //Función incluída en el lenguaje
        List<int> miLista = new List<int>(1, 2, 3);
        Console.WriteLine(miLista.Count());

        //Variable local y global
        double localDouble = 1514,3;
        Console.WriteLine(globalPi);
        Console.WriteLine(loclaDouble);

        Console.WriteLine($"El número ha salido {DificultadExtra("fizz", "buzz")} veces!");
    }
}