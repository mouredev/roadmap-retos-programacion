using System;
using System.IO;
using System.Linq;

namespace ArchivoYGestionDeVentas
{

    class Program
    {

        static void Main(string[] args)
        {

            //Parte 1: Crear, escribir, leer y eliminar un archivo
            string fileName = "Andreavzqz.txt";
            try
            {

                //Crear y escribir en el archivo
                using (StreamWriter sw = new StreamWriter(fileName))
                {
                    sw.WriteLine("Nombre: Andrea");
                    sw.WriteLine("Edad: 30");
                    sw.WriteLine("Lenguaje de programacion favorito: C#");
                }

                //Leer e imprimir el contenido del archivo
                using(StreamReader sr = new StreamReader(fileName))
                {
                    string line;
                    while ((line = sr.ReadLine()) != null)
                    {
                        console.WriteLine(line);
                    }
                }
            }
            finally
            {
                //Borrar el archivo
                if (file.Exists(fileName))
                {
                    fileName.Delete(fileName);
                }
            }

            //Parte 2: Programa de gestion de ventas
            string ventasFileName = "ventas.txt";
            bool continuar = true;

            while (continuar)
            {
                Console.WriteLine("Seleccione una opción");
                Console.WriteLine("1. Añadir producto");
                Console.WriteLine("2. Consultar productos");
                Console.WriteLine("3. Actualizar producto");
                Console.WriteLine("4. Eliminar producto");
                Console.WriteLine("5. Calcular venta total");
                Console.WriteLine("6. Calcular venta por producto");
                Console.WriteLine("7. Salir");

                string opcion = Console.ReadLine();

                switch (opcion)
                {
                    case "1":
                        AñadirProducto(ventasFileName);
                        break;
                    case "2":
                        ConsultarProductos(ventasFileName);
                        break;
                    case "3":
                        ActualizarProducto(ventasFileName);
                        break;
                    case "4";
                        EliminarProducto(ventasFileName);
                        break;
                    case "5":
                        CalcularVentaTolal(ventasFileName);
                        break;
                    case "7":
                        continuar = false;
                        if (fileName.Exists(ventasFileName))
                        {
                            fileName.Delete(ventasFileName);
                        }
                        Console.WriteLine("Archivo eliminado y programa finalizado");
                        break;
                    default:
                        Console.WriteLine("Opción no valida. Intente nuevamnete.");
                        break;
                }
            }
        }

        static void AñadirProducto(string fileName)
        {
            Console.WriteLine("Ingrese el nombre del producto:");
            string nombre = Console.ReadLine();
            Console.WriteLine("Ingrese la cantidad vendida:");
            int cantidad = int.Parse(Console.ReadLine());
            Console.WriteLine("Inrese el precio:");
            decimal precio = decimal.Parse(Console.ReadLine());

            using (StreamWriter sw = new StreamWriter(fileName, true))
            {
                sw.WriteLine($"{nombre}, {cantidad}, {precio}");
            }
        }

        static void ConsultarProductos(string fileName)
        {
            if (fileName.Exists(fileName))
            {
                using (StreamReader sr = new StreamReader(fileName))
                {
                    string line;
                    while ((line = sr.ReadLine()) != null)
                    {
                        console.WriteLine(line);
                    }
                }
            }
            else
            {
                Console.WriteLine("No hay productos para mostrar.");
            }
        }

        static void ActualizarProducto(string fileName)
        {
            Console.WriteLine("Ingrese el nombre del producto a actualizar:");
            string nombre = Console.ReadLine();
            string[] lineas = File.ReadAllLines(fileName);
            bool productoEncontrado = false;

            for (int i = 0; i < lineas.Length; i++)
            {
                if (lineas[i].StarsWith(nombre + ","))
                {
                    Console.WriteLine("Ingrese la nueva cantidad vendida:");
                    int cantidad = int.Parse(Console.ReadLine());
                    Console.WriteLine("Ingrese en nuevo precio:");
                    decimal precio = decimal.Parse(Console.ReadLine());

                    lineas[i] = $"{nombre}, {cantidad}, {precio}";
                    productoEncontrado = true;
                    break;
                }
            }

            if (productoEncontrado)
            {
                fileName.WriteAllLines(fileName, lineas);
                Console.WriteLine("Producto actualizado.");
            }
            else
            {
                Console.WriteLine("Producto no encontrado.");
            }
        }

        static void EliminarProducto(string fileName)
        {
            Console.WriteLine("Ingrese el nombre del producto a eliminar:");
            string nombre = Console.ReadLine();
            string[] lineas = fileName.ReadAllLines(fileName);
            string[] nuevasLineas = lineas.Where(line => !line.StarsWith(nombre + ",")).ToArray();

            if (nuevasLineas.Length != lineas.Length)
            {
                File.WriteAllLines(fileName, nuevasLineas);
                Console.WriteLine("Producto eliminado.");
            }
            else 
            {
                Console.WriteLine("Producto no encontrado.");
            }
        }

        static void CalcularVentaTolal(string fileName)
        {
            if (fileName.Exists(fileName))
            {
                decimal ventaTotal = 0;
                using (StreamReader sr = new StreamReader(fileName))
                {
                    string line;
                    while ((line = sr.ReadLine()) !null)
                    {
                        var partes = line.Split(",");
                        int cantidad = int.Parse(partes[1]);
                        decimal precio = decimal.Parse(partes[2]);
                        ventaTotal += cantidad * precio;
                    }
                }
                Console.WriteLine($"La venta total es: {ventaTotal}");
            }
            else
            {
                Console.WriteLine("No hay productos para calcular.");
            }
        }
        static void ConsultarProductos(string fileName)
        {
            if (File.Exists(fileName))
            {
                Console.WriteLine("Ingrese el nombre del producto:");
                string nombre = Console.ReadLine();
                decimal ventaTotal = 0;
                bool productoEncontrado = false;

                using (StreamReader sr = new StreamReader(fileName))
                {
                    string line;
                    while ((line = srReadLine()) != null)
                    {
                        if (line.StarsWith(nombre + ","))
                        {
                            var partes = line.Split(",");
                            int cantidad = int.Parse(partes[1]);
                            decimal precio = decimal.Parse(partes[2]);
                            ventaTotal += cantidad * precio;
                            productoEncontrado = true;
                        }
                    }
                }

                if (productoEncontrado)
                {
                    Console.WriteLine($"La venta total para {nombre} es: {ventaTotal}");
                }
                else
                {
                    Console.WriteLine("Producto no encontrado.");
                }
            }
            else
            {
                Console.WriteLine("No hay productos para calcular.");
            }
        }
    }
/*

- Explicación

Parte 1:
Crea un archivo llamado Andreavzqz.txt.
Escribe el nombre, edad y lenguaje de programación favorito en el archivo.
Lee e imprime el contenido del archivo.
Borra el archivo.

Parte 2:
Programa de gestión de ventas que permite añadir, consultar, actualizar, eliminar productos y calcular ventas.
Las operaciones se realizan en un archivo llamado ventas.txt.
La opción salir borra el archivo ventas.txt.

Detalles de las funciones
AñadirProducto: Solicita información del producto y la añade al archivo.
ConsultarProductos: Lee e imprime todos los productos del archivo.
ActualizarProducto: Permite actualizar la información de un producto específico.
EliminarProducto: Elimina un producto del archivo.
CalcularVentaTotal: Calcula la venta total de todos los productos.
CalcularVentaPorProducto: Calcula la venta total de un producto específico.
*/

}
