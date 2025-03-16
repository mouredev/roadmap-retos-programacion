enum Days
{
    MONDAY = 1,
    TUESDAY = 2,
    WEDNESDAY = 3,
    THURSDAY = 4,
    FRIDAY = 5,
    SATURDAY = 6,
    SUNDAY = 7
}
enum OrderStatus
{
    PENDING = 1,
    SEND = 2,
    DELIVERED = 3,
    CANCELLED = 4
}
class Program
{
    static void Main(string[] args)
    {
        // Enumeraciones
        PrintDay(1);
        PrintDay(2);
        PrintDay(3);
        PrintDay(4);
        PrintDay(5);
        PrintDay(6);
        PrintDay(7);

        // Ejercicio Extra
        Console.ReadLine();
        Console.Clear();
        bool salir = false;
        List<Order> orders = new List<Order>();

        do
        {
            Menu();
            int opcion = 0;
            int.TryParse(Console.ReadLine(), out opcion);

            switch(opcion)
            {
                case 1:
                    CheckOrders(orders);
                    break;
                case 2:
                    AddOrder(ref orders);
                    break;
                case 3:
                    Send(ref orders);
                    break;
                case 4:
                    Deliver(ref orders);
                    break;
                case 5:
                    Cancel(ref orders);
                    break;
                case 6:
                    Console.Clear();
                    Console.WriteLine("Hasta la próxima...");
                    salir = true;
                    Thread.Sleep(1000);
                    break;
                default:
                    Console.Clear();
                    Console.WriteLine("Opción no válida...");
                    break;
            }
        } while (!salir);


    }
    static void PrintDay(int day) => 
        Console.WriteLine((Days)day);

    static int id = 1;
    static void Menu()
    {
        Console.WriteLine("---Sistema de pedidos---");
        Console.WriteLine("1.- Consultar pedidos");
        Console.WriteLine("2.- Crear nuevo pedido");
        Console.WriteLine("3.- Enviar pedido");
        Console.WriteLine("4.- Entregar pedido");
        Console.WriteLine("5.- Cancelar pedido");
        Console.WriteLine("6.- Salir");
        Console.WriteLine("Elija la opción deseada...");

    }
    static bool CheckOrders(List<Order> orders)
    {
        Console.Clear();
        if (orders.Count == 0)
        {
            Console.WriteLine("No hay pedidos registrados...");
            return false;
        }
            
        foreach (var order in orders)
            Console.WriteLine($"Id: {order.Id}, Estado: {(OrderStatus)order.State}");
        return true;
    }
    static void AddOrder(ref List<Order> orders)
    {
        Console.Clear();
        var order = new Order(id);
        id++;
        orders.Add(order);
        Console.WriteLine("Pedido creado...");
        Console.WriteLine($"Id: {order.Id}, Estado: {(OrderStatus)order.State}");
    }
    static void Send(ref List<Order> orders)
    {
        Console.Clear();
        if (!CheckOrders(orders))
        {
            return;
        }
        var result = SearchOrder(orders);
        if (!result.Item1)
            return;
        var order = orders.FirstOrDefault(o => o.Id == result.Item2);
        if (order.State == (int)OrderStatus.CANCELLED)
        {
            Console.WriteLine("El pedido ha sido cancelado, no es posible enviarlo...");
            return;
        }
        else if (order.State != (int)OrderStatus.PENDING)
        {
            Console.WriteLine("El pedido solo puede ser enviado si su estado es PENDING...");
            return;
        }
        order.State = (int)OrderStatus.SEND;
        Console.WriteLine("El pedido ha sido enviado...");


    }
    static void Deliver(ref List<Order> orders)
    {
        Console.Clear();
        if (!CheckOrders(orders))
        {
            return;
        }
        var result = SearchOrder(orders);
        if (!result.Item1)
            return;
        var order = orders.FirstOrDefault(o => o.Id == result.Item2);
        if (order.State == (int)OrderStatus.CANCELLED)
        {
            Console.WriteLine("El pedido ha sido cancelado, no es posible entregarlo...");
            return;
        }
        else if (order.State != (int)OrderStatus.SEND)
        {
            Console.WriteLine("El pedido solo puede ser enviado si su estado es SEND...");
            return;
        }
        order.State = (int)OrderStatus.DELIVERED;
        Console.WriteLine("El pedido ha sido entregado...");
    }
    static void Cancel(ref List<Order> orders)
    {
        Console.Clear();
        if (!CheckOrders(orders))
        {
            return;
        }
        var result = SearchOrder(orders);
        if (!result.Item1)
            return;
        var order = orders.FirstOrDefault(o => o.Id == result.Item2);
        if (order.State == (int)OrderStatus.CANCELLED)
        {
            Console.WriteLine("El pedido ya ha sido cancelado...");
            return;
        }
        else if (order.State == (int)OrderStatus.DELIVERED)
        {
            Console.WriteLine("El pedido ya ha sido entregado...");
            return;
        }
        order.State = (int)OrderStatus.CANCELLED;
        Console.WriteLine("El pedido ha sido cancelado...");
    }
    static (bool, int) SearchOrder(List<Order> orders)
    {
        Console.WriteLine("Ingresa Id de pedido...");
        int idBusqueda = 0;
        int.TryParse(Console.ReadLine(), out idBusqueda);

        if (idBusqueda == 0)
        {
            Console.WriteLine("El Id no es válido...");
            return (false, idBusqueda);
        }
        if (orders.Where(o => o.Id == idBusqueda).Count() == 0)
        {
            Console.WriteLine($"El pedido con Id {idBusqueda} no existe...");
            return (false, idBusqueda);
        }
        return (true, idBusqueda);

    }
}
class Order
{
    public int Id { get; set; }
    public int State { get; set; }

    public Order(int id)
    {
        Id = id;
        State = (int)OrderStatus.PENDING;
    }
}