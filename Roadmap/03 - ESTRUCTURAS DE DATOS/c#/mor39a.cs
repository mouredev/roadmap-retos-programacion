/*
--------------------------------------------------------------------------------------------------------
Instrucciones:

    1. Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
    2. Utiliza operaciones de inserción, borrado, actualización y ordenación.

Dificultad extra:
    Crea una agenda de contactos por terminal.
        - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
        - Cada contacto debe tener un nombre y un número de teléfono.
        - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
          los datos necesarios para llevarla a cabo.
        - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
          (o el número de dígitos que quieras)
        - También se debe proponer una operación de finalización del programa.
--------------------------------------------------------------------------------------------------------
*/

#region Arreglos

//Los array tienen un tamaño fijo y almacenan elementos de un tipo especifico.

// Definiciones:
using System.Runtime.InteropServices;

string[] myArray = {
    "Un dato",
    "Otro dato",
    "Y otro dato"
};
string[] otroArray = new string[10];

// Insercion:
// Dado que son de tamaño fijo no se pueden hacer inserciones.

// Borrado:
myArray[0] = null!; //Esta seria lo mas parecido a hacer un borrado de un dato.
myArray = new string[3]; // De esta forma se pueden borrar todos los datos (y de paso volver a asignar el tamaño)

// Actualizacion:
myArray[0] = "Nuevo dato";

// Reorganizacion:
// No se puede reorganizar directamente, se necesitaria la ayuda de otro array
otroArray = myArray;
myArray[0] = otroArray[2];
myArray[1] = otroArray[0];
myArray[2] = otroArray[1];

#region Arreglos Multidimencionales

// Son arreglos de mas de una dimancion

// Definiciones:
string[,] myMatriz = {
    {"Primera dimencion", "Segunda dimencion", }
};
string[,] myMatriz2 = new string[1, 2];

#endregion

#region Arreglos de arreglos

// Son arreglos de arreglos

//Definiciones:
string[][] myJaggedArray = {
    ["Un", "Array"],
    ["Otro", "Array"]
};
string[][] myJaggedArray2 = new string[5][];

#endregion

#endregion

#region Listas

// Las listas a diferencia de los array no tienen un tamaño fijo.
// Lo que permite insertar, eliminar y acceder facilmente a los datos.
// Tambien almacenan datos de un tipo especifico.

// Definicion:
List<string> myList = new();

// Insercion:
myList.Add("Nuevo elemento");

// Borrado:
for (int i = 0; i < 10; i++) myList.Add(null!); // Temporal para tener elemento que eliminar
myList.Remove("Nuevo elemento"); // Elimina un dato en especifico por su contenido
myList.RemoveAt(0); // Elimina un dato en especifico por su index
myList.RemoveRange(0, 3); // Elimina un rango
myList.Clear(); // Elimina todo

// Actualizacion:
for (int i = 0; i < 10; i++) myList.Add(i.ToString()); // Temporal para tener elemento que actualizar
myList[0] = "Dato actualizado"; // Actualiza por indice

// Reorganizacion:
myList.Sort(); // Ordena de manera acendente
myList.Sort((x, y) => y.CompareTo(x)); // Ordena de manera desendente

#endregion

#region Diccionarios

// Los diccionarios permiten guardar una lista de elementos (de tipo especifico)
// bajo una llave (de otro o el mismo tipo especifico).
// Tambien tienen un tamaño flexible, por lo que tambien pueden insertar, eliminar
// y acceder a datos aun mas facil que con las listas.
// No permite llaves repetidas.

// Definicion:
Dictionary<string, int> /*<llave, valor>*/ myDictionary = new();

// Insercion:
myDictionary.Add("Uno", 1);

// Borrado:
for (int i = 0; i < 10; i++) myDictionary.Add(i.ToString(), i); // Temporal para tener elemento que eliminar
myDictionary.Remove("Uno"); // Eliminacion por llave
int datoEliminadoDic;
myDictionary.Remove("1", out datoEliminadoDic); // Elimina por llave y guarda el valor en el segundo parametro
myDictionary.Clear(); // Elimina todos los valores

// Actualizacion:
for (int i = 10; i > 0; i--) myDictionary.Add(i.ToString(), i); // Temporal para tener elemento que actualizar
myDictionary["2"] = 3; // Actualiza por llave

// Reorganizacion:
myDictionary = myDictionary.OrderBy(x => x.Key).ToDictionary(); // Ordena por la llave, pero toca volverlo a asignar.
myDictionary = myDictionary.OrderBy(x => x.Value).ToDictionary(); // Ordena por la valor, pero toca volverlo a asignar.

#endregion

#region Colas

// Sigen el principio FIFO (First In, First Out)
// Solo permite interactuar, o mas bien, eliminar el primer elemento
// No tiene metodo de actualizacion ni reorganizacion.

// Definicion:
Queue<string> myQueue = new();

// Insercion:
myQueue.Enqueue("Yo ire primero");
myQueue.Enqueue("Luego ire yo");
myQueue.Enqueue("Y luego yo");

// Borrado:
string valorQueue = myQueue.Dequeue(); // Elimina el primer valor y lo retorna
myQueue.Clear(); // Elimina todos los valores

// Reorganizacion:
// Se que dije que no se puede reorganizar, pero si lo conviertes en una lista
// y luego nuevamente a una cola, se puede lograr
for (int i = 0; i < 0; i++) myQueue.Enqueue(i.ToString()); // Temporal para tener elemento que reorganizar
List<string> tempQList = myQueue.ToList();
tempQList.Sort();
myQueue = new(tempQList);
// PD: Este mismo enfoque se puede usar para la actualizacion

#region Colas Prioritarias

// Es una estructura de datos que permite guardar elementos con una prioridad asociada

// Definicion:
PriorityQueue<string, int> /*<valor, prioridad>*/ myPriorityQueue = new();

// Insercion:
myPriorityQueue.Enqueue("Valor", 1);
myPriorityQueue.Enqueue("Otro valor", 2);

#endregion

#endregion

#region Pilas

// Sigue el principio LIFO (Last In, First Out)
// Solo permite interactuar, o mas bien, eliminar el ultimo elemento
// No tiene metodo de actualizacion ni reorganizacion.

// Definicion:
Stack<string> myStack = new();

// Insercion:
myStack.Push("Yo ire primero");
myStack.Push("No, ire yo");
myStack.Push("Se equivocan, ire yo");

// Borrado:
string valorStack = myStack.Pop(); // Elimina el ultimo elemento y lo retorna.

// Reorganizacion:
// Se que dije que no se puede reorganizar, pero si lo conviertes en una lista
// y luego nuevamente a una pila, se puede lograr
for (int i = 0; i < 0; i++) myStack.Push(i.ToString()); // Temporal para tener elemento que reorganizar
List<string> tempSList = myStack.ToList();
tempSList.Sort();
myStack = new(tempSList);
// PD: Este mismo enfoque se puede usar para la actualizacion

#endregion

#region Conjuntos

// Es una coleccion no ordenada
// Dada su naturaleza no permite reorganizar datos, pero tampoco actualizar
// No permite datos duplicados por lo que es muy util para verificar si hay datos duplicados en una estructura de datos

// Definicion:
HashSet<string> myHashSet = new();

// Insercion:
myHashSet.Add("Hola mundo");

// Borrado:
myHashSet.Remove("Hola mundo");
myHashSet.Clear(); // Elimina todo

// Actualizacion:
// La unica manera de actualizar datos es eliminandolos y volviendolos a añadir

#region Conjunto Ordenado

// Parecido al HashSet, pero mantiene los elementos ordenados siempre y automaticamente

// Definicion
SortedSet<string> mySortedSet = new();

#endregion

#endregion

#region Tuplas

// Agrupan un numero fijo de elementos de diferentes tipos

// Definicion:
var myTuple = Tuple.Create("Hola", 2);
var myTuple2 = ("Chao", "1", 5);

// Actualizacion:
myTuple = Tuple.Create("Nuevo valor", myTuple.Item2);
myTuple2.Item1 = "Nuevo valor";

#endregion

#region Lista enlazada

// Es una lista que permite la adiccion y eliminacion desde cualquier parte de la misma.
// Aunque consume mas memoria debido a sus apuntadores

// Definicion:
LinkedList<string> myLinkedList = new();

// Insercion:
myLinkedList.AddFirst("Se añade al principio");
myLinkedList.AddLast("Se añade al final");
myLinkedList.AddBefore(myLinkedList.First!, "Se añade antes de");
myLinkedList.AddAfter(myLinkedList.Last!, "Se añade despues de");

// Borrado:
myLinkedList.Remove("Se añade despues de"); // Elimina un objeto especifico
myLinkedList.RemoveFirst(); // Elimina el primer objeto
myLinkedList.RemoveLast(); // Elimina el ultimo objeto

//La actualizacion y reorganizacion es igual que una lista normal

#endregion

#region Span y Memory

// Imagina que tienes un array muy grande
string[] arrayImaginario = new string[1000];
// Y solo vas a trabajar en algunos datos, como lo harias?
// Copiando?
string[] arrayCopia = new string[100];
Array.Copy(arrayImaginario, 100, arrayCopia, 0, 100);
// Esto consume memoria y es muy poco eficiente
// Ademas de que luego tendras que volver a pasar los datos al array original
Array.Copy(arrayCopia, 0, arrayImaginario, 100, 100);

// Para eso estan Span y Memory
// Estos te permiten acceder a estos datos sin necesidad de hacer una copia
Span<string> mySpan = arrayImaginario.AsSpan(100, 100);

// Lo unico es que Span vive en la memoria rapida (stack),
// por lo que, anque lo hace mas rapido, solo se guardara mientras lo estas usando
// ademas de que no permite usar async
// Para eso usas Memory
Memory<string> myMemory = arrayImaginario.AsMemory(100, 100);
// Este vive en la memoria mas duradera (heap),
// por lo que puedes guardarlo y usarlo despues, aunque esto lo hace mas lento

#endregion

#region Extra

/*Dificultad extra:
    Crea una agenda de contactos por terminal.
        - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
        - Cada contacto debe tener un nombre y un número de teléfono.
        - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
          los datos necesarios para llevarla a cabo.
        - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
          (o el número de dígitos que quieras)
        - También se debe proponer una operación de finalización del programa.*/

bool inProgram = true;

while (inProgram)
{
    Console.WriteLine("\nMenu Principal:\n");

    Console.WriteLine("Seleccione una opcion:");
    Console.WriteLine("     1. Agregar un nuevo contacto");
    Console.WriteLine("     2. Editar un contacto");
    Console.WriteLine("     3. Buscar un contacto");
    Console.WriteLine("     4. Eliminar un contacto");
    Console.WriteLine("     5. Salir");

    ConsoleKeyInfo input = Console.ReadKey();
    Console.WriteLine();

    string? name;
    string? number;
    string? countryCode;

    switch (input.KeyChar)
    {
        case '1': // Nuevo contacto
            InputNumber();
            Console.WriteLine(ContactBook.AddContact(name, number, countryCode) ? $"Contacto {name} agregado exitosamente." : $"No se pudo agregar a {name}.");
            break;
        case '2': // Editar contacto
            InputNumber();
            Console.WriteLine(ContactBook.UpdateContact(name, number, countryCode) ? $"El contacto {name} fue editado exitosamente" : $"No fue posible editar el contacto {name}.");
            break;
        case '3': // Buscar contacto
            InputName();
            Console.WriteLine(ContactBook.GetContact(name));
            break;
        case '4': // Eliminar contacto
            InputName();
            Console.WriteLine(ContactBook.DeleteContact(name) ? $"Contacto {name} eliminado exitosamente." : $"No se pudo eliminar a {name}.");
            break;
        case '5': // Salir
            inProgram = false;
            Console.WriteLine("Hasta luego");
            return;
        default: // Opcion no valida
            Console.WriteLine("No a ingresado una opcion valida");
            break;
    }
    Console.WriteLine("Oprima cualquier tecla para continuar.");
    Console.ReadKey();

    void InputNumber()
    {
        bool validNumber = false;

        InputName();        

        Console.WriteLine("Ingrese el codigo de pais (opcional - enter para omitir):");
        countryCode = Console.ReadLine();
        do
        {
            Console.WriteLine("Ingrese el numero telefonico:");
            number = Console.ReadLine();
            switch (ContactBook.VerifyNumber(number))
            {
                case 0:
                    validNumber = true;
                    break;
                case 1:
                    Console.WriteLine("El numero no puede ser nullo.");
                    break;
                case 2:
                    Console.WriteLine("Solo se admiten numeros.");
                    break;
                case 3:
                    Console.WriteLine("El numero es muy largo, por favor ingrese hasta 10 digitos.");
                    break;
                default:
                    Console.WriteLine("Numero no valido.");
                    break;
            }
        } while (!validNumber);

    }

    void InputName()
    {
        bool validName = false;
        do
        {
            Console.WriteLine("Escriba el nombre:");
            name = Console.ReadLine();
            if (!string.IsNullOrWhiteSpace(name)) validName = true;
            else Console.WriteLine("Nombre no valido.");
        } while (!validName);
    }
}

public static class ContactBook
{
    #region Private Declarations

    private static Dictionary<string, string> contactBook = new();

    #endregion

    #region Public Procedures

    public static int VerifyNumber(string? number)
    {
        if (string.IsNullOrWhiteSpace(number)) return 1;
        number = number.Replace(" ", "");
        if (!number.All(char.IsDigit)) return 2;
        else if (number.Length > 10) return 3;
        else return 0;
    }

    public static bool AddContact(string? name, string? number, string? countryCode = null)
    {
        if (VerifyNumber(number) != 0 || string.IsNullOrWhiteSpace(name)) return false;
        contactBook.Add(name, FormatNumber(number, countryCode));
        return true;
    }

    public static string GetContact(string? name)
        => !string.IsNullOrWhiteSpace(name) && contactBook.ContainsKey(name) ? contactBook[name] : $"El contacto {name} no existe";

    public static bool DeleteContact(string? name)
    {
        if (!string.IsNullOrWhiteSpace(name) && contactBook.ContainsKey(name))
        {
            contactBook.Remove(name);
            return true;
        } else return false;
    }

    public static bool UpdateContact(string? name, string? newNumber, string? newCountryCode = null)
    {
        if (VerifyNumber(newNumber) != 0 || string.IsNullOrWhiteSpace(name)) return false;
        contactBook[name] = FormatNumber(newNumber, newCountryCode);
        return true;
    }

    #endregion

    #region Private Procedures

    private static string FormatNumber(string? number, string? countryCode = null)
    {
        if (string.IsNullOrWhiteSpace(number)) return null!;
        number = number.Replace(" ", "");
        if (!string.IsNullOrWhiteSpace(countryCode) && countryCode.Replace(" ", "").All(char.IsDigit))
        {
            countryCode = countryCode.Replace(" ", "");
            if (number.Length != 10) return $"+{countryCode.Replace(" ", "")} {number}";
            else return $"+{countryCode.Replace(" ", "")} {number[..3]} {number.Substring(3, 3)} {number[6..]}";
        }
        if (number.Length != 10) return number;
        else return $"{number[..3]} {number.Substring(3, 3)} {number[6..]}";
    }

    #endregion
}

#endregion
