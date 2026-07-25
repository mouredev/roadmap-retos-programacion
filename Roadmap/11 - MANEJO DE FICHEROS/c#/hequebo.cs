class Program
{
    static int id = 1;
    static void Main(string[] args)
    {
        #region Ficheros
        /* Cadena de texto con el nombre del archivo
         * Al solo especificar el nombre del archivo se genera en bin\Debug\net8.0 
         * dentro de la solución
         */
        string path = $"hequebo.txt";

        // Creación del archivo

        File.AppendAllText(path, "Emilio" + Environment.NewLine);
        File.AppendAllText(path, "27 años" + Environment.NewLine);
        File.AppendAllText(path, "C#" + Environment.NewLine);

        // Lectura del archivo
        string content = File.ReadAllText(path);
        Console.WriteLine(content);

        // Eliminación del archivo
        Thread.Sleep(1000);
        File.Delete(path);
        Console.WriteLine("Se eliminó el archivo...");
        Console.ReadLine();
        #endregion
        List<Producto> venta = new List<Producto> ();
        bool salir = false;
        do
        {
            MostrarMenu();
            string? opcion = Console.ReadLine();
            switch (opcion.ToLower())
            {

                case "a":
                    AgregarProducto(ref venta);
                    break;
                case "b":
                    Consultar(venta);
                    break;
                case "c":
                    ActualizarProducto(ref venta);
                    break;
                case "d":
                    EliminarProducto(ref venta);
                    break;
                case "e":
                    salir = true;
                    Console.WriteLine("Hasta la próxima...");
                    Thread.Sleep(2000);
                    break;
                default:
                    Console.WriteLine("Opción no válida...");
                    Thread.Sleep(2000);
                    break;
            }

        } while (!salir);

    }
    static void MostrarMenu()
    {
        Console.WriteLine("----SISTEMA DE VENTAS----");
        Console.WriteLine("a.- Agregar  Producto.");
        Console.WriteLine("b.- Consultar Productos.");
        Console.WriteLine("c-- Actualizar Producto.");
        Console.WriteLine("d.- Eliminar Producto.");
        Console.WriteLine("e.- Terminar venta.");
        Console.WriteLine("Seleccione operación a realizar:");

    }
    static void AgregarProducto(ref List<Producto> venta)
    {
        Console.Clear();
        var producto = new Producto();
        Console.WriteLine("Ingresa el nombre del producto");
        producto.Id = id;
        producto.Nombre = Console.ReadLine();
        producto.Cantidad = IngresarCantidad();
        producto.PrecioUnitario = IngresarPrecio();
        producto.Total = producto.Cantidad * producto.PrecioUnitario;

        venta.Add(producto);
        Console.WriteLine("Producto agregado correctamente");
        Console.WriteLine($"{producto.Id}.- Producto: {producto.Nombre}, Cantidad: {producto.Cantidad}, " +
                $"Precio: {producto.PrecioUnitario}, Total: {producto.Total}");
        id++;

    }
    static bool Consultar(List<Producto> venta)
    {
        Console.Clear();
        if (venta.Count == 0) 
        {
            Console.WriteLine("No hay productos registrados...");
            return false;
        }
        foreach (var item in venta)
            Console.WriteLine($"{item.Id}.- Producto: {item.Nombre}, Cantidad: {item.Cantidad}, " +
                $"Precio: {item.PrecioUnitario}, Total: {item.Total}");
        return true;
    }

    static int IngresarCantidad()
    {
        int cantidad = 0;
        bool esValido = false;
        do
        {
            Console.WriteLine("Ingresa la cantidad vendida");
            int.TryParse(Console.ReadLine(), out cantidad);
            if (cantidad != 0)
                esValido = true;
            else
                Console.WriteLine("Cantidad no valida...");
        } while (!esValido);
        return cantidad;
    }
    static decimal IngresarPrecio()
    {
        decimal precio = 0;
        bool esValido = false;
        do
        {
            Console.WriteLine("Ingresa el precio del producto");
            decimal.TryParse(Console.ReadLine(), out precio);
            if (precio != 0)
                esValido = true;
            else
                Console.WriteLine("Precio no válido...");
        } while (!esValido);
        return precio;
    }
    static void ActualizarProducto(ref List<Producto> venta)
    {
        if (!Consultar(venta))
        {
            return;
        }
        Console.WriteLine("Ingresa id de Producto a actualizar");
        int id = IngresarId();
        if (BuscarPorId(id, venta) == 0)
        {
            Console.WriteLine($"No existe el producto con Id {id}...");
            return;
        }
        var producto = venta.FirstOrDefault(p => p.Id == id);
        Console.WriteLine("Ingresa nombre del producto");
        producto.Nombre = Console.ReadLine();
        producto.Cantidad = IngresarCantidad();
        producto.PrecioUnitario = IngresarPrecio();
        producto.Total = producto.Cantidad * producto.PrecioUnitario;
        Console.WriteLine("Producto actualizado correctamente");
        Console.WriteLine($"{producto.Id}.- Producto: {producto.Nombre}, Cantidad: {producto.Cantidad}, " +
                $"Precio: {producto.PrecioUnitario}, Total: {producto.Total}");
    }
    static int IngresarId()
    {
        bool esValido = false;
        int id;
        do
        {
            id = 0;
            int.TryParse(Console.ReadLine(), out id);
            if (id != 0)
                esValido = true;
            else
                Console.WriteLine("Id no válido...");

        } while (!esValido);

        return id;
    }
    static int BuscarPorId(int id, List<Producto> venta)
    {
        return venta.Select(p => p.Id == id).Count();
    }
    static void EliminarProducto(ref List<Producto> venta)
    {
        if (!Consultar(venta))
            return;
        Console.WriteLine("Ingresa id de Producto a eliminar");
        int id = IngresarId();
        if (BuscarPorId(id, venta) == 0)
        {
            Console.WriteLine($"No existe el producto con Id {id}...");
            return;
        }
        var producto = venta.FirstOrDefault(p => p.Id == id);
        venta.Remove(producto);
        Console.WriteLine("Producto eliminado correctamente");
    }
}
class Producto
{
    public int Id { get; set; }
    public string? Nombre { get; set; }
    public int Cantidad { get; set; }
    public decimal PrecioUnitario { get; set; }
    public decimal Total {  get; set; }

}
