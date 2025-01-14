using System;

class Program
{
    static void Main()
    {
        Stack<string> urls = new Stack<string>();
        Extra.Navegador(urls);

        Queue<string> cola = new Queue<string>();
        Extra.Imprimir(cola);
    }
}
class Extra
{
    public static void Navegador(Stack<string> urls)
    {
        Console.WriteLine($"Ingrese una url valida o seleccione una de estas opciones: " +
                          $"\n 1.Atras" +
                          $"\n 2.Salir");
        string opcion = Console.ReadLine();

        switch (opcion)
        {
            case "1":
                if (urls.Count > 0)
                {
                    urls.Pop();
                    if (urls.Count > 0)
                    {
                        Console.WriteLine($"Has regresado a la web: {urls.Peek()}");
                    }
                    else
                    {
                        Console.WriteLine("No hay más páginas en el historial.");
                    }
                }
                else
                {
                    Console.WriteLine("El historial está vacío. No puedes regresar.");
                }
                break;
            case "2":
                Console.WriteLine("Saliendo del navegador.");
                return;
            default:
                urls.Push(opcion);
                Console.WriteLine($"Has navegado a la web {urls.Peek()}");
                break;
        }
        Navegador(urls);
    }
    public static void Imprimir(Queue<string> cola)
    {
        Console.WriteLine($"Ingrese un documento o seleccione una de estas opciones: " +
                          $"\n 1.Imprimir" +
                          $"\n 2.Salir");
        string opcion = Console.ReadLine();

        switch (opcion)
        {
            case "1":
                if (cola.Count > 0)
                {
                    if (cola.Count > 0)
                    {
                        Console.WriteLine($"El documento {cola.Dequeue()} ha sido impreso");
                    }
                    else
                    {
                        Console.WriteLine("No hay más documentos para imprimir.");
                    }
                }
                else
                {
                    Console.WriteLine("No hay más documentos para imprimir.");
                }
                break;
            case "2":
                Console.WriteLine("Apagando impresora.");
                return;
            default:
                cola.Enqueue(opcion);
                Console.WriteLine($"El documento {opcion} ha sido agregado");
                break;
        }
        Imprimir(cola);
    }
}
