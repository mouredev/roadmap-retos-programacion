/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
using System.Collections;
using static System.Runtime.InteropServices.JavaScript.JSType;

class Program
{

    private class Artista
    {
        public int ArtistId { get; set; }
        public string Name { get; set; }
    }

    private class Contacto
    {
        public string Name { get; set; }
        public string Number_Phone { get; set; }
    }

    public static void Main(string[] args)
    {
        _Queue();
        _Array();
        _List();
        _Dictionary();
        _Stack();
        Agenda();
    }

    private static void _Queue()
    {
        /*
         La estrucutra de datos de Queue sigue la regla de First In First Out (Primero en entrar, primero en salir)
         A esta estructura de datos podemos designarle un tamaño al momento de crea una nueva instancia, o también
         podemos indicarle que tipo de dato se le estará asignando.
         */
        Console.WriteLine("------------- Queue ----------------");

        // Formas en la cual podemos utilizarlo
        Queue queue = new Queue();
        Queue queue2 = new Queue(5);
        Queue<Artista> queue3 = new Queue<Artista>();

        // Para agregar un nuevo elemento a la lista podemos utilizar el metodo Enqueue y como argumento el dato
        queue3.Enqueue(new Artista
        {
            ArtistId = 1,
            Name = "Estuardo"
        });

        queue3.Enqueue(new Artista
        {
            ArtistId = 2,
            Name = "Lilian"
        });

        queue3.Enqueue(new Artista
        {
            ArtistId = 3,
            Name = "Bob Esponja"
        });

        // Al momento de iterar sobre la estructura, este nos devolvera el orden en el cual se fueron agregando a la estructura
        foreach(var item in queue3)
        {
            Console.WriteLine($"Hola soy el artista {item.ArtistId}, me llamo {item.Name}.");
        }

        // Para eliminar elementos de esta estructura tenemos dos funciones
        /*
         * Dequeue(), Este elimina el primer elemento pero lo devuelve
         */
        var eliminadoDequeue = queue3.Dequeue();
        Console.WriteLine("Elimnado:" + eliminadoDequeue.Name);

        foreach (var item in queue3)
        {
            Console.WriteLine($"Hola soy el artista {item.ArtistId}, me llamo {item.Name}.");
        }

        // Para acceder elementos de esta estructura tenemos dos funciones
        /*
         * Peek(), Accede al primer elemento pero no lo elimina
         * FirstOrDefault(lamda)
         */
        var accederPeek = queue3.Peek();
        Console.WriteLine($"Accedido a {accederPeek.Name}");

        var accederId = queue3.FirstOrDefault(x => x.ArtistId == 3);

        // Para actualizar datos de algún elemento en esta estructura hacemos lo siguiente:
        var actualizarQueue3 = queue3.FirstOrDefault(x => x.ArtistId == 2);
        actualizarQueue3.Name = "Adalberta";
        Console.WriteLine(actualizarQueue3.Name);
    }

    private static void _Array()
    {
        /*
         * Los Array son una colección ordenada de elementos los cuales tienen un índice identificador.
         * Muchas de las estructuras de datos que utilizamos son en realidad Arrays con funcionalidades añadidas.
         * En C# al utilizar Arrays debemos especificar el tamaño al momento de crear la instancia y tambien el tipo.
         * Además los arrays como la mayoria de estructuras de datos empiezan con el índice 0
         */
        Console.WriteLine("------------- Array ----------------");

        string[] array = new string[10];

        // Para agregar un nuevo elemento debemos seguir lo siguiente
        // nombre[indice_ordenado] = valor;
        array[0] = "Lilian";
        array[1] = "Estuardo";
        Console.WriteLine(array[0], array[1]);

        // Para acceder a un índice en específico deberás de hacer lo siguiente:
        // nombre[indice_a_acceder]
        Console.WriteLine(array[1]);

        // Para actualizar un array deberás de seguir lo siguiente:
        // nombre[indice_a_actualizar] = nuevo_valor;
        array[0] = "Lili";
        Console.WriteLine(array[0]);

        // Para "eliminar" elementos de los arrays se puede lograr de la siguiente manera
        array[1] = null;
        Console.WriteLine(array[1]);        
    }

    private static void _List() 
    {
        /*
         * Las listas en C# utilizan Arrays "under the hood (Bajo el capó)" pero fueron optimizadas para el uso en caso de
         * que no se sepa el tamaño de la lista.
         */
        Console.WriteLine("------------- List ----------------");

        // Inicializar una lista
        List<string> list = new List<string>();

        // Agregar elementos a la lista
        list.Add("Lilian");
        list.Add("Estuardo");
        list.Add("Pentium");

        // Ver la cantidad de elementos que tiene nuestra lista
        Console.WriteLine(list.Count);

        // Podemos ver si existe algún valor en específico
        Console.WriteLine(list.Contains("Carro"));

        // Obtener objetos específicos
        Console.WriteLine(list.Find(x => x == "Estuardo"));

        // Actualizar un valor específico
        list[1] = "ESTUARDO";
        Console.WriteLine(list[1]);

        // Eliminar elementos
        list.Remove("Pentium");

        // Recorrer la lista
        list.ForEach(x => Console.WriteLine(x));
    }

    private static void _Dictionary() {
        /*
         * Para crear un diccionario en C# únicamente debemos intanciarlo, los diccionarios es una colección para almacenar datos de forma "clave-valor"
         * los cuales pueden ser de diferente tipos de datos.
         */
        Console.WriteLine("------------- Dictionary ----------------");

        // Instanciar un diccionario
        Dictionary<string, string> dict = new Dictionary<string, string>();

        // Agregar elementos
        dict.Add("Mujer", "Lilian");
        dict.Add("Hombre", "Estuardo");

        // Acceder a un elemento, para ello debemos usar su clave
        Console.WriteLine(dict["Mujer"]);
        Console.WriteLine(dict["Hombre"]);

        // Paraa ctualizar un elemento lo hacemos por medio de su clave
        dict["Hombre"] = "ESTUARDO";
        Console.WriteLine(dict["Hombre"]);

        // Para eliminar tenemos dos opciones
        // Remove: Elininaras por medio de su clave
        // Clear: Limpia todo el diccionario
        dict.Remove("Mujer");
        Console.WriteLine(dict);
    }

    private static void _Stack() {
        /*
         *  Esta estrucutra de datos sigue el consejo de pila "Último en entrar, primero en salir"
         *  Al igual que las demás estructuras de datos debemos inicializarla
         */
        Console.WriteLine("------------- Stack ----------------");

        // Inicializar Stack o crear el objeto Stack
        Stack<string> stack = new Stack<string>();

        // Agregar valores a la estructura
        stack.Push("C#");
        stack.Push("Python");
        stack.Push("Java");

        // Para ver el último elemento que añadimos
        Console.WriteLine(stack.Peek());

        // Para remover el último elemento que fue añadido
        stack.Pop();
        Console.WriteLine(stack.Peek());

        // Buscar un valor específico
        Console.WriteLine(stack.FirstOrDefault(x => x.Equals("C#")));
    }

    private static void Agenda()
    {
        Console.WriteLine();
        Console.WriteLine();
        List<Contacto> contactos = new List<Contacto>();
        int opcion = -1;

        Console.WriteLine("---- Bienvenido a tu agenda de contactos ----");

        while (opcion != 0)
        {
            Console.WriteLine();
            Console.WriteLine();
            Console.WriteLine();
            Console.WriteLine("¿Qué deseas hacer?");
            Console.WriteLine("[1] - Buscar contacto");
            Console.WriteLine("[2] - Agregar contacto");
            Console.WriteLine("[3] - Actualizar contacto");
            Console.WriteLine("[4] - Eliminar Contacto");
            Console.WriteLine("[0] - Salir ");

            Console.Write("Escoje una opción: ");
            try { 
                opcion = Convert.ToInt32(Console.ReadLine());

                switch (opcion){
                    case 0:
                        Console.WriteLine("Adios");
                        break;
                    case 1:
                        Search();
                        break;
                    case 2:
                        Create();
                        break;
                    case 3:
                        Update();
                        break;
                    case 4:
                        Delete();
                        break;
                }
            }catch(Exception)
            {
                Console.WriteLine("Por favor escoge una opción correcta");
            }
        }

        void Search()
        {
            string dato;
            Console.WriteLine("Escribe el número de teléfono o nombre del contacto: ");
            dato = Console.ReadLine();

            var busqueda = contactos.FirstOrDefault(x => x.Name == dato || x.Number_Phone == dato);
            if (busqueda != null)
            {
                Console.WriteLine("Tu contacto: ");
                Console.WriteLine($"Nombre: {busqueda.Name}");
                Console.WriteLine($"Número: {busqueda.Number_Phone}");
                Thread.Sleep(1000);
                Console.WriteLine("Regresando...");
                Thread.Sleep(1000);
            }
            
        }

        void Create()
        {
            string dato1;
            Int64 dato2;
            string dato3;

            Console.WriteLine("-- Creando Nuevo Contacto --");
            Console.WriteLine("Nombre de tu contacto:");
            dato1 = Console.ReadLine();
            Console.WriteLine("Número de telefono de tu contacto:");
            try
            {
                dato2 = Convert.ToInt64(Console.ReadLine());
                if (dato2 < 0 || dato2 > 99999999999)
                {
                    Console.WriteLine("Error, no se permite esa longitud del número");
                }

                dato3 = Convert.ToString(dato2);
                contactos.Add(new Contacto
                {
                    Name = dato1,
                    Number_Phone = dato3,
                });

                Console.WriteLine("Contacto Guardado.");
                Thread.Sleep(1000);
                Console.WriteLine("Regresando...");
                Thread.Sleep(1000);
            }
            catch
            {
                Console.WriteLine("Error, solo se permiten números");
            }

        }

        void Update()
        {
            int option;

            Console.WriteLine("¿Qué deseas editar?");
            Console.WriteLine("[1] - Editar Nombre");
            Console.WriteLine("[2] - Editar número");

            try
            {

                option = Convert.ToInt32(Console.ReadLine());
                switch (option)
                {
                    case 1:
                        string dato;
                        Console.WriteLine("Escribe el número de teléfono o nombre del contacto: ");
                        dato = Console.ReadLine();

                        var busqueda = contactos.FirstOrDefault(x => x.Name == dato || x.Number_Phone == dato);
                        if (busqueda != null)
                        {
                            string nuevo;
                            Console.WriteLine("Escribe el nuevo nombre: ");
                            nuevo = Console.ReadLine();
                            busqueda.Name = nuevo;
                        }
                        else
                        {
                            Console.WriteLine("Contacto no encontrado.");
                        }
                        break;
                    case 2:
                        string dato2;
                        Int64 dato3;

                        Console.WriteLine("Escribe el número de teléfono o nombre del contacto: ");
                        dato = Console.ReadLine();

                        var busqueda2 = contactos.FirstOrDefault(x => x.Name == dato || x.Number_Phone == dato);
                        if (busqueda2 != null)
                        {
                            string nuevo;
                            Console.WriteLine("Escribe el nuevo número: ");
                            nuevo = Console.ReadLine();

                            dato3 = Convert.ToInt64(nuevo);
                            if (dato3 < 0 || dato3 > 99999999999)
                            {
                                Console.WriteLine("Error, no se permite esa longitud del número");
                            }
                            else
                            {
                                busqueda2.Number_Phone = nuevo;
                                Console.WriteLine("Contacto Guardado.");
                                Thread.Sleep(1000);
                                Console.WriteLine("Regresando...");
                                Thread.Sleep(1000);
                            }
                        }
                        else
                        {
                            Console.WriteLine("Contacto no encontrado.");
                        }


                        break;
                    default:
                        Console.WriteLine("No existe esa opcion");
                        break;
                }
            }
            catch
            {
                Console.WriteLine("Error");
            }
        }

        void Delete()
        {
            string datos;

            Console.WriteLine("Escribe el número de teléfono o nombre del contacto: ");
            datos = Console.ReadLine();
            var contact = contactos.FirstOrDefault(x => x.Name == datos || x.Number_Phone == datos);
            contactos.RemoveAll(x => x.Name == datos || x.Number_Phone == datos);

            if (contact != null)
            {
                Console.WriteLine("Eliminando");
                Thread.Sleep(1000);
                Console.WriteLine("Saliendo...");
                Thread.Sleep(1000);
            }
            else
            {
                Console.WriteLine("Contacto no encontrado.");
            }
        }
    }
}
