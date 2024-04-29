/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */

using System;

namespace Roadmap11
{
    class ExtraExercise {

        /*
            * Init method: create the file `ventas.txt` if it doesn't exist
            * we also print the menu
        */
        public static void Init() {
            string path = "ventas.txt";
            if (!System.IO.File.Exists(path)) {
                System.IO.File.Create(path);
            }
            PrintMenu();
        }

        /*
            * PrintMenu method: print the menu
        */
        public static void PrintMenu() {
            Console.WriteLine("1. Añadir producto");
            Console.WriteLine("2. Consultar producto");
            Console.WriteLine("3. Actualizar producto");
            Console.WriteLine("4. Eliminar producto");
            Console.WriteLine("5. Venta total");
            Console.WriteLine("6. Venta por producto");
            Console.WriteLine("7. Salir");
            Console.WriteLine("Seleccione una opción: ");
            int option = Convert.ToInt32(Console.ReadLine());
            HandleOption(option);
        }

        /*
            * HandleOption method: handle the option selected by the user
            * @param option: the option selected by the user
        */
        public static void HandleOption(int option) {
            switch (option) {
                case 1:
                    AddProduct();
                    break;
                case 2:
                    GetProduct();
                    break;
                case 3:
                    UpdateProduct();
                    break;
                case 4:
                    DeleteProduct();
                    break;
                case 5:
                    TotalSale();
                    break;
                case 6:
                    SaleByProduct();
                    break;
                case 7:
                    DeleteFile();
                    break;
                default:
                    Console.WriteLine("Opción no válida.");
                    break;
            }
        }

        /*
            * AddProduct method: add a product to the file
        */
        public static void AddProduct() {
            Console.WriteLine("Ingrese el nombre del producto: ");
            string name = Console.ReadLine();
            Console.WriteLine("Ingrese la cantidad vendida: ");
            int quantity = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Ingrese el precio: ");
            double price = Convert.ToDouble(Console.ReadLine());
            string path = "ventas.txt";
            string line = $"{name}, {quantity}, {price}";
            System.IO.File.AppendAllText(path, line);
            Console.WriteLine("Producto añadido.");
            PrintMenu();
        }

        /*
            * GetProduct method: get a product from the file
        */
        public static void GetProduct() {
            Console.WriteLine("Ingrese el nombre del producto: ");
            string name = Console.ReadLine();
            string path = "ventas.txt";
            string[] lines = System.IO.File.ReadAllLines(path);
            foreach (string line in lines) {
                string[] data = line.Split(",");
                if (data[0].Trim() == name) {
                    Console.WriteLine($"Producto: {data[0]}");
                    Console.WriteLine($"Cantidad vendida: {data[1]}");
                    Console.WriteLine($"Precio: {data[2]}");
                    return;
                }
            }
            Console.WriteLine("Producto no encontrado.");
            PrintMenu();
        }

        /*
            * UpdateProduct method: update a product from the file
        */
        public static void UpdateProduct() {
            Console.WriteLine("Ingrese el nombre del producto: ");
            string name = Console.ReadLine();
            string path = "ventas.txt";
            string[] lines = System.IO.File.ReadAllLines(path);
            for (int i = 0; i < lines.Length; i++) {
                string[] data = lines[i].Split(",");
                if (data[0].Trim() == name) {
                    Console.WriteLine("Ingrese la nueva cantidad vendida: ");
                    int quantity = Convert.ToInt32(Console.ReadLine());
                    Console.WriteLine("Ingrese el nuevo precio: ");
                    double price = Convert.ToDouble(Console.ReadLine());
                    lines[i] = $"{name}, {quantity}, {price}";
                    System.IO.File.WriteAllLines(path, lines);
                    Console.WriteLine("Producto actualizado.");
                    PrintMenu();
                    return;
                }
            }
            Console.WriteLine("Producto no encontrado.");
            PrintMenu();
        }

        /*
            * DeleteProduct method: delete a product from the file
        */
        public static void DeleteProduct() {
            Console.WriteLine("Ingrese el nombre del producto: ");
            string name = Console.ReadLine();
            string path = "ventas.txt";
            string[] lines = System.IO.File.ReadAllLines(path);
            for (int i = 0; i < lines.Length; i++) {
                string[] data = lines[i].Split(",");
                if (data[0].Trim() == name) {
                    lines[i] = "";
                    System.IO.File.WriteAllLines(path, lines);
                    Console.WriteLine("Producto eliminado.");
                    PrintMenu();
                    return;
                }
            }
            Console.WriteLine("Producto no encontrado.");
            PrintMenu();
        }

        /*
            * TotalSale method: calculate the total sale
        */
        public static void TotalSale() {
            string path = "ventas.txt";
            string[] lines = System.IO.File.ReadAllLines(path);
            double total = 0;
            foreach (string line in lines) {
                string[] data = line.Split(",");
                total += Convert.ToInt32(data[1]) * Convert.ToDouble(data[2]);
            }
            Console.WriteLine($"Venta total: {total}");
            PrintMenu();
        }

        /*
            * SaleByProduct method: calculate the sale by product
        */
        public static void SaleByProduct() {
            Console.WriteLine("Ingrese el nombre del producto: ");
            string name = Console.ReadLine();
            string path = "ventas.txt";
            string[] lines = System.IO.File.ReadAllLines(path);
            foreach (string line in lines) {
                string[] data = line.Split(",");
                if (data[0].Trim() == name) {
                    double total = Convert.ToInt32(data[1]) * Convert.ToDouble(data[2]);
                    Console.WriteLine($"Venta por producto: {total}");
                    PrintMenu();
                    return;
                }
            }
            Console.WriteLine("Producto no encontrado.");
            PrintMenu();
        }

        /*
            * DeleteFile method: delete the file `ventas.txt`
        */
        public static void DeleteFile() {
            string path = "ventas.txt";
            System.IO.File.Delete(path);
            Console.WriteLine("Archivo eliminado.");
        }


        public static void Main(string[] args) {
            Init();
        }
    }
    class FileManagement
    {
        public void CreateFile(string username)
        {
            string path = username + ".txt";
            string nombre = "Jamer José";
            string edad = "24";
            string lenguaje = "TypeScript";
            string[] lines = {
                $"Nombre: {nombre}",
                $"Edad: {edad}",
                $"Lenguaje de programación favorito: {lenguaje}"
            };

            System.IO.File.WriteAllLines(path, lines);
        }

        public void DeleteFile(string username)
        {
            string path = username + ".txt";
            System.IO.File.Delete(path);
        }

        static void Main(string[] args)
        {
            FileManagement fileManagement = new FileManagement();
            string username = "jamerrq";

            fileManagement.CreateFile(username);
            Console.WriteLine($"Archivo {username}.txt creado.");

            string path = username + ".txt";
            string[] lines = System.IO.File.ReadAllLines(path);

            foreach (string line in lines)
            {
                Console.WriteLine(line);
            }

            fileManagement.DeleteFile(username);
            Console.WriteLine($"El archivo {username}.txt ha sido eliminado.");
        }
    }
}
