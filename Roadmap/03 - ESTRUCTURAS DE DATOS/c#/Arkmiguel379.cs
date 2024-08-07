//==================== ESTRUCTURAS DE DATOS ====================

// ARREGLO/ARRAY (Almacenan elementos de manera contigua en memoria y permiten un acceso rápido mediante índices)

Console.WriteLine("===== ARRAY / ARREGLO ===== \n");

int[] array = { 1, 5, 3, 2, 4 };

foreach (int elemento in array)
{
    Console.WriteLine(elemento);
}

Console.WriteLine("\n");

// INSERSION <-- Insersion como tal no se puede

Console.WriteLine("ARRAY con 'insercion' \n");

int[] nuevoArray = new int[array.Length + 1]; // <-- Lo que hay que hacer es crear otro array que contenga la misma cantidad de indices del array original + 1

for (int i = 0; i < array.Length; i++)
{
    nuevoArray[i] = array[i];
}

nuevoArray[array.Length] = 6;

foreach (int elemento in nuevoArray)
{
    Console.WriteLine(elemento);
}

Console.WriteLine("\n");

// ORDENACION 

Console.WriteLine("ARRAY ordenada \n");

Array.Sort(array);

foreach (int elemento in array)
{
    Console.WriteLine(elemento);
}

Console.WriteLine("\n");

// ACTUALIZACION

Console.WriteLine("ARRAY actualizada \n");

array[4] = 379;

foreach (int elemento in array)
{
    Console.WriteLine(elemento);
}

Console.WriteLine("\n");


// LISTA/LIST (Dinámicamente redimensionables y proporcionan métodos para insertar, eliminar y buscar elementos)

Console.WriteLine("===== LIST / LISTA ===== \n");

List<int> lista = new List<int> { 1, 5, 3, 2, 4 };

foreach (int elemento in lista)
{
    Console.WriteLine(elemento);
}

Console.WriteLine("\n");

// INSERCION

Console.WriteLine("LISTA con insercion \n");

lista.Add(6);

foreach (int elemento in lista)
{
    Console.WriteLine(elemento);
}

Console.WriteLine("\n");

// ELIMINACION

Console.WriteLine("LISTA con eliminacion \n");

lista.Remove(6);

foreach (int elemento in lista)
{
    Console.WriteLine(elemento);
}

Console.WriteLine("\n");

// ORDENACION

Console.WriteLine("LISTA con ordenacion \n");

lista.Sort();

foreach (int elemento in lista)
{
    Console.WriteLine(elemento);
}

Console.WriteLine("\n");

// ACTUALIZACION 

Console.WriteLine("LISTA con actualizacion \n");

lista[0] = 89;

foreach (int elemento in lista)
{
    Console.WriteLine(elemento);
}

Console.WriteLine("\n");



// PILA/STACK (Implementan el principio LIFO (último en entrar, primero en salir))

Console.WriteLine("===== PILA / STACK ===== \n");

Stack<int> stack = new Stack<int>(new[] {1, 2, 3, 4, 5});


foreach (int elemento in stack)
{
    Console.WriteLine(elemento);
}

Console.WriteLine("\n");

// INSERCION 

Console.WriteLine("PILA con Insercion \n");

stack.Push(6);

foreach (int elemento in stack)
{
    Console.WriteLine(elemento);
}

Console.WriteLine("\n");

//ELIMINACION

Console.WriteLine("PILA con Eliminacion \n");

stack.Pop();

foreach (int elemento in stack)
{
    Console.WriteLine(elemento);
}

Console.WriteLine("\n");

// COLAS/QUEUE Implementan el principio FIFO (primero en entrar, primero en salir))

Console.WriteLine("===== COLA / QUEUE ===== \n");

Queue<int> cola = new Queue<int>(new[] { 1, 2, 3, 4, 5 });

foreach (int elemento in cola)
{
    Console.WriteLine(elemento);
}

Console.WriteLine("\n");

// INSERCION 

Console.WriteLine("COLA con Insercion \n");

cola.Enqueue(6);

foreach (int elemento in cola)
{
    Console.WriteLine(elemento);
}

Console.WriteLine("\n");

// INSERCION 

Console.WriteLine("COLA con Eliminacion \n");

cola.Dequeue();

foreach (int elemento in cola)
{
    Console.WriteLine(elemento);
}

Console.WriteLine("\n");

// CONJUNTOS/HASHSET (Almacenan elementos únicos sin duplicados)

Console.WriteLine("===== CONJUNTOS / HASHSET ===== \n");

HashSet<int> conjunto = new HashSet<int> { 1, 2, 3, 4, 5};

// INSERCION 

Console.WriteLine("CONJUNTO con Insercion \n");

conjunto.Add(6);

foreach (int elemento in conjunto)
{
    Console.WriteLine(elemento);
}

Console.WriteLine("\n");

// ELIMINACION 

Console.WriteLine("CONJUNTO con Eliminacion \n");

conjunto.Remove(6);

foreach (int elemento in conjunto)
{
    Console.WriteLine(elemento);
}

Console.WriteLine("\n");

HashSet<int> conjunto2 = new HashSet<int> { 6, 7, 8, 4, 10 };

conjunto.UnionWith(conjunto2);

foreach (int elemento in conjunto)
{
    Console.WriteLine(elemento);
}

Console.WriteLine("\n");


// DICCIONARIO/DICCIONARY (Almacenan pares clave-valor y proporcionan acceso rápido a los valores mediante las claves)

Console.WriteLine("===== DICCIONARIO / DICCIONARY ===== \n");

Dictionary<string, string> diccionario = new Dictionary<string, string>()
{
    {"Nombre", "Miguel"},
    {"Apellido", "Moreno"},
    {"Edad", "28"},
    {"Alias", "Logan"}
};

foreach (var dict in diccionario)
{
    string clave = dict.Key;
    string valor = dict.Value;

    Console.WriteLine($"{clave} {valor}");
}

Console.WriteLine("\n");

// INSERCION 

Console.WriteLine("DICCIONARIO con Insercion \n");

diccionario.Add("Correo", "arkangel-159@hotmail.com"); // <-- El metodo Add se encarga de agregar un nuevo registro en el diccionario

foreach (var dict in diccionario)
{
    string clave = dict.Key;
    string valor = dict.Value;

    Console.WriteLine($"{clave} {valor}");
}

Console.WriteLine("\n");

// ACTUALIZACION 

Console.WriteLine("DICCIONARIO con Actualizacion \n");

diccionario["Correo"] = "blaziken.257@gmail.com"; /* <-- Se escribe la clave y posteriormente se le modifica el nuevo valor que se desea 
                                                    asignar */

foreach (var dict in diccionario)
{
    string clave = dict.Key;
    string valor = dict.Value;

    Console.WriteLine($"{clave} {valor}");
}

Console.WriteLine("\n");

// ELIMINACION 

Console.WriteLine("DICCIONARIO con Eliminacion \n");

diccionario.Remove("Correo"); // <-- El metodo Remove se encarga de eliminar un registro en el diccionario segun la clave que le sea escrita

foreach (var dict in diccionario)
{
    string clave = dict.Key;
    string valor = dict.Value;

    Console.WriteLine($"{clave} {valor}");
}

Console.WriteLine("\n");

// ORDENACION

SortedDictionary<string, string> diccionarioO = new SortedDictionary<string, string>() /* <-- La clase SortedDictionary hace un diccionario 
                                                                                         que se ordena solo */
{
    {"Nombre", "Miguel"},
    {"Apellido", "Moreno"},
    {"Edad", "28"},
    {"Alias", "Logan"},
    {"Correo", "blaziken.257@gmail.com"}
};

foreach (var dic in diccionarioO)
{
    string clave = dic.Key;
    string valor = dic.Value;

    Console.WriteLine($"{clave} {valor}");
}

Console.WriteLine("\n");

// ==================== EXTRA =========================

Dictionary<string, int> agenda = new Dictionary<string, int>()
{
    {"Miguel", 379},
    {"Daniel", 257},
    {"Juan", 654},
    {"Claudia", 258}
};

bool operacion = false;

while (!operacion)
{
    Console.WriteLine("=== AGENDA === \n");
    Console.WriteLine("Oprime el numero correspondiente para cada accion \n \n 1. Buscar Contacto \n 2. Insertar Contacto \n 3. Actualizar Contacto \n 4. Eliminar Contacto \n");
    string accion = Console.ReadLine();
    Console.WriteLine();

    if (accion == "1")
    {
        Console.WriteLine("Escribe el nombre o el numero del contacto que deseas buscar \n");
        string dato = Console.ReadLine();
        Console.WriteLine();

        int value;
        int.TryParse(dato, out value);

        while (!agenda.ContainsKey(dato) && !agenda.ContainsValue(value))
        {
            Console.WriteLine("No se ha encontrado el nombre o numero ingresado \n Intentalo nuevamente \n");
            dato = Console.ReadLine();
            int.TryParse(dato, out value);
            Console.WriteLine();
        }

        foreach (var contacto in agenda)
        {
            string clave = contacto.Key;
            int valor = contacto.Value;

            if (clave == dato || valor.ToString() == dato)
            {
                Console.WriteLine($"Contacto encontrado: {clave} {valor} \n");
                break;
            }
        } 
    }
    else if (accion == "2")
    {
        Console.WriteLine("Escribe el nombre y el numero del contacto que deseas crear \n El numero no debe de exceder los 11 digitos \n");
        Console.Write("Nombre: ");
        string nombre = Console.ReadLine();
        

        Console.Write("Numero: ");

        int maxLen = 11;
        string numero;
        int numV = 0;
        bool numeroValido = false;

        while (!numeroValido)
        {
            numero = Console.ReadLine();
            Console.WriteLine();

            if (numero.Length > maxLen)
            {
                Console.WriteLine("El numero excede los 11 digitos. Ingrese un numero que no exceda esa cantidad \n");
            }
            else
            {
                if (int.TryParse(numero, out numV))
                {
                    numeroValido = true;
                }
                else
                {
                    Console.WriteLine("Valor ingresado no valido \n Ingrese un valor que sea numerico \n");
                }
            }
        }

        agenda.Add(nombre, numV);

    }
    else if (accion == "3")
    {
        Console.WriteLine("¿Que deseas actualizar? \n 1.Nombre \n 2.Numero \n");

        string update = Console.ReadLine();
        Console.WriteLine();

        if (update == "1")
        {
            Console.Write("Ingresa el nombre del contacto que deseas cambiar: ");
            string nombreA = Console.ReadLine();
            Console.WriteLine();

            while (!agenda.ContainsKey(nombreA))
            {
                Console.WriteLine("El nombre ingresado no existe \n Intentalo nuevamente \n");
                nombreA = Console.ReadLine();
                Console.WriteLine();
            }

            if (agenda.ContainsKey(nombreA))
            {
                Console.Write("Ingresa el nuevo nombre: ");
                string nombreN = Console.ReadLine();
                Console.WriteLine();

                Console.WriteLine("");

                ActualizarClave(agenda, nombreA, nombreN);

                Console.WriteLine($"El nombre del contacto {nombreA} ha sido actualizado a {nombreN} \n");
            }
        }
        else if (update == "2")
        {
            Console.Write("Ingresa el nombre del contacto que deseas cambiar: ");
            string nombreA = Console.ReadLine();
            Console.WriteLine();

            while (!agenda.ContainsKey(nombreA))
            {
                Console.WriteLine("El nombre ingresado no existe \n Intentalo nuevamente \n");
                nombreA = Console.ReadLine();
                Console.WriteLine();
            }

            Console.Write("Ingresa el nuevo numero: ");

            string numero;
            int numV = 0;
            bool numeroValido = false;

            while (!numeroValido)
            {
                numero = Console.ReadLine();
                Console.WriteLine();

                if (int.TryParse(numero, out numV))
                {
                    numeroValido = true;
                }
                else
                {
                    Console.WriteLine("Valor ingresado no valido \n Ingrese un valor que sea numerico \n");
                }
            }

            agenda[nombreA] = numV;

            Console.WriteLine($"Numero actualizado a {numV} \n");
        }
    }
    else if (accion == "4")
    {
        Console.WriteLine("Escribe el nombre del contacto que deseas eliminar \n");
        string del = Console.ReadLine();
        Console.WriteLine();

        while (!agenda.ContainsKey(del))
        {
            Console.WriteLine("El nombre ingresado no existe \n Intentalo nuevamente \n");
            del = Console.ReadLine();
            Console.WriteLine();
        }

        agenda.Remove(del);
    }

    Console.WriteLine("¿Deseas seguir trabajando en la agenda? \n 1. Si \n 2. No \n");

    bool close = false;

    while (!close) {

        string rep = Console.ReadLine();
        Console.WriteLine();

        if (rep == "1")
        {
            close = true;
        }
        else if (rep == "2")
        {
            Console.WriteLine("Agenda cerrada");
            close = true;
            operacion = true;
        }
        else
        {
            Console.WriteLine("Comando no valido. Ingrese alguno de los comandos que se muestran en pantalla \n");
        }
    }

    Console.WriteLine("\n");

    foreach (var contacto in agenda)
    {
        string clave = contacto.Key;
        int valor = contacto.Value;

        Console.WriteLine(clave + " " + valor);
    }

    Console.WriteLine();
}

// =================================================================================

static void ActualizarClave(Dictionary<string,int> diccionario, string claveAntigua, string claveNueva)
{
    if (diccionario.ContainsKey(claveAntigua))
    {
        int valor = diccionario[claveAntigua];

        diccionario.Remove(claveAntigua);

        diccionario.Add(claveNueva, valor);
    }
    else
    {
        Console.WriteLine("La clave proporcionada no existe");
    }
}
