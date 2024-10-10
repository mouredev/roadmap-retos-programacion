class Program
{
    static void Main(string[] args)
    {
        // Estructuras de Datos
        
        // Arreglos o Arrays
        /* 
            -Almacenan elementos del mismo tipo.
            -Su tamaño es definido al momento de
            su creación.
            -Pueden tener multiples dimensiones
        */
        string[] personas = { "Hugo", "Paco", "Luis" }; // Se puede inicializar definiendo los elementos que lo conforman 
        int[] edades = new int[5]; // Tambien se puede indicar el tamaño al inicializarlo para su llenado posterior
        for (int i = 1; i < 5; i++)
            edades[i] = i;

        string[,] coordenadads = new string[5, 5]; // Un array de dos dimensiones se conoce como matríz
        /*
         * Para recorrer una matriz podemos utilizar dos ciclos for para 
         * recorrer tanto sus renglones como sus columnas
         */
        for (int i = 0; i < 5; i++)
        {
            for (int j = 0; j < 5; j++)
            {
                coordenadads[i, j] = $"{i},{j}";
            }
        }

        /* 
         * Al tener su tamaño definido al momento de creación
         * no es posible agregar nuevos elementos, pero si 
         * reemplazar los ya existentes al conocer su posición
         * o índice. Los índices se incializan en 0, por lo que
         * el último elemento de un array con 5 elementos se
         * encuentra en el índice 4
         */
        edades[4] = 6;
        /* 
         * edades[5] = 6 <- esto daría un error ya que el tamaño
         *                  del array es de 5 por lo que el índice
         *                  5 estaría fuera de ese límite
         */

        /* 
         * Para elminar elementos de un array se puede usar el metodo
         * Array.Clear() en el cual se indica a partir de cual indice
         * quieres eliminar y la cantidad de elmentos a eliminar.
         * Sin embargo el tamaño del array no cambia y en los índices
         * donde se elimino se coloca un valor por default como el 0
         */
        Array.Clear(edades, 2, 2);
        foreach (int edad in edades)
            Console.WriteLine(edad);

        // Modificación
        /* 
         * Para modificar solo se debe indicar el indice del elemento
         * a modificar y asignarle el nuevo valor
         */
        edades[0] = 5;
        edades[2] = 7;
        edades[3] = 2;

        // Ordenamiento
        /* 
         * El metodo Array.Sort() ordena los elemento de
         * mayor a menor por default en caso de tipos enteros
         * o alfabéticamente en casa de chars o strings, teniendo la opción
         * de enviar varias conbinacione de parámetros 
         * para configurar el ordenamiento
         */

        char[] letras = { 'f', 'b', 'a', 'h', 'c' };
        Array.Sort(letras);
        Console.Write("{");
        foreach (char c in letras)
            Console.Write($"{c},");

        Console.Write("}");

        // Listas
        /*
         * También llamadas colecciones las listas
         * permiten almacenar varios datos de un mismo
         * tipo. A diferencia del array el tamaño de
         * un lista es dinamico y no se tiene que indicar
         * al momento de inicializarla. Además cuenta 
         * con metodos para el manejo de sus datos de una
         * manera más fácil
         */

        List<string> paises = new List<string>();
        // Agregar de datos
        paises.Add("México");
        paises.Add("España");
        paises.Add("Perú");
        paises.Add("Colombia");
        // Eliminar datos
        paises.Remove("Perú");

        // Modificar
        /*
         * Para modificar una lista se puede hacer 
         * de manera similar a un array e indicar
         * el índice a modificar. Sin embargo al ser
         * posible eliminar y agregar elementos el
         * indice del elemento puede cambiar por lo
         * que primero se tendría que buscar dicho 
         * índice
         */
        paises[1] = "Españita";
        paises[0] = "Estados Unidos Mexicanos";

        // Ordenar
        /*
         * Se ordenan los elementos de manera similar
         * a  como se hace con arrays
         */
        paises.Sort();

        // Diccionario
        /*
         * Representa una colección de claves y valores
         * o key-value pairs
         */
        Dictionary<string, string> languages = new Dictionary<string, string>();
        // Agregar
        /*
         * Se agreagan tanto la clave como el valor.
         * Las claves no pueden ser duplicadas pero los
         * valores sí
         */
        languages.Add("C#", "https://learn.microsoft.com/en-us/dotnet/csharp/");
        languages.Add("Python", "https://www.python.org/");
        languages.Add("Java", "https://www.java.com/es/");
        languages.Add("Javascript", "https://developer.mozilla.org/es/docs/Web/JavaScript");
        languages.Add("Php", "https://www.php.net/manual/es/intro-whatis.php");
        languages.Add("Kotlin", "https://kotlinlang.org/");

        // Eliminar
        /*
         * Para eliminar se utiliza el método Remove()
         * indicando la clave de elemento, de manera
         * utilizando la clave como un índice
         */
        languages.Remove("Java");
        // Modificar
        /*
         * Para modificar solo se índica la 
         * clave del elemento a modificar
         */
        languages["Python"] = "python.org";

        // Ordenar
        /*
         * Los diccionarios no tienen un metodo propio
         * para ser ordenados. Sin embargo puede utilizarse 
         * Linq para ordenarlos
         */
        languages = (from language in languages
                    orderby language.Key ascending
                    select language).ToDictionary();

        // Queue
        /*
         * Queue o fila es una colección de datos
         * donde se aplica el método FIFO (First In First Out).
         * Como su nombre lo indica el primer elemento en entrar a
         * la colección es el primero en salir
         */

        Queue<string> turnos = new Queue<string>();
        // Agregar 
        /*
         * Se utiliza el método Enqueue()
         */
        turnos.Enqueue("Uno");
        turnos.Enqueue("Dos");
        turnos.Enqueue("Tres");
        turnos.Enqueue("Cuatro");
        turnos.Enqueue("Cinco");

        // Eliminar
        turnos.Dequeue();
        /*
         * Para elminar se utiliza el metodo Dequeue()
         * se elimina el primer elemento en se añadido
         * no se puede indicar el elemento a remover
         */

        // No es posible modificar u ordenar una fila

        // Stack
        /*
         * Stack o pila es una colección de datos
         * donde se aplica el método FILO (First In Last Out).
         * Como su nombre lo indica el primer elemento en entrar a
         * la colección es el ultimo en salir
         */

        Stack<int> stack = new Stack<int>();
        // Agregar
        /*
         * Para agregar se utiliza el método Push
         */
        stack.Push(1);
        stack.Push(2);
        stack.Push(3);
        stack.Push(4);
        stack.Push(5);

        // Eliminar
        /*
         * Se utiliza el método Pop() para remover
         * el último elemento agregado a la pila
         */
        stack.Pop();

        // No es posible modificar u ordenar una pila
    }
}