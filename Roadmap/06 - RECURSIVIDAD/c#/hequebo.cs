class Program
{
    static void Main(string[] args)
    {
        // Recursividad
        Console.WriteLine("----Recursividad----");
        Console.WriteLine("---Imprimir del 100 al 1---");
        ImprimirNumeros();
        Console.ReadLine();
        Console.Clear();

        // Ejercicio Extra
        Console.WriteLine("---Ejercicio extra---");
        bool salir = false;

        do
        {
            MostrarMenu();
            string opcion = Console.ReadLine();
            switch (opcion)
            {
                case "A":
                case "a":
                    Console.Clear();
                    Console.WriteLine("---FACTORIAL---");
                    Console.WriteLine("Ingresa el número a calcular su factorial:");
                    int num = int.Parse(Console.ReadLine());
                    int factorial = CalcularFactorial(num);
                    Console.WriteLine($"El factorial de {num} es {factorial}");
                    break;
                case "B":
                case "b":
                    Console.Clear();
                    Console.WriteLine("---FIBONACCI---");
                    Console.WriteLine("Ingresa la posición a calcular");
                    int posicion = int.Parse(Console.ReadLine());
                    int valor = CalcularFibonacci(posicion);
                    Console.WriteLine($"El valor de la posición {posicion} en la serie Fibonacci es {valor}");
                    break;
                case "C":
                case "c":
                    Console.WriteLine("Hasta la próxima");
                    salir = true;
                    Thread.Sleep(2000);
                    break;
                default:
                    Console.WriteLine("Opción no valida...");
                    break;
            }
        } while (!salir);


    }

    static void ImprimirNumeros(int n = 100)
    {
        Console.WriteLine(n);
        if (n > 1)
        {
            n--;
            ImprimirNumeros(n);
        } 
    }

    static void MostrarMenu()
    {
        Console.WriteLine("----MENU----");
        Console.WriteLine("a.- Calcular Factorial");
        Console.WriteLine("b.- Calcular valor de posición en serie Fibonacci");
        Console.WriteLine("c.- Salir");
        Console.WriteLine("Seleccione una opción");
    }
    static int CalcularFactorial(int num)
    {
        if (num == 0 || num == 1)
            return 1;
        return num * CalcularFactorial(num - 1);
    }
    static int CalcularFibonacci(int posicion)
    {
        if (posicion <= 0)
        {
            Console.WriteLine("La posición debe de ser un número entero positivo...");
            return 0;
        }
        if (posicion == 1) 
            return 0;
        if (posicion == 2 || posicion == 3)
            return 1;

        return CalcularFibonacci(posicion - 1) + CalcularFibonacci(posicion - 2);
    }
        
}
