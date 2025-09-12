/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
*/

/*
 * explicitamente tiene que utilizarse List en vez de Array, ya que el array
 * tiende a ser una estructura que tiene que ser inicializada su tamaño o sus elementos
 * antes de compilar
 */


//PILA O STACK
List<int> pila = new();
int opc = 1, eli = 2;
int num = 0;


while (opc != 2)
{
    Console.WriteLine("Quiere seguir agregando mas numeros ? Si(1) No(2)");
    opc = int.Parse(Console.ReadLine());
    if (opc == 2) continue;
    Console.Clear();
    Console.WriteLine("Digite el numero a agregar:");
    num  = int.Parse(Console.ReadLine());
    pila.Add(num);
    Console.Clear();
    int peek = pila.IndexOf(num);//peek for the stack
    Console.WriteLine("\nLa pila es esta hasta el momento:\n ");
    pila.Reverse();
    if(pila.Count() > 0)//verificar que la pila tenga elementos para poder mostrarlos
    {
        foreach (int i in pila)//mostrar todos los elementos de la pila
        {
            Console.WriteLine(i);
        }
    }
    else
    {
        Console.WriteLine("La pila no tiene elementos");
    }
    pila.Reverse();
    Console.WriteLine($"Desea eliminar el ultimo numero de la pila? En este caso {pila[peek]} \n Si(1) No(2)");
    eli = int.Parse(Console.ReadLine());
    if(eli == 1)
    {
        pila.Remove(pila[peek]); //eliminar el ultimo elemento ingresado
    }
    Console.Clear();
}

pila.Reverse();
Console.WriteLine("\n Pila Final \n");
if (pila.Count() > 0)//verificar que la pila tenga elementos para poder mostrarlos
{
    foreach (int i in pila)//mostrar todos los elementos de la pila
    {
        Console.WriteLine(i);
    }
}
else
{
    Console.WriteLine("La pila no tiene elementos");
}

//COLA O QUEUE primero en entrar primero en salir
List<int> cola = new();


int opc = 1, eli = 2;
int num = 0;


while (opc != 2)
{
    Console.WriteLine("Quiere seguir agregando mas numeros a la cola ? Si(1) No(2)");
    opc = int.Parse(Console.ReadLine());
    if (opc == 2) continue;
    Console.Clear();
    Console.WriteLine("Digite el numero a agregar:");
    num = int.Parse(Console.ReadLine());
    cola.Add(num);
    Console.Clear();
    int salida = cola[0];//salida para la cola
    Console.WriteLine("\nCola o queue actual:\n ");
    if (cola.Count() > 0)//verificar que la pila tenga elementos para poder mostrarlos
    {
        foreach (int i in cola)//mostrar todos los elementos de la pila
        {
            Console.Write(i + "-");
        }
        Console.WriteLine("");
    }
    else
    {
        Console.WriteLine("La pila no tiene elementos");
    }
    Console.WriteLine($"Desea eliminar el elemento de la cola[ se eliminará el primero]? En este caso valor: {salida} \n Si(1) No(2)");
    eli = int.Parse(Console.ReadLine());
    if (eli == 1)
    {
        cola.Remove(salida); //eliminar el primer elemento en la cola
    }
    Console.Clear();
}

Console.WriteLine("\n Cola o queue Final \n");
if (cola.Count() > 0)//verificar que la pila tenga elementos para poder mostrarlos
{
    foreach (int i in cola)//mostrar todos los elementos de la pila
    {
        Console.Write(i + "-");
    }
    Console.WriteLine("");
}
else
{
    Console.WriteLine("La cola no tiene elementos");
}


/*
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */


 Stack<string> browser = new Stack<string>();

string pagina = "";


while (true)
{
    Console.WriteLine("Ingresa una url o interactua con atras/siguiente/salir");
    pagina = Console.ReadLine();
    if(pagina == "salir")
    {
        break;
    }else if( pagina == "siguiente")
    {
        continue;
    }else if(pagina == "atras")
    {
        if(browser.Count > 0) browser.Pop();
    }
    else
    {
        browser.Push(pagina);
    }

    if (browser.Count > 0)
    {
        Console.Clear();
        Console.WriteLine("Pagina actual [HEAD]-> " + browser.Peek());
    }
    else
    {
        Console.WriteLine("Estas en la pagina de inicio");
    }
}


Queue<string> queue = new Queue<string>();
string pagina2 = "";
while (true)
{
    Console.WriteLine("Que desea hacer? Imprimir o agregar una hoja a la impresora(nombre del archivo) | Salir");
    pagina2 = Console.ReadLine();
    Console.Clear();
    if (pagina2 == "imprimir")
    {
        if(queue.Count > 0) Console.WriteLine($" Documento impreso correctamente : {queue.Dequeue()}");
        else Console.WriteLine("Bandeja Vacía. Impresora sin documentos pendientes para imprimir");
    }
    else if(pagina2 == "salir")
    {
        break;
    }
    else
    {
        queue.Enqueue(pagina2);
        Console.WriteLine("Documento guardado y listo para imprimir");
    }
}