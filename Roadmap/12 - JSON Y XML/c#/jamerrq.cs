/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 */

using System;

namespace Roadmap12
{
    class JsonAndXML
    {
        static void createFile (string extension) {
            string path = "datos." + extension;
            if (!System.IO.File.Exists(path)) {
                System.IO.File.Create(path);
            }
        }

        static void writeToFile (string extension) {
            string path = "datos." + extension;
            if (extension == "xml") {
                System.IO.File.WriteAllText(path, "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n");
                System.IO.File.AppendAllText(path, "<datos>\n");
                System.IO.File.AppendAllText(path, "    <nombre>Jamerrq</nombre>\n");
                System.IO.File.AppendAllText(path, "    <edad>25</edad>\n");
                System.IO.File.AppendAllText(path, "    <fecha_nacimiento>1996-01-01</fecha_nacimiento>\n");
                System.IO.File.AppendAllText(path, "    <lenguajes>\n");
                System.IO.File.AppendAllText(path, "        <lenguaje>C#</lenguaje>\n");
                System.IO.File.AppendAllText(path, "        <lenguaje>JavaScript</lenguaje>\n");
                System.IO.File.AppendAllText(path, "    </lenguajes>\n");
                System.IO.File.AppendAllText(path, "</datos>");
            } else if (extension == "json") {
                System.IO.File.WriteAllText(path, "{\n");
                System.IO.File.AppendAllText(path, "    \"nombre\": \"Jamerrq\",\n");
                System.IO.File.AppendAllText(path, "    \"edad\": 25,\n");
                System.IO.File.AppendAllText(path, "    \"fecha_nacimiento\": \"1996-01-01\",\n");
                System.IO.File.AppendAllText(path, "    \"lenguajes\": [\n");
                System.IO.File.AppendAllText(path, "        \"C#\",\n");
                System.IO.File.AppendAllText(path, "        \"JavaScript\"\n");
                System.IO.File.AppendAllText(path, "    ]\n");
                System.IO.File.AppendAllText(path, "}");
            }
        }

        static void readAndPrintFile (string extension) {
            string path = "datos." + extension;
            if (System.IO.File.Exists(path)) {
                string content = System.IO.File.ReadAllText(path);
                Console.WriteLine(content);
            }
        }

        static void deleteFile (string extension) {
            string path = "datos." + extension;
            if (System.IO.File.Exists(path)) {
                System.IO.File.Delete(path);
            }
        }

        static int printMenu () {
            Console.WriteLine("1. Crear archivo XML");
            Console.WriteLine("2. Crear archivo JSON");
            Console.WriteLine("3. Mostrar contenido del archivo XML");
            Console.WriteLine("4. Mostrar contenido del archivo JSON");
            Console.WriteLine("5. Borrar archivos");
            Console.WriteLine("6. Salir");
            Console.WriteLine("Seleccione una opción: ");
            return Convert.ToInt32(Console.ReadLine());
        }

        static void Main(string[] args)
        {
            int option = 0;
            do {
                option = printMenu();
                switch (option) {
                    case 1:
                        createFile("xml");
                        writeToFile("xml");
                        break;
                    case 2:
                        createFile("json");
                        writeToFile("json");
                        break;
                    case 3:
                        readAndPrintFile("xml");
                        break;
                    case 4:
                        readAndPrintFile("json");
                        break;
                    case 5:
                        deleteFile("xml");
                        deleteFile("json");
                        break;
                    case 6:
                        break;
                    default:
                        Console.WriteLine("Opción no válida.");
                        break;
                }
            } while (option != 6);
        }
    }
}
