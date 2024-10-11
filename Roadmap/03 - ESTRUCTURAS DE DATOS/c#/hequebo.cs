class Program
{
    static List<Contacto> agenda = new List<Contacto>
    {
        new Contacto(1, "Emilio", "612123456"),
        new Contacto(2, "Samantha", "62134567"),
        new Contacto(3, "Aldo", "6124573154")
    };
    static int id = 4;
    static void Main(string[] args)
    {
        // Estructuras de Datos

        #region Arrays
        // Arreglos o Arrays
        /* 
            -Almacenan elementos del mismo tipo.
            -Su tamaño es definido al momento de
            su creación.
            -Pueden tener multiples dimensiones
        */
        string[] personas = { "Hugo", "Paco", "Luis" }; // Se puede inicializar definiendo los elementos que lo conforman 
        int[] edades = new int[5]; // Tambien se puede indicar el tamaño al inicializarlo para su llenado posterior
        for (int i = 1; i < 5; i++) // => {1, 2, 3, 4, 5}
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
        
        // Agregar
        /* 
         * Al tener su tamaño definido al momento de creación
         * no es posible agregar nuevos elementos, pero si 
         * reemplazar los ya existentes al conocer su posición
         * o índice. Los índices se incializan en 0, por lo que
         * el último elemento de un array con 5 elementos se
         * encuentra en el índice 4
         */
        edades[4] = 6; // => {1, 2, 3, 4, 6}
        /* 
         * edades[5] = 6 <- esto daría un error ya que el tamaño
         *                  del array es de 5 por lo que el índice
         *                  5 estaría fuera de ese límite
         */

        // Eliminar
        /* 
         * Para elminar elementos de un array se puede usar el metodo
         * Array.Clear() en el cual se indica a partir de cual indice
         * quieres eliminar y la cantidad de elmentos a eliminar.
         * Sin embargo el tamaño del array no cambia y en los índices
         * donde se elimino se coloca un valor por default como el 0
         */
        Array.Clear(edades, 2, 2); // => {1, 2, 0, 0, 6}

        // Modificar
        /* 
         * Para modificar solo se debe indicar el indice del elemento
         * a modificar y asignarle el nuevo valor
         */
        edades[0] = 5; // => {5, 2, 0, 0, 6}
        edades[2] = 7; // => {5, 2, 7, 0, 6}
        edades[3] = 2; // => {5, 2, 7, 2, 6}

        // Ordenar
        /* 
         * El metodo Array.Sort() ordena los elemento de
         * mayor a menor por default en caso de tipos enteros
         * o alfabéticamente en casa de chars o strings, teniendo la opción
         * de enviar varias conbinacione de parámetros 
         * para configurar el ordenamiento
         */

        char[] letras = { 'f', 'b', 'a', 'h', 'c' };
        Array.Sort(letras); // => {a, b, c, f, h}
        #endregion
        #region Listas
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
        paises.Add("Colombia");// => {"México", "España", "Perú", "Colombia"}
        // Eliminar
        paises.Remove("Perú"); // => {"México", "España", "Colombia"}

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
        paises[1] = "Españita"; // => {"México", "Españita", "Colombia"}
        paises[0] = "Estados Unidos Mexicanos"; // => {"Estados Unidos Mexicanos", "España", "Colombia"}

        // Ordenar
        /*
         * Se ordenan los elementos de manera similar
         * a  como se hace con arrays
         */
        paises.Sort(); // => {"Colombia", "Españita", "Estados Unidos Mexicanos"}
        #endregion
        #region Diccionario
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
        #endregion
        #region Queue
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
        turnos.Enqueue("Uno"); // => {"Uno"}
        turnos.Enqueue("Dos"); // => {"Uno", "Dos"}
        turnos.Enqueue("Tres"); // => {"Uno", "Dos", "Tres"}
        turnos.Enqueue("Cuatro"); // => {"Uno", "Dos", "Tres", "Cuatro"}
        turnos.Enqueue("Cinco"); // => {"Uno", "Dos", "Tres", "Cuatro", "Cinco"}

        // Eliminar
        turnos.Dequeue(); // => {"Dos", "Tres", "Cuatro", "Cinco"}
        /*
         * Para elminar se utiliza el metodo Dequeue()
         * se elimina el primer elemento en se añadido
         * no se puede indicar el elemento a remover
         */

        // No es posible modificar u ordenar una fila
        #endregion
        #region Stack
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
        stack.Push(1); // => {1}
        stack.Push(2); // => {1, 2}
        stack.Push(3); // => {1, 2, 3}
        stack.Push(4); // => { 1, 2, 3, 4}
        stack.Push(5); // => { 1, 2, 3, 4, 5}

        // Eliminar
        /*
         * Se utiliza el método Pop() para remover
         * el último elemento agregado a la pila
         */
        stack.Pop(); // => { 1, 2, 3, 4}

        // No es posible modificar u ordenar una pila
        #endregion
        #region Linked List
        // Listas enlazadas
        /*
         * Una lista enlazada o linked list
         * es una colección de datos en la
         * cual todos sus elementos estan relacionados
         */

        LinkedList<string> list = new LinkedList<string>();
        // Agregrar elementos
        /*
         * Existen cuatro metodos diferente para agregar
         * elmentos o nodos a una lista enlazada
         */
        list.AddFirst("Primer elemento"); //Se agrega un nodo al inicio de la lista
        list.AddLast("Cuarto elemento"); // Se agrega un nodo al final de la lista
        LinkedListNode<string> current = list.Last; // Tomamos el último nodo para agregar otro en una posición anterior
        list.AddBefore(current, "Segundo elemento"); // Agregamos el nuevo nodo antes del nodo indicado
        current = list.Find("Segundo elemento"); // Seleccionamos el nodo que acabamos de agregar
        list.AddAfter(current, "Tercer elemento"); // Agregamos el nodo después del nodo indicado
        list.AddLast("Quinto elemento");
        list.AddLast("Sexto elemento");
        list.AddLast("Séptimo elemento");

        // Eliminar
        /*
         * Existen tres formas diferentes para 
         * elminiar elementos o nodos
         */
        list.RemoveFirst(); // Se elimina el primer nodo de la lista
        list.RemoveLast(); // Se elimina el último nodo de la lista
        current = list.Find("Tercer elemento"); // Se busca el nodo a eliminar
        list.Remove(current); // Se elimina indicando el nodo

        // Modificar
        current = list.Find("Segundo elemento"); // Se busca elemento a modificar
        current.Value = "Primer elemento"; // Se asigna a la propiedad value el nuevo valor 

        // Ordenar
        /*
         * Para ordenar es necesario crear una
         * segunda lista para almecenar el resultado
         * de la función Sort() ya que esta no 
         * modifica la lista a ordenar
         */
        var orderedList = list.Order();

        #endregion
        #region HashSet
        // Hash Set

        /*
         * Conjunto de datos que no
         * admite elementos repetidos
         * y no tiene un orden
         */

        HashSet<int> numeros = new HashSet<int>();
        // Agregar
        numeros.Add(1);
        numeros.Add(2);
        numeros.Add(3);
        numeros.Add(3);
        numeros.Add(4);
        numeros.Add(5);
        /*
         * Aunque se indique la instruccón de agregar el número 3
         * el hashset solo contiene 5 elemento ya que no acepta
         * valores repetidos
         */
        Console.WriteLine($"El hash tiene {numeros.Count} elementos");

        // Eliminar

        numeros.Remove(1); // Se indica el valor a eliminar

        // No es posible modificar un elemento o ordenar el hashset
        #endregion
        // Agenda telefónica
        
        bool salir = false;

        Console.WriteLine();
        Console.WriteLine();
        while (!salir)
        {
            Console.WriteLine("----SISTEMA DE AGENDA TELEFONICA----");
            MostrarMenu();

            int opcion;
            int.TryParse(Console.ReadLine(), out opcion);
            if (opcion == 0)
            {
                Console.Clear();
                Console.WriteLine("Opción no valida, intente de nuevo");
            }
            switch (opcion)
            {
                case 1:
                    Console.Clear();
                    if (agenda.Count == 0)
                    {
                        Console.WriteLine("Su agenda está vacía...");
                        break;
                    }
                    MostrarAgenda(agenda);
                    break;
                case 2:
                    BuscarContacto();
                    break;
                case 3:
                    AgregarContacto();
                    break;
                case 4:
                    ModificarContacto();
                    break;
                case 5:
                    EliminarContacto();
                    break;
                case 6:
                    Console.Clear();
                    Console.WriteLine("Hasta la próxima...");
                    Thread.Sleep(1000);
                    salir = true;
                    break;
                default:
                    Console.Clear();
                    Console.WriteLine("Opción no valida, intente de nuevo");
                    break;
            }

        }
        
    }
    static void MostrarMenu()
    {
        Console.WriteLine("1.- Consultar contactos");
        Console.WriteLine("2.- Buscar contacto");
        Console.WriteLine("3.- Agregar un nuevo contacto");
        Console.WriteLine("4.- Modificar contacto existente");
        Console.WriteLine("5.- Eliminar contacto");
        Console.WriteLine("6.- Salir");
        Console.WriteLine("Por favor elija una opción...");
    }
    static void MostrarAgenda(List<Contacto> agenda)
    {
        foreach (var contacto in agenda)
            Console.WriteLine($"ID: {contacto.Id}, Nombre: {contacto.Nombre}, Teléfono: {contacto.Telefono}");
    }
    static void BuscarContacto()
    {
        Console.Clear();
        Console.WriteLine("Ingrese el nombre del contacto que desea buscar:");
        string contacto = Console.ReadLine();
        var resultado = agenda.Where(c => c.Nombre.ToUpper().Contains(contacto.ToUpper())).ToList();
        Console.Clear();
        if (resultado.Count() == 0)
        {
            Console.WriteLine("No se encontró ningún contacto...");
            return;
        }
        Console.WriteLine("Se encontraron los siguientes contactos:");
        MostrarAgenda(resultado);
    }
    static string IngresarNombre()
    {
        string nombre = "";
        do
        {
            Console.WriteLine("Ingrese el nombre del contacto");
            nombre = Console.ReadLine();
            if (nombre == "")
            {
                Console.Clear();
                Console.WriteLine("El nombre ingresado no es valido, intente de nuevo");
            }
        } while (nombre == "");
        return nombre;
    }
    static string IngresarTelefono()
    {
        Int64 num;
        string telefono;
        bool esValido = true;
        do
        {
            esValido = true;
            Console.WriteLine("Ingrese el número del contacto");
            telefono = Console.ReadLine();
            if (!Int64.TryParse(telefono, out num) | telefono.Length > 11)
            {
                Console.Clear();
                Console.WriteLine("El número ingresado no es valido, intente de nuevo");
                esValido = false;
            }
        } while (!esValido);
        return telefono;
    }
    static void AgregarContacto()
    {
        Console.Clear();
        string nombre = IngresarNombre();
        string telefono = IngresarTelefono();
        agenda.Add(new Contacto(id, nombre, telefono));
        Console.Clear();
        Console.WriteLine("El contacto se agregó correctamente:");
        Console.WriteLine($"ID: {id}, Nombre: {nombre}, Telefono: {telefono}");
        id++;
    }
    static int BuscarPorId()
    {
        bool esValido = true;
        int idContacto;
        do
        {
            esValido = true;
            Console.WriteLine("Especifique el id del contacto");

            int.TryParse(Console.ReadLine(), out idContacto);
            if (idContacto == 0)
            {
                Console.WriteLine("Por favor ingrese un id válido...");
                esValido = false;
            }
            else if (agenda.Where(c => c.Id == idContacto).Count() == 0)
            {
                Console.WriteLine($"No existe ningún contacto con el id {idContacto}...");
                esValido = false;
            }

        } while (!esValido);
        return idContacto;
    }
    static void ModificarContacto()
    { 
        Console.Clear();
        MostrarAgenda(agenda);
        int idContacto = BuscarPorId();

        string nombre = IngresarNombre();
        string telefono = IngresarTelefono();
        var contacto = agenda.FirstOrDefault(c => c.Id == idContacto);
        contacto.Nombre = nombre;
        contacto.Telefono = telefono;
        Console.Clear();
        Console.WriteLine("Contacto modificado existosamente");
        MostrarAgenda(agenda);

    }
    static void EliminarContacto()
    {
        Console.Clear();
        MostrarAgenda(agenda);
        int idContacto = BuscarPorId();
        var contacto = agenda.FirstOrDefault(c => c.Id == idContacto);
        Console.WriteLine("Se eliminará el siguiente contacto:");
        Console.WriteLine($"ID: {contacto.Id}, Nombre: {contacto.Nombre}, Teléfono: {contacto.Telefono}");
        Console.WriteLine("Para confirmar ingrese la tecla s, para cancelar ingrese otra tecla");
        string respuesta = Console.ReadLine();
        if( respuesta.ToUpper() == "S")
        {
            agenda.Remove(contacto);
            Console.WriteLine("El contacto se eliminó correctamente...");
        }
        else
        {
            Console.WriteLine("La operación ha sido cancelada...");
        }
        Thread.Sleep(2000);
        Console.Clear();
    }

    class Contacto
    {
        public int Id { get; set; }
        public string Nombre { get; set; }
        public string Telefono { get; set; }

        public Contacto(int id, string nombre, string telefono) 
        {
            this.Id = id;
            this.Nombre = nombre;
            this.Telefono = telefono;
        }
    }
}