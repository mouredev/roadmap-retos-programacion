/*
 * 1.- Un delegado es una variable que almacena una
 * función y define la estructura de esta misma
 * El delegado Operation establece que la función
 * que le sea asignada debe de recibir dos parámetros
 * de tipo entero y devolver un número entero
 */
delegate int Operation(int x, int y);

delegate void OrderProcess(string dish);
class Program
{
    static void Main(string[] args)
    {
        /*
         * 5.- Asignamos a una variable de tipo
         * Operation la función Addition
         */
        Operation op = Addition;
        /*
         * 6.- Ejecutamos la función ShowResult con la función
         * op como parámetro
         */
        ShowResult(3, 5, op);
        /*
         * El concepto de miltifusión permite 
         * almacenar más de una función en un delegado
         * por lo que dentro de order se encuentran las
         * tres funciones definidas
         */
        OrderProcess order = Confirm;
        order += Ready;
        order += Deliver;
        ProcessOrder("Hamburgesa", order);
    }
    /*
     * 2.- La función Addition cumple con los
     * requisitos establecidos por el delegado
     * Operation
     */
    static int Addition(int x, int y) => x + y;
    /*
     * 3.- La función ShowResult tiene como parámetros
     * dos números enteros y una función que sea del
     * tipo Operation
     */
    static void ShowResult(int x, int y, Operation op)
    {
        /*
         * 4.- Dentro de la función ShowResult se ejecuta
         * la función que se envío como parámetro
         */
        Console.WriteLine($"El resultado es: {op(x, y)}");
    }
    static void Confirm(string dish)  
    { 
        Console.WriteLine($"La orden de {dish} ha sido confirmada"); 
        int seconds = new Random().Next(1,10);
        Console.WriteLine(seconds);
        Thread.Sleep(seconds * 1000);
    }
    static void Ready(string dish) 
    {
        Console.WriteLine($"La orden de {dish} está lista");
        int seconds = new Random().Next(1, 10);
        Console.WriteLine(seconds);
        Thread.Sleep(seconds * 1000);
    }
    static void Deliver(string dish) => Console.WriteLine($"La orden de {dish} ha sido entregada");
    static void ProcessOrder(string dish, OrderProcess order)
    {
        Console.WriteLine("Se recibió orden");
        order(dish);
    }
}
