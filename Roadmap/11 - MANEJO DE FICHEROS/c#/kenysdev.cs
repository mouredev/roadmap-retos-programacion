/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  C#                            ║
╚═══════════════════════════════════════╝
-----------------------------------------------
MANEJO DE FICHEROS
-----------------------------------------------

Fuente: https://imaginaformacion.com/tutoriales/manipulacion-archivos-c-sharp
*/
using System;
using System.Diagnostics;
using System.IO;
#pragma warning disable CA1050
public class Program {
    public class FileMg(string path) {
        public string Path { get; set; } = path;

        public void CreateFile() {
            try {
                if (!File.Exists(Path)) {
                    FileStream archivo = File.Create(Path);
                    archivo.Close();
                }
            } catch (Exception ex) {
                Console.WriteLine("Error->f.CreateFile->" + ex.Message);
            }
        }

        public void AppendLine(string line) {
            try {
                using StreamWriter writer = File.AppendText(Path);
                writer.WriteLine(line);

            } catch (Exception ex) {
                Console.WriteLine("Error->f.AppendLine->" + ex.Message);
            }
        }
        public void WriteLines(List<string> lines) {
            try {
                File.WriteAllLines(Path, lines);

            } catch (Exception ex) {
                Console.WriteLine("Error->f.WriteLines->" + ex.Message);
            }
        }

        public List<string>? ReadLines() {
            try {
                List<string> lines = [.. File.ReadAllLines(Path)];
                return lines;

            } catch (Exception ex) {
                Console.WriteLine("Error->f.ReadLines->" + ex.Message);
                return null;
            }
        }

        public void Print() {
            try {
                string[] lines = File.ReadAllLines(Path);
                foreach (string line in lines) {
                    Console.WriteLine(line);
                }
            } catch (Exception ex) {
                Console.WriteLine("Error->f.Print->" + ex.Message);
            }
        }

        public int QueryFile(string qry) {
            try {
                string[] lines = File.ReadAllLines(Path);
                int i = 0;
                foreach (string ln in lines) {
                    string[] parts = ln.Split(',');
                    string name = parts[0];
                    if (name == $"[{qry}]") {
                        Console.WriteLine(ln);
                        return i;
                    }
                    i += 1;
                }
                Console.WriteLine("No existe.");
                return -1;
                
            } catch (Exception ex) {
                Console.WriteLine("Error->QueryFile->" + ex.Message);
                return -1;
            }
        }        

        public void DeleteFile() {
            try {
                File.Delete(Path);
                Console.WriteLine(Path + "-> Eliminado.");

            } catch (Exception ex) {
                Console.WriteLine("Error->DeleteFile->" + ex.Message);
            }
        }
    }
/*
* Desarrolla un programa de gestión de ventas que almacena sus datos en un 
* archivo .txt.
* - Cada producto se guarda en una línea del arhivo de la siguiente manera:
*   [nombre_producto], [cantidad_vendida], [precio].
* - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
*   actualizar, eliminar productos y salir.
* - También debe poseer opciones para calcular la venta total y por producto.
* - La opción salir borra el .txt.
*/
    const string PATH = "sale_mgt.txt";
    const string MSG = @"
        Gestión de Ventas:
╔═════════════════════════════════╗
║ 1. Agregar        4. Editar     ║  
║ 2. Consultar      5. Facturar   ║
║ 3. Eliminar       6. salir.     ║
╚═════════════════════════════════╝
";
    static string AddProduct(
    FileMg Sale, string? prod = "", string? qty = "", string? price = "") {
        while (true) {
            if (string.IsNullOrWhiteSpace(prod)) {
                Console.WriteLine("Debe ingresar un nombre de producto.");
                Console.Write("Producto: ");
                prod = Console.ReadLine();

            } else if (string.IsNullOrWhiteSpace(qty) || !double.TryParse(qty, out _)) {
                Console.WriteLine("Debe ingresar una cantidad.");
                Console.Write("Cantidad: ");
                qty = Console.ReadLine();

            } else if (string.IsNullOrWhiteSpace(price) || !double.TryParse(price, out _)) {
                Console.WriteLine("Debe ingresar un precio.");
                Console.Write("Precio: ");
                price = Console.ReadLine();

            } else {
                string line = $"[{prod}], [{qty}], [{price}]";
                Sale.AppendLine(line);
                Console.WriteLine("\nGuardado");
                Console.WriteLine(MSG);
                return $"{line}";
            }
        }
    }

    static void QueryProduct(FileMg Sale, string qry = "") {
        if (qry.Length == 0) {
            Console.WriteLine("\nConsultar Producto.");
            Console.Write("Nombre: ");
            qry = Console.ReadLine()!;
        }
        Sale.QueryFile(qry);
    }

    static void DeleteProduct(FileMg Sale, string qry = "") {
        if (qry.Length == 0) {
            Console.WriteLine("\nEliminar Producto.");
            Console.Write("Nombre: ");
            qry = Console.ReadLine()!;
        }
        int numLine = Sale.QueryFile(qry);
        if (numLine != -1) {
            List<string> products = [.. Sale.ReadLines()];
            products.RemoveAt(numLine);
            Sale.WriteLines(products);
            Console.WriteLine("Producto eliminado");
        }
    }

    static void UpdateProduct(FileMg Sale, string qry = "") {
        if (qry.Length == 0) {
            Console.WriteLine("\nEditar Producto.");
            Console.Write("Nombre: ");
            qry = Console.ReadLine()!;
        }
        int numLine = Sale.QueryFile(qry);
        if (numLine != -1) {
            List<string> products = [.. Sale.ReadLines()];
            string line = AddProduct(Sale);
            products[numLine] = line;
            Sale.WriteLines(products);
        }
    }

    static void Invoice(FileMg Sale) {
        Console.WriteLine("\nFactura\n-------------------------");
        List<string> lines = Sale.ReadLines()!;
        double total = 0;
        foreach (string line in lines) {
            var a = line.Split(',')[1].Trim();
            double qty = double.Parse(a.Trim(' ', '[', ']'),
            System.Globalization.CultureInfo.InvariantCulture);

            var b = line.Split(',')[2].Trim();
            double price = double.Parse(b.Trim(' ', '[', ']'),
            System.Globalization.CultureInfo.InvariantCulture);

            var ln = line.Trim('\n');
            double subTotal = qty * price;
            string FsubTotal = $"${subTotal:0.00}";
            Console.WriteLine($"{ln} -> {FsubTotal}");
            total += subTotal;
        }
        Console.WriteLine($"\nMonto total: ${total:0.00}");
    }

    //_________________________________
    static void Main() {
        FileMg user = new("kenysdev.txt");
        user.CreateFile();
        List<string> lines = ["Ken", "121"];
        user.WriteLines(lines);
        user.AppendLine(".py");
        user.Print();
        user.DeleteFile();

        //_________________________________
        FileMg Sale = new(PATH);
        Sale.CreateFile();
        Console.WriteLine(MSG);

        while (true) {
            Console.Write("\nOpción: ");
            string option = Console.ReadLine()!;

            switch (option) {
                case "1": AddProduct(Sale); break;
                case "2": QueryProduct(Sale); break;  
                case "3": DeleteProduct(Sale); break;    
                case "4": UpdateProduct(Sale); break;
                case "5": Invoice(Sale); break;
                case "6":
                    Console.WriteLine("Adios");
                    Sale.DeleteFile(); 
                    return; 
                default:
                    Console.WriteLine("Opción 1 -> 6");
                    break;
            }
        }
    }
}

