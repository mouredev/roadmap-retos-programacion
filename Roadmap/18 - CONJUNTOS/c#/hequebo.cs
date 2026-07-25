class Program
{
    static void Main(string[] args)
    {
        #region Conjuntos
        // Conjuntos
        Console.WriteLine("----Conjuntos----");
        var conjunto = new List<int> { 1, 2, 3, 4, 5, 6 };
        Console.Write("Conjunto inicial: ");
        Console.Write(string.Join(", ", conjunto));
        Console.WriteLine();

        // Agregar elemento al final
        conjunto.Add(7);
        Console.Write("Agregar elemento al final con .Add(item): ");
        Console.Write(string.Join(", ", conjunto));
        Console.WriteLine();

        // Agregar elemento al inicio
        conjunto.Insert(0, 0);
        Console.Write("Agregar elemento al inicio con .Insert(index, item): ");
        Console.Write(string.Join(", ", conjunto));
        Console.WriteLine();

        // Agregar varios elementos al final del bloque
        conjunto.AddRange(new List<int> { 11, 12, 15, 14 });
        Console.Write("Agregar varios elementos al final con .AddRange(collection): ");
        Console.Write(string.Join(", ", conjunto));
        Console.WriteLine();

        // Agregar varios elementos en posición concreta
        conjunto.InsertRange(8, new List<int> { 8, 9, 10 });
        Console.Write("Agregar varios elementos en posición específica con .InsertRange(index, collection): ");
        Console.Write(string.Join(", ", conjunto));
        Console.WriteLine();

        // Eliminar elemnto en posición específica
        conjunto.RemoveAt(13);
        Console.Write("Eliminar un elemento en posición específica con .RemoveAt(index): ");
        Console.Write(string.Join(", ", conjunto));
        Console.WriteLine();

        // Actualizar elemento en posición específica
        conjunto[13] = 13;
        Console.Write("Actualzar un elemento en posición específica con collection[index] = value: ");
        Console.Write(string.Join(", ", conjunto));
        Console.WriteLine();

        // Comprobar si un elemento existe en el conjunto
        Console.WriteLine("Buscar elemento en conjubto con Contains(item)");
        if (conjunto.Contains(6))
            Console.WriteLine("Dentro del conjunto existe el elemento 6");

        // Eliminar todo el contenido del conjunto 
        conjunto.Clear();
        Console.WriteLine("Se eliminan todos los elmentos del conjunto to .Clear()");
        #endregion

        #region Extra
        // Ejercicio Extra
        Console.ReadLine();
        Console.Clear();
        Console.WriteLine("----Extra----");
        var conjunto1 = new List<int> { 5, 7, 6, 2, 0 };
        var conjunto2 = new List<int> { 5, 3, 1, 0, 9 };

        Console.Write("Primer conjunto: ");
        Console.Write(string.Join(", ", conjunto1));
        Console.WriteLine();

        Console.Write("Segundo conjunto: ");
        Console.Write(string.Join(", ", conjunto2));
        Console.WriteLine();


        // Unión
        /*
         * La operación Union devuelve una colección con 
         * todos los elementos únicos  de las dos colecciones
         * especificacdas
         */
        Console.WriteLine("---Union---");
        var union = from item in conjunto1.Union(conjunto2)
                    select item;
        Console.Write("Resultado de la operación de conjuntos Union: ");
        Console.Write(string.Join(", ", union));
        Console.WriteLine();

        // Intersección
        /*
         * La operación Intersección devuelve una
         * colección con elementos que se encuentran
         * en ambas colecciones
         */
        Console.WriteLine("---Intersección---");
        var intersection = from item in conjunto1.Intersect(conjunto2)
                           select item;
        Console.Write("Resultado de la operación de conjuntos Intersección: ");
        Console.Write(string.Join(", ", intersection));
        Console.WriteLine();

        // Diferencia
        /*
         * La operación Diferencia devuelve una colección
         * con elementos de la primera colección que no se
         * encuentran en la segunda
         */
        Console.WriteLine("---Diferencia---");
        var difference = from item in conjunto1.Except(conjunto2)
                         select item;
        Console.Write("Resultado de la operación de conjuntos Diferencia: ");
        Console.Write(string.Join(", ", difference));
        Console.WriteLine();

        // Diferencia Simétrica
        /*
         * La opercacion de Diferencia Simétrica 
         * modifica el primer conjunto para que 
         * contenga elementos que existen dentro de sí
         * o dentro del segundo conjunto, pero no en ambos
         */
        Console.WriteLine("---Diferencia Simétrica---");
        /*
         * El método SymmetricExceptWith existe para la 
         * estructura HashSet
         */
        var hash1 = new HashSet<int>(conjunto1);
        var hash2 = new HashSet<int>(conjunto2);
        
        hash1.SymmetricExceptWith(hash2);

        Console.Write("Resultado de la operación de conjuntos Diferencia Simétrica: ");
        Console.Write(string.Join(", ", hash1));
        Console.WriteLine();
        #endregion

    }
}