using System.Collections.Immutable;

namespace elmarqueli
{
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
    public class EjercicioArray
    {
        static int[] m_array = Array.Empty<int>();

        public EjercicioArray(int[] nums)
        {
            m_array = nums;
        }
        /// <summary>
        /// Imprime los elementos del array.
        /// </summary>
        public void Print(string Prompt)
        {
            Console.Write(Prompt);
            foreach (int elemento in m_array)
            {
                Console.Write($" {elemento}");
            }
            Console.WriteLine("\n");
        }

        /// <summary>
        /// Inserta 2 numeros mas al array
        /// </summary>
        public void Insert(int Value)
        {
            Array.Resize(ref m_array, m_array.Length + 1);
            m_array[m_array.Length - 1] = Value;
        }

        /// <summary>
        /// Ordena el array.
        /// </summary>
        public void Sort()
        {
            Array.Sort(m_array);
        }

        /// <summary>
        /// Eliminacion de un elemento en el array
        /// </summary>
        /// <param name="Value"></param>
        public void Delete(int Value)
        {
            // Creamos una nueva lista excluyendo al elemento a eliminar.
            var new_array = m_array.Where(x => x != Value).ToArray();

            // Redimiencionamos el array con una posision menos.
            Array.Resize(ref m_array, m_array.Length - 1);

            // Finalmente asignamos el valor del array nuevo al redimensionado.
            m_array = new_array;
        }

        /// <summary>
        /// Actualiza el array modificando la posision 5 y 6
        /// </summary>
        public void UpDate(int Index, int Value)
        {
            m_array[Index] = Value;
        }

        /// <summary>
        /// Permite la modificacion de un elemento en la coleccion.
        /// Utilice la funcion predicate para buscar el elemento a modificar
        /// </summary>
        /// <param name="Element">Elemento en la coleccion</param>
        /// <param name="Value">Valor para la actualizacion</param>
        /// <returns>Verdadero si la actualizacion fue correcta</returns>
        public bool UpDate(Predicate<int> Element, int Value)
        {
            Sort();
            var index = -1;

            for (int i = 0; i < m_array.Length; i++)
            {
                if (Element.Invoke(m_array[i]))
                {
                    index = i; break;
                };
            }

            if (index == -1)
                return false;

            m_array[index] = Value;
            this.Sort();

            return true;
        }
    }

    public class EjercicioList
    {
        private List<int> m_Ints;
        public EjercicioList(List<int> Ints)
        {
            m_Ints = Ints;
        }
        public void Print(string Prompt)
        {
            Console.Write(Prompt);
            m_Ints.ToList().ForEach((x) => {
                Console.Write($" {x}");
            });
            Console.WriteLine("\n");
        }

        public void Insert(int Value)
        {
            m_Ints.Add(Value);
        }

        public void Sort()
        {
            m_Ints.Sort();
        }

        public void Delete(int Value)
        {
            m_Ints.Remove(Value);
        }

        /// <summary>
        /// Permite modificar un elemento de la coleccion
        /// </summary>
        public void UpDate(int Index, int Value)
        {
            m_Ints[Index] = Value;
        }

        /// <summary>
        /// Permite modificar un elemento de la coleccion
        /// Utilice la funcion predicate para buscar el elemento a modificar.
        /// </summary>
        /// <param name="Match">Elemento en la coleccion</param>
        /// <param name="Value">Valor para la actualizacion</param>
        /// <returns>Verdadero si la actualizacion fue correcta</returns>
        public bool UpDate(Predicate<int> Match, int Value)
        {
            Sort();
            var index = -1;

            index = m_Ints.FindIndex((x) => Match.Invoke(x));

            if (index == -1) return false;

            m_Ints[index] = Value;

            this.Sort();

            return true;
        }
    }

    public class EjercicioStack
    {
        // último en entrar, primero en salir
        private Stack<int> m_Ints;
        public EjercicioStack(Stack<int> ints)
        {
            m_Ints = ints;
        }

        public void Print(string Prompt)
        {
            Console.Write(Prompt);
            m_Ints.ToList().ForEach((x) => {
                Console.Write($" {x}");
            });
            Console.WriteLine("\n");
        }

        public void Insert(int Value)
        {
            m_Ints.Push(Value);
        }

        /// <summary>
        /// Elimina el ultimo en entrar.
        /// </summary>
        /// <returns>Número eliminado</returns>
        public int Delete()
        {
            return m_Ints.Pop();
        }
    }

    public class EjercicioQueue
    {
        // Primero en entrar, primero en salir
        private Queue<int> m_Queue;
        public EjercicioQueue(Queue<int> ints)
        {
            m_Queue = ints;
        }
        /// <summary>
        /// Imprime el contenido de la colección
        /// </summary>
        /// <param name="Prompt"></param>
        public void Print(string Prompt)
        {
            Console.Write(Prompt);
            m_Queue.ToList().ForEach((x) => {
                Console.Write($" {x}");
            });
            Console.WriteLine("\n");
        }

        /// <summary>
        /// Agrega un número a la colección
        /// </summary>
        /// <param name="Value"></param>
        public void Insert(int Value)
        {
            m_Queue.Enqueue(Value);
        }

        /// <summary>
        /// Quita el primer número agregado recientemente.
        /// </summary>
        public int Delete()
        {
            return m_Queue.Dequeue();
        }
    }

    public class EjercicioHashSet
    {
        // Establecemos la variable para la colección
        private HashSet<int> m_Set;
        public EjercicioHashSet(HashSet<int> ints)
        {
            // Inicializamos la colección
            m_Set = ints;
        }

        public void Print(string Prompt)
        {
            Console.Write(Prompt);
            m_Set.ToList().ForEach((x) => {
                Console.Write($" {x}");
            });
            Console.WriteLine("\n");
        }

        /// <summary>
        /// Agrega un nuevo número.
        /// </summary>
        /// <param name="Value"></param>
        public void Insert(int Value)
        {
            m_Set.Add(Value);
        }

        /// <summary>
        /// Quita el número indicado.
        /// </summary>
        /// <param name="Value"></param>
        public void Delete(int Value)
        {
            m_Set.Remove(Value);
        }

        /// <summary>
        /// Ordena la colección
        /// </summary>
        public void Sort()
        {
            var newHashSet = new HashSet<int>();
            m_Set.ToImmutableSortedSet().ToList().ForEach(x =>
            {
                newHashSet.Add(x);
            });

            m_Set = newHashSet;
        }
    }

    public class EjercicioDictionary
    {
        private Dictionary<int, string> m_Dictionary;
        public EjercicioDictionary(Dictionary<int, string> dictionary)
        {
            m_Dictionary = dictionary;
        }

        /// <summary>
        /// Imprime la coleccion.
        /// </summary>
        /// <param name="Prompt"></param>
        public void Print(string Prompt)
        {
            Console.Write(Prompt);
            m_Dictionary.ToList().ForEach((x) => {
                Console.Write($" {x}");
            });
            Console.WriteLine("\n");
        }

        /// <summary>
        /// Inserta un nuevo registro.
        /// </summary>
        /// <param name="Id"></param>
        /// <param name="Nombre"></param>
        /// <returns></returns>
        public bool Insert(int Id, string Nombre)
        {
            if (!m_Dictionary.ContainsKey(Id))
            {
                m_Dictionary.Add(Id, Nombre);
                return true;
            }
            else
                return false;
        }

        /// <summary>
        /// Elimina un registro excistente.
        /// </summary>
        /// <param name="Id"></param>
        public void Delete(int Id)
        {
            m_Dictionary.Remove(Id);
        }

        /// <summary>
        /// Actualiza un registro.
        /// </summary>
        /// <param name="id"></param>
        /// <param name="Nombre"></param>
        public void UpDate(int id, string Nombre)
        {
            m_Dictionary[id] = Nombre;
        }

        /// <summary>
        /// Ordena la coleccion.
        /// </summary>
        public void Sort()
        {
            var ff = new Dictionary<int, string>();
            var sorted = new SortedDictionary<int, string>(m_Dictionary);
            sorted.ToList().ForEach(x => ff.Add(x.Key, x.Value));
            m_Dictionary = ff;
        }
    }

    // ***** Extra: Programa, Agenda de Contactos (AddressBook)
    public static class AddressBook
    {
        private static string m_Nombre = string.Empty;
        private static int m_TelefonNumber;
        private static Dictionary<int, Action>? m_ActionMenu;
        private static Dictionary<string, int>? m_Agenda;
        static AddressBook()
        {
            m_Agenda = new Dictionary<string, int>();

            // Podemos crear un diccionario con el numero de la opcion, y la funcion correspondiente,
            // de esta manera en el futuro podremos extender la funsionalidad de la agenda agegando funciones
            // y agregando estas al diccionario => m_ActionMenu
            m_ActionMenu = new Dictionary<int, Action>();
            m_ActionMenu.Add(1, MenuFind);
            m_ActionMenu.Add(2, MenuInsert);
            m_ActionMenu.Add(3, MenuUpDate);
            m_ActionMenu.Add(4, MenuDelete);
            m_ActionMenu.Add(5, MenuExit);
        }

        static public void InitProgram() => MainMenu();

        static Action PrintOptions = () =>
        {
            Console.Clear();
            Console.WriteLine("*** Menú Principal Agenda ***\n");

            Console.WriteLine("---- Seleccione una de las siguientes opciones:\n");

            Console.WriteLine("1 - Buscar contacto...\n");
            Console.WriteLine("2 - Agregar contacto...\n");
            Console.WriteLine("3 - Modificar contacto...\n");
            Console.WriteLine("4 - Eliminar contacto...\n");
            Console.WriteLine("5 - Exit\n");

            Console.Write("Seleccione una opcion: ");
            var option = Console.ReadLine();

            // Verificamos que sea de tipo número.
            if (int.TryParse(option, out int op))
            {
                var actionMenu = m_ActionMenu[op];
                actionMenu.Invoke();
            }
            else
            {
                Console.WriteLine("La opcion ingresada debe ser un número entero, intente nuevamente.\nPresione Enter para continuar....");
                Console.ReadLine();
                PrintOptions();
            }
        };

        static void MainMenu()
        {
            PrintOptions();
        }

        static void MenuInsert()
        {
            Console.Clear();
            Console.WriteLine("*** Menú Agregar Contacto ***\n");

            Console.Write("Escriba el Nombre: ");
            var name = Console.ReadLine();
            Console.Write("Escriba un numero de telefono de asta 11 digitos: ");
            var telefon = Console.ReadLine();

            if (int.TryParse(telefon, out int op) && telefon.Count() <= 11)
            {
                if (!m_Agenda.ContainsKey(name))
                {
                    m_Agenda.Add(name, op);
                    Console.WriteLine("\nContacto ingresado con exito!!.\nEnter para Menu Principal.");
                    Console.ReadLine();
                    MainMenu();
                }
                else
                {
                    Console.WriteLine("El contacto ya existe!!.\nPresione Enter para continuar....");
                    Console.ReadLine();
                    MenuInsert();
                }
            }
            else
            {
                Console.WriteLine("Error!!, número telefonico no valido!.\nPresione Enter para continuar....");
                Console.ReadLine();
                MenuInsert();
            }
        }

        static void MenuDelete()
        {
            Console.Clear();
            Console.WriteLine("*** Menú Eliminar Contacto ***\n");

            Console.Write("Escriba Nombre del contacto: ");
            var name = Console.ReadLine();

            if (!m_Agenda.ContainsKey(name))
            {
                m_Agenda.Remove(name);
                Console.WriteLine("\nContacto eliminado con exito!!.\nEnter para Menu Principal.");
                Console.ReadLine();
                MainMenu();
            }
            else
            {
                Console.WriteLine("El contacto no existe!!.\nPresione Enter para continuar....");
                Console.ReadLine();
                MenuInsert();
            }
        }

        static void MenuUpDate()
        {
            Console.Clear();
            Console.WriteLine("*** Menú Modificar Contacto ***\n");

            Console.WriteLine("1 - Modificar el nombre");

            Console.WriteLine("2 - Modificar el Telefono");

            Console.WriteLine("3 - Menu Principal");

            var opt = Console.ReadLine();

            if (int.TryParse(opt, out int op))
            {
                Console.Write("Nombre del contacto a modificar: ");
                var name = Console.ReadLine();

                if (m_Agenda.ContainsKey(name))
                {
                    var reName = "";
                    switch (op)
                    {
                        case 1:
                            Console.Write("Nuevo nombre: ");
                            reName = Console.ReadLine();

                            var newValues = new KeyValuePair<string, int>(reName, m_Agenda[name]);

                            m_Agenda.Remove(name);
                            m_Agenda.Append(newValues);

                            Console.WriteLine("\nContacto Modificado con exito!!.\nEnter para continuar.");
                            Console.ReadLine();
                            MenuUpDate();
                            break;
                        case 2:
                            bool exit = false;
                            while (!exit)
                            {
                                Console.Write("Número de telefono nuevo, no mas de 11 digitos: ");
                                reName = Console.ReadLine();
                                if (int.TryParse(reName, out int o) && reName.Count() <= 11)
                                {
                                    m_Agenda[name] = (o);
                                    Console.WriteLine("\nContacto Modificado con exito!!.\nEnter para continuar.");
                                    Console.ReadLine();
                                    MenuUpDate();
                                    exit = true;
                                }
                            }
                            break;
                        case 3:
                            MainMenu();
                            break;
                    }
                }
                else
                {
                    Console.WriteLine("El contacto no existe!!.\nPresione Enter para continuar....");
                    Console.ReadLine();
                    MenuUpDate();
                }
            }
            else
            {
                Console.WriteLine("Error!!, opcion no valida!.\nPresione Enter para continuar....");
                Console.ReadLine();
                MenuUpDate();
            }
        }

        static void MenuFind()
        {
            Console.Clear();
            Console.WriteLine("*** Menú Buscar Contacto ***\n");

            Console.Write("Escriba el Nombre ó exit para Menu principal: ");
            var name = Console.ReadLine();

            if (m_Agenda.ContainsKey(name))
            {
                m_Agenda.ToList().ForEach(x =>
                {
                    Console.WriteLine($"\n Nombre: {x.Key} - Telefono {x.Value}");
                });
                Console.ReadLine();
                MainMenu();
            }
            else if (name.ToLower() == "exit")
                MainMenu();
            else
            {
                Console.WriteLine("El contacto no existe!!.\nPresione Enter para continuar....");
                Console.ReadLine();
                MenuFind();
            }
        }

        static void MenuExit()
        {
            Console.Clear();
            Console.WriteLine("Gracias por usar AddressBook, Saliendo de la aplicacion....");
            Console.ReadLine();
            Environment.Exit(0);
        }
    }


  class Program
	{
		static void Main(string[] args)
		{
            var numRetire = 0;

            Console.WriteLine("***** Array ******\n");

            var EjrArray = new EjercicioArray(new int[] { 1, 2, 5, 7, 3, 4 ,11});

            EjrArray.Print("Array actual:");

            EjrArray.Delete(4);

            EjrArray.Print("Eliminando el número { 4 }:");

            EjrArray.Insert(4);

            EjrArray.Print("Insertando el núemro { 4 }:");

            EjrArray.Sort();

            EjrArray.Print("Array ordenado:");

            if (EjrArray.UpDate((x) => x == 11, 6))
                EjrArray.Print("Actualización correcta!!! se cambio el { 11 } por el { 6 }:");
            else
                Console.WriteLine("El elemento a modificar no se encuentra!!!");


            // **************************************************************

            Console.WriteLine("***** List ******\n");

            var EjrList = new EjercicioList(new List<int> { 1, 3, 2, 5, 4, 11, 12 });

            EjrList.Print("Lista actual:");

            EjrList.Sort();

            EjrList.Print("Lista ordenada:");

            EjrList.Insert(6);

            EjrList.Print("Elemento { 6 } insertado:");

            EjrList.Delete(12);

            EjrList.Print("Elemento { 12 } eliminado crrectamente:");

            if (EjrList.UpDate((x) => x == 11, 7))
                EjrList.Print("Actualizacion Correcta!! se cambio el { 11 } por el { 7 }:");
            else
                Console.WriteLine("Actualizacion Incirrecta, no existe el elemento a acutalizar!!");

            // **************************************************************

            Console.WriteLine("***** Stack ******\n");

            var EjrStack = new EjercicioStack(new Stack<int>(new int[] { 1, 2, 3, 5 }));

            EjrStack.Print("Pila actual:");

            EjrStack.Insert(6);

            EjrStack.Print("Número { 6 } agregado a la pila:");

            numRetire = EjrStack.Delete();

            EjrStack.Print($"Quitando de la pila el ultimo número agregado: [{numRetire}] ->");

            // **************************************************************

            Console.WriteLine("***** Queue ******\n");

            var EjrQueue = new EjercicioQueue(new Queue<int>(new int[] {2, 1, 4, 8, 6}));

            EjrQueue.Insert(3);

            EjrQueue.Print("Agregando a la cola el numero { 3 }:");

            numRetire =  EjrQueue.Delete();

            EjrQueue.Print($"Quitando de la cola el primer número agregado:[{numRetire}] ->");

            // **************************************************************

            Console.WriteLine("***** HashSet ******\n");

            var EjrHashSet = new EjercicioHashSet(new HashSet<int>() { 1,2,3,4,6,5});

            EjrHashSet.Print("Lista HashSet acutal:");

            EjrHashSet.Insert(7);

            EjrHashSet.Print("Agregando el número { 7 }:");

            // Como el número 7 ya esta agergado anteriormente este no se agregara otra ves
            EjrHashSet.Insert(7);

            EjrHashSet.Print("Queriendo Agregando el número { 7 } nuevamente:");

            EjrHashSet.Sort();
            
            EjrHashSet.Print("Ordenando el HashSet:");

            EjrHashSet.Delete(7);

            EjrHashSet.Print("Quitando el número { 7 }:");

            // **************************************************************

            Console.WriteLine("***** Dictionary ******\n");

            var EjrDictionary = new EjercicioDictionary(new Dictionary<int, string>() { { 0, "Pablo" },{3,"Carol"}, { 1, "Roberto" }, { 2,"Romina"} });

            EjrDictionary.Print("Diccionario actual:");

            // No se insertara ya que el id 3 ya exciste.
            if(!EjrDictionary.Insert(3, "Guillermo"))
                Console.WriteLine("Se quiere agregar a Guillermo con el { id 3 } pero este id ya existe!!\n");
            else
                EjrDictionary.Print("El registro { 3, Guillermo } a sido ingresado con exito!!:");

            if (!EjrDictionary.Insert(4, "Romina Piriz"))
                Console.WriteLine("Se quiere agregar a Romina con el { id 4 } pero este ya existe!!\n");
            else
                EjrDictionary.Print("El registro { 4, Romina Piriz } a sido ingresado con exito!!:");

            EjrDictionary.Sort();
            EjrDictionary.Print("Diccionario ordenado:");

            EjrDictionary.Delete(0);
            EjrDictionary.Print("Se a eliminado el registro { 0 }:");

            EjrDictionary.UpDate(3, "Carol Sofia");
            EjrDictionary.Print("Se a actualizado el registro { 3 }:");


            // **************************************************************

            Console.WriteLine("\n\n========== Extra: Programa Agenda ==========\n");

            AddressBook.InitProgram();
        }
    }
}
