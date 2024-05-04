// El Stack es un tipo de coleccion LIFO, el último de entrar es el primero en salir.

Stack<string> posiciones = new Stack<string>();

// Añadir
posiciones.Push("Uno");
posiciones.Push("Dos");
posiciones.Push("Tres");
posiciones.Push("Cuatro");

Console.WriteLine("El Stack actualmente es: ");
foreach (var item in posiciones)
{
    Console.Write($"{item} ");
}

Console.WriteLine("\nEl Push empuja literalmente una posicion");

// Borramos con Pop el valor posicionado arriba de la pila, que será el ultimo en entrar
posiciones.Pop();

// Adquirir el valor del ultimo elemento en entrar sin borrar
string valorArriba = posiciones.Peek();
Console.WriteLine($"\nEl valor que está mas arriba despues de un borrado es: {valorArriba}");

// Busqueda dentro del Stack cocn Contains, este devuelve true en caso de encontrar valor

bool siHay = posiciones.Contains("Dos");
if (siHay)
{
    Console.WriteLine("Buscamos el Dos y lo encontramos");
}

// Queue es una cola donde el primer en entrar es el primero en salir.

Queue<int> numeros = new Queue<int>();

numeros.Enqueue(1);
numeros.Enqueue(2);
numeros.Enqueue(3);
numeros.Enqueue(4);
numeros.Enqueue(5);
numeros.Enqueue(6);

Console.WriteLine("El Queue actualmente es: ");
foreach (var item in numeros)
{
    Console.Write($"{item} ");
}

// Borrar al primero en añadir
numeros.Dequeue();

// Vemos el que seria el siguiente en salir pero sin borrar
int proxSalir = numeros.Peek();

Console.WriteLine($"\nDespues de un borrado, el siguiente en salir seria {proxSalir}");

// añadimos numeros repetidos

numeros.Enqueue(1);
numeros.Enqueue(3);
numeros.Enqueue(4);
numeros.Enqueue(7);

// Con Distinct podemos reunion los valores no repetidos unicamente
Console.WriteLine("Valores no repetidos despues de añadir alguno");
IEnumerable<int> distintos = numeros.Distinct();
foreach (var item in distintos)
{
    Console.Write($"{item} ");
}

Console.WriteLine("----------------------");

// ## Dificultad Extra

// Navegador
void NavegadorWeb()
{
    Stack<string> direcciones = new Stack<string>();
    Stack<string> descartes = new Stack<string>();
    string resp = "";

    do
    {
        Console.WriteLine("Indique la pagina a la que navegar, atras, adelante o salir");
        resp = Console.ReadLine().ToUpper();
        switch (resp)
        {
            case "SALIR":
                break;
            case "ATRAS":
                if (direcciones.Count > 0)
                {
                    descartes.Push(direcciones.Pop());
                }

                break;
            case "ADELANTE":
                if (descartes.Count > 0)
                {
                    direcciones.Push(descartes.Pop());
                }

                break;
            default:
                direcciones.Push(resp);
                break;
        }

        if (direcciones.Count > 0)
        {
            Console.WriteLine($"Navegaste a {direcciones.Peek()}");
        }
        else
        {
            Console.WriteLine("Pagina de Inicio");
        }
    } while (resp != "SALIR");
}

NavegadorWeb();

// Impresora

void Impresora()
{
    string resp = "";
    Queue<string> colaImpresora = new Queue<string>();

    do
    {
        Console.WriteLine("Impresora compartida, añada documento, indique IMPRIMIR o salir");
        resp = Console.ReadLine().ToUpper();

        switch (resp)
        {
            case "SALIR":
                break;
            case "IMPRIMIR":
                colaImpresora.Dequeue();
                break;
            default:
                colaImpresora.Enqueue(resp);
                break;
        }

        if (resp == "SALIR")
        {
            Console.WriteLine("SALIENDO");
        }
        else
        {
            if (colaImpresora.Count > 0)
            {
                Console.WriteLine($"El documento actual es: {colaImpresora.Peek()}");
            }
            else
            {
                Console.WriteLine("Sin documentos en cola");
            }
        }
    } while (resp != "SALIR");
}

Impresora();