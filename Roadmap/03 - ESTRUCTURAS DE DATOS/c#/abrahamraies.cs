// Author: Abraham Raies https://github.com/abrahamraies

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

using System;
using System.Collections.Generic;

 class Program {
    static void Main (string[] args){
        #region Estructuras soportadas
        Console.WriteLine("Estructuras soportadas: ");

        #region Arrays

        // Arreglos: Una colección de elementos del mismo tipo almacenados en una ubicación de memoria continua.
        Console.WriteLine("Array: ");

        int[] numbersInArray = new int[5];
        string[] names = {"Jorge","Emilio"};
        int[] numbersInArray2 = new int[] {5,4,3,2,6,1};

        // ADD: No es posible redimencionar un arreglo directamente, es necesario crear un nuevo arreglo.

        // Delete: No es posible eliminar un elemento de un arreglo, es necesario crear un nuevo arreglo sin ese elemento.

        // Update: 
        numbersInArray[0] = 2; // Modifica el primer elemento del arreglo.

        // Order:
        Array.Sort(numbersInArray2); // Ordena los elementos de menor a mayor
        Console.WriteLine("Array " + string.Join(", " , numbersInArray2));
        #endregion

        #region Lists
        // Listas: Una colección genérica que puede crecer dinámicamente.
        Console.WriteLine("Lists: ");

        List<int> numberList = new List<int>();
        List<int> numberList2 = new List<int> {2,3,4,7,1};

        // ADD:
        numberList.Add(3); // Inserta un elemento al final de la lista.
        numberList.Insert(1,4); // Inserta el elemento de valor 4 en el indice 1.

        // Delete:
        numberList2.Remove(4); // Elimina la primera aparicion del elemento de valor 4.
        numberList2.RemoveAt(2); // Elmina el elemento en el indice 2.

        // Update: 
        numberList[0] = 2; // Modifica el primer elemento de la lista.

        // Order:
        numberList.Sort(); // Ordena los elementos de menor a mayor.
        Console.WriteLine("List " + string.Join(", " , numberList2));
        #endregion

        #region Dictionary
        // Diccionarios: Una colección de pares clave-valor.
        Console.WriteLine("Dictionary: ");

        Dictionary<int,string> numberNames = new Dictionary<int, string>();

        // ADD:
        numberNames.Add(1,"One"); // Inserta un par.

        // Delete:
        numberNames.Remove(2); // Quita el par clave-valor con la clave 2.

        // Update: 
        numberNames[0] = "Uno"; // Modifica el valor para el elemento 1.

        // Order: No se pueden ordenar los elementos en un diccionario.
        foreach (var kvp in numberNames)
        {
            Console.WriteLine("Diccionario: {0} = {1}", kvp.Key, kvp.Value);
        }
        #endregion

        #region HashSet
        // HashSet: Una colección de elementos únicos.
        Console.WriteLine("HashSet: ");

        HashSet<int> uniqueNumbers = new HashSet<int>();

        // ADD:
        uniqueNumbers.Add(1); // Inserta un elemento.
        uniqueNumbers.Add(2);
        // Delete:
        uniqueNumbers.Remove(2); // Quita un elemento.

        // Update: No se puede modificar un elemento, pero si se puede eliminar y agregar uno.

        // Order: No se pueden ordenar los elementos.
        Console.WriteLine("HashSet " + string.Join(", ", uniqueNumbers));
        #endregion

        #region Queue
        // Colas: Una colección FIFO (First-In-First-Out).
        Console.WriteLine("Queue: ");

        Queue<string> queue = new Queue<string>();

        // ADD:
        queue.Enqueue("first"); // Agrega el elemento first a la cola.
        queue.Enqueue("second");
        // Delete:
        string first = queue.Dequeue(); // Quita y retorna el primer elemento.

        // Update: No se pueden actualizar los elementos con un metodo propio. Para hacerlo es necesario realizar una busqueda del elemento, crear una queue temporal, sacar todos los elementos anteriores, remover el valor deseado y agregarlo con el nuevo valor.

        // Order: No se pueden ordenar los elementos en una cola, el primero que entra es el primero que sale.
        Console.WriteLine("Queue " + string.Join(", ", queue));
        #endregion

        #region Stack
        // Pilas: Una colección LIFO (Last-In-First-Out).
        Console.WriteLine("Stack: ");

        Stack<string> stack = new Stack<string>();

        // ADD:
        stack.Push("First"); // Agrega el elemento first a la pila.
        stack.Push("Second");
        // Delete:
        string firstElement = stack.Pop(); // Quita y retorna el primer elemento.

        // Update: No se pueden actualizar los elementos con un metodo propio. Para hacerlo es necesario realizar una busqueda del elemento, crear una pila temporal, sacar todos los elementos anteriores, remover el valor deseado y agregarlo con el nuevo valor.

        // Order: No se pueden ordenar los elementos en una pla, el ultimo que entra es el primero que sale.
        Console.WriteLine("Stack " + string.Join(", ", stack));
        #endregion

        #region Matrix
        // Matriz multidimensional: Array que tiene más de una dimensión, como una tabla de dos dimensiones (matriz) o más.
        Console.WriteLine("Multidimensional matrix: ");

        int[,] matrix = new int[3, 3];

        // ADD: No se pueden redimensionar directamente. Debes crear una nueva matriz si necesitas una matriz de diferente tamaño.

        // Delete: No se puede eliminar directamente elementos. Necesitas crear una nueva matriz y copiar los elementos deseados.

        // Update:
        matrix[0, 1] = 7; // Actualiza el valor en la posición [0, 1]

        // Order: Para ordenarla es necesario convertirla a una lista, ordenarla y luego volver a convertirla a matriz.
        for (int i = 0; i < matrix.GetLength(0); i++)
        {
            for (int j = 0; j < matrix.GetLength(1); j++)
            {
                Console.Write(matrix[i, j] + " ");
            }
            Console.WriteLine();
        }
        #endregion

        #region Jagged Matrix
        // Matriz Jagged: Es un array de arrays. Cada "fila" puede tener una longitud diferente.
        Console.WriteLine("Jagged Matrix: ");

        int[][] jaggedArray = new int[3][];
            jaggedArray[0] = new int[] { 1, 2 };
            jaggedArray[1] = new int[] { 3, 4, 5 };
            jaggedArray[2] = new int[] { 6, 7, 8, 9 };

        // ADD: Es necesario re-ajustar el tamaño del array.
        Array.Resize(ref jaggedArray[1], 4);
        jaggedArray[1][3] = 10;

        // Delete: Es necesario implementar LINQ

        // Update:
        jaggedArray[1][2] = 20; // Actualiza el tercer elemento de la segunda fila

        // Order: 
        Array.Sort(jaggedArray[1]); //Ordena una fila especifica.
        for (int i = 0; i < jaggedArray.Length; i++)
        {
            for (int j = 0; j < jaggedArray[i].Length; j++)
            {
                Console.Write(jaggedArray[i][j] + " ");
            }
            Console.WriteLine();
        }
        #endregion

        #region Enum
        // Enum: Es un tipo de valor que define un conjunto de constantes con nombre.
        Console.WriteLine("Enum: ");

        // public enum DaysOfWeek
        //{
        //    Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
        //}
		

        // ADD / Update / Delete: No se puede añadir, actualizar o eliminar valores en un enum después de su definición.

        // Order: Los valores de un enum tienen un orden predefinido basado en su declaración.
        #endregion

        #region Tupla
        // Tuple: Es una estructura de datos que puede contener un número fijo de elementos de tipos diferentes.
        Console.WriteLine("Tuple: ");

        var person = (Name: "Alice", Age: 30);

        // ADD / Delete: No se pueden añadir ni eliminar elementos en una tupla. Se necesita crear una nueva tupla.

        // Update: Es necesario crear una nueva tupla con los valores actualizados.
        var updatedPerson = (Name: person.Name, Age: 31);

        // Order: No es posible ordenar una tupla.
        Console.WriteLine($"Name: {person.Name}, Age: {person.Age}");
        #endregion

        #region Record
        // Record: Es un tipo de referencia que proporciona un mecanismo conciso para definir un tipo inmutable con igualdad de valores.
        Console.WriteLine("Record: ");

        //public record Person(string Name, int Age);

        // ADD / Delete: No se pueden añadir ni eliminar propiedades en un record después de su definición.
        //Person person = new Person("Sonia", 30);
        // Update: Usar la sintaxis with para crear una nueva instancia con valores actualizados.
        var olderPerson = person with { Age = 31 };

        // Order: Hay que crear una lista, y utilizar LINQ para ordenarla.
        Console.WriteLine($"Name: {person.Name}, Age: {person.Age}");
        #endregion

        #region LinkedList
        // LinkedList: Es una colección de nodos que permite una inserción y eliminación eficientes.
        Console.WriteLine("LinkedList: ");

        LinkedList<int> linkedList = new LinkedList<int>();

        // ADD: Existen distintos metodos para agregar un elemento a una lista linkeada:
        linkedList.AddLast(1); // Agregar el valor 1 al ultimo nodo
        linkedList.AddFirst(0); //Agrega el valor 0 al primer nodo.
        linkedList.AddAfter(linkedList.First, 2); //Luego del primer nodo agrega el elemento 2.
        linkedList.AddLast(3);
        linkedList.AddLast(4);

        // Delete:
        linkedList.Remove(2); // Elimina el primer nodo que contiene el valor 2
        linkedList.RemoveFirst(); // Elimina el primer nodo
        linkedList.RemoveLast(); // Elimina el último nodo

        // Update: Linq para buscarlo y luego se puede modificar el valor con la propiedad value.
        var node = linkedList.Find(1);
        node.Value = 10;

        // Order: Hay que crear una lista, utilizar LINQ para ordenarla y luego volver a convertirla a una linkedList.
        
        #endregion
        
        #endregion
        
        #region Ejercicio Extra:

        ContactList agenda = new ContactList();

		while(true)
        {
            ShowMenu();
            Console.Write("Selecciona una opción: ");
            string opcion = Console.ReadLine();
            switch (int.Parse(opcion))
            {
                case 1:
                    Console.WriteLine("Ingresar el nombre del contacto a buscar");
                    string nameToSearch = Console.ReadLine();
					agenda.SearchContact(nameToSearch);
					break;
				case 2:
					Console.WriteLine("Ingresar el nombre del contacto a agregar");
                    string nameToAdd = Console.ReadLine();
                    Console.WriteLine("Ingresar el numero del contacto a agregar");
                    string numberToAdd = Console.ReadLine();
                    agenda.AddContact(nameToAdd,numberToAdd);
					break;
				case 3:
                    Console.WriteLine("Ingresar el nombre del contacto a actualizar");
                    string nameToUpdate = Console.ReadLine();
                    Console.WriteLine("Ingresar el nuevo numero del contacto a actualizar");
                    string numberToUpdate = Console.ReadLine();
                    agenda.UpdateContact(nameToUpdate,numberToUpdate);
					break;
				case 4:
					Console.WriteLine("Ingresar el nombre del contacto a eliminar");
                    string nameToDelete = Console.ReadLine();
                    agenda.DeleteContact(nameToDelete);
					break;
				case 5:
					Console.WriteLine("\n Adios");
					return;
                default:
					Console.WriteLine("Opcion no valida");
					break;
            }
        }
        #endregion
	}

	static void ShowMenu(){
		Console.WriteLine("\n--- Agenda de Contactos ---");
        Console.WriteLine("1# Buscar contacto");
        Console.WriteLine("2# Crear contacto");
        Console.WriteLine("3# Actualizar contacto");
        Console.WriteLine("4# Eliminar contacto");
        Console.WriteLine("5# Salir");
	}

    
}

public class ContactList{
	private Dictionary<string,string> contacts;

    public ContactList(){
        contacts = new Dictionary<string, string>();
    }

    public void AddContact(string name, string number){
        if(contacts.ContainsValue(number)){
            Console.WriteLine("El contacto ya existe.");
        }else{
            contacts.Add(name,number);
            Console.WriteLine("Usuario agregado correctamente.");
        }
    }

    public void SearchContact(string name){
        if(contacts.TryGetValue(name, out string number)){
            Console.WriteLine($"Nombre: {name}, Número: {number}");
        }
        else
        {
            Console.WriteLine("Contacto no encontrado.");
        }
    }

    public void UpdateContact(string name, string newNumber){
        if(contacts.ContainsKey(name)){
            contacts[name] = newNumber;
            Console.WriteLine("Contacto actualizado exitosamente.");
        }
        else
        {
            Console.WriteLine("Contacto no encontrado.");
        }
    }

    public void DeleteContact(string name){
        if(contacts.Remove(name)){
            Console.WriteLine("Contacto eliminado exitosamente.");
        }
        else
        {
            Console.WriteLine("Contacto no encontrado.");
        }
    }

    public void AllContacts(){
        Console.WriteLine("Lista de contactos:");
        foreach (var contact in contacts)
        {
            Console.WriteLine($"Nombre: {contact.Key}, Número: {contact.Value}");
        }
    }
}