using System.Numerics;

namespace _03_estructuras
{
    internal class Program
    {
        public static Dictionary<string, int> myContacts = new Dictionary<string, int>();
        
        static void Main(string[] args)
        {
            /*
              * EJERCICIO:
              * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
              *   en tu lenguaje.
              * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
              *
              * DIFICULTAD EXTRA (opcional):
              * Crea una agenda de contactos por terminal.
              * - Debes implementar funcionalidades de búsqueda, inserción, actualización
              *   y eliminación de contactos.
              * - Cada contacto debe tener un nombre y un número de teléfono.
              * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
              *   y a continuación los datos necesarios para llevarla a cabo.
              * - El programa no puede dejar introducir números de teléfono no númericos y con más
              *   de 11 dígitos (o el número de dígitos que quieras).
              * - También se debe proponer una operación de finalización del programa.
              */


            // ------------------ ESTRUCTURAS DE DATOS
            // ------------------ Queue
            Console.WriteLine(" ------------------ QUEUE ------------- ");
            var queue = new Queue<Contact>();

            Console.WriteLine(" --- Insertar en la cola");
            // Insertar en la cola
            queue.Enqueue(new Contact("Juan", 65959494));
            queue.Enqueue(new Contact("Maria", 4949594));
            queue.Enqueue(new Contact("Xavi", 9394399));
            queue.Enqueue(new Contact("Susan", 34935959));
            queue.Enqueue(new Contact("Ricardo", 34934599));
            foreach (var contact in queue)
            {
                Console.WriteLine($"Nombre: {contact.name}, Telefono: {contact.phoneNumber}");
            }

            Console.WriteLine(" --- Eliminar primer elemento de la cola");
            // Eliminar el primer elemento de la cola
            queue.Dequeue();
            foreach (var contact in queue)
            {
                Console.WriteLine($"Nombre: {contact.name}, Telefono: {contact.phoneNumber}");
            }

            Console.WriteLine(" --- Ordenación");
            // Ordenación
            queue.Order();

            // Actualizar un elemento
            Console.WriteLine(" --- Actualizar un elemento de la cola");
            queue.Peek().name = "Manuel";
            foreach (var contact in queue)
            {
                Console.WriteLine($"Nombre: {contact.name}, Telefono: {contact.phoneNumber}");
            }

            Console.WriteLine(" --- Eliminar todos los elementos de la cola");
            // Borra todos los elementos
            queue.Clear();
            foreach (var contact in queue)
            {
                Console.WriteLine($"Nombre: {contact.name}, Telefono: {contact.phoneNumber}");
            }





            // ------------------ Array
            Console.WriteLine("\r\n\r\n ------------------ ARRAY ------------- ");
            Console.WriteLine(" --- Insertar en array");
            // Insertar en el array
            var contactsArray = new Contact[3];
            contactsArray[0] = new Contact("Pedro", 4969696);
            contactsArray[1] = new Contact("Rodrigo", 8695949);
            contactsArray[2] = new Contact("Miriam", 9359595);
            foreach (var contact in contactsArray)
            {
                if (contact == default) continue;
                Console.WriteLine($"{contact.name} - {contact.phoneNumber}");
            }

            Console.WriteLine(" --- Ordenación del array");
            // Ordenación
            contactsArray.Order();

            // Actualizar un elemento
            Console.WriteLine(" --- Actualizar un elemento del array");
            contactsArray[1].name = "Actualizado";
            foreach (var contact in contactsArray)
            {
                Console.WriteLine($"Nombre: {contact.name}, Telefono: {contact.phoneNumber}");
            }




            // ------------------ List
            Console.WriteLine("\r\n\r\n ------------------ LIST ------------- ");
            Console.WriteLine(" --- Insertar en una list");
            // Insertar en el list
            var contactList = new List<Contact>();
            contactList.Add(new Contact("Pedro", 4969696));
            contactList.Add(new Contact("Marlo", 5848438));
            contactList.Add(new Contact("Susana", 34838348));
            foreach (var contact in contactList)
            {
                if (contact == default) continue;
                Console.WriteLine($"{contact.name} - {contact.phoneNumber}");
            }

            // Cantidad total de elementos en la lista
            Console.WriteLine($"Contactos en la lista: {contactList.Count}");

            // Encontrar objetos por propiedades especificas
            Console.WriteLine($"Encuentra el teléfono del contacto Pedro: {contactList.Find(x => x?.name == "Pedro").phoneNumber}");
            foreach (var contact in contactList)
            {
                if (contact == default) continue;
                Console.WriteLine($"{contact.name} - {contact.phoneNumber}");
            }

            // Actualizar un elemento
            Console.WriteLine(" --- Actualizar un elemento de la lista");
            contactList[0].phoneNumber = 2;
            foreach (var contact in contactList)
            {
                Console.WriteLine($"Nombre: {contact.name}, Telefono: {contact.phoneNumber}");
            }

            Console.WriteLine(" --- Ordenación de la lista");
            // Ordenación
            contactList.Order();

            Console.WriteLine(" --- Eliminar todos los elementos de la lista");
            // Borra todos los elementos
            contactList.Clear();
            foreach (var contact in contactList)
            {
                Console.WriteLine($"Nombre: {contact.name}, Telefono: {contact.phoneNumber}");
            }




            // ------------------ Stack
            Console.WriteLine("\r\n\r\n ------------------ STACK ------------- ");
            Console.WriteLine(" --- Insertar en una stack");
            // Insertar en el stack
            var stackContact = new Stack<Contact>();
            stackContact.Push(new Contact("Pedro", 4969696));
            stackContact.Push(new Contact("Maria", 943943));
            stackContact.Push(new Contact("Sandra", 34835843));
            stackContact.Push(new Contact("Georgina", 2384848));
            foreach (var contact in stackContact)
            {
                if (contact == default) continue;
                Console.WriteLine($"{contact.name} - {contact.phoneNumber}");
            }

            // Pop para remover el último elemento que fue añadido a nuestro stack.
            stackContact.Pop();

            foreach (var contact in stackContact)
            {
                if (contact == default) continue;
                Console.WriteLine($"{contact.name} - {contact.phoneNumber}");
            }

            // Peek para ver el ultimo elemento que añadimos.
            Console.WriteLine(stackContact.Peek().name);


            Console.WriteLine(" --- Ordenación del stack");
            // Ordenación
            stackContact.Order();

            Console.WriteLine(" --- Eliminar todos los elementos del stack");
            // Borra todos los elementos
            stackContact.Clear();
            foreach (var contact in stackContact)
            {
                Console.WriteLine($"Nombre: {contact.name}, Telefono: {contact.phoneNumber}");
            }




            // ------------------ Dictionary
            Console.WriteLine("\r\n\r\n ------------------ DICTIONARY ------------- ");
            Console.WriteLine("--- Detallado en el ejercicio");


            // ------------------ Crea una agenda de contactos por terminal
            Console.WriteLine("\r\n\r\n ------------------ EXAMPLE ------------- ");
            int option = 0;

            do
            {
                Console.WriteLine($"Seleccione una opción:\r\n" +
                    $"1 - Buscar contacto\r\n" +
                    $"2 - Insertar contacto\r\n" +
                    $"3 - Actualizar contacto\r\n" +
                    $"4 - Eliminar contacto\r\n" +
                    $"5 - Salir");

                int.TryParse(Console.ReadLine(), out option);

                switch (option)
                {
                    case 1:
                        // Buscar contacto
                        BuscarContacto();
                        break;

                    case 2:
                        // Insertar contacto
                        InsertarContacto();
                        break;

                    case 3:
                        // Actualizar contacto
                        ActualizarContacto();
                        break;

                    case 4:
                        // Eliminar contacto
                        EliminarContacto();
                        break;

                    case 5:
                        // Salir
                        option = 5;
                        break;

                    case 0:
                    default:
                        Console.WriteLine("Opción no disponible.");
                        Console.ReadKey();
                        break;
                }

                Console.Clear();

            } while (option != 5);
        }


        public static void ShowContacts()
        {
            try
            {
                Console.WriteLine("Lista de contactos:");
                foreach (KeyValuePair<string, int> kvp in myContacts)
                {
                    Console.WriteLine($"{kvp.Key} - {kvp.Value}");
                }

            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }
        }

        /// <summary>
        /// Función para buscar contacto en la agenda
        /// </summary>
        public static void BuscarContacto()
        {
            try
            {
                if (myContacts.Count > 0)
                {
                    // Mostrar todos los contactos de la agenda
                    ShowContacts();

                    // Buscar el contacto en concreto
                    Console.WriteLine("Introduzca el nombre del contacto:");
                    string name = Console.ReadLine();

                    if (myContacts.TryGetValue(name, out var value))
                    {
                        Console.WriteLine($"{name} - {value}");
                    }
                    else
                    {
                        Console.WriteLine("Contacto no encontrado");
                        Console.ReadKey();
                    }
                } 
                else
                {
                    Console.WriteLine("No existen contactos en la agenda");
                    Console.ReadKey();
                }

            } catch(Exception e) { 
                Console.WriteLine(e.ToString());
            }

        }

        /// <summary>
        /// Función para insertar contacto en la agenda
        /// </summary>
        public static void InsertarContacto()
        {
            try
            {
                Console.WriteLine("Introduzca nombre del contacto:");
                string name = Console.ReadLine();

                // Verificar si nombre (clave ya existe en el diccionario);
                if (myContacts.TryGetValue(name, out var value))
                {
                    Console.WriteLine("Contacto ya existente");
                    Console.ReadKey();
                }
                else
                {
                    Console.WriteLine("Introduzca número de teléfono:");
                    int.TryParse(Console.ReadLine(), out int phoneNumber);

                    double data = Math.Floor(Math.Log10(phoneNumber) + 1);

                    if (data > 0 && data < 11)
                    {
                        myContacts.Add(name, phoneNumber);
                    }
                    else
                    {
                        Console.WriteLine("Número de teléfono incorrecto.\r\nDebe comprender entre 1 y 11 números");
                        Console.ReadKey();
                    }
                }  
            }

            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }

        /// <summary>
        /// Método para actualizar un contacto de la agenda
        /// </summary>
        public static void ActualizarContacto()
        {
            try
            {
                if (myContacts.Count > 0)
                {
                    // Mostrar listado de contactos
                    ShowContacts();

                    // Buscar el contacto en concreto
                    Console.WriteLine("Introduzca el nombre del contacto:");
                    string name = Console.ReadLine();

                    if (myContacts.TryGetValue(name, out var value))
                    {
                        Console.WriteLine("Introduzca el nuevo número de teléfono:");
                        int.TryParse(Console.ReadLine(), out int phoneNumber);

                        double data = Math.Floor(Math.Log10(phoneNumber) + 1);

                        if (data > 0 && data < 11)
                        {
                            myContacts[name] = phoneNumber;
                        }
                        else
                        {
                            Console.WriteLine("Número de teléfono incorrecto.\r\nDebe comprender entre 1 y 11 números");
                            Console.ReadKey();
                        }
                    }
                    else
                    {
                        Console.WriteLine("Contacto no encontrado");
                        Console.ReadKey();
                    }
                }
                else
                {
                    Console.WriteLine("No existen contactos en la agenda");
                    Console.ReadKey();
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }

        /// <summary>
        /// Método para eliminar un contacto de la agenda
        /// </summary>
        public static void EliminarContacto()
        {
            try
            {
                if (myContacts.Count > 0)
                {
                    // Mostrar listado de contactos
                    ShowContacts();


                    // Buscar el contacto en concreto
                    Console.WriteLine("Introduzca el nombre del contacto:");
                    string name = Console.ReadLine();

                    if (myContacts.TryGetValue(name, out var value))
                    {
                        Console.WriteLine($"{name} - {value}");
                        myContacts.Remove(name);
                    }
                    else
                    {
                        Console.WriteLine("Contacto no encontrado");
                        Console.ReadKey();
                    }
                }
                else
                {
                    Console.WriteLine("No existen contactos en la agenda");
                    Console.ReadKey();
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }
    }

    public class Contact
    {
        public string name;
        public int phoneNumber;

        public Contact(string name, int phoneNumber)
        {
            this.name = name;
            this.phoneNumber = phoneNumber;
        }
    }
}
