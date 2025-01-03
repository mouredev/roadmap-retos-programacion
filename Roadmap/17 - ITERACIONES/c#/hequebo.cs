class Program
{
    static void Main(string[] args)
    {
        #region Bucles
        // Bucle While
        /*
         * Un bucle While verifica primero que la 
         * condición sea verdadera antes de ejecutar
         * su bloque de código. Por default no interactua
         * con su condición de salida por lo que si en este
         * caso nunca se aumenta el valor de i el bucle se
         * volverá un bucle infinito.
         */
        Console.WriteLine("---While---");
        int i = 1;
        while (i <= 10)
        {
            Console.Write($"{i}, ");
            i++;
        }
        Console.WriteLine();

        // Bucle Do While
        /*
         * Al contrario del bucle While el bucle 
         * Do While se ejecuta por lo menos una vez
         * y verifica su condición al final del bloque
         * de igual manera se tiene que modificar dentro del
         * bloque de código la variable i
         */
        Console.WriteLine("---Do While---");
        i = 1;
        do
        {
            Console.Write($"{i}, ");
            i++;
        } while (i <= 10);
        Console.WriteLine();
        // Bucle For
        /*
         * En un bucle For en su definición además de 
         * indicar la condición para ejecutar el código
         * tambien se modifica la variable i por lo que es
         * menos probable que se cree un bucle infinito
         */
        Console.WriteLine("---Bucle For---");
        for (i = 1; i <= 10; i++)
        {
            Console.Write($"{i}, ");
        }
        Console.ReadLine();
        #endregion
        #region Extra
        Console.WriteLine("----Extra----");
        List<string> lenguajes = new List<string>
        {
            "C#",
            "Java",
            "Python",
            "PHP",
            "C++",
            "Javascript",
            "Kotlin"
        };

        Console.WriteLine("---While---");
        i = 0;
        while (i < lenguajes.Count)
        {
            Console.Write($"{lenguajes[i]} | ");
            i++;
        }
        Console.WriteLine();

        Console.WriteLine("---Do While---");
        i = 0;
        do
        {
            Console.Write($"{lenguajes[i]} | ");
            i++;
        } while (i < lenguajes.Count);
        Console.WriteLine();

        Console.WriteLine("---For---");
        for(i = 0; i < lenguajes.Count; i++)
            Console.Write($"{lenguajes[i]} | ");
        Console.WriteLine();

        Console.WriteLine("---For Each---");
        foreach (string lenguaje in lenguajes)
            Console.Write($"{lenguaje} | ");
        Console.WriteLine();

        Console.WriteLine("---Recursión---");
        Recursion(lenguajes);
        #endregion
    }
    static void Recursion(List<string> list)
    {
        if(list.Count == 0)
            return;
        Console.Write($"{list.First()} | ");
        list.RemoveAt(0);
        
        Recursion(list);
    }
}